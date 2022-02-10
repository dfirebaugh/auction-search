class Search:
    def request(self, auction, base_url, term, price_upper_limit):
        self.price_upper_limit = price_upper_limit
        auctions = auction.search(auction, base_url, term)
        return self.filter_auctions_by_price(auctions)
    def filter_auctions_by_price(self, auctions):
        filtered_auctions = []
        for auction in auctions:
            if auction.current_bid is None:
                continue
            if float(auction.current_bid) < float(self.price_upper_limit):
                filtered_auctions.append(auction)

        return filtered_auctions
