from out.slack import SlackHook
from out.pdf import generate_pdf

def print_auctions(auction_results):
    for auction in auction_results:
        print(auction.text())


def out(config=None, results="", search_term="", upper_price_limit=""):
    if config['generate_pdf'] == True:
        generate_pdf(search_term=search_term, upper_price_limit=upper_price_limit, auctions=results)
        print("done.")
        return

    slack_hook = config['slack_hook']

    if len(config["slack_hook"]) > 0:
        slack = SlackHook(slack_hook)
        slack.send(results)
        return
    print_auctions(results)
