# Text sizes
FONT = 'Calibri'
MAIN_TEXT_SIZE = 150
INPUT_FONT_SIZE = 26
SWITCH_FONT_SIZE = 18

# Colores

GREEN = '#50BFAB'
DARK_GREEN = '#3A8A7B'
WHITE = '#F2F2F2'
BLACK = '#2F1F1F'
LIGHT_GRAY = '#E8E8E8'
GRAY = '#D9D9D9'

# titile hex

TITLE_HEX_COLOR = 0x00ABBF50 

"""import customtkinter as ctk
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
        weightInput(self)

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


    
class weightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color= WHITE)
        self.grid(row = 2, column = 0, sticky = 'nsew', padx = 10, pady = 10)

        

if __name__ == '__main__':
    App()"""