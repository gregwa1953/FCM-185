
# ----------------------------
# Import colorset file
# Created by G.D. Walters
# ----------------------------
    
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *


newset={"Greg1": {"BG1": "gray54", "BG2": "gray86", "BG3": "gray64", "FG1": "white", "FG2": "black", "FG3": "black"}, "Vintage1": {"BG1": "#8E3200", "BG2": "#D7A86E", "BG3": "#A64B2A", "FG1": "white", "FG2": "black", "FG3": "black"}, "Vintage2": {"BG1": "#362706", "BG2": "#464E2E", "BG3": "#ACB992", "FG1": "white", "FG2": "white", "FG3": "black"}}


def do_tk_widgets(Toplevel, colorset):
    # global colorset

    style = ttk.Style()
    style.theme_use('default')
    no_AB = ['Entry', 'Message', 'Listbox', 'Text', 'Frame', 'Labelframe']
    # Widgets that have no Foreground attributes
    no_FG = ['Frame']
    TWidgets = [
        'TButton', 'TCheckbutton', 'TCombobox', 'TEntry', 'TFrame', 'TLabel',
        'TLabelframe', 'TMenubutton', 'TPanedwindow', 'TNotebook',
        'Horizontal.TProgressbar', 'Vertical.TProgressbar', 'TProgressbar',
        'TRadiobutton', 'Horizontal.TScale', 'Vertical.TScale', 'TScale',
        'TSeparator', 'Treeview', 'TSizeGrip', 'TSpinbox'
    ]
    Containers = ['Frame', 'Labelframe', 'Tframe', 'TLabelframe']
    # ===================================================
    # Start with the Toplevel (Toplevel has no foreground attribute)
    # ===================================================

    Toplevel.configure(bg=colorset['BG1'])

    # ===================================================
    # Now get all the child widgets of the Toplevel, but
    # don't go into containers yet
    # ===================================================
    style.map(
        "TNotebook.Tab",
        background=[("selected", colorset['BG1']), ("active", colorset['BG2']),
                    ("!active", colorset['BG3'])],
        foreground=[("selected", colorset['FG1']), ("active", colorset['FG2']),
                    ("!active", colorset['FG3'])],
    )
    style.map('TButton',
              background=[('disabled', '#d9d9d9'),
                          ('pressed', colorset['BG3']),
                          ('active', colorset['BG2'])],
              foreground=[('disabled', colorset['FG3']),
                          ('pressed', colorset['FG3']),
                          ('active', colorset['FG2'])])
    style.configure('.', background=colorset['BG1'])
    style.configure('.', foreground=colorset['FG1'])

    kids = Toplevel.winfo_children()
    for kid in kids:
        thiskid = kid.winfo_class()
        # ===================================================
        # Try to do the background/foreground colours
        # ===================================================
        print(f'Thiskid: {thiskid}')
        if thiskid in Containers:
            tlftext = f'{thiskid}.Label'
            if thiskid in TWidgets:
                style.configure(thiskid,
                                background=colorset['BG1'],
                                foreground=colorset['FG1'])
                style.configure(tlftext,
                                background=colorset['BG1'],
                                foreground=colorset['FG1'])
                style.configure(thiskid)
            else:
                kid.configure(background=colorset['BG1'],
                              foreground=colorset['FG1'])
            print(f'Thiskid: {thiskid}')
            siblings = kid.winfo_children()
            for sib in siblings:
                print(f'Working {sib} - {sib.winfo_class()}')
                # if thiskid not in TWidgets:
                if sib.winfo_class() not in TWidgets:
                    sib.config(bg=colorset['BG1'])
                    if sib.winfo_class() not in no_FG:
                        sib.config(fg=colorset['FG1'])
                    if sib.winfo_class() not in no_AB:
                        try:
                            sib.config(activebackground=colorset['BG2'])
                            sib.config(activeforeground=colorset['FG2'])
                        except:
                            pass
                else:
                    cls = sib.winfo_class()
                    if cls == 'TFrame':
                        sibs2 = sib.winfo_children()
                        print(sibs2)
                        for si in sibs2:
                            print(si.winfo_class())
                            if (si.winfo_class()
                                    == 'Treeview') or (si.winfo_class()
                                                       == 'TScrollbar'):
                                pass
                            else:
                                si.configure(background=colorset['BG1'],
                                             foreground=colorset['FG1'])
                    if cls == 'TLabel':
                        sib.configure(background=colorset['BG1'],
                                      foreground=colorset['FG1'])

        elif thiskid not in TWidgets:
            print(f'Thiskid: {thiskid} - Kid: {kid}')
            kid.config(bg=colorset['BG1'])
            if thiskid not in no_FG:
                kid.config(fg=colorset['FG1'])
            if thiskid not in no_AB:
                try:
                    kid.config(activebackground=colorset['BG2'])
                    kid.config(activeforeground=colorset['FG2'])
                except:
                    pass
    Toplevel.update()
    
