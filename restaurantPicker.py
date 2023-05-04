#import section - remember to add to Mu/IDE
import requests
from bs4 import BeautifulSoup
import random


#setting url (TODO: add in categories for later)
url = f"https://www.yelp.com/search?find_desc=Restaurants&find_loc=Campbell-Grant%2C+Tucson%2C+AZ&attrs=RestaurantsPriceRange2.2%2CRestaurantsPriceRange2.1&sortby=rating&cflt=hotdogs%2Csandwiches%2Crestaurants%2Cfood%2Ctradamerican%2Cnewamerican%2Cpizza%2Cburgers&l=g%3A-111.00448608398438%2C32.199147648438405%2C-110.90217590332031%2C32.2862619119968"


#HTML work
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
restaurant_tags = soup.find_all(rel = "noopener", class_= "css-1m051bw", role = "link")
restaurants = [tag.text for tag in restaurant_tags]

# randomly select three restaurant options
options = random.sample(restaurants, 3)

# print the options to the user
print("Here are three random restaurant options in Tucson, AZ:")
for i, option in enumerate(options):
    print(f"{i+1}. {option}")
