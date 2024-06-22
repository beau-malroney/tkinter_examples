# import required library 
from threading import Thread
import webbrowser, webview
from tkinter import *
  
# creating root 
root = Tk() 
  
# setting GUI title 
root.title("WebBrowsers") 
  
# setting GUI geometry 
root.geometry("660x660") 

# Open website 
def open_site_in_tkinter(title, link):
    webview.create_window(title, link) 
    webview.start() 

# call webbrowser.open() function. 
def open_in_browser(link):  
    webbrowser.open(link) 

link = 'https://www.google.com'
title = "The Google"

t2 = Thread(target=open_in_browser, args=(link,)).start()
open_site_in_tkinter(title, link)
open_in_browser(link)