import statistics
import numpy
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
from matplotlib import pyplot

def convert(string):
    if ("to" in string.get_text()):
        # print(f"this one has a two in it: {string.get_text()}" )
        prices = string.get_text().replace("$","").replace(",","").replace(" ","").replace("to"," ").split()
        for i in prices:
            return float(i)
    else:
        return float(string.get_text().replace("$","").replace(",",""))

def performSearch(keyword):
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
            return output
            # summarize(keyword, output)
            # plotHistogram(keyword, output)

        except:
            print("Encountered an error. Please try again.")

def summarizeTest(keyword, output_list):
    output_string = f"Results for: {keyword.title()} \nPrice Range: ${min(output_list)} - ${max(output_list)}\nMedian Price: ${round(statistics.median(output_list),2)}\nMean Price: ${round(statistics.mean(output_list),2)}"
    return output_string

def summarize(keyword, output_list):
    print("\n--------------------------------------------------")
    print("{:^50}".format(f"Results for: {keyword.title()}"))
    print("--------------------------------------------------")
    print(f"Price Range: ${min(output_list)} - ${max(output_list)}")
    print(f"Median Price: ${round(statistics.median(output_list),2)}")
    print(f"Mean Price: ${round(statistics.mean(output_list),2)}")
    print(f"Mode Price: ${round(statistics.mode(output_list),2)}")
    print("--------------------------------------------------")

def plotHistogram(keyword, output_list):
    numpyArray = numpy.array(output_list)
    increment = max(output_list)/10
    bins_array = [0]
    total = 0
    for i in range(10):
        total+=increment
        bins_array.append(total)

    fig, ax = pyplot.subplots(figsize=(5,5), tight_layout = True)
    ax.hist(numpyArray, bins=bins_array, color="#09689B")
    ax.set_title(f"Prices: {keyword.title()}")
    ax.set_xlabel("prices")
    ax.set_ylabel("counts")

    pyplot.show()