import tkinter

class myWindow(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.firstName = tkinter.Entry(self)
        self.firstName.pack()
        self.firstName["width"] = 40
        self.name = tkinter.StringVar()
        self.name.set("Please insert your name: ")
        self.firstName["textvariable"] = self.name

        self.exitButton = tkinter.Button(self)
        self.exitButton["text"] = "Exit"
        self.exitButton["command"] = self.quit
        self.exitButton.pack(side="right")

        self.deleteButton = tkinter.Button(self)
        self.deleteButton["text"] = "Delete"
        self.deleteButton["command"] = self.onDelete
        self.deleteButton.pack(side="left")

    def onDelete(self):
        self.name.set("")
        self.name.set("Please insert your name: ")


def main():
    root = tkinter.Tk()
    app = myWindow(root)
    app.mainloop()

#######################################################################################################
main()
