import requests
from bs4 import BeautifulSoup


# URL = "https://realpython.github.io/fake-jobs/"
URL = "https://info.nsf.org/Certified/Common/Company.asp?CompanyName=3m&Standard=061"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(page.text)
print('\n' * 100)
print(soup.prettify())

