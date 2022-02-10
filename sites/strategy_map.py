from sites.Cannons import CannonsAuction
from auction.search import Search

auction_sites = [
    {
        "strategy": CannonsAuction,
        "base_url": "https://bid.cannonsauctions.com"
    },
    {
        "strategy": CannonsAuction,
        "base_url": "https://auction.ebidlocal.com"
    }
]

def search_all_sites(search):
    searcher = Search()

    results = []
    for site in auction_sites:
        response_list = searcher.request(site["strategy"], site["base_url"], search["search_term"], search["upper_limit"])
        for auction in response_list:
            results.append(auction)
    return results
