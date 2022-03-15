import csv
import time
import tkinter as tk

from selenium import webdriver

root = tk.Tk()
root.geometry("400x300")
root.title("Youtube Scarping Comment")

items = []

tk.Label(root, text="copy link", font="arial 15 bold").grid(row=0, column=0)
link = tk.StringVar()
tk.Entry(root, textvariable=link).grid(row=0, column=1)


def OpenDriver():
    driver = webdriver.Chrome("E:\Program Files\chromeDriver\chromedriver.exe")
    driver.get(link.get())
    driver.execute_script('window.scrollTo(1, 500)')
    time.sleep(5)
    driver.execute_script('window.scrollTo(1, 3000);')
    username_elems = driver.find_elements_by_xpath('//*[@id="author-text"]')
    comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
    for username, comment in zip(username_elems, comment_elems):
        item = {}
        item['Author'] = username.text
        item['Comment'] = comment.text
        items.append(item)
    filename = "comments.csv"
    with open(filename, "w", newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, ['Author', 'Comment'])
        w.writeheader()
        for item in items:
            w.writerow(item)
    driver.close()


tk.Button(root, text="Open", bg="white",
          padx=2, command=OpenDriver).grid(row=0, column=2)
root.mainloop()
