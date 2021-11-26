# scraper

execution: python scraper.py

This is a simple scraper built with python and utilizes the BeautifulSoup module.  
First draft only scrapes the first page of cars for sale and extracts the following details  
  description of post  
  price  
  location  
  link to the posts page on craigslist  

Recent Additions:  
Scraper, Database, DescParser and CarScraper classes created  
sqlite database created to store all items found on cars for sale craiglist page  
another scraper in the works for gathering all car makes and models  
  I want to use this to parse craigslist descriptions for this information so that I  
  can store car year make and model in database  
  
TODOS  
-might want to integrate more url's for scraping more than just the cars for sale page  
-allow for querying of scraped data(price, location, time of post, limit to first 10 posts, etc.)  
-may want to add other pieces of data for post objects(time of post) 
-continuing work on carsScraper to get all models for each make  

CLASS INFO:  
  
Scraper class:  
gather post elements from craigslist cars for sale page and store into sqlite database  

CarsScraper class:
gather post elements from  https://www.supercars.net/blog/all-brands/ to store all makes  
and models into a dictionary for DescParser class 

DescParser class:  
take a string description from a craigslist post and find a year make, and model if available  

DB class:  
initialize sqlite database for craigslist post information  
store Post objects provided by Scraper

Post class:
simple class to hold information provided by web scraper 


Demo output:  
some diagnostic output showing the scraping of multiple pages  
![Screenshot (429)](https://user-images.githubusercontent.com/43590688/143510463-be984d09-189f-45c0-b969-45ab573bdffc.png)  

sqlite database contents from Scraper class that was found in craigslist cars for sale pages  
![Screenshot (430)](https://user-images.githubusercontent.com/43590688/143510494-568a0f48-3ba1-468f-9a4e-1a2133191de9.png)

