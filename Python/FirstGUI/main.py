import tkinter

class myWindow(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.lblFirstName = tkinter.Entry(self)
        self.lblFirstName.pack()
        self.lblFirstName["width"] = 40
        self.name = tkinter.StringVar()
        self.name.set("Please insert your name: ")
        self.lblFirstName["textvariable"] = self.name

        self.btnExit = tkinter.Button(self)
        self.btnExit["text"] = "Exit"
        self.btnExit["command"] = self.quit
        self.btnExit.pack(side="right")

        self.btnDelete = tkinter.Button(self)
        self.btnDelete["text"] = "Delete"
        self.btnDelete["command"] = self.onDelete
        self.btnDelete.pack(side="left")

    def onDelete(self):
        self.name.set("")
        self.name.set("Please insert your name: ")


def main():
    root = tkinter.Tk()
    app = myWindow(root)
    app.mainloop()

#######################################################################################################
main()
