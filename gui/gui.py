from tkinter import *
from tkinter import ttk
from sites.strategy_map import search_all_sites
from out.out import out

def init_gui():
    main_view().mainloop()

def main_view():
    root = Tk()
    frm = ttk.Frame(root, padding=10, height=1000, width=1280)
    frm.grid()
    e1 = ttk.Entry(frm)
    e2 = ttk.Entry(frm)
    ttk.Label(frm, text="Search Term").grid(column=0, row=0)
    e1.grid(row=1, column=0)
    ttk.Label(frm, text="Upper Limit").grid(column=1, row=0)
    e2.grid(row=1, column=1)
    ttk.Button(frm, text="Seach", command=(lambda e=frm: execute_search(e1.get(),e2.get()))).grid(column=2, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=4)
    return root

def execute_search(search_term, upper_price_limit):
    print("execute search...")
    print(search_term)
    print(upper_price_limit)
    found_auctions = search_all_sites({"search_term": search_term, "upper_limit": upper_price_limit})
    combined_results = ""
    for auction in found_auctions:
        combined_results += auction.text()
    out(results=combined_results)
