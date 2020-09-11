# Direct links collector for [postimages.org](http://postimages.org/)
Script to get direct urls for all the photos in a gallery

<br>

## Download (for ChromeDriver):
- Download the latest release [here](http://bit.ly/postimg-direct-url-releases)

<br>

## Launching:
- double click
- or directly with argument: `python get_direct_urls.py --link [gallery url]`
- **the script will automatically copy the links to your clipboard**  
  
<br>  
  
## Preview:
![preview](https://user-images.githubusercontent.com/25122875/92968314-307eea00-f47b-11ea-8e01-72201e21f62d.png)

<br>

## Sidenotes:
- When compiling yourself you will need: `selenium` & `paperclip`  
- And a WebDriver - https://pypi.org/project/selenium/#drivers
  - Place in the same folder as `.py` file
  - When using other WebDriver than Chrome edit lines [50-53]
