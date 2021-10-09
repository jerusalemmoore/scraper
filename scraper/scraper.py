import requests
from post import Post
from bs4 import BeautifulSoup

list = []
findings = []
URL = "https://chico.craigslist.org/d/cars-trucks/search/cta"
page = requests.get(URL)
#print(page.content)
soup = BeautifulSoup(page.content, "html.parser")
list = soup.find_all(class_='result-info')
counter = 0
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

for post in findings:
    print(post.description)
    print(post.price)
    print(post.location)
    print(post.url)
    print("\n\n")
