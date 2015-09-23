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
        self._visited_list = set([])

    def __repr__(self):
        """
        returns easy-to visualize version of queue
        """
        representation = "Queue: "
        for item in self._search_queue:
            representation += str(item) + '\t'
        representation += '\nVisited: '
        for item in self._visited_list:
            representation += str(item) + '\t'
        return representation

    def check_visited(self, url):
        """
        checks if supplied URL has been visited
        returns Boolean
        """
        return url in self._visited_list

    def enqueue(self, url):
        """
        enqueues supplied url
        checks to make sure not visited
        """
        if not self.check_visited(url):
            self._search_queue.append(url)

    def dequeue(self):
        """
        dequeues and returns url from queue
        checks if url is in visited list
        if url is in visited list - pulls another one until queue is empty
        """
        if len(self._search_queue) > 0:
            test_url = self._search_queue.pop(0)
            if not self.check_visited(test_url):
                return test_url
            else:
                return self.dequeue()

    def add_to_visited(self, url):
        """
        adds supplied url to visited list
        """
        self._visited_list.add(url)

    def clear_visited_list(self):
        """
        clears visited list of all value
        """
        self._visited_list = set([])
