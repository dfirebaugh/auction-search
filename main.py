
"""
    runs on a schedule.
    contains a list of sites
    each site will have it's own implementation of how to preform a search
    we will likely need to parse the results from some of these sites because some of them return html
"""

from sites.Cannons import CannonsAuction
from search import Search

def main():
    searcher = Search()
    searcher.request(CannonsAuction, "drill")


if __name__ == "__main__":
    main()