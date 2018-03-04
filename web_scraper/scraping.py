import requests
from bs4 import BeautifulSoup as Soup

print()


# we use class_ bec class is a keyword in Python
def get_results_on_page(scraped_url):
    soup = Soup(scraped_url, 'lxml')
    results_list = []
    results_dict = {}

    for search_result_row in soup.find_all('tr'):
        job_link = search_result_row.find('a', class_="joblink")
        company = search_result_row.find('a', class_="company_link")
        if job_link and "Python" in job_link.text:
            if job_link not in results_list:
                results_list.append(job_link)
                job_description = job_link.text
                company_description = company.text
                link = job_link['href']
                if job_description not in results_dict:
                    results_dict[job_description] = company_description, "https://www.jobs.bg/" + link
                else:
                    results_dict[job_description] += company_description, "https://www.jobs.bg/" + link
                #print(job_description)
                #print("Company: " + company_description)
                #print("Go to offer: https://www.jobs.bg/" + link)
                #print()
    #print(results_dict)
    return results_dict


def print_jobs():
    try:
        scraped_url1 = requests.get(
            "https://www.jobs.bg/front_job_search.php?&location_sid=1&keywords%5B0%5D=python").text
        scraped_url2 = requests.get(
            "https://www.jobs.bg/front_job_search.php?frompage=15&location_sid=1&keywords%5B0%5D=python").text
        scraped_url3 = requests.get(
            "https://www.jobs.bg/front_job_search.php?frompage=30&location_sid=1&keywords%5B0%5D=python").text

        return get_results_on_page(scraped_url1), get_results_on_page(scraped_url2), get_results_on_page(scraped_url3)

    except ImportError as e:
        print("Pages couldn't load properly. Sorry for the inconvenience: ", e)

print_jobs()