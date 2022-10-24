import parsing_functions as file

"""
This module focuses on scraping the National Sanitation Foundation website.
Conceptually, it performs the following steps:
	1. Requests the URL using the built-in requests library
	2. Parses its HTML using Beautiful Soup
	3. Identifies the relevant company entries from which the user seeks certification information
	4. Outputs links to that information
"""

nsf_companies_url = 'https://info.nsf.org/Certified/Common/Company.asp?CompanyName=&Standard=061'
nsf_chemicals_url = 'https://info.nsf.org/Certified/Common/Company.asp?Standard=060'

soup = file.create_soup(nsf_companies_url)
all_processed_companies = file.get_company_elements(soup)

title_input = input('Enter the company name that manufactures the product in question: ')

input_companies = file.get_desired_companies_only(all_processed_companies, title_input)
file.output_useful_company_details(input_companies, title_input)
