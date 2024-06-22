import logging
from tkinter import *
import time 
from threading import *
from tkinter.scrolledtext import ScrolledText

threads = []

class TextHandler(logging.Handler):

    def __init__(self, text):
        logging.Handler.__init__(self)
        # Logging text
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text.configure(state='normal')
            self.text.insert(END, f"{record.threadName} {msg}\n")
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(END)
        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)

def createTextHanlder(textbox):
    text_handler = TextHandler(textbox)

    # Logging configuration
    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s [%(threadName)s] [%(levelname)s] %(name)s: %(message)s "
        )

    # Add the handler to logger
    logger = logging.getLogger()        
    logger.addHandler(text_handler)

# use threading   
def threading(): 
    # Call work function 
    t1=Thread(target=work) 
    t1.start() 
    threads.append(t1)
  
# work function 
def work(): 
    logging.info("sleep time start") 
  
    for i in range(10): 
        logging.info(i) 
        time.sleep(1) 
  
    logging.info("sleep time stop")

class myGUI(Frame):

    # This class defines the graphical user interface 

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.build_gui()

    def build_gui(self):                    
        # Build GUI
        self.root.title('Tkinter Threading')
        self.root.option_add('*tearOff', 'FALSE')
        self.grid(column=0, row=1, sticky='ew')
        self.grid_columnconfigure(0, weight=1, uniform='a')
        self.grid_columnconfigure(1, weight=1, uniform='a')
        self.grid_columnconfigure(2, weight=1, uniform='a')
        self.grid_columnconfigure(3, weight=1, uniform='a')

        # Add text widget to display logging info
        st = ScrolledText(self, state='disabled')
        st.configure(font='TkFixedFont')
        st.grid(column=0, row=1, sticky='swe', columnspan=3)

        createTextHanlder(st)

        # Create Button 
        Button(self.root,text="Eat Me",command = threading).grid(sticky='nw', column=0, row=0)
        Button(self.root,text="Drink Me",command = threading).grid(sticky='ne',column=4, row=0) 

def main():
    try:
        # Create Object 
        root = Tk() 
        myGUI(root)
        # Execute Tkinter
        root.mainloop()
    except Exception as e:
        logging.info(f"Failed with error.\n{e}")
    finally:
        for t in threads:
            logging.info(f"Joining thread {t.name}")
            t.join()
        logging.info("Processing completed")

main()