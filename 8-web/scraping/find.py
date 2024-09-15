import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = '....'

# Send a GET request to the page
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    
    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all article titles
    titles = soup.find_all('a', class_='title')
    
    # Find all publication dates
    dates = soup.find_all('span', class_='sc-hyBbbR jhbVH publish-date')
    
    # Ensure both lists are the same length
    if len(titles) != len(dates):
        print("Warning: Number of titles and dates do not match.")
    
    # Print article titles and their publication dates
    for title, date in zip(titles, dates):
        print(f"Title: {title.get_text(strip=True)}")
        print(f"Date: {date.get_text(strip=True)}")
        print('---')
except requests.RequestException as e:
    print(f"Request failed: {e}")
