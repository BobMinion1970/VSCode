import tkinter
import tkinter.font

######################################### Classes ##################################
class FirstGridGUI(tkinter.Frame):

    def __init__(self, parent):
        #tkinter.Frame.__init__(self)
        super().__init__(parent)
        self.createWidgets()
    
    def onLabelClick(self, event):
        if event.widget["text"] == "1":
            self.lblGray.configure(bg="red")

        if self.lblGray.cget("bg") == "gray":
            self.lblGray.configure(bg="red")

        
    def createWidgets(self):
       
        self.grid_rowconfigure( 0, weight=1)
        self.grid_columnconfigure( 0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.lblGray = tkinter.Label(text="1", bg='gray', font='Arial 24 bold')
        self.lblGray.bind('<Button-1>', self.onLabelClick)
        self.lblGray.grid(row=0, column=0, sticky="NESW")
        self.lblGreen = tkinter.Label(text="2", width=10, height=5, bg='green', font='Arial 24 bold')
        self.lblGreen.grid(row=0, column=1, sticky="NESW")
        self.lblYellow = tkinter.Label(text="3", width=10, height=5, bg='yellow', font='Arial 24 bold')
        self.lblYellow.grid(row=0, column=2, sticky='NESW')
        self.lblBlue = tkinter.Label( width=10, height=5, bg='blue')
        self.lblBlue.grid(row=1, column=0, sticky='NESW')
        self.lblBrown = tkinter.Label(width=10, height=5, bg='brown')
        self.lblBrown.grid(row=1, column=1, sticky='NESW')
        self.lblRed = tkinter.Label(width=10, height=5, bg='red')
        self.lblRed.grid(row=1, column=2, sticky='NESW')
        self.lblGold = tkinter.Label(width=10, height=5, bg='gold')
        self.lblGold.grid(row=2, column=0, sticky='NESW')
        self.lblPurple = tkinter.Label(width=10, height=5, bg='purple')
        self.lblPurple.grid(row=2, column=1, sticky='NESW')
        self.lblBlack = tkinter.Label(width=10, height=5, bg='black')
        self.lblBlack.grid(row=2, column=2, sticky='NESW')
        
######################################### Functions ##################################
def main():
    root = tkinter.Tk(screenName="FirstGridGUI")
    root.resizable(True, True)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    app = FirstGridGUI(root)
    app.grid(row=0, column=0, sticky='NESW')
    
    app.mainloop()

########################################### Main #####################################
main()