import requests
from bs4 import BeautifulSoup
import configparser

def get_place_details(api_key, company_name):
    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        'key': api_key,
        'input': company_name,
        'inputtype': 'textquery',
        'fields': 'place_id,geometry,name,user_ratings_total',
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and 'candidates' in data and data['candidates']:
        place_id = data['candidates'][0]['place_id']
        return get_place_details_by_id(api_key, place_id)
    else:
        return None

def get_place_details_by_id(api_key, place_id):
    base_url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        'key': api_key,
        'place_id': place_id,
        'fields': 'name,rating,formatted_address,user_ratings_total',
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and 'result' in data:
        return data['result']
    else:
        return None

def scrape_and_search(api_key, website_url):
    # Send a GET request to the URL
    response = requests.get(website_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Dictionary to store review counts for each company
        review_counts = {}

        # Extract and print all <tr> elements
        for tr in soup.find_all('tr'):
            # Find the <p> element within each <tr>
            p_element = tr.find('p')

            if p_element:
                company_name = p_element.text.strip()
                print(f"Company Name: {company_name}")

                # Get place details using Google Places API
                place_details = get_place_details(api_key, company_name)

                if place_details:
                    review_count = place_details.get('user_ratings_total', 0)
                    review_counts[company_name] = review_count

                    print(f"Name: {place_details['name']}")
                    print(f"Rating: {place_details.get('rating', 'N/A')}")
                    print(f"Review Count: {review_count}")
                    print(f"Address: {place_details.get('formatted_address', 'N/A')}")
                else:
                    print(f"No details found for {company_name}")

                # Add a newline for better separation in the output
                print('\n')
            else:
                print("No <p> element found in this <tr>.")

        # Sort companies based on review count and print the top 10
        sorted_companies = sorted(review_counts.items(), key=lambda x: x[1], reverse=True)
        print("\nTop 10 Companies with the Most Reviews:")
        for company, review_count in sorted_companies[:10]:
            print(f"{company}: {review_count} reviews")

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    # Read configuration from config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')

    api_key = config['Settings']['api_key']
    website_url = config['Settings']['website_url']

    # Call the function with the extracted API key and website URL
    scrape_and_search(api_key, website_url)

