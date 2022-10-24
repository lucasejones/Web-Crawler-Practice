import requests
from bs4 import BeautifulSoup

companies_url = 'https://info.nsf.org/Certified/Common/Company.asp?CompanyName=&Standard=061'
chemicals_url = 'https://info.nsf.org/Certified/Common/Company.asp?Standard=060'
# include units url as well

# page = requests.get(chemicals_url)
page = requests.get(companies_url)
soup = BeautifulSoup(page.content, 'html.parser')


content_area = soup.find(id='content-area')
# print(content_area)
companies = content_area.find_all('table')
# print(companies)

all_companies = {}
for company in companies:
	products_link_fragment = company.find_all('a')[0]['href']
	products_link_beginning = 'https://info.nsf.org'
	products_link = products_link_beginning + products_link_fragment
	company_name = company.find('a').text.strip()


	# duplicate handling
	entry_count = 2
	while True:
		if company_name in all_companies:
			if entry_count == 2:
				company_name = company_name + ' (entry 2)'
				entry_count += 1

			elif entry_count > 2:
				previous_entry_substring = f'(entry {entry_count - 1})'
				updated_entry_substring = f'(entry {entry_count})'
				company_name = company_name.replace(previous_entry_substring,
													updated_entry_substring)
				entry_count += 1
		else:
			break

	all_companies[company_name] = products_link


# for k, v in all_companies.items():
	# print(k, v)


title_input = input('Enter the company name that manufactures the product in question: ')

desired_companies = {}
for company in all_companies:
	if title_input in company.lower().strip(',.') or title_input in company.strip(',.'):
			desired_companies[company] = all_companies[company]

print('_' * 40)
print(f'{len(desired_companies)} matching listings for "{title_input}": ', '\n')
for company in desired_companies:
	print('Company name: ', company)
	print('Details:', desired_companies[company])
	print()



# concept:
# to incorporate multiple sites, you need to build multiple unique scrapers.
# once each scraper has been built and outputs a data structure containing the useful information,
	# you need to combine these into a super structure and iterate through them to find if there's
	# one or more matching links, so you can then return those matching links onto the browser.

# implementation:
# make a scrapers folder, put each of the 7 organizations into their own scraper in this folder
# outside that, make a module that imports these 7 and stores their ran outputs in a super structure
	# this module contains only function definitions
# main would then import and run this other module, along with any other necessary logic.

# future steps:
# could also put the results from all 7 sites into a database, and when the user starts typing it
# queries the database and auto-completes any matching results (name + link) underneath.
	# when the user presses enter in their search, whatever links are displayed underneath become
	# clickable, which when clicked redirect to the corresponding certification site.
# consider including some feature that indicates multiple certifications
