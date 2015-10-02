"""
Main control script to crawl info-go
"""
import url_queue


START_PAGE = 'http://www.infogo.gov.on.ca/infogo/office.do?actionType=telephonedirectory&unitId=%d'
DOMAINS = ['infogo.gov.on.ca']


def main_script(start_url, domain_list):
    ig_queue = url_queue.URLSearchQueue()
    ig_queue.enqueue(start_url)


print(__name__)