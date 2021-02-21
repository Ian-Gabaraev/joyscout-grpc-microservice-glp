from scripts import env

import requests


class Page:

    def __init__(self, page):
        self.url = env['PS_URL']
        self.page = page

    @property
    def content(self):
        return requests.get(self.url % self.page).content

    @property
    def empty(self):
        return not bool(len(self.content) // 100_000)  # empty PS4 page averages 30,000 bytes


def approximate_range():
    """
    Running the binary search without a predetermined
    searching range is slow, therefore this algorithm
    defines a range of 20, among which there is the
    page that satisfies the requirement mentioned in
    the following docstring
    """
    start_with_page = env['START_WITH']

    while True:
        if Page(page=start_with_page).empty:
            return start_with_page-20, start_with_page
        else:
            start_with_page += 20


def find_final_page():
    """
    This binary search returns a value
    as soon as the following requirement is satisfied:

    ** page N is non-empty **
    ** page N+ is empty **

    where N is any positive integer, ranging from 0 to N+1,
    where 'emptiness' is defined by page's source code size
    """

    start, end = approximate_range()
    found = False

    while not found:
        median = (end + start) // 2
        if not Page(median).empty and Page(median+1).empty:
            found = True
        elif Page(median).empty:
            start = 0
            end = median
        elif not Page(median+1).empty:
            start = median
            end = end

    return int(median)
