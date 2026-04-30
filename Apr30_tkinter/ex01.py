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
        #root.geometry('500x200+100+300')
        root.resizable(width=False, height=False)

        GLabel_233=tk.Label(root)
        GLabel_233["text"] = "label"
        GLabel_233.place(x=170,y=50,width=70,height=25)

        mybutton=tk.Button(root)
        mybutton["text"] = "Button1111111111111111111111"
        mybutton.place(x=310,y=90,width=70,height=25)
        mybutton["command"] = self.GButton_573_command

        GCheckBox_434=tk.Checkbutton(root)
        GCheckBox_434["text"] = "CheckBox"
        GCheckBox_434.place(x=110,y=180,width=70,height=25)
        GCheckBox_434["offvalue"] = "0"
        GCheckBox_434["onvalue"] = "1"
        GCheckBox_434["command"] = self.GCheckBox_434_command

        GRadio_921=tk.Radiobutton(root)
        GRadio_921["text"] = "RadioButton"
        GRadio_921.place(x=310,y=180,width=85,height=25)
        GRadio_921["command"] = self.GRadio_921_command

        GLineEdit_996=tk.Entry(root)
        GLineEdit_996["text"] = "Entry"
        GLineEdit_996.place(x=100,y=310,width=70,height=25)

        GListBox_512=tk.Listbox(root)
        GListBox_512.place(x=340,y=280,width=80,height=25)

    def GButton_573_command(self):
        print("Button is pressed")


    def GCheckBox_434_command(self):
        print("command")


    def GRadio_921_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
