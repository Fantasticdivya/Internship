#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# # Question-1 Write a python program to display IMDB’s Top rated 100 Indian movies’ data
# https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year ofrelease) and make data frame.

# In[2]:


page = requests.get("https://www.imdb.com/list/ls056092300/") 
page


# In[3]:


# website is not allowing scraping so i am spcaping data from some other website 


# In[4]:


page = requests.get("https://www.moviecrow.com/hindi/top-100-movies")
page


# In[5]:


soup = BeautifulSoup(page.content)


# In[6]:


movies = []

for i in soup.find_all('div',class_="film_name"):
    movies.append(i.text.replace('\n',''))
    
movies    


# In[7]:


ratings = []

for i in soup.find_all('div',class_="movies_rating"):
    ratings.append(i.text.replace('\n',''))
    
ratings    


# In[8]:


storyline = []

for i in soup.find_all('div',class_="story_line"):
    storyline.append(i.text.replace('\n',''))
    
storyline    


# In[9]:


len(movies),len(ratings),len(storyline)


# In[10]:


#making dataframe
df = pd.DataFrame({'Titles':movies, 'Ratings': ratings, 'Stoyline':storyline})

df


# # Question-2   Write a python program to scrape details of all the posts from https://www.patreon.com/coreyms .Scrape the
# heading, date, content and the likes for the video from the link for the youtube video from the post.

# In[11]:


page = requests.get("https://www.patreon.com/coreyms")
page


# In[12]:


soup = BeautifulSoup(page.content)


# In[13]:


soup


# In[14]:


soup.title.text


# In[15]:


heading = []

for i in soup.find_all('div',class_="sc-bBHxTw jIEOUn"):
    heading.append(i.text)
    
heading    


# In[16]:


date = []

for i in soup.find_all('div',class_="sc-1vtl1y3-0 a-DGjN"):
    date.append(i.text)
    
date    


# In[17]:


content = []

for i in soup.find_all('div',class_="sc-cfnzm4-0 daxSFj"):
    content.append(i.text)
    
content    
    


# In[18]:


likes = []

for i in soup.find_all('span',class_="sc-dkPtRN eEJGed"):
    likes.append(i.text)
    
likes    


# In[19]:


# in the above quetion no 2 i am not able to fetch data from website even after trying multiple times and using different tags and classes. 


# # Question-3 Write a python program to scrape house details from mentioned URL. It should include house title, location,
# area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar,
# Rajaji Nagar

# In[20]:


page = requests.get("https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NzgzNjkyLCJsb24iOjc3LjY0MDgzNTYsInBsYWNlSWQiOiJDaElKa1FOM0dLUVdyanNSTmhCUUpyaEdEN1UiLCJwbGFjZU5hbWUiOiJJbmRpcmFuYWdhciJ9LHsibGF0IjoxMi45MzA3NzM1LCJsb24iOjc3LjU4MzgzMDIsInBsYWNlSWQiOiJDaElKMmRkbFo1Z1ZyanNSaDFCT0FhZi1vcnMiLCJwbGFjZU5hbWUiOiJKYXlhbmFnYXIifSx7ImxhdCI6MTIuOTk4MTczMiwibG9uIjo3Ny41NTMwNDQ1OTk5OTk5OSwicGxhY2VJZCI6IkNoSUp4Zlc0RFBNOXJqc1JLc05URy01cF9RUSIsInBsYWNlTmFtZSI6IlJhamFqaW5hZ2FyIn1d&radius=2.0&city=bangalore&locality=Indiranagar,Jayanagar,Rajajinagar")
page


# In[21]:


soup = BeautifulSoup(page.content)


# In[22]:


titles = []

for i in soup.find_all('h2',class_="heading-6 flex items-center font-semi-bold m-0"):
    titles.append(i.text)
    
titles    


# In[23]:


location = []

for i in soup.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95"):
    location.append(i.text)
    
location    


# In[24]:


price_emi_area = []

for i in soup.find_all('div',class_="font-semi-bold heading-6" ):
    price_emi_area.append(i.text)
    
price_emi_area   


# # Question - 4 Write a python program to scrape first 10 product details which include product name , price , Image URL from
# https://www.bewakoof.com/bestseller?sort=popular

# In[25]:


page = requests.get("https://shop.bewakoof.com/bestseller?sort=popular")
page


# In[26]:


soup = BeautifulSoup(page.content)


# In[27]:


bestsellers = []

for i in soup.find_all('span',class_="sc-a6c4ca6a-0 PYPED"):
    bestsellers.append(i.text)
    
bestsellers 
top_10 = bestsellers[:10]
top_10   
    


# In[28]:


prices = []

for i in soup.find_all('div',class_="product-card_product_price_container__Ek01t"):
    prices.append(i.text.replace('₹','   '))
    
top_10_prices = prices[:10]
top_10_prices


# In[29]:


images = soup.find_all("img")


# In[30]:


image_urls = []
for image in images:
    if "src" in image.attrs:
        image_urls.append(image.attrs["src"])


for url in image_urls:
    print(url)
    
url = url[:10]
url
    


# # Question -5  Please visit https://www.cnbc.com/world/?region=world and scrap
# a)headings
# b) date
# c) News link

# In[31]:


cnbc_world = requests.get("https://www.cnbc.com/world/?region=world")
cnbc_world


# In[32]:


cnbc = BeautifulSoup(cnbc_world.content)


# In[33]:


heading=[]

for i in cnbc.find_all('a',class_='LatestNews-headline'):
    heading.append(i.text)
heading 


# In[34]:


time=[]
for i in cnbc.find_all('time',class_='LatestNews-timestamp'):
    time.append(i.text)
time


# In[35]:


links=[]
for i in cnbc.find_all('a',class_='LatestNews-headline'):
    links.append(i.get('href'))
links


# # Question-6 Please visit https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloadedarticles/
# and scrap
# a)Paper title
# b) date
# c) Author

# In[36]:


page =requests.get("https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/")
page


# In[37]:


soup = BeautifulSoup(page.content)


# In[38]:


titles = []
for i in soup.find_all('h2',class_="h5 article-title"):
    titles.append(i.text.replace('\n',' '))
    
titles    


# In[39]:


paper_titles = []

for i in soup.find_all('h2', class_="h5 article-title"):
    title = i.get_text(strip=True)  
    paper_titles.append(title)

print(paper_titles)


# In[40]:


date=[]
for i in soup.find_all('p',class_="article-date"):
     date.append(i.text)
        
        
date 


# In[41]:


authors = []
for i in soup.find_all('p',class_="article-authors"):
    authors.append(i.text)
    
authors    


# In[ ]:





# In[ ]:




