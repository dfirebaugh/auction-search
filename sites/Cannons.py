import requests
from bs4 import BeautifulSoup
import re

from auction import Auction

class CannonsAuction:
    def search(self, base_url, search_term):
        self.search_term = search_term

        pageSize = 100
        self.base_url = base_url
        search_url = "/Public/GlobalSearch/GetGlobalSearchResults?pageNumber=1&pagesize={}&filter=Current&sortBy=enddate_asc&search={}".format(pageSize, search_term)

        payload={}
        headers = {}

        self.response = requests.request("GET", self.base_url+search_url, headers=headers, data=payload)
        return self.parse(self)
    def parse(self):
        parsed_auctions = []
        soup = BeautifulSoup(self.response.text, 'html.parser')
        current_auctions = soup.find("div", {"class": "search-listitem"})
        children = current_auctions.findChildren("div" , recursive=False)
        for child in children:
            auction = Auction()
            auction.set_search_term(self.search_term)
            current_bid = child.find(text=re.compile('Current Bid : (\d+)'))
            if current_bid:
                auction.set_current_bid(current_bid[-4:])
            links = child.find_all("a", {"class": "linkbutton"})
            for link in links:
                auction.lot_id = link.text.strip()
                auction.link = self.base_url+link['href']
            parsed_auctions.append(auction)
        return parsed_auctions
