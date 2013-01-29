#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2013 "Andre Raabe <andre.raabe@gmail.com>"
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#

__appname__ = 'tkExceptionDialog'
__author__ = 'Andre Raabe <andre.raabe@gmail.com>'
__version__ = '0.1'
__license__ = 'MIT'

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
