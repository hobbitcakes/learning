import urllib, argparse, os, sys
# HTML Parser
from bs4 import BeautifulSoup

def get_dino(dino):
	# Construct the Dino URL
	url = "https://en.wikipedia.org/wiki/%s" % dino
	
	# Open the site and download the HTML into the var html_data
	html_data = urllib.urlopen(url).read()

	# Parse the HTML
	soup = BeautifulSoup(html_data,"lxml")

	# Find the specific tag needed
	sections = soup.find_all('table', attrs={'class':'infobox biota'})
	return sections

print(get_dino(sys.argv[1]))
