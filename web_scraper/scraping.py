import logging
from typing import Dict, List, Set, Tuple

import requests
from bs4 import BeautifulSoup as Soup

HOST = 'https://www.jobs.bg/'
PATH = 'front_job_search.php'
CONTAINER_CLASS = 'mdc-layout-grid__inner'
JOB_LINK_CLASS = 'black-link-b'
COMPANY_LINK_CLASS = 'right'

logging.basicConfig(
    filename='scraping.log',
    level=logging.INFO,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)


def get_results_on_page(scraped_url: str) -> Dict[str, Set[Tuple[str, str]]]:
    """Return a dictionary where the keys are Python job titles, and the values
    are sets ot tuples containing company names and links to the job listings."""
    soup = Soup(scraped_url, 'lxml')
    results_dict = {}

    for search_result_row in soup.find_all('div', class_=CONTAINER_CLASS):
        job_link = search_result_row.find('a', class_=JOB_LINK_CLASS)
        company_link = search_result_row.find('div', class_=COMPANY_LINK_CLASS)

        if job_link and 'Python' in job_link['title']:
            company_description = company_link.find('a')['title'] if company_link and company_link.find('a') else ''
            job_description = job_link['title']
            link = job_link['href']

            results_dict[job_description] = results_dict.get(
                job_description, {(company_description, link)}).union({(company_description, link)})

    return results_dict


def print_jobs(limit: int = 3) -> List[dict]:
    """Construct urls for scrapping in the range of the limit parameter,
    get the results on the page and return them as a list of dictionaries.
    """
    results = []

    for i in range(limit):
        scraped_url = f'{HOST}{PATH}?frompage={i * 15}&location_sid=1&keywords%5B0%5D=python'

        try:
            request = requests.get(scraped_url).text
            result = get_results_on_page(request)
            if result and result not in results:
                results.append(result)
        except ImportError as e:
            logging.error("Page couldn't load properly: %s", e)

    return results


print_jobs()
