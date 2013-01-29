#!/usr/bin/env python
# -*- coding: utf-8 -*-

__appname__ = 'tkExceptionDialog'
__author__ = 'André Raabe <andre.raabe@gmail.com>'
__version__ = '0.1'
__license__ = 'MIT?'

import Tkinter as tk
import ttk
import sys
import traceback
from datetime import datetime
import platform
import os
import tkFont


class AutoScrollbar(ttk.Scrollbar):
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        ttk.Scrollbar.set(self, lo, hi)
        self.update_idletasks()


class tkExceptionDialog(object):
    def __init__(self, parent=None, additionalMessage=None):
        self.top = tk.Toplevel(parent)
        self.parent = parent
        self.top.title("Errors occured")

        self.mainFrame = ttk.Frame(self.top)
        self.mainFrame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W),
            columnspan=3, rowspan=3, padx=7, pady=7)

        self.scrollbarX = AutoScrollbar(self.mainFrame, orient=tk.HORIZONTAL)
        self.scrollbarX.grid(row=1, column=0, sticky=tk.EW, columnspan=3)
        self.scrollbarY = AutoScrollbar(self.mainFrame)
        self.scrollbarY.grid(row=0, column=1, sticky=tk.N + tk.SE)

        self.textField = tk.Text(self.mainFrame, wrap=tk.NONE,
            xscrollcommand=self.scrollbarX.set,
            yscrollcommand=self.scrollbarY.set)
        self.textField.insert(1.0, self.buildExceptionInfo(additionalMessage))
        self.textField.config(state=tk.DISABLED)
        self.textField.grid(row=0, column=0, sticky=tk.NSEW)

        self.scrollbarX.config(command=self.textField.xview)
        self.scrollbarY.config(command=self.textField.yview)

        btnCopy = ttk.Button(self.mainFrame, text="Copy to clipboard",
            command=self.toclip, width=16)
        btnCopy.grid(row=2, column=0, pady=7, sticky=tk.SW)

        btnOk = ttk.Button(self.mainFrame, text="OK", command=self.ok,
            width=16)
        btnOk.grid(row=2, column=0, sticky=tk.SE, pady=7)
        btnOk.focus_set()

        self.top.bind('<Control-c>', func=self.toclip)
        self.top.bind("<Return>", self.ok)

        self.textField.tag_add('Date', '1.0', '1.9')
        bold_font = tkFont.Font(self.textField, self.textField.cget("font"))
        bold_font.configure(weight="bold")
        self.textField.tag_configure('Date', font=bold_font,
            foreground="blue")
        self.textField.tag_add('Version', '2.0', '2.15')
        bold_font = tkFont.Font(self.textField, self.textField.cget("font"))
        bold_font.configure(weight="bold")
        self.textField.tag_configure('Version', font=bold_font,
            foreground="blue")
        self.textField.tag_add('Platform', '3.0', '3.9')
        bold_font = tkFont.Font(self.textField, self.textField.cget("font"))
        bold_font.configure(weight="bold")
        self.textField.tag_configure('Platform', font=bold_font,
            foreground="blue")
        self.textField.tag_add('CallingDir', '4.0', '4.12')
        bold_font = tkFont.Font(self.textField, self.textField.cget("font"))
        bold_font.configure(weight="bold")
        self.textField.tag_configure('CallingDir', font=bold_font,
            foreground="blue")
        self.textField.tag_add('WorkingDir', '5.0', '5.12')
        bold_font = tkFont.Font(self.textField, self.textField.cget("font"))
        bold_font.configure(weight="bold")
        self.textField.tag_configure('WorkingDir', font=bold_font,
            foreground="blue")
        self.textField.tag_add('SystemEncoding', '6.0', '6.24')
        bold_font = tkFont.Font(self.textField, self.textField.cget("font"))
        bold_font.configure(weight="bold")
        self.textField.tag_configure('SystemEncoding', font=bold_font,
            foreground="blue")
        self.textField.tag_add('FileEncoding', '7.0', '7.29')
        bold_font = tkFont.Font(self.textField, self.textField.cget("font"))
        bold_font.configure(weight="bold")
        self.textField.tag_configure('FileEncoding', font=bold_font,
            foreground="blue")

        self.top.update_idletasks()
        xp = (self.top.winfo_screenwidth() / 2) - \
             (self.top.winfo_width() / 2) - 50
        yp = (self.top.winfo_screenheight() / 2) - \
             (self.top.winfo_height() / 2) - 50
        glist = [self.top.winfo_width(), self.top.winfo_height(), xp, yp]
        self.top.geometry('{0}x{1}+{2}+{3}'.format(*glist))
        self.top.protocol("WM_DELETE_WINDOW", self.ok)
        self.top.minsize(width=200, height=200)

        self.top.columnconfigure(0, weight=1)
        self.top.rowconfigure(0, weight=1)
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)

        self.top.transient(self.parent)
        self.top.grab_set()
        if self.parent is not None:
            self.parent.wait_window(self.top)

    def buildExceptionInfo(self, additionalMessage=None):
        if not additionalMessage:
            additionalMessage = ""
        errMsg = """Date (UTC): {0}
Python version: {1}
Platform: {2}
Calling dir: {3}
Working dir: {4}
System default encoding: {5}
System default file encoding: {6}
{7}
{9}
{7}
{8}""".format(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        sys.version.split()[0],
        platform.platform(),
        os.getcwd(),
        sys.path[1],
        sys.getdefaultencoding(),
        sys.getfilesystemencoding(),
        "-" * 58,
        "".join(traceback.format_exception(*sys.exc_info())),
        additionalMessage)
        return errMsg

    def toclip(self, event=None):
        self.top.clipboard_clear()
        self.top.clipboard_append(self.textField.get(index1=1.0,
            index2=tk.END + '-1c'))

    def ok(self, *args):
        self.top.destroy()
