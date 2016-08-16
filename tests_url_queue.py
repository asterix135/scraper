"""
Test battery for url_queue class
"""

import url_queue
TESTURL1 = 'http://www.google.ca'
TESTURL2 = 'http://www.google.com'
TESTURL3 = 'http://www.google.ca/'
TESTURL4 = 'http://www.google.ca'


def test1():
    """
    test creation of UrlSearchQueue
    """
    test_queue = url_queue.URLSearchQueue()
    if type(test_queue) == url_queue.URLSearchQueue:
        print(str(test_queue))
        print('test 1 succeeded\n')
    else:
        print('test 1 failed\n')
    return test_queue


def test2(urlqueue):
    """
    test enqueuing of url
    """
    urlqueue.enqueue(TESTURL1)
    urlqueue.enqueue(TESTURL2)
    urlqueue.enqueue(TESTURL3)
    urlqueue.enqueue(TESTURL4)
    print('\ntest2:')
    print(str(urlqueue))


def test3(urlqueue):
    """
    test dequeuing of url
    """
    print('\ntest3:')
    print(urlqueue.dequeue())
    print(urlqueue.dequeue())
    print(str(urlqueue))


def test4(urlqueue):
    """
    tests adding url to visited list
    """
    print('\ntest4:')
    urlqueue.add_to_visited(TESTURL1)
    urlqueue.add_to_visited(TESTURL3)
    print(str(urlqueue))


def test5(urlqueue):
    """
    tests adding url to queue when url is in visited list
    """
    print('\ntest 5:')
    urlqueue.enqueue(TESTURL1)
    urlqueue.enqueue(TESTURL2)
    print(str(urlqueue))


def test6(urlqueue):
    """
    tests dequeuing when url is in visited list
    """
    print('\ntest 6:')
    print(urlqueue.dequeue())
    print(str(urlqueue))


def test7(urlqueue):
    """
    tests clearing visited list
    """
    print('\ntest 7:')
    urlqueue.clear_visited_list()
    print(str(urlqueue))


def test_battery():
    """
    master control of tests
    """
    test_q = test1()
    test2(test_q)
    test3(test_q)
    test4(test_q)
    test5(test_q)
    test6(test_q)
    test7(test_q)


if __name__ == '__main__':
    test_battery()
