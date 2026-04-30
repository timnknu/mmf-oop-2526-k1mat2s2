import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_150=tk.Button(root)
        GButton_150["text"] = "Button"
        GButton_150.place(x=60,y=90,width=70,height=25)
        GButton_150["command"] = self.GButton_150_command

        GButton_350=tk.Button(root)
        GButton_350["text"] = "But123ton"
        GButton_350.place(x=330,y=70,width=170,height=25)
        GButton_350["command"] = self.GButton_350_command

        GLabel_262=tk.Label(root)
        GLabel_262["text"] = "label VERY LONG TEXT"
        GLabel_262['bg'] = "white"
        GLabel_262.place(x=160,y=40,width=270,height=225)
        def myfunc(event):
            print('Mouse moved', event.x, event.y)
        GLabel_262.bind("<Motion>", myfunc)

        GRadio_806=tk.Radiobutton(root)
        GRadio_806["text"] = "RadioButton"
        GRadio_806.place(x=120,y=210,width=85,height=25)
        GRadio_806["command"] = self.GRadio_806_command

        GRadio_30=tk.Radiobutton(root)
        GRadio_30["text"] = "RadioButton"
        GRadio_30.place(x=110,y=240,width=85,height=25)
        GRadio_30["command"] = self.GRadio_30_command

        GCheckBox_423=tk.Checkbutton(root)
        GCheckBox_423.place(x=350,y=220,width=70,height=25)
        GCheckBox_423["offvalue"] = "0"
        GCheckBox_423["onvalue"] = "1"
        GCheckBox_423["command"] = self.GCheckBox_423_command

    def GButton_150_command(self):
        print("command")


    def GButton_350_command(self):
        print("right button clicked")


    def GRadio_806_command(self):
        print("command")


    def GRadio_30_command(self):
        print("command")


    def GCheckBox_423_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
