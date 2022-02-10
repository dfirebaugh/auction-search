from sites.strategy_map import search_all_sites
from out.out import out
from gui.gui import init_gui
import yaml

with open(r'./search.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

def main():
    if(config["use_gui"] == True):
        init_gui(config=config)
        return

    search_list = config['search_parameters']

    found_auctions = []
    for search in search_list:
        found_auctions = search_all_sites(search)

    combined_results = ""
    for auction in found_auctions:
        combined_results += auction.text()

    out(config=config, results=combined_results)


if __name__ == "__main__":
    main()
