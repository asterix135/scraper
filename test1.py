import parse_page

TEST_MULTI = 'http://alberta.ca/albertaFiles/includes/directorysearch/goaBrowse.cfm?txtSearch=Service%20Alberta&Ministry=SA&LevelID=45901&userid=115325#115325&varExpandID=-1'
TEST_SINGLE = 'http://alberta.ca/albertaFiles/includes/directorysearch/goaBrowse.cfm?txtSearch=Service%20Alberta&Ministry=SA&LevelID=97332&userid=110353#110353&varExpandID=-1'
TEST_START = 'goaBrowse'


def test1():
    """
    Test page load function
    """
    page1 = parse_page.fetch_page(TEST_SINGLE)
    if page1:
        print('test 1 success')
    else:
        print('test 1 failure)')


def test2():
    page1 = parse_page.fetch_page(TEST_SINGLE)
    url_list = parse_page.extract_urls(page1, TEST_START)
    for item in url_list:
        print(item)


def test_battery():
    """
    Runs battery of tests
    Comment out as needed
    """
    test1()
    test2()


if __name__ == '__main__':
    test_battery()
