#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6b
#  in conjunction with Tcl version 8.6
#    Aug 13, 2022 07:41:41 AM CDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import applytest2_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    style.map('TCheckbutton',background =
           [('selected', _bgcolor), ('active', _ana2color)], indicatorcolor =
           [('selected', _fgcolor), ('!active', _bgcolor)])
    style.map('TNotebook.Tab', background =
            [('selected', _bgcolor), ('active', _tabbg1),
            ('!active', _ana2color)], foreground =
            [('selected', _fgcolor), ('active', _tabfg1), ('!active',  _tabfg2)])
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("899x769+484+263")
        top.minsize(1, 1)
        top.maxsize(4225, 1410)
        top.resizable(0,  0)
        top.title("Toplevel 0")
        top.configure(highlightcolor="black")

        self.top = top
        self.combobox = tk.StringVar()
        self.combobox1 = tk.StringVar()
        self.che49 = tk.IntVar()
        self.selectedButton = tk.IntVar()
        self.tch48 = tk.IntVar()

        self.btnExit = tk.Button(self.top)
        self.btnExit.place(x=740, y=20, height=33, width=113)
        self.btnExit.configure(activebackground="beige")
        self.btnExit.configure(borderwidth="2")
        self.btnExit.configure(command=applytest2_support.on_btnExit)
        self.btnExit.configure(compound='left')
        self.btnExit.configure(text='''Exit''')

        self.Labelframe1 = tk.LabelFrame(self.top)
        self.Labelframe1.place(x=150, y=60, height=305, width=700)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(text='''Tk Widgets''')

        self.Checkbutton1 = tk.Checkbutton(self.Labelframe1)
        self.Checkbutton1.place(x=40, y=50, height=33, width=167
                , bordermode='ignore')
        self.Checkbutton1.configure(activebackground="beige")
        self.Checkbutton1.configure(anchor='w')
        self.Checkbutton1.configure(borderwidth="2")
        self.Checkbutton1.configure(compound='left')
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(relief="groove")
        self.Checkbutton1.configure(selectcolor="#d9d9d9")
        self.Checkbutton1.configure(text='''Check''')
        self.Checkbutton1.configure(variable=self.che49)

        self.Entry1 = tk.Entry(self.Labelframe1)
        self.Entry1.place(x=230, y=50, height=23, width=166, bordermode='ignore')

        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")

        self.Label1 = tk.Label(self.Labelframe1)
        self.Label1.place(x=50, y=20, height=21, width=139, bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(compound='left')
        self.Label1.configure(text='''Checkbutton''')

        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(x=230, y=20, height=21, width=99, bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(compound='left')
        self.Label2.configure(text='''Entry Widget''')

        self.Listbox1 = tk.Listbox(self.Labelframe1)
        self.Listbox1.place(x=440, y=50, height=76, width=84
                , bordermode='ignore')
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(selectbackground="#c4c4c4")

        self.Message1 = tk.Message(self.Labelframe1)
        self.Message1.place(x=550, y=50, height=61, width=122
                , bordermode='ignore')
        self.Message1.configure(borderwidth="2")
        self.Message1.configure(padx="1")
        self.Message1.configure(pady="1")
        self.Message1.configure(relief="sunken")
        self.Message1.configure(text='''Message''')
        self.Message1.configure(width=122)

        self.Radiobutton1 = tk.Radiobutton(self.Labelframe1)
        self.Radiobutton1.place(x=40, y=123, height=33, width=168
                , bordermode='ignore')
        self.Radiobutton1.configure(activebackground="beige")
        self.Radiobutton1.configure(anchor='w')
        self.Radiobutton1.configure(borderwidth="2")
        self.Radiobutton1.configure(compound='left')
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(relief="groove")
        self.Radiobutton1.configure(selectcolor="#d9d9d9")
        self.Radiobutton1.configure(text='''Radio''')
        self.Radiobutton1.configure(variable=self.selectedButton)

        self.Label3 = tk.Label(self.Labelframe1)
        self.Label3.place(x=40, y=100, height=21, width=129, bordermode='ignore')

        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w')
        self.Label3.configure(compound='left')
        self.Label3.configure(text='''Radiobutton''')

        self.Scale1 =  tk.Scale(self.Labelframe1, from_=0.0, to=100.0, resolution=1.0)
        self.Scale1.place(x=240, y=130, height=104, width=49)
        self.Scale1.configure(activebackground="beige")
        self.Scale1.configure(troughcolor="#d9d9d9")

        self.Scale2 =  tk.Scale(self.Labelframe1, from_=0.0, to=100.0, resolution=1.0)
        self.Scale2.place(x=300, y=180, height=42, width=104)
        self.Scale2.configure(activebackground="beige")
        self.Scale2.configure(orient="horizontal")
        self.Scale2.configure(troughcolor="#d9d9d9")

        self.Spinbox1 = tk.Spinbox(self.Labelframe1, from_=1.0, to=100.0)
        self.Spinbox1.place(x=440, y=180, height=23, width=88
                , bordermode='ignore')
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(font="TkDefaultFont")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")

        self.Text1 = tk.Text(self.Labelframe1)
        self.Text1.place(x=30, y=190, height=74, width=166, bordermode='ignore')
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(wrap="word")

        self.Frame1 = tk.Frame(self.Labelframe1)
        self.Frame1.place(x=570, y=170, height=75, width=105
                , bordermode='ignore')
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")

        self.Label4 = tk.Label(self.Labelframe1)
        self.Label4.place(x=575, y=140, height=21, width=99, bordermode='ignore')

        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(anchor='w')
        self.Label4.configure(compound='left')
        self.Label4.configure(text='''Frame Widget''')

        self.Label5 = tk.Label(self.Labelframe1)
        self.Label5.place(x=440, y=150, height=21, width=79, bordermode='ignore')

        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(anchor='w')
        self.Label5.configure(compound='left')
        self.Label5.configure(text='''Spinbox''')

        self.Label6 = tk.Label(self.Labelframe1)
        self.Label6.place(x=310, y=150, height=21, width=79, bordermode='ignore')

        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(anchor='w')
        self.Label6.configure(compound='left')
        self.Label6.configure(text='''HScale''')

        self.Label7 = tk.Label(self.Labelframe1)
        self.Label7.place(x=250, y=100, height=21, width=69, bordermode='ignore')

        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(anchor='w')
        self.Label7.configure(compound='left')
        self.Label7.configure(text='''VScale''')

        self.Label8 = tk.Label(self.Labelframe1)
        self.Label8.place(x=40, y=164, height=21, width=119, bordermode='ignore')

        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(anchor='w')
        self.Label8.configure(compound='left')
        self.Label8.configure(text='''Text Widget''')

        _style_code()
        self.TLabelframe1 = ttk.Labelframe(self.top)
        self.TLabelframe1.place(x=150, y=370, height=375, width=700)
        self.TLabelframe1.configure(relief='')
        self.TLabelframe1.configure(text='''Tlabelframe''')

        self.TButton1 = ttk.Button(self.TLabelframe1)
        self.TButton1.place(x=10, y=50, height=28, width=83, bordermode='ignore')

        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Tbutton''')
        self.TButton1.configure(compound='left')

        self.TCheckbutton1 = ttk.Checkbutton(self.TLabelframe1)
        self.TCheckbutton1.place(x=130, y=50, width=144, height=21
                , bordermode='ignore')
        self.TCheckbutton1.configure(variable=self.tch48)
        self.TCheckbutton1.configure(takefocus="")
        self.TCheckbutton1.configure(text='''Tcheck''')
        self.TCheckbutton1.configure(compound='left')

        self.TCombobox1 = ttk.Combobox(self.TLabelframe1)
        self.TCombobox1.place(x=340, y=50, height=21, width=177
                , bordermode='ignore')
        self.TCombobox1.configure(textvariable=self.combobox)
        self.TCombobox1.configure(takefocus="")

        self.TEntry1 = ttk.Entry(self.TLabelframe1)
        self.TEntry1.place(x=10, y=120, height=21, width=164
                , bordermode='ignore')
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="xterm")

        self.TLabel1 = ttk.Label(self.TLabelframe1)
        self.TLabel1.place(x=340, y=20, height=19, width=80, bordermode='ignore')

        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''TCombobox''')
        self.TLabel1.configure(compound='left')

        self.TLabel2 = ttk.Label(self.TLabelframe1)
        self.TLabel2.place(x=20, y=90, height=19, width=122, bordermode='ignore')

        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''TEntry Widget''')
        self.TLabel2.configure(compound='left')

        self.TFrame1 = ttk.Frame(self.TLabelframe1)
        self.TFrame1.place(x=200, y=110, height=75, width=125
                , bordermode='ignore')
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.TLabelframe2 = ttk.Labelframe(self.TLabelframe1)
        self.TLabelframe2.place(x=340, y=110, height=75, width=150
                , bordermode='ignore')
        self.TLabelframe2.configure(relief='')
        self.TLabelframe2.configure(text='''Tlabelframe''')

        self.TProgressbar1 = ttk.Progressbar(self.TLabelframe1)
        self.TProgressbar1.place(x=10, y=220, width=100, height=19
                , bordermode='ignore')

        self.TLabel3 = ttk.Label(self.TLabelframe1)
        self.TLabel3.place(x=10, y=190, height=19, width=102
                , bordermode='ignore')
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''TProgressbar''')
        self.TLabel3.configure(compound='left')

        self.TScale1 = ttk.Scale(self.TLabelframe1, from_=0, to=1.0)
        self.TScale1.place(x=140, y=230, height=100, width=17)
        self.TScale1.configure(orient="vertical")
        self.TScale1.configure(takefocus="")

        self.TScale2 = ttk.Scale(self.TLabelframe1, from_=0, to=1.0)
        self.TScale2.place(x=180, y=260, height=17, width=100)
        self.TScale2.configure(takefocus="")

        self.TSpinbox1 = ttk.Spinbox(self.TLabelframe1, from_=1, to=100)
        self.TSpinbox1.place(x=310, y=260, height=20, width=95
                , bordermode='ignore')
        self.TSpinbox1.configure(background="white")
        self.TSpinbox1.configure(takefocus="")

        self.TNotebook1 = ttk.Notebook(self.TLabelframe1)
        self.TNotebook1.place(x=450, y=210, height=136, width=212
                , bordermode='ignore')
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text='''Page 1''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text='''Page 2''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(2, text='''Page 3''', compound="left"
                ,underline='''-1''', )

        self.TCombobox2 = ttk.Combobox(self.top)
        self.TCombobox2.place(x=270, y=20, height=21, width=177)
        self.TCombobox2.configure(textvariable=self.combobox1)
        self.TCombobox2.configure(takefocus="")

        self.Label9 = tk.Label(self.top)
        self.Label9.place(x=80, y=20, height=21, width=179)
        self.Label9.configure(anchor='w')
        self.Label9.configure(compound='left')
        self.Label9.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Label9.configure(text='''Available Color Sets:''')

def start_up():
    applytest2_support.main()

if __name__ == '__main__':
    applytest2_support.main()




