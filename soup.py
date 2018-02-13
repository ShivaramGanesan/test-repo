import urllib2
import re
#import urllib2.request as a

from bs4 import BeautifulSoup


def scrape_flipkart(fk_link):
	# for flipkart
	response = urllib2.urlopen('https://www.flipkart.com/nexus-5-white-16-gb/p/itmefwjz5azprgjm?pid=MOBDQ9VXXXX6NF8V&srno=s_1_2&otracker=search&lid=LSTMOBDQ9VXXXX6NF8VVGKG1A&fm=SEARCH&iid=e1398c39-e571-4b5f-b668-3dbba4df10e1.MOBDQ9VXXXX6NF8V.SEARCH&ppt=Search%20Page&ppn=Search%20Page&ssid=d54yt68ie80000001517501542914&qH=e39d50e6f69ef1da')
	html = response.read()

	soup = BeautifulSoup(html)

	rate = soup.find('div', {'class' : '_1vC4OE _37U4_g'})
	a = re.findall(">\d+,*\d+<", str(rate))
	prod_name = soup.find('h1', {'class' : '_3eAQiD'})

	name = re.findall("-->.+<!--", str(prod_name))


	print "prod name=", name[0][3:-4]
	print "Flipkart rate", a[0][1:-1]


def scrape_snapdeal(sd_link):
	#SNAPDEAL

	response1 = urllib2.urlopen('https://www.snapdeal.com/product/iball-compbook-exemplaire-notebook-intel/642208106293#bcrumbSearch:laptop')
	page = response1.read()

	soup1 = BeautifulSoup(page)

	product_name_snapdeal = soup1.find('h1', {'class' : 'pdp-e-i-head'}).string
	print 'name=', product_name_snapdeal
	rate_snapdeal = soup1.find('span', {'class' : 'payBlkBig'}).string
	print 'rate sd = ', rate_snapdeal

def find_link_flipkart(search_key):

def find_link_snapdeal(search_key):


search_key = raw_input()
fk_link = find_link_flipkart(search_key)
sd_link = find_link_snapdeal(search_key)
scrape_snapdeal(sd_link)
scrape_flipkart(fk_link)

