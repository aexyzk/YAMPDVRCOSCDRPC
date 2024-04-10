import requests
from bs4 import BeautifulSoup
import os

def find_image(query):
    url = f'https://www.google.com/search?q={query}&tbm=isch'

    # Send GET request to Google Images
    response = requests.get(url)

    # Parse HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first image URL
    img_url = soup.find_all('img')

    return img_url[1]['src']

if __name__ == "__main__":
    print(find_image("Saviors - Green Day cover"))