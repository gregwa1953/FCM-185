#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Aug 12, 2022 03:22:50 AM CDT  platform: Linux

import sys
# from .ColorSetCreator_support import CurrentSelected
# from Summer1 import colorset as Summer1, do_tk_widgets
# from DarkChocolate import colorset as DarkChoc
# from Vintage1 import colorset as Vintage1
# from Greg1 import colorset as Greg1, do_tk_widgets
# from ColorSetImport import Coffee1, DarkChocolate, DarkChocolate2, Greg1, Neon1, Vintage1, Warm1, do_tk_widgets
from ColorSetImport import newset, do_tk_widgets
# ========================================
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import applytest2

_debug = False


def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = applytest2.Toplevel1(_top1)
    startup()
    root.mainloop()


def startup():
    global colorset, lst
    LoadCombo()
    _top1.title(f'Multiple Widgets Set from import file - using set Greg1')
    if _debug:
        print(lst)


def LoadCombo():
    global lst, sets, colorset

    lst = [*newset]
    print(lst)
    _w1.TCombobox2["values"] = lst
    _w1.TCombobox2.bind("<<ComboboxSelected>>", lambda e: on_ComboSelect(e))
    sets = newset
    colorset = newset[lst[0]]

    # do_tk_widgets(_top1, colorset)
    _w1.TCombobox2.current(0)
    _w1.TCombobox2.set(lst[0])

    # _top1.update()


def on_ComboSelect(e):
    global lst, sets
    selected = _w1.combobox1.get()
    print(f"Combobox Select: {selected}")
    # colorset = sets[lst.index(selected)]
    print(f'Index: {lst.index(selected)}')
    colorset = sets[selected]
    print(colorset)
    _top1.title(
        f'Multiple Widgets Set from import file - using set {selected}')
    do_tk_widgets(_top1, colorset)


def on_btnExit(*args):
    print('applytest2_support.on_btnExit')
    for arg in args:
        print('    another arg:', arg)
    sys.stdout.flush()
    sys.exit()


def on_btnGetChildren(*args):
    print('applytest2_support.on_btnGetChildren')
    for arg in args:
        print('    another arg:', arg)
    sys.stdout.flush()


if __name__ == '__main__':
    applytest2.start_up()
