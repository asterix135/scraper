import parse_page

TEST_MULTI = 'http://alberta.ca/albertaFiles/includes/directorysearch/goaBrowse.cfm?txtSearch=Service%20Alberta&Ministry=SA&LevelID=45901&userid=115325#115325&varExpandID=-1'
TEST_SINGLE = 'http://alberta.ca/albertaFiles/includes/directorysearch/goaBrowse.cfm?txtSearch=Service%20Alberta&Ministry=SA&LevelID=97332&userid=110353#110353&varExpandID=-1'
TEST_START = 'goaBrowse'
URL_START = 'http://alberta.ca/albertaFiles/includes/directorysearch/'


def test1():
    """
    Test page load function
    """
    page1 = parse_page.fetch_page(TEST_SINGLE)
    if page1:
        print('test 1 success\n')
        return page1
    else:
        print('test 1 failure\n')


def test2(soup_object):
    """
    Tests url extraction
    """
    url_list = parse_page.extract_urls(soup_object, TEST_START)
    print(url_list[:5])
    print('\ntest 2 successful\n')
    return url_list


def test3(url_list):
    """
    tests merging of URL head and tail
    """
    full_url_list = parse_page.append_to_url(url_list, URL_START)
    print(full_url_list[:5])
    print('\ntest3 successful\n')
    return full_url_list


def test_battery():
    """
    Runs battery of tests
    Comment out as needed
    """
    result1 = test1()
    result2 = test2(result1)
    test3(result2)


if __name__ == '__main__':
    test_battery()
