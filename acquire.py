from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import os




# Updated with Instructor Code
def blog_soup():
    url = 'https://codeup.edu/blog/'
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = [link['href'] for link in soup.select('.more-link')]
    
    articles = []
    
    for url in links:
        
        url_response = get(url, headers=headers)
        soup = BeautifulSoup(url_response.text)
        
        title = soup.find('h1', class_='entry-title').text
        content = soup.find('div', class_='entry-content').text.strip()
        
        article_dict = {
            'title': title,b
            'content': content
        }
        
        articles.append(article_dict)



def inshort_soup():
    categories = ['business', 'sports', 'technology', 'entertainment']
    
    inshorts = []
    
    for category in categories:
        
        url = 'https://inshorts.com/en/read' + '/' + category
        response = get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        titles = [span.text for span in soup.find_all('span', itemprop='headline')]
        contents = [div.text for div in soup.find_all('div', itemprop='articleBody')]
        
        for i in range(len(titles)):
            
            article = {
                'title': titles[i],
                'content': contents[i],
                'category': category,
            }
            
            inshorts.append(article)
