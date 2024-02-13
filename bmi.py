import customtkinter as ctk
from settings import *
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

class App(ctk.CTk):
    def __init__(self):

        # window setup
        super().__init__(fg_color= GREEN)
        self.title('')
        self.iconbitmap('bmi.ico')
        self.geometry('400x400')
        self.resizable(False, False)
        self.change_title_bar_color(TITLE_HEX_COLOR)

        # layout
        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0,1,2,3), weight = 1, uniform='as')
        # widgets
        ResultText(self)

        self.mainloop()
    def change_title_bar_color(self, HexColore):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            title_bar_color = HexColore
            windll.dwmapi.DwmSetWindowAttribute(
                HWND,
                35,
                byref(c_int(title_bar_color)),
                sizeof(c_int)
        )        
        except: 
            pass
class ResultText(ctk.CTkLabel):
    def __init__(self, parent):
        font = ctk.CTkFont(family = FONT, size= MAIN_TEXT_SIZE, weight= 'bold')
        super().__init__(
            master = parent,
            text = 34.4,
            font = font,
            text_color = WHITE)
        self.grid(row = 0, column = 0, rowspan = 2, sticky = 'nwes')

if __name__ == '__main__':
    App()