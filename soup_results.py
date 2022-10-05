import requests
from bs4 import BeautifulSoup


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

# finding just the job titles:
developer_jobs = soup_results.find_all(
	'h2', string=lambda text: 'python' in text.lower()
	)
print(developer_jobs)
