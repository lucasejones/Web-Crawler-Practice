import requests
from bs4 import BeautifulSoup

"""
This module focuses on scraping a hypothetical job listings website. 
Conceptually, it performs the following steps: 
	1. Requests the URL using the built-in requests library
	2. Parses its HTML using Beautiful Soup
	3. Identifies only the relevant information from any given job listing (title, company, location, and application link)
	4. Allows the user to filter further by providing as many desired job titles as they like
	5. Outputs all relevant data that reflects those job listings.
"""


def create_soup(url: str) -> object:
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	return soup

# URL = "https://info.nsf.org/Certified/Common/Company.asp?CompanyName=3m&Standard=061"


def find_soup_results(soup: object) -> object:
	results = soup.find(id="ResultsContainer")
	return results


def get_job_elements(soupy_results: object) -> list:
	"""
	Takes a beautiful soup object.
	Returns all jobs as a list of tuples, each containing the job title, the company name, the location, and a link through which to apply
	"""

	job_elements = soupy_results.find_all('div', class_='card-content')

	all_jobs = []
	for job_element in job_elements:
		application_link = job_element.find_all('a')[1]['href']
		title_element = job_element.find('h2', class_='title')
		company_element = job_element.find('h3', class_='subtitle')
		location_element = job_element.find('p', class_='location')
		all_jobs.append((title_element.text.strip(), company_element.text.strip(), location_element.text.strip(), application_link))

	return all_jobs


def desired_jobs_only_list(scraped_jobs: list, titles: list) -> list:
	"""
	Takes a list of jobs and a list of job titles you'd like to identify.
	Returns: A list of tuples containing only jobs relevant to the passed titles
	"""

	desired_jobs = []

	for job in scraped_jobs:
		for title in titles:
			if title in job[0].lower():
				desired_jobs.append(job)

	return desired_jobs


def desired_jobs_only(scraped_jobs: list, *titles: str) -> list:
	"""
	Takes a list of jobs and an arbitrary number of job titles you'd like to identify from that list. 
	Returns: A list of tuples containing only jobs relevant to the passed titles
	"""

	desired_jobs = []

	for job in scraped_jobs:
		for title in titles:
			if title in job[0].lower():
				desired_jobs.append(job)

	return desired_jobs


def output_useful_job_details(wanted_jobs: list) -> None:
	"""
	Takes the desired jobs as a list of tuples and prints it in a more readable format.
	"""

	print('_' * 40)
	print(f'{len(wanted_jobs)} matching open roles: ', '\n')
	for role in wanted_jobs:
		print('Details: ', role[:-1])
		print('Apply here:', role[-1])
		print()


if __name__ == "__main__":
	pass
	