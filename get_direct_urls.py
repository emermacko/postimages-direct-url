from selenium import webdriver

import platform
import os
import time
import argparse
import pyperclip

links = []
urls = []

def get_urls():
    os.system(clear)

    imgs = driver.find_elements_by_css_selector('.img')
    print('[OK] Found ', len(imgs), ' photos')

    for img in imgs:
        urls.append(img.get_attribute('href'))

    time.sleep(1)
    index = 1
    for url in urls:
        driver.get(url)
        links.append(driver.find_element_by_css_selector('#main-image').get_attribute('src'))
        print(f'[OK] Getting links [{index}/{len(urls)}]\r', end="")
        index += 1

    clipboard = ''
    #links.sort(key = lambda x: int(x.split('/')[4].split('-')[0]))     ## optional sorting ## create your own rule
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
parser.add_argument('-l', '--link', metavar='[link]', nargs=1, help='Directly link the gallery')
args = parser.parse_args()

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=options)

OS = platform.system()
if OS == 'Windows':
    clear = 'cls'
elif OS == 'Linux' or OS == 'Darwin':
    clear = 'clear'
else: clear = ''

url = ''
if args.link:
    url = args.link[0]

os.system(clear)
while not check_link(url):
    url = input('[>] Link to gallery: ')

try:
    get_urls()
except Exception as e:
    print('[ERROR] ', e)
