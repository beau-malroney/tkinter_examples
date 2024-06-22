import tkinter as tk
from tkhtmlview import HTMLLabel
root = tk.Tk()
root.title("Web Browser Window")
root.geometry("720x250")
browser = HTMLLabel(root)
browser.pack(fill="both", expand=True)
browser.set_html('<h1>Hello, world!</h1>')
root.mainloop()