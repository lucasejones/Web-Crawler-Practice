import requests
from bs4 import BeautifulSoup


def create_soup(url: str) -> object:
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	return soup

# URL = "https://info.nsf.org/Certified/Common/Company.asp?CompanyName=3m&Standard=061"
stirred_soup = create_soup("https://realpython.github.io/fake-jobs/")

def find_soup_results(soup: object) -> object:
	results = soup.find(id="ResultsContainer")
	return results


soup_results = find_soup_results(stirred_soup)

def get_job_elements(soupy_results: object) -> list:
	"""
	Takes a beautiful soup object.
	Returns all jobs as a list of tuples, each containing the job title, the company name, and the location
	"""

	job_elements = soupy_results.find_all('div', class_='card-content')

	# for job_element in job_elements:
	# 	print(job_element, end='\n' * 2) 

	all_jobs = []
	for job_element in job_elements:
		title_element = job_element.find('h2', class_='title')
		company_element = job_element.find('h3', class_='subtitle')
		location_element = job_element.find('p', class_='location')
		all_jobs.append((title_element.text.strip(), company_element.text.strip(), location_element.text.strip()))

	return all_jobs


all_processed_jobs = get_job_elements(soup_results)
# print(all_processed_jobs)


def desired_jobs_only(scraped_jobs: list, *titles: str) -> list:
	"""
	Takes a list of jobs and an arbitrary number of job titles you'd like to identify from that list. 
	Returns: A list of tuples containing only jobs relevant to the passedd titles
	"""

	desired_jobs = []

	for job in scraped_jobs:
		for title in titles:
			if title in job[0].lower():
				desired_jobs.append(job)

	return desired_jobs


odd_jobs = desired_jobs_only(all_processed_jobs, 'broker', 'barrister', 'radiographer')
dev_jobs = desired_jobs_only(all_processed_jobs, 'developer', 'programmer', 'software')


## optional printed ouputs 
# print('_' * 40)
# print('All job titles: ', '\n')
# print(all_processed_jobs)
# print('_' * 40)
# print('Desired jobs only: ', '\n')
# print(desired_jobs_only(all_processed_jobs, 'broker', 'barrister', 'radiographer'))
# print('_' * 40)


def output_useful_job_details(desired_jobs: list) -> None:
	"""
	Takes the desired jobs as a list of tuples and prints it in a more readable format.
	"""

	print('_' * 40)
	print('All matching open roles: ', '\n')
	for role in desired_jobs:
		print(role)


print(output_useful_job_details(dev_jobs))

