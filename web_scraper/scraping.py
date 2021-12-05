import logging
from typing import Dict, List, Set, Tuple

import requests
from bs4 import BeautifulSoup as Soup

HOST = 'https://www.jobs.bg/'
PATH = 'front_job_search.php'

logging.basicConfig(
    filename='scraping.log',
    level=logging.WARNING,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)


def get_results_on_page(scraped_url: str) -> Dict[str, Set[Tuple[str, str]]]:
    """Return a dictionary where the keys are Python job titles, and the values
    are sets ot tuples containing company names and links to the job listings."""
    soup = Soup(scraped_url, 'lxml')
    results_dict = {}

    for search_result_row in soup.find_all('tr'):

        job_link = search_result_row.find('a', class_='card__title')
        company_link = search_result_row.find('a', class_='company_link')
        if job_link and 'Python' in job_link.text:
            job_description = job_link.text
            company_description = company_link.text
            link = job_link['href']
            if job_description not in results_dict:
                results_dict[job_description] = {(company_description, HOST + link)}
            else:
                results_dict[job_description].add((company_description, HOST + link))

    return results_dict


def print_jobs(limit: int = None) -> List[dict]:
    """Construct urls for scrapping in the range of the limit parameter,
    get the results on the page and return them as a list of dictionaries.
    """
    if limit is None:
        limit = 3
    results = []

    for i in range(limit):
        scraped_url = f'{HOST}{PATH}?frompage={i * 15}&location_sid=1&keywords%5B0%5D=python'
        try:
            request = requests.get(scraped_url).text
            result = get_results_on_page(request)
            if result:
                results.append(result)
        except ImportError as e:
            logging.error("Page couldn't load properly: %s" % e)

    return results


print_jobs()
