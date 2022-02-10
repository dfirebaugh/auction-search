from sites.strategy_map import search_all_sites
from out.out import out
from gui.gui import init_gui
import yaml
from os.path import exists

default_config = {
    "use_gui": True,
    "generate_pdf": True,
}

def main():
    config = default_config
    if exists('./search.yml'):
        with open(r'./search.yml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)

    if(config["use_gui"] == False):
        search_list = config['search_parameters']

        found_auctions = []
        for search in search_list:
            found_auctions = search_all_sites(search)

        combined_results = ""
        for auction in found_auctions:
            combined_results += auction.text()

        return
    init_gui(config=config)


if __name__ == "__main__":
    main()
