# Direct links collector for [postimages.org](http://postimages.org/)
Script to get direct urls for all the photos in a gallery

<br>

## Download (ChromeDriver):
- Latest release [here](https://github.com/emermacko/postimages-direct-url/releases)

<br>

## Launching:
- double click
- or directly with argument: `python get_direct_urls.py --link [gallery url]`
- **the script will automatically copy the links to your clipboard**  
  
<br>  
  
<br>  
  
![get_urls](https://user-images.githubusercontent.com/25122875/89898195-90664480-dbe0-11ea-9e15-2d629b9cee69.jpg)

<br>

## Requirements when compiling yourself:
- Python 3.7
- Pip - `python get-pip.py`
- Selenium - `pip install selenium`
- Pyperclip - `pip install pyperclip`
- WebDriver - https://pypi.org/project/selenium/#drivers
  - Place in the same folder as `.py` file
  - When using other WebDriver than Chrome edit lines [51-54]
