

from itertools import cycle
import requests
from bs4 import BeautifulSoup


# Rotating proxy code
# List of proxy IP addresses
#------------------------------------------------------------------------------
# Define the list of proxies
proxies = [
    'proxy1.example.com:8000',
    'proxy2.example.com:8000',
    'proxy3.example.com:8000',
    # Add more proxies as needed
]

# Create an infinite iterator from the proxy list
proxy_pool = cycle(proxies)

# Function to scrape and save data from a single page
def scrape_page(url):
    # Get the next proxy from the iterator
    proxy = next(proxy_pool)
    proxy_dict = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }

    try:
        # Make a request using the proxy
        response = requests.get(url, proxies=proxy_dict)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the article title
        title = soup.find('h1').text

        # Save the content to a file named after the article title
        with open(f'{title}.txt', 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f'Saved data for article: {title}')

    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')

# Function to perform scraping on multiple pages
def scrape_pages(start_url, num_pages):
    current_url = start_url

    for _ in range(num_pages):
        scrape_page(current_url)

        # Navigate to the next page (customize this part according to your needs)
        # Example: update the current_url to the URL of the next page
        # current_url = get_next_page_url(current_url)

# Usage example
start_url = 'https://example.com/news'
num_pages = 5

scrape_pages(start_url, num_pages)

#------------------------------------------------------------------------------
# Example usage
url = 'https://www.example.com'
# make_request_with_proxy(url)

# we scraping code
def scrape_news(url):
    # Send a GET request to the website
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if request fails

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the HTML elements containing the news articles
    article_elements = soup.find_all('article')

    # Extract information from each article
    for article in article_elements:
    # Extract the title
        title_element = article.find('h2')
        title = title_element.text.strip() if title_element else 'N/A'

    # Extract the summary
        summary_element = article.find('p')
        summary = summary_element.text.strip() if summary_element else 'N/A'

    # Extract the link
        link_element = article.find('a')
        link = link_element['href'] if link_element else '#'

    # Print the extracted information
        print('Title:', title)
        print('Summary:', summary)
        print('Link:', link)
        print('---')

#-------------------------------------------------------------------------------------------
# Example usage
# url = 'https://example.com/news'  # Replace with the actual URL of the news website
# scrape_news(url)

# traverse from page to page and scrape
# def scrape_pages(urls):
#    for url in urls:
#        response = requests.get(url)
 #       soup = BeautifulSoup(response.content, 'html.parser')

    # Perform scraping operations on the current page
    # For example, let's extract all the headlines from the page

  #      headlines = soup.find_all('h2', {'class': 'headline'})
   #     for headline in headlines:
    #        print(headline.text.strip())

    # Extract the next page URL
    #   next_page_link = soup.find('a', {'class': 'next-page'})
    #  if next_page_link:
    #     next_page_url = next_page_link['href']
    # Add the next page URL to the list of URLs to scrape
    #    urls.append(next_page_url)

# List of initial URLs to scrape
# initial_urls = [
    'https://www.example.com/page1',
    'https://www.example.com/page2',
    # Add more initial URLs as needed
# ]

# scrape_pages(initial_urls)


# python code to save scraped data to a file to parse elsewhere
# def scrape_pages(urls):
#    for url in urls:
#        response = requests.get(url)
#        soup = BeautifulSoup(response.content, 'html.parser')

    # Perform scraping operations on the current page
    # For example, let's extract all the headlines from the page
#        headlines = soup.find_all('h2', {'class': 'headline'})

    # Open a file in write mode
#        with open('scraped_data.txt', 'a') as file:
#            for headline in headlines:
#                file.write(headline.text.strip() + '\n')

    # Extract the next page URL
#        next_page_link = soup.find('a', {'class': 'next-page'})
#        if next_page_link:
#            next_page_url = next_page_link['href']
    # Add the next page URL to the list of URLs to scrape
#            urls.append(next_page_url)

# List of initial URLs to scrape
# initial_urls = [
#    'https://www.example.com/page1',
#    'https://www.example.com/page2',
    # Add more initial URLs as needed
# ]

# scrape_pages(initial_urls)
# In this example, we added a file writing operation using Python's open function and the with statement, which ensures that the file is properly closed after writing. The scraped headlines are written to a file called scraped_data.txt, with each headline on a separate line.

# You can modify the file name and path according to your requirements. Additionally, you can choose different file modes (e.g., 'w' for write mode, 'a' for append mode) based on how you want the data to be written to the file.

# After running this code, the scraped data will be written to the specified file, which you can then use as input for a separate algorithm or further processing.

# Remember to handle exceptions and errors that may occur during file operations, such as IOError or PermissionError, to ensure the robustness of your code.

# You're welcome! That sounds like a good plan. By separating the scraping and parsing tasks, you can have a more modular and flexible approach to handling the data you collect. The scraping algorithm can focus on extracting the data from the web pages and saving it to a file, while the parsing algorithm can handle the analysis, filtering, and sorting of the data.

# Once you have the data saved in a file, you can develop a separate parser algorithm that reads the file, processes the data, and performs any necessary sorting or analysis. You can use Python's file I/O operations or consider using specialized parsing libraries, depending on the format of the data and the complexity of the parsing requirements.

# If the data is in a structured format like JSON or XML, you can use Python's built-in libraries (json or xml.etree.ElementTree) to parse the data. If the data is in a more custom or complex format, you may need to implement your own parsing logic using regular expressions or other string manipulation techniques.

# Remember to consider error handling, data validation, and performance optimizations when developing your parsing algorithm to ensure it operates efficiently and accurately on the collected data.
