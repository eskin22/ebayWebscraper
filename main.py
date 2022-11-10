#importing libraries for use later
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import statistics
import methods

#define function for converting currency strings to floats for arithmetic
def convert(string):
    if ("to" in string.get_text()):
        # print(f"this one has a two in it: {string.get_text()}" )
        prices = string.get_text().replace("$","").replace(",","").replace(" ","").replace("to"," ").split()
        for i in prices:
            return float(i)
        
    
    else:
        return float(string.get_text().replace("$","").replace(",",""))

#prompt user for keyword, format that keyword for html, generate ebay url
print("\n--------------------------------------------------")
print("{:^50}".format("eBay Web-Scraper"))
print("--------------------------------------------------")
keyword = input("Please enter an item you would like to see price information for: ")
keyword_html = keyword.replace(" ", "+")
keyword_link = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312&_nkw={keyword_html}&_sacat=0"

#make new request with request library to ebay with some header information
req = Request(keyword_link, headers={'User-Agent':'Mozilla/5.0'})

#open the webpage using the get request that was returned
webpage = urlopen(req).read()
with requests.Session() as c:

    #call beautiful soup library object to make parsing/manipulating the html easier
    soup = BeautifulSoup(webpage, 'html.parser')

    #find all instances of the price label on the webpage
    list1 = soup.find_all("span", attrs="s-item__price")

    #try to convert the list of prices scraped into floats or throw exception
    try:
        output = list(map(convert, list1))
        methods.summarize(keyword, output)
        methods.plotHistogram(keyword, output)

    except:
        print("Encountered an error. Please try again.")

