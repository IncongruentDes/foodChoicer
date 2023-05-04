import requests
from bs4 import BeautifulSoup
import random

# get user input for location
location = "Tucson, AZ"

# scrape Yelp for restaurant names in that location
#url = f"https://www.yelp.com/search?find_desc=Restaurants&find_loc={location}"
url = f"https://www.yelp.com/search?find_desc=Restaurants&find_loc=Campbell-Grant%2C+Tucson%2C+AZ&attrs=RestaurantsPriceRange2.2&sortby=ratinghttps://www.yelp.com/search?find_desc=Restaurants&find_loc=Campbell-Grant%2C+Tucson%2C+AZ&attrs=RestaurantsPriceRange2.2%2CRestaurantsPriceRange2.1&sortby=rating&cflt=hotdogs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
#restaurant_tags = soup.find_all("h4", class_="css-1l5lt1i")
restaurant_tags = soup.find_all(rel = "noopener", class_= "css-1m051bw", role = "link")
# create list of restaurant names from scraped tags
restaurants = [tag.text for tag in restaurant_tags]

# randomly select three restaurant options
options = random.sample(restaurants, 3)

# print the options to the user
print("Here are three random restaurant options in Tucson, AZ:")
for i, option in enumerate(options):
    print(f"{i+1}. {option}")
