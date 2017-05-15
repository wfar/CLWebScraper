"""Scrapes craigslist cars section for all ads up to the pages selected. Returns title, price, and location if given."""

import requests as r 
from bs4 import BeautifulSoup

def cl_web_scrape(max_pages):
    #Crawls and scrapes all ads from cl cars section. Prints title, price, and location.
    ad_count = ''
    page = 1
    x = 120
    while page <= max_pages:
        url = 'https://chicago.craigslist.org/search/cta' + ad_count
        source = r.get(url)
        text = source.text
        soup = BeautifulSoup(text.encode('ascii', 'ignore'), 'lxml')
        for a in soup.findAll('a', {'class': 'result-title hdrlnk'}):
            href = a.get('href')
            title = a.string
            ad_url = 'https://chicago.craigslist.org' + href            
            print('\n' + title)
            get_price(ad_url)
            get_location(ad_url)
            print(ad_url)
        
        ad_count = '?s=' + str(x)
        x += 120
        page += 1
    
def get_price(ad_url):
    #Gets the price for each posting.
    source = r.get(ad_url)
    text = source.text
    soup = BeautifulSoup(text, 'lxml')
    for span in soup.findAll('span', {'class': 'price'}):
        price = span.string
        print('Price:' , price)

def get_location(ad_url):
    #Gets the location (if there is one) for each posting.
    source = r.get(ad_url)
    text = source.text
    soup = BeautifulSoup(text, 'lxml')
    soup_content = soup.find('small')
    if soup_content is not None:
        location = soup_content.string
        print('Location:' , location)

def main():
    #Runs entire program.
    try:
        max_pages = int(input('How many pages do you want to search?\n> '))
        cl_web_scrape(max_pages)
    except:
        print('Please enter an integer')
        main()
        
    

    

if __name__ ==  "__main__":
    main()
