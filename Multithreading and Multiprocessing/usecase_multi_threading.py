'''
https://docs.langchain.com/oss/python/langchain/overview

https://docs.langchain.com/oss/python/langchain/context-engineering

https://docs.langchain.com/oss/python/langchain/ui
'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://docs.langchain.com/oss/python/langchain/overview',

'https://docs.langchain.com/oss/python/langchain/context-engineering',

'https://docs.langchain.com/oss/python/langchain/ui'
]

def fetchContent(url):
    response= requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.get_text())} characters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetchContent, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched.")