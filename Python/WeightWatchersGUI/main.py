import tkinter

class myProgram(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    def onCalculate():
        return 0

    def createWidgets(self):
        self.lblJoule = tkinter.Label(self) 
        self.lblJoule["text"] = "Please provide kJoule: "
        self.lblJoule.pack()
        self.lblInputJoule = tkinter.Entry(self)
        self.lblInputJoule.pack(side="left")
        self.lblInputJoule["width"] = 10
        self.strJoule = tkinter.StringVar()
        self.lblInputJoule["textvariable"] = self.strJoule

        self.btnExit = tkinter.Button(self)
        self.btnExit[text] = "Exit"
        self.btnExit[commmand] = self.quit
        self.btnExit.
        self.btnExit.pack(side="right")

        self.btnCalc = tkinter.Button(self)
        self.btnCalc[text] = "Calculate"
        self.btnCalc[command] = self.onCalculate

        


def main():
    root = tkinter.Tk()
    app = myProgram(root)
    app.mainloop()


##################################################################################
main()