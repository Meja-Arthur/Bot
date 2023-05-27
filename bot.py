
import sys
import requests
from bs4 import BeautifulSoup
import urllib.request

# Base URL of the video site
base_url = "https://www.xnxx.com"

# Number of pages to scrape
num_pages = 2

sys.stdout.reconfigure(encoding='utf-8')

# Iterate over the pages
for page in range(1, num_pages + 1):
    # Construct the URL of the page
    url = f"{base_url}/videos?page={page}"
    
    # Send a GET request to the URL
    response = requests.get(url)

    response.encoding = 'utf-8'

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the HTML elements that contain the video links
    video_elements = soup.find_all("a", class_="video-link")

    # Iterate over the video elements
    for video_element in video_elements:
        # Extract the URL of the video
        video_url = video_element["href"]
        
        # Download the video
        urllib.request.urlretrieve(f"{base_url}{video_url}", f"downloaded_videos/video_{page}.mp4")
        print(f"Video from page {page} downloaded successfully!")
