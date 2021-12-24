import requests
import re

class CannonsAuction:
    def search(self, term):
        pageSize = 100
        url = "https://bid.cannonsauctions.com/Public/GlobalSearch/GetGlobalSearchResults?pageNumber=1&pagesize={}&filter=Current&sortBy=enddate_asc&search={}".format(pageSize, term)

        payload={}
        headers = {}

        self.response = requests.request("GET", url, headers=headers, data=payload)
        print(self.response.text)
        print("$"+self.getPrice(self))
    def getPrice(self):
        match = re.search('Current Bid : (\d+)', self.response.text)
        if match:
            return match.group(1) 
        return ""