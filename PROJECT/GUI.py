import sys
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog



try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import CNN as cnn

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True




def vp_start_gui(Form_Number):
    global val, w, root,top
    root = tk.Tk()
    top = Toplevel1(root, Form_Number)
    root.mainloop()


w = None
global sis


# ttt= tk.StringVar()
class call_back_end:
    def Create_Model(FilePath):
        trainpath = FilePath + "/train"
        validpath = FilePath + "/valid"
        cnn.DataSetFunctions.CreateModel(trainpath)


class Home_Form_Setting:
    def creat_browse_button():
        if Toplevel1.flag == 1:
            folderPath = filedialog.askdirectory()
            Folder_path=folderPath
            print(folderPath)

        else:
            filetype = (('Portable Network Graphics', '*.png'), ("All files", "*.*"))
            filename = askopenfilename(initialdir="C:/Users", filetypes=filetype, title="fdf")
            Folder_path=filename
        top.update_Entry(Folder_path,top.level)






    def changeflag():
        if (Toplevel1.flag == 0):
            Toplevel1.flag = 1
        else:
            Toplevel1.flag = 0


class Toplevel1:
    flag = 0
    level=0

    formLevel = None
    sis = None

    def __init__(self, top=None, Number=None):
        self.level=Number
        if Number == 0:
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9'  # X11 color: 'gray85'
            _ana1color = '#d9d9d9'  # X11 color: 'gray85'
            _ana2color = '#ececec'  # Closest X11 color: 'gray92'
            self.style = ttk.Style()
            if sys.platform == "win32":
                self.style.theme_use('winnative')
            self.style.configure('.', background=_bgcolor)
            self.style.configure('.', foreground=_fgcolor)
            self.style.configure('.', font="TkDefaultFont")
            self.style.map('.', background=
            [('selected', _compcolor), ('active', _ana2color)])

            top.geometry("737x450+269+167")
            top.title("Home")
            top.configure(background="#ffffff")
            top.configure(highlightbackground="#f0f0f0f0f0f0")
            top.configure(highlightcolor="#646464646464")

            self.menubar = tk.Menu(top, font="TkMenuFont", bg='#ffffff', fg='#ffffff')
            top.configure(menu=self.menubar)

            self.Button1 = tk.Button(top)
            self.Button1.place(relx=0.841, rely=0.356, height=34, width=107)
            self.Button1.configure(activebackground="#ececec")
            self.Button1.configure(activeforeground="#000000")
            self.Button1.configure(background="#d9d9d9")
            self.Button1.configure(command=Home_Form_Setting.creat_browse_button)
            self.Button1.configure(disabledforeground="#a3a3a3")
            self.Button1.configure(foreground="#000000")
            self.Button1.configure(highlightbackground="#d9d9d9")
            self.Button1.configure(highlightcolor="black")
            self.Button1.configure(pady="0")
            self.Button1.configure(text='''Browse''')
            self.Button1.configure(width=107)

            self.Text1 = tk.Entry(top)
            self.Text1.place(relx=0.461, rely=0.356, relheight=0.053, relwidth=0.358)

            self.Text1.configure(background="white")
            self.Text1.configure(font="TkTextFont")
            self.Text1.configure(foreground="black")
            self.Text1.configure(highlightbackground="#d9d9d9")
            self.Text1.configure(highlightcolor="black")
            self.Text1.configure(insertbackground="black")
            self.Text1.configure(selectbackground="#c4c4c4")
            self.Text1.configure(selectforeground="black")
            self.Text1.configure(width=264)
           # self.Text1.configure(wrap="word")

            self.Test = tk.Button(top)
            self.Test.place(relx=0.57, rely=0.622, height=44, width=127)
            self.Test.configure(activebackground="#ececec")
            self.Test.configure(activeforeground="#000000")
            self.Test.configure(background="#fff5fe")
            self.Test.configure(borderwidth=".5")
            self.Test.configure(disabledforeground="#a3a3a3")
            self.Test.configure(font="-family {Segoe UI} -size 12")
            self.Test.configure(foreground="#000000")
            self.Test.configure(highlightbackground="#d9d9d9")
            self.Test.configure(highlightcolor="black")
            self.Test.configure(pady="0")
            self.Test.configure(text='''Start Test''')
            self.Test.configure(width=127)

            self.Label1 = tk.Label(top)
            self.Label1.place(relx=0.299, rely=0.356, height=21, width=101)
            self.Label1.configure(background="#ffffff")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(foreground="#000000")
            self.Label1.configure(text='''Choose file/folder''')

            self.Checkbutton1 = tk.Checkbutton(top)
            self.Checkbutton1.place(relx=0.733, rely=0.267, relheight=0.056
                                    , relwidth=0.083)
            self.Checkbutton1.configure(activebackground="#ececec")
            self.Checkbutton1.configure(activeforeground="#000000")
            self.Checkbutton1.configure(background="#ffffff")
            self.Checkbutton1.configure(command=Home_Form_Setting.changeflag)
            self.Checkbutton1.configure(disabledforeground="#a3a3a3")
            self.Checkbutton1.configure(foreground="#000000")
            self.Checkbutton1.configure(highlightbackground="#d9d9d9")
            self.Checkbutton1.configure(highlightcolor="black")
            self.Checkbutton1.configure(justify='left')
            self.Checkbutton1.configure(text='''Folder''')
            #        self.Checkbutton1.configure(variable=Home_support.che48)

            self.TSeparator1 = ttk.Separator(top)
            self.TSeparator1.place(relx=0.237, rely=0.0, relheight=1.0)
            self.TSeparator1.configure(orient="vertical")

            self.HomeBtn = ttk.Button(top, command=Move_Between_Formms.Go_To_Home_Form)
            self.HomeBtn.place(relx=0.0, rely=0.044, height=85, width=176)
            self.HomeBtn.configure(takefocus="")
            self.HomeBtn.configure(text='''Home''')
            self.HomeBtn.configure(width=176)

            self.Statisticsbtn = ttk.Button(top, command=Move_Between_Formms.Go_To_Statistics_Form)
            self.Statisticsbtn.place(relx=0.0, rely=0.233, height=85, width=176)
            self.Statisticsbtn.configure(takefocus="")
            self.Statisticsbtn.configure(text='''Statistics''')

            self.Monitiringbtn = ttk.Button(top, command=Move_Between_Formms.Go_To_Monitiring_Form)
            self.Monitiringbtn.place(relx=0.0, rely=0.422, height=85, width=176)
            self.Monitiringbtn.configure(takefocus="")
            self.Monitiringbtn.configure(text='''Monitiring''')

            self.Model_Btn = ttk.Button(top, command=Move_Between_Formms.Go_To_CreateModel_Form)
            self.Model_Btn.place(relx=0.0, rely=0.611, height=85, width=176)
            self.Model_Btn.configure(takefocus="")
            self.Model_Btn.configure(text='''Create Model''')

            self.Helpbtn = ttk.Button(top, command=Move_Between_Formms.Go_To_Help_Form)
            self.Helpbtn.place(relx=0.0, rely=0.811, height=85, width=176)
            self.Helpbtn.configure(takefocus="")
            self.Helpbtn.configure(text='''Help''')
            Toplevel1.formLevel = top
        elif Number == 3:
            Toplevel1.flag = 1
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9'  # X11 color: 'gray85'
            _ana1color = '#d9d9d9'  # X11 color: 'gray85'
            _ana2color = '#ececec'  # Closest X11 color: 'gray92'
            self.style = ttk.Style()
            if sys.platform == "win32":
                self.style.theme_use('winnative')
            self.style.configure('.', background=_bgcolor)
            self.style.configure('.', foreground=_fgcolor)
            self.style.configure('.', font="TkDefaultFont")
            self.style.map('.', background=
            [('selected', _compcolor), ('active', _ana2color)])

            top.geometry("737x450+269+167")
            top.title("Create Model")
            top.configure(background="#ffffff")
            top.configure(highlightbackground="#f0f0f0f0f0f0")
            top.configure(highlightcolor="#646464646464")

            self.menubar = tk.Menu(top, font="TkMenuFont", bg='#ffffff', fg='#ffffff')
            top.configure(menu=self.menubar)

            self.Button1 = tk.Button(top, command=Home_Form_Setting.creat_browse_button)
            self.Button1.place(relx=0.841, rely=0.356, height=34, width=107)
            self.Button1.configure(activebackground="#ececec")
            self.Button1.configure(activeforeground="#000000")
            self.Button1.configure(background="#d9d9d9")
            self.Button1.configure(disabledforeground="#a3a3a3")
            self.Button1.configure(foreground="#000000")
            self.Button1.configure(highlightbackground="#d9d9d9")
            self.Button1.configure(highlightcolor="black")
            self.Button1.configure(pady="0")
            self.Button1.configure(takefocus="0")
            self.Button1.configure(text='''Browse''')

            self.Label1 = tk.Label(top)
            self.Label1.place(relx=0.299, rely=0.367, height=21, width=101)
            self.Label1.configure(activebackground="#f9f9f9")
            self.Label1.configure(activeforeground="black")
            self.Label1.configure(background="#ffffff")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(foreground="#000000")
            self.Label1.configure(highlightbackground="#d9d9d9")
            self.Label1.configure(highlightcolor="black")
            self.Label1.configure(text='''Choose Folder''')
            self.Create = tk.Button(top)
            self.Create.place(relx=0.543, rely=0.733, height=44, width=127)
            self.Create.configure(activebackground="#ececec")
            self.Create.configure(activeforeground="#000000")
            self.Create.configure(background="#fff5fe")
            self.Create.configure(borderwidth=".5")
            self.Create.configure(disabledforeground="#a3a3a3")
            self.Create.configure(font="-family {Segoe UI} -size 12")
            self.Create.configure(foreground="#000000")
            self.Create.configure(highlightbackground="#d9d9d9")
            self.Create.configure(highlightcolor="black")
            self.Create.configure(pady="0")
            self.Create.configure(takefocus="0")
            self.Create.configure(text='''Create''')
            self.Label1_9 = tk.Label(top)
            self.Label1_9.place(relx=0.299, rely=0.256, height=21, width=101)
            self.Label1_9.configure(activebackground="#f9f9f9")
            self.Label1_9.configure(activeforeground="black")
            self.Label1_9.configure(background="#ffffff")
            self.Label1_9.configure(disabledforeground="#a3a3a3")
            self.Label1_9.configure(foreground="#000000")
            self.Label1_9.configure(highlightbackground="#d9d9d9")
            self.Label1_9.configure(highlightcolor="black")
            self.Label1_9.configure(text='''Model Name''')

            self.Entry1 = tk.Entry(top)
            self.Entry1.place(relx=0.461, rely=0.267, height=20, relwidth=0.358)
            self.Entry1.configure(background="white")
            self.Entry1.configure(disabledforeground="#a3a3a3")
            self.Entry1.configure(font="TkFixedFont")
            self.Entry1.configure(foreground="#000000")
            self.Entry1.configure(insertbackground="black")
            self.Entry1.configure(takefocus="0")
            self.Entry1.configure(width=264)



            #            ttt.set("ghg")
            # ds= "fdfdfd"
            self.Entry1_10 = tk.Entry(top)
            self.Entry1_10.place(relx=0.461, rely=0.367, height=20, relwidth=0.358)
            self.Entry1_10.configure(background="white")
            self.Entry1_10.configure(disabledforeground="#a3a3a3")
            self.Entry1_10.configure(font="TkFixedFont")
            self.Entry1_10.configure(foreground="#000000")
            self.Entry1_10.configure(highlightbackground="#d9d9d9")
            self.Entry1_10.configure(highlightcolor="black")
            self.Entry1_10.configure(insertbackground="black")
            self.Entry1_10.configure(selectbackground="#c4c4c4")
            self.Entry1_10.configure(selectforeground="black")
            self.Entry1_10.configure(takefocus="0")
#

            self.TSeparator1 = ttk.Separator(top)
            self.TSeparator1.place(relx=0.237, rely=0.0, relheight=1.0)
            self.TSeparator1.configure(orient="vertical")
            self.TSeparator1.configure(takefocus="0")
            self.HomeBtn = ttk.Button(top, command=Move_Between_Formms.Go_To_Home_Form)
            self.HomeBtn.place(relx=0.0, rely=0.044, height=85, width=176)
            self.HomeBtn.configure(takefocus="")
            self.HomeBtn.configure(text='''Home''')
            self.HomeBtn.configure(width=176)

            self.Statisticsbtn = ttk.Button(top, command=Move_Between_Formms.Go_To_Statistics_Form)
            self.Statisticsbtn.place(relx=0.0, rely=0.233, height=85, width=176)
            self.Statisticsbtn.configure(takefocus="")
            self.Statisticsbtn.configure(text='''Statistics''')

            self.Monitiringbtn = ttk.Button(top, command=Move_Between_Formms.Go_To_Monitiring_Form)
            self.Monitiringbtn.place(relx=0.0, rely=0.422, height=85, width=176)
            self.Monitiringbtn.configure(takefocus="")
            self.Monitiringbtn.configure(text='''Monitiring''')

            self.Model_Btn = ttk.Button(top, command=Move_Between_Formms.Go_To_CreateModel_Form)
            self.Model_Btn.place(relx=0.0, rely=0.611, height=85, width=176)
            self.Model_Btn.configure(takefocus="")
            self.Model_Btn.configure(text='''Create Model''')

            self.Helpbtn = ttk.Button(top, command=Move_Between_Formms.Go_To_Help_Form)
            self.Helpbtn.place(relx=0.0, rely=0.811, height=85, width=176)
            self.Helpbtn.configure(takefocus="")
            self.Helpbtn.configure(text='''Help''')
            Toplevel1.formLevel = top
    def update_Entry(self,Text,level_Entry):
        if(level_Entry == 3):
            self.Entry1_10.delete(0,END)
            self.Entry1_10.insert(0,Text)
        elif(level_Entry == 0):
            self.Text1.delete(0,END)
            self.Text1.insert(0,Text)

class Move_Between_Formms:
    def Go_To_Home_Form():
        Toplevel1.formLevel.destroy()

        vp_start_gui(0)

    def Go_To_Statistics_Form():
        Toplevel1.formLevel.destroy()
        vp_start_gui(1)

    def Go_To_Monitiring_Form():
        Toplevel1.formLevel.destroy()
        vp_start_gui(2)

    def Go_To_CreateModel_Form():
        Toplevel1.formLevel.destroy()
        vp_start_gui(3)

    def Go_To_Help_Form():
        Toplevel1.formLevel.destroy()
        vp_start_gui(5)


if __name__ == '__main__':
    vp_start_gui(3)





