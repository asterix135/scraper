"""
Specific implementation to crawl BC gov directory
"""

import parse_page
import url_queue

TEST_START = 'goaBrowse'
START_PAGE = 'http://alberta.ca/albertaFiles/includes/directorysearch/dsp_browse_ministry_hierarchy.cfm?item=1'
URL_START = 'http://alberta.ca/albertaFiles/includes/directorysearch/'


def alberta_directory_crawl():
    """
    Main routine to crawl AB government directory
    """
    crawl_queue = url_queue.URLSearchQueue()
