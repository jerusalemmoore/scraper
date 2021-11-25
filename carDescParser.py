# parser reads description of craigslist post and tries to find year make and model
import re
class CarDescParser():
    def __init__(self):
        self.make = 'N/A'
        self.model = 'N/A'
        self.year = 'N/A'

    # take string and attempt to parse to get make, model, and year
    def parseDesc(self, description):
        # self.make = getMake(description)
        # self.model = getModel(description)
        self.year = getYear(description)

    # currently works for 4 digit year, need check for 2 digit year if no 4 digit year found
    # and edge case if no year found
    def getYear(self, description):
        year = re.search('(19[6789][0-9])|20[12345][0-9]', description)
        print(year)

parser = CarDescParser()
parser.getYear('2014 Audi A5 Premium Cabriolet 2D Convertible Silver - FINANCE ONLINE')
