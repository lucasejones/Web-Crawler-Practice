import requests
from bs4 import BeautifulSoup


'''
This module demonstrates similar functionality to the other module here, but importantly does not scale well to multiple job title inputs.

I'm leaving this here for future reference in case this is a useful structure for another context.
'''

def create_soup(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	return soup


stirred_soup = create_soup("https://realpython.github.io/fake-jobs/")

def get_results(soupy):
	results = soupy.find(id='ResultsContainer')
	return results


soup_results = get_results(stirred_soup)
# print(soup_results)



def get_desired_jobs(soupy_results, title):
	"""
	Takes a beautiful soup object and a keyword related to the position you seek.
	Returns all jobs as a list of tuples, each containing the job title, the company name, and the location
	"""

	specific_jobs = soupy_results.find_all(
		'h2', string=lambda text: title in text.lower()
		)
	# print(python_jobs)

	specific_job_elements = [
		h2_element.parent.parent.parent for h2_element in specific_jobs
	]

	# print(python_job_elements)

	new_jobs = []
	for job_element in specific_job_elements:
		application_link = job_element.find_all('a')[1]['href']

		title_element = job_element.find('h2', class_='title')
		company_element = job_element.find('h3', class_='subtitle')
		location_element = job_element.find('p', class_='location')
		new_jobs.append((title_element.text.strip(), company_element.text.strip(), location_element.text.strip(), application_link))

	return new_jobs


desired_jobs = get_desired_jobs(soup_results, 'software')

for job in desired_jobs:
	print('Details: ', job[:-1])
	print('Apply here:', job[-1])
	print()



