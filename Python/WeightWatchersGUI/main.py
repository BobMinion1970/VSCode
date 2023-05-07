import tkinter 
import tkinter.messagebox

#################################### Classes ##################################################
class myProgram(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def onCalculate(self):
        result=float(self.lblInputJoule.get()) * 0.24
        self.lblKalorien["text"] = str(result)
        return 
    
    def onExit(self):
        tkinter.messagebox.showinfo(title = "MyProgram", message = "App will be closed", options=None)
        self.quit()
     
    def createWidgets(self):
        self.lblJoule = tkinter.Label(self, text="Please provide kJoule: ") 
        self.lblJoule.pack()
        self.lblInputJoule = tkinter.Entry(self)
        self.lblInputJoule.pack()
        self.lblInputJoule["width"] = 10
        self.btnExit = tkinter.Button(self, text = "Exit", command=self.onExit)
        #self.btnExit["text"] = "Exit"
        #self.btnExit["commmand"] = self.quit
        self.btnExit.pack()
        
        self.btnCalc = tkinter.Button(self, text="Calculate", command=self.onCalculate)
        self.btnCalc.pack()
        self.lblKalorien = tkinter.Label(self)
        self.lblKalorien.pack()  

#################################### Functions ##################################################
def main():
    root = tkinter.Tk(screenName="WeightWatcher")
    root.title("Weight Watcher's Fun")
    root.geometry('440x200')
    root.update()
    app = myProgram(root)
    app.mainloop()


##################################################################################
main()