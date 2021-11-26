import requests
from post import Post
from database import DB
from bs4 import BeautifulSoup

# class  CarsScraper():
#     def __init__(self):
#         self.carMakesModels = {}
#         self.list = []
#         self.findings = []
#         self.url =
# dict to hold makes as key and list of models at value
makesModels = {}
# used for holding elements found on webpage
list = []
findings = []
url = "https://www.supercars.net/blog/all-brands/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
print("retrieving data...")
list = soup.find_all("a", {"rel":""})
# the process here checks for all anchor elements because all make names
# include one, as well as an empty rel val
# In order to acquire purely makes from the page takes additional processing
for item in list:
    # check if string from anchor element is one word as make is one work
    string = item.text
    wordsInString = string.split()
    if len(wordsInString) == 1:
        # on the webpage, all makes are completely uppercase, thus i use this
        # to get only elements with text that is all uppercase as chances are that word is a make
        if string.isupper():
            # check if I haven't already inserted a make into dict to hold makes and models
            if string not in makesModels.keys():
                makesModels[string] = []
# print(list)
print(makesModels)
