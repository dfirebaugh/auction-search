from re import search

class Auction:
    current_bid = None
    def set_current_bid(self, bid):
        self.current_bid = bid
    def set_link(self, link):
        self.link = link
    def set_lot_id(self, lot_id):
        self.lot_id = lot_id
    def set_search_term(self, search_term):
        self.search_term = search_term
    def print(self):
        print("================")
        print("search_term: " + self.search_term)
        print("lot_id: "+ self.lot_id)
        if self.current_bid:
            print("current_bid: " + self.current_bid)
        print("link: " + self.link)
        print("\n")
    def text(self):
        current_bid = self.current_bid
        if self.current_bid is None:
            current_bid = "unknown"

        return f"================\nsearch_term: {self.search_term}\nlot_id: {self.lot_id}\ncurrent_bid: {current_bid}\nlink: {self.link}\n\n"
