# working on database for storing car posts from web scraper, currently db works
# with tests data
import sqlite3
import os
from post import Post
# establish database and return ptr to database
class DB:

    # constructor
    def __init__(self):
        # verification function checking if db exists
        def check_db(filename):
            return os.path.exists(filename)

        self.dbName = "scraperDB"
        self.conn = sqlite3.connect(self.dbName)
        exists = check_db(self.dbName)
        # print(exists)
        self.cursor = self.conn.cursor()
        # this commands makes a new table everytime db is initialized
        # the thought is since it is used for craigslist scraper at the moment
        # I want a table that represents the most recent set of posts on craigslist cars for sale page
        self.cursor.executescript('''
            DROP TABLE IF EXISTS carPosts;
            CREATE TABLE carPosts(
                id INTEGER,
                description STRING,
                price STRING,
                location STRING,
                url STRING,
                PRIMARY KEY(id));
                ''')
        self.conn.commit()



    # insert post object created by craigslist scraper into dababase
    def insertPost(self, post):
        desc = post.description
        price = post.price
        location = post.location
        url = post.url
        self.cursor.execute('INSERT INTO carPosts (description, price, location, url) VALUES(?, ?, ?, ?)',
                            (desc, price, location, url))
        self.conn.commit()
    # return query as list  for all posts
    def getData(self):
        self.cursor.execute('SELECT * FROM carPosts')
        return self.cursor.fetchall()

    def getPostDescriptions(self):
        self.conn.row_factory = lambda cursor, row: row[0]
        c = self.cursor
        descs = c.execute('SELECT description FROM carPosts').fetchall()
        return descs
    # make function for displaying data
# db = DB()

# diagnostic, run to make sure db functions work properly
# scraper = DB()
# for i in range(100):
#     post = Post("description", "price", "locaiton", "url")
#     scraper.insertPost(post)
# for post in scraper.getData():
#     # print("hello")
#     print(post)
# for desc in scraper.getPostDescriptions():
#     print(desc)
