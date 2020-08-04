# Direct links collector for [postimages.org](http://postimages.org/)
Gets direct urls for all the photos in a gallery

<br>

## Download (ChromeDriver):
- Latest release [here](https://github.com/emermacko/postimages-direct-url/releases)

<br>

## Launching:
- double click
- or directly with argument: `python get_direct_urls.py --link [gallery url]`

<br>

## Requirements when compiling yourself:
- Python 3.7
- Pip - `python get-pip.py`
- Selenium - `pip install selenium`
- Pyperclip - `pip install pyperclip`
- WebDriver - https://pypi.org/project/selenium/#drivers
  - Place in the same folder as `.py` file
  - When using other WebDriver than Chrome edit lines [51-54]
