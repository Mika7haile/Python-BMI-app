import customtkinter as ctk
from settings import *
from ctypes import windll, byref, sizeof, c_int


class App(ctk.CTk):
    def __init__(self):

        # window setup
        super().__init__(fg_color= GREEN)
        self.title('')
        self.iconbitmap('bmi.ico')
        self.geometry('400x400')
        self.resizable(False, False)
        self.change_title_bar_color()
        self.mainloop()
    def change_title_bar_color(self):
        HWND = windll.user32.GetParent(self.winfo_id())
        title_bar_color = 0x0000FF00
        windll.dwmapi.DwmSetWindowAttribute(
            HWND,
            35,
            byref(c_int(title_bar_color)),
            sizeof(c_int)
        )        

App()