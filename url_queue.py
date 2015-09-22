"""
Manage a Queue of URLs
Also keep track of visited URLs
"""


class URLSearchQueue:
    """
    Queue to manage URLs to be visited
    manages list of visited websites
    """

    def __init__(self):
        """
        sets up Queue object with empty queue
        and empty visited list
        """
        self._search_queue = []
        self._visited_list = []

    def check_visited(self, url):
        """
        checks if supplied URL has been visited
        returns Boolean
        """
        # TODO: This seems like it could be slow, depending
        return url in self._visited_list

    def enqueue(self, url):
        """
        enqueues supplied url
        """
        self._search_queue.append(url)
