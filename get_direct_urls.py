from selenium import webdriver
from tqdm import tqdm

import os
import time
import argparse
import pyperclip
import sys

links = []
urls = []

def get_urls():
    imgs = driver.find_elements_by_css_selector('.img')
    print(f'[OK] Found {len(imgs)} photos')

    for img in imgs:
        urls.append(img.get_attribute('href'))

    time.sleep(1)
    index = 1
    for url in tqdm(urls, desc="[OK] Downloading: ", unit="file", ncols=70, bar_format="{desc}{n_fmt}/{total_fmt} {bar} {percentage:3.0f}%"):
        driver.get(url)
        links.append(driver.find_element_by_css_selector('#main-image').get_attribute('src'))
        index += 1

    clipboard = ''
    #links.sort(key = lambda x: int(x.split('/')[4].split('-')[0]))     ## optional sorting ## create your own rule if needed
    for link in links:
        clipboard += (link + '\n')

    pyperclip.copy(clipboard)
    print('\n[FINISHED] All urls copied to clipboard')


def check_link(url):
    try:
        driver.get(url)
        return not driver.find_element_by_css_selector('.container h1').get_attribute('innerText')[:3] == '404'
    except:
        return False

####################

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', metavar='url', nargs=1, help='Directly link to the gallery')
parser.add_argument('-i', '--id', metavar='id', nargs=1, help='Gallery id - last part of the url')
args = parser.parse_args()

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=options)

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
url = args.url[0] if args.url else ''

clear()
while not check_link(url):
    url = input('[>] Link to gallery: ')

clear()
try:
    get_urls()
except Exception as e:
    print('[ERROR] ', e)

