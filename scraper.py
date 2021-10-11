import requests
from post import Post
from bs4 import BeautifulSoup

list = []
findings = []

URL = "https://chico.craigslist.org/d/cars-trucks/search/cta"
itemsPerPage = 120

page = requests.get(URL)
#print(page.content)
soup = BeautifulSoup(page.content, "html.parser")
totalItems = soup.find(class_='totalcount')
print(totalItems.string)


itemsPerPage = 120
firstRun = True
while itemsPerPage < int(totalItems.string):
    if firstRun:
        URL = "https://chico.craigslist.org/d/cars-trucks/search/cta"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        list = soup.find_all(class_='result-info')
        firstRun = False
        for item in list:
            # print(item)
            description = item.find(class_="result-title hdrlnk")
            url = description['href']
        #    print(description['href'])
            #print(description.string)
            price = item.find(class_="result-price")
            location = item.find(class_="result-hood")

            post = Post(description.string,price.string,location.string, url)
            findings.append(post)


    else:
        URL = "https://chico.craigslist.org/d/cars-trucks/search/cta?s=" + str(itemsPerPage)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        list = soup.find_all(class_='result-info')
        for item in list:
            # print(item)
            description = item.find(class_="result-title hdrlnk")
            url = description['href']
        #    print(description['href'])
            #print(description.string)
            price = item.find(class_="result-price")
            location = item.find(class_="result-hood")

            post = Post(description.string,price.string,location.string, url)
            findings.append(post)
        #
        # for post in findings:
        #     print(counter)
        #     print(post.description)
        #     print(post.price)
        #     print(post.location)
        #     print(post.url)
        #     print("\n\n")
        #     counter += 1

        itemsPerPage += 120
counter = 1

for post in findings:
    print(counter)
    print(post.description)
    print(post.price)
    print(post.location)
    print(post.url)
    print("\n\n")
    counter += 1
