import requests
from bs4 import BeautifulSoup

companies_url = 'https://info.nsf.org/Certified/Common/Company.asp?CompanyName=&Standard=061'
chemicals_url = 'https://info.nsf.org/Certified/Common/Company.asp?Standard=060'
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


	# # duplicate handling (under construction)
	# entry_count = 2
	# while True:
	# 	if company_name in all_companies:
	# 		initial_entry_substring = f'(entry {entry_count})'
	# 		entry_count += 1
	#
	# 		if entry_count == 3:
	# 			company_name = company_name + ' ' + initial_entry_substring
	# 			all_companies[company_name] = products_link
	#
	# 		elif entry_count > 3:
	# 			print(company_name, entry_count)
	# 			break
	# 			updated_entry_substring = f'(entry {entry_count})'
	# 			company_name = company_name.replace(f'(entry {entry_count - 1})',
	# 												updated_entry_substring)
	# 				# first time this runs:
	# 				# initial entry substring is set to 3, updated is set to 4.
	# 				# but 3 entry 3 never exists in this elif block.
	# 			all_companies[company_name] = products_link
	# 			entry_count += 1
	# 	else:
	# 		break


	all_companies[company_name] = products_link


for k, v in all_companies.items():
	if 'entry' in k:
		print(k, v)
	else:
		print(k, v)


# company_name = 'test company'
# initial_entry_substring = '(entry 2)'
# new_substring = '(entry 3)'
#
# company_name = company_name + ' ' + initial_entry_substring
# company_name = company_name.replace(initial_entry_substring, new_substring)

# print(company_name)

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
