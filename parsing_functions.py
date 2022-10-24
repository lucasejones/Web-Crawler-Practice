import requests
from bs4 import BeautifulSoup


def create_soup(url: str) -> object:
	"""
	Takes the url of the page you'd like to scrape.
	Returns the html as a beautiful soup object
	"""

	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	return soup


def get_company_elements(soup_results: object) -> dict:
	"""
	Takes a beautiful soup object.
	Returns: all companies as a dictionary, where each key is the company name and each value is
	the corresponding link to the company's certification details page.
	"""

	content_area = soup_results.find(id='content-area')
	# print(content_area)
	companies = content_area.find_all('table')

	all_companies = {}
	for company in companies:
		products_link_fragment = company.find_all('a')[0]['href']
		products_link_beginning = 'https://info.nsf.org'
		products_link = products_link_beginning + products_link_fragment
		company_name = company.find('a').text.strip()

		formatted_company_name = handle_duplicates(all_companies, company_name)
		all_companies[formatted_company_name] = products_link

	return all_companies


def handle_duplicates(companies_dict: dict, name: str) -> str:
	"""
	Takes the dictionary of existing companies and if the entry is a duplicate, appends a unique
	identifying string.
	Returns the new, unique company entry name
	"""

	entry_count = 2
	while True:
		if name in companies_dict:
			if entry_count == 2:
				name = name + ' (entry 2)'
				entry_count += 1

			elif entry_count > 2:
				previous_entry_substring = f'(entry {entry_count - 1})'
				updated_entry_substring = f'(entry {entry_count})'
				name = name.replace(previous_entry_substring,
													updated_entry_substring)
				entry_count += 1
		else:
			break

	return name


def get_desired_companies_only(scraped_companies: dict, name: str) -> dict:
	"""
	Takes the dictionary of scraped companies and the company name input by the user.
	Returns: A dictionary containing only companies relevant to the user input, where the key is
	the company name and the value is the corresponding link to the company's certification
	details page.
	"""

	desired_companies = {}
	for company in scraped_companies:
		if name in company.lower().strip(',.') or name in company.strip(',.'):
			desired_companies[company] = scraped_companies[company]

	return desired_companies



def output_useful_company_details(user_companies: dict, name: str) -> None:
	"""
	Takes the scraped information for desired companies as a dict, and the user-input company
	name as a string and prints it in a more readable format.
	"""

	print('_' * 40)
	print(f'{len(user_companies)} matching listings for "{name}": ', '\n')
	for company in user_companies:
		print('Company name: ', company)
		print('Details:', user_companies[company])
		print()
