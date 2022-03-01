# MostPopularWords

# Goal: Find the most popular words on a given website. 

import requests 
import re
from bs4 import BeautifulSoup


def get_html_of(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}
    r = requests.get(url, headers=headers)

    if r.status_code != 200: 
        print(f'Status code returned: {r.status_code}')

    return r.text

def get_all_words_from(url):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'lxml')
    words_tags_removed = soup.get_text()
    all_words = re.findall(r"\w+", words_tags_removed)

    return all_words
    
def count_occurrences_in(word_list): 
    most_popular_words = {}

    for word in word_list: 
        if word not in most_popular_words:
            most_popular_words[word] = 1
        else: 
            most_popular_words[word] += 1
    
    return most_popular_words


if __name__ == '__main__':
    all_words = get_all_words_from('https://apple.com') # Change website if needed. 
    counted_words = count_occurrences_in(all_words)

    for k, v in counted_words.items():
        if v > 10:  # Change this if the occurences of each word are much higher. 
            print(k, v)

