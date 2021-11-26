import requests
from post import Post
from database import DB
from bs4 import BeautifulSoup

class Scraper():
    def __init__(self):
        self.__db = DB()
        # used to gather relevent elements and store information in Post object
        self.__list = []
        # used to store Post objects
        self.__findings = []
        # currently only url for cars and trucks for sale on craigslist
        self.__url = "https://chico.craigslist.org/d/cars-trucks/search/cta"
        # posts in one craisglist page, used for incrementing through all pages
        self.__itemsPerPage = 120
        
    def retrievePosts(self):
        page = requests.get("https://chico.craigslist.org/d/cars-trucks/search/cta")
        soup = BeautifulSoup(page.content, "html.parser")
        totalItems = soup.find(class_='totalcount')
        print("Scraper retrieving data...")
        print("total items retrieved " + totalItems.string)
        # itemsPerPage = 120
        firstRun = True
        # process all carPosts on page
        while self.__itemsPerPage < int(totalItems.string):
            # IF FIRST RUN URL IS ROOT URL
            if firstRun:
                URL = "https://chico.craigslist.org/d/cars-trucks/search/cta"
                print("first run")
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")
                self.__list = soup.find_all(class_='result-info')
                firstRun = False
                for item in self.__list:
                    # print(item)
                    description = item.find(class_="result-title hdrlnk")
                    url = description['href']
                #    print(description['href'])
                    #print(description.string)
                    price = item.find(class_="result-price")
                    location = item.find(class_="result-hood")

                    post = Post(description.string,price.string,location.string, url)
                    self.__findings.append(post)
                print('end first run')

            else:
                # IF NOT FIRST RUN URL APPENDS itemsPerPage IN URL TO GO TO NEXT LIST OF POSTS
                print("running " + str(self.__itemsPerPage))
                URL = "https://chico.craigslist.org/d/cars-trucks/search/cta?s=" + str(self.__itemsPerPage)
                # get page to process with url
                page = requests.get(URL)
                #parse page from get request
                soup = BeautifulSoup(page.content, "html.parser")
                # list of all car post findings
                self.__list = soup.find_all(class_='result-info')
                for item in self.__list:
                    # print(item)
                    description = item.find(class_="result-title hdrlnk")
                    url = description['href']
                    price = item.find(class_="result-price")
                    location = item.find(class_="result-hood")
                    # create post object and add to findings
                    post = Post(description.string,price.string,location.string, url)
                    self.__findings.append(post)
                self.__itemsPerPage += 120
                print("done running " + str(self.__itemsPerPage))


        counter = 1
        for post in self.__findings:
            self.__db.insertPost(post)
            # print(counter)
            # print(post.description)
            # print(post.price)
            # print(post.location)
            # print(post.url)
            # print("\n\n")
            # counter += 1

    # present raw data of posts stored in database from craigslist cars for sales page
    def presentDBContents(self):
        for entry in self.__db.getData():
            print(entry)
        # for entry in self.__db.getData():
        #     print(entry)
    # I'm using this to gather test strings into a list for a string parser that will gather information for car year
    # and posibly make and model
    def presentCarDescs(self):
        for desc in self.__db.getPostDescriptions():
            print(desc)

def main():
    scraper = Scraper()
    # print('yes')
    scraper.retrievePosts()
    scraper.presentCarDescs()
    # db = DB()
    # list = []
    # findings = []
    #
    # URL = "https://chico.craigslist.org/d/cars-trucks/search/cta"
    # itemsPerPage = 120
    #
    # page = requests.get(URL)
    # #print(page.content)
    # soup = BeautifulSoup(page.content, "html.parser")
    # totalItems = soup.find(class_='totalcount')
    # print(totalItems.string)


    # itemsPerPage = 120
    # firstRun = True
    # # process all carPosts on page
    # while itemsPerPage < int(totalItems.string):
    #     # IF FIRST RUN URL IS ROOT URL
    #     if firstRun:
    #         URL = "https://chico.craigslist.org/d/cars-trucks/search/cta"
    #         page = requests.get(URL)
    #         soup = BeautifulSoup(page.content, "html.parser")
    #         list = soup.find_all(class_='result-info')
    #         firstRun = False
    #         for item in list:
    #             # print(item)
    #             description = item.find(class_="result-title hdrlnk")
    #             url = description['href']
    #         #    print(description['href'])
    #             #print(description.string)
    #             price = item.find(class_="result-price")
    #             location = item.find(class_="result-hood")
    #
    #             post = Post(description.string,price.string,location.string, url)
    #             findings.append(post)
    #
    #
    #     else:
    #         # IF NOT FIRST RUN URL APPENDS itemsPerPage IN URL TO GO TO NEXT LIST OF POSTS
    #         URL = "https://chico.craigslist.org/d/cars-trucks/search/cta?s=" + str(itemsPerPage)
    #         # get page to process with url
    #         page = requests.get(URL)
    #         #parse page from get request
    #         soup = BeautifulSoup(page.content, "html.parser")
    #         # list of all car post findings
    #         list = soup.find_all(class_='result-info')
    #         for item in list:
    #             # print(item)
    #             description = item.find(class_="result-title hdrlnk")
    #             url = description['href']
    #             price = item.find(class_="result-price")
    #             location = item.find(class_="result-hood")
    #             # create post object and add to findings
    #             post = Post(description.string,price.string,location.string, url)
    #             findings.append(post)
    #         itemsPerPage += 120
    #
    #
    # counter = 1
    # for post in findings:
    #     db.insertPost(post)
    #     # print(counter)
    #     # print(post.description)
    #     # print(post.price)
    #     # print(post.location)
    #     # print(post.url)
    #     # print("\n\n")
    #     # counter += 1
    #
    #
    #
    # for entry in db.getData():
    #     print(entry)
main()
