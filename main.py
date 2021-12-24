
"""
    runs on a schedule.
    contains a list of sites
    each site will have it's own implementation of how to preform a search
    we will likely need to parse the results from some of these sites because some of them return html
"""

from search import Search
from sites.strategy_map import auction_sites
from comms.slack import SlackHook
import yaml

with open(r'./search.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

def main():
    searcher = Search()
    search_list = config['search_parameters']

    found_auctions = []
    for search in search_list:
        for site in auction_sites:
            response_list = searcher.request(site["strategy"], site["base_url"], search["search_term"], search["upper_limit"])
            for auction in response_list:
                found_auctions.append(auction)

    combined_results = ""
    for auction in found_auctions:
        combined_results += auction.text()

    slack_hook = config['slack_hook']
    slack = SlackHook(slack_hook)
    slack.send(combined_results)

if __name__ == "__main__":
    main()
