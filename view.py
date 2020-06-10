from tkinter import *
import tkinter.filedialog
from controller import inject_msg
import tkMessageBox

class View:
    def __init__(self):
        self.master = Tk()
        self.master.title("MsgInjector")
        self.master.geometry("500x125")
        self.master.resizable(False, False)
        self.init_labels()
        self.file_path = ""
        self.init_buttons()
        self.message= ""
        self.init_textfield()

    def init_labels(self):
        file_label = Label(self.master, text="File to inject: ")
        file_label.place(x=10, y=10)
        text_label = Label(self.master, text="Message: ")
        text_label.place(x=10, y=50)
        self.file_name = Label(self.master, text="")
        self.file_name.place(x=210, y=10)

    def init_textfield(self):
        self.entry = Entry(self.master, width=45, textvariable=self.message)
        self.entry.place(x=100, y=50)

    def init_buttons(self):
        file_dialogbutton = Button(self.master, text="Browse file...", activebackground="yellow", command=self.get_file)
        file_dialogbutton.place(x=100, y=9)
        inject_button = Button(self.master, text="Inject!", activebackground="yellow", padx=50, font=("Helvetica", 15), command=self.inject)
        inject_button.place(x=190, y=85)

    def get_file(self):
        self.file_path = tkinter.filedialog.askopenfilename(initialdir="./", title="select")
        self.file_name.config(text=self.file_path)

    def inject(self):
        try:
            inject_msg(self.file_path, self.entry.get())
            tkMessageBox.showinfo("Success box", "Message injected correctly!")
            self.file_name.config(text="")
            self.entry.delete(0,'end')
            self.file_path= ""
            self.message= ""
        except:
            tkMessageBox.showerror("Error box", "Missing parametres!")
            self.file_name.config(text="")
            self.entry.delete(0, 'end')

    def start(self):
        mainloop()
