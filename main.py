import scraping_practice_multiple_parameters as file

"""
This module focuses on scraping a hypothetical job listings website. 
Conceptually, it performs the following steps: 
	1. Requests the URL using the built-in requests library
	2. Parses its HTML using Beautiful Soup
	3. Identifies only the relevant information from any given job listing (title, company, location, and application link)
	4. Allows the user to filter further by providing as many desired job titles as they like
	5. Outputs all relevant data that reflects those job listings.
"""


def main():
	stirred_soup = file.create_soup("https://realpython.github.io/fake-jobs/")
	# future URL = "https://info.nsf.org/Certified/Common/Company.asp?CompanyName=3m&Standard=061"

	soup_results = file.find_soup_results(stirred_soup)
	all_processed_jobs = file.get_job_elements(soup_results)
	
	# This is where you can easily create useful responses by specifying specific job titles you're seeking. 
	title_inputs = input('Enter any number of titles you\'re looking for, separated by a space: ')
	formatted_title_inputs = title_inputs.split(' ')
	print(formatted_title_inputs)

	dev_jobs = file.desired_jobs_only(all_processed_jobs, 'developer', 'programmer', 'software')
	odd_jobs = file.desired_jobs_only(all_processed_jobs, 'broker', 'barrister', 'radiographer')
	unique_jobs = file.desired_jobs_only_list(all_processed_jobs, formatted_title_inputs)

	print(file.output_useful_job_details(unique_jobs))


if __name__ == "__main__":
	main()
