import urllib
# HTML Parser
from bs4 import BeautifulSoup

# url. Go ahead and open it in your browser
#url = "http://labfiles.linuxacademy.com/python/scraping/courses.html"
url = "https://en.wikipedia.org/wiki/Diplodocus"

# Open the site and download the HTML into the var html_data
html_data = urllib.urlopen(url).read()

soup = BeautifulSoup(html_data,"lxml")

# Find the specific tag needed
sections = soup.find_all('table', attrs={'class':'infobox biota'})
print(sections)

