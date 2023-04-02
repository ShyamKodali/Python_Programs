# Web Scrapping using Requests and BeautifulSoup
# Importing neccessary Libraries 
import requests as re
from bs4 import BeautifulSoup


# 1. Inspect Data Source (Elements - HTML structure of that page) through Developer Tools on Browser 
# 2. Scrape HTML content from the page 
# 3. Parse HTML code with BeautifulSoup 

# =============================================================================
# Scrapping HTML content from the page : For Websites having LOGIN Authentication : If Response <200> Then it is OK Authentication so, we can Scrape
# from requests.auth import HTTPBasicAuth
# basic = HTTPBasicAuth('username', 'password')
# re.get('https://villagecinemas.com.au/vrewards/login/basic-auth/user/pass', auth=basic)
# =============================================================================


# =============================================================================
# url1 = 'https://realpython.github.io/fake-jobs/'
# response1 = re.get(url=url1).text
# print(response1)
# =============================================================================

url = 'https://realpython.github.io/fake-jobs/'
response = re.get(url=url)
soup = BeautifulSoup(response.content,'html.parser')
results = soup.find(id="ResultsContainer")

# Returns an Iterable containing all HTML content 
job_elements = results.find_all("div", class_="card-content")


# To find particular child element with class name 
for i in job_elements:
    title_element = i.find("h2", class_="title")
    company_element = i.find("h3", class_="company")
    location_element = i.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print('***************************')

# Returns an Iterable containing all HTML content of particular Text
job_elements_by_text = results.find_all("h2", string=lambda text:"Python" in text.lower())
python_job_elements = [ h2_element.parent.parent.parent for h2_element in job_elements_by_text ]

# To find particular Text content 
for j in python_job_elements:
    title_element_by_text = j.find("h2", class_="title")
    company_element_by_text = j.find("h3", class_="company")
    location_element_by_text = j.find("p", class_="location")
    print(title_element_by_text.text.strip())
    print(company_element_by_text.text.strip())
    print(location_element_by_text.text.strip())
    print('***************************')
    

# To find particular Link content 
for l in python_job_elements:
    links = l.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")

