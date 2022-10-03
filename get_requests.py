import requests
from bs4 import BeautifulSoup


URL = "https://realpython.github.io/fake-jobs/"
# URL = "https://info.nsf.org/Certified/Common/Company.asp?CompanyName=3m&Standard=061"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# print(page.text)
# print('\n' * 100)
# print(soup.prettify())



# URL = "https://info.nsf.org/Certified/Common/Company.asp?CompanyName=3m&Standard=061"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")


# finding all the engineer jobs
engineer_jobs = []
for text in soup.find_all('a'):
	job = text.get('href')
	if 'engineer' in job:
		engineer_jobs.append(job)



# formatting the job postings that contain an engineering role
import re 

stripped = []
for job in engineer_jobs:
	# print(job)
	leading = "https://realpython.github.io/fake-jobs/jobs/"
	useful = job[len(leading):]
	useful = useful.replace('.html', '')
	more_useful = useful.replace('-', ' ')
	even_more_useful = re.sub(r'[0-9]', '', more_useful)
	final = even_more_useful.strip()
	stripped.append(final)

# stripped = sorted(stripped)
# print(stripped)

# fixing entries to not begin with engineer
for job in stripped:
	if job[:8] == 'engineer':
		stripped.remove(job)
		job = job.replace('engineer ', '')
		job += ' engineer'
		stripped.append(job)


stripped = sorted(stripped)
# print(stripped)
	
for job in engineer_jobs:
	print(job)

for job in stripped:
	print(job)

print(len(stripped))



job_elements = results.find_all('div', class_='card-content')
# print(job_elements.prettify())
for job_element in job_elements:
	print(job_element, end='\n' * 2) 

