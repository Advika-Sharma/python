#import requests
#
#url = "https://real-time-amazon-data.p.rapidapi.com/deals-v2"
#
#querystring = {"country":"US","min_product_star_rating":"ALL","price_range":"ALL","discount_range":"ALL"}
#
#headers = {
#	"x-rapidapi-key": "4750d0bd76msh08c12eb80d7a0e1p13e88fjsna5930088e0bb",
#	"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
#}
#
#response = requests.get(url, headers=headers, params=querystring)
#
#print(response.json())

import requests
from bs4 import BeautifulSoup
url="https://finance.yahoo.com/quote/AMZN/"
headers={'user agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
html_page=requests.get(url,headers=headers)
soup=BeautifulSoup(html_page.content,'lxml')
header_info=soup.find_all('div',class_="left svelte-ezk9pj")[0]
stock_title=header_info.find('h1').get_text()
print(stock_title.content)