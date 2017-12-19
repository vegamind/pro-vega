
#TKINTER SCRIPT

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

def poop_poop():
    response = textInfo.get()
    if response != "":
        changeLabelText().set(response)
    return

def main():

    t = threading.Thread(target = poop_poop())

    response = textInfo.get()
    response = response.strip(" ") #removes leading and trailing spaces

    if response != "":
        showinfo("HEY!", "-->"+ response + "<--") #("title of box", text you entered)
        #showinfo("HEY!", "-->"+ response + "<--") #arrows used for checking spacing. Debug Only


    return

root = Tk()
root.title("tkat")

#root.resizable(0,0) #blocks changing size of window
mainFrame = ttk.Frame(root, padding="3 3 12 12") #tk.Frame also an option. Google it
mainFrame.grid(column = 0, row = 0, sticky = (N,W,E,S))
mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)

ttk.Label(mainFrame, text="testString").grid(column=1,row=1,sticky=W)
textInfo = StringVar()  #makes a text entry box
textInfoContents = ttk.Entry(mainFrame, width=13, textvariable=textInfo) #width of text entry box
textInfoContents.grid(column=1, row=2, sticky=(W,E)) #location of text entry box

save = ttk.Button(mainFrame, text="Save", command=main) #skip the "()" when calling main
save.grid(column=1, row=4, sticky=(W)) #variable.gridlocation(column=1, row=3, sticky=(W(*as in left side*)))

ttk.Label(mainFrame, text='').grid(column=1, row=3)
ttk.Label(mainFrame, text='').grid(column=1, row=5)
changeLabelText = StringVar()
changeLabel = ttk.Label(mainFrame, textvariable=changeLabelText).grid(column=1, row=6)


root.mainloop()
