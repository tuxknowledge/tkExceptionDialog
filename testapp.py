#!/usr/bin/env python
# -*- coding: utf-8 -*-

__appname__ = 'tkExceptionDialog'
__author__ = 'André Raabe <andre.raabe@gmail.com>'
__version__ = '0.1'
__license__ = 'MIT?'

import Tkinter as tk
import ttk
import tkExceptionDialog

import sys


def handleException(*args):
    tkExceptionDialog.tkExceptionDialog(
        additionalMessage="Product: " + __appname__)
    sys.exc_clear()


def raiseException():
    raise Exception("Testexception")


def _simpleTest():
    """Small routine to show the usage"""
    root = tk.Tk()
    sys.excepthook = handleException
    root.report_callback_exception = handleException
    root.title("Testapplication for tkExceptionDialog")
    frame = ttk.Frame(root)
    c = tk.Text(frame)
    c.pack(side=tk.TOP)
    frame.pack()
    btn = ttk.Button(root, text="Raise exception", command=raiseException)
    btn.pack()
    root.mainloop()

if __name__ == '__main__':
    _simpleTest()
