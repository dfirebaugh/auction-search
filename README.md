# Auction Search
Search all those pesky auction sites for the items you are looking for.

This app is written in a way that you could add additional strategies for more sites without having to change much of the existing code.

## Config
You must update the `search.yml` file with your search parameters and slack hook (will potentially add additional communication strategies at a later time).

## Dependencies

```
pip install pyyaml
pip install requests
pip install beautifulsoup4
pip install reportlab
```

> note: on linux I had to run `sudo apt-get install python3-tk`
## Build

To build to an executable

```sh
python3.9.exe -m PyInstaller --onefile main.py
```
