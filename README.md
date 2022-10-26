# Certification Information Program

## Overview 

This is a companion repo to the Django-Site repo I'm also working on. Both repos ultimately seek 
to create a centralized location where civil engineers can easily determine the certification status of various manufacturers' products. 

While the other repo is focused on creating the site the engineer will ultimately interact with, 
this repo focuses on building the web scraping tools that will supply the data to that site.

### Example
Typing 'victa' into the search bar would display the names of the 5 entries on the National 
Sanitation Foundation website related to 
the company "Victaulic", the organization designation of NSF, as well as links for each entry.

## Future Progress
### Organizations to Scrape
As it currently stands, the files in here are specific to only a single certification site, but I'm 
working to add others. I will update this readme as I progress towards my goal. 

The certification organizations are:
1. The National Sanitation Foundation (NSF)
2. Underwriters Labs (UL)
3. Factory Mutual (FM)
4. Water Quality Association (WQA)
5. Canadian Standards Association (CSA)
6. International Association of Plumbing and Mechanical Officials (IAMPO)
7. Truesdale Labs


### Implementation
I intend to put the results from all 7 sites into a database, which will be accessed through 
user input on the Django site. When the user starts 
typing the company in question into the text field, this input queries the database and 
auto-completes any matching results 
(name, organization name, and link) underneath.
Then, when the user presses enter in their search, whatever links are displayed underneath become 
clickable, which when clicked redirect to the corresponding certification site.

 

