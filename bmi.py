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
        self.title('BMI')
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
class ResultText(ctk.CTkLabel):
    def __init__(self, parent):
        font = ctk.CTkFont(family = FONT, size= MAIN_TEXT_SIZE, weight= 'bold')
        super().__init__(
            master = parent,
            text = 34.4,
            font = font,
            text_color = WHITE)
        self.grid(row = 0, column = 0, rowspan = 2, sticky = 'nwes')
class weightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color= WHITE)
        self.grid(row = 2, column = 0, sticky = 'nsew', padx = 10, pady = 10)

        # layout 
        self.rowconfigure(0, weight= 1, uniform= "b")
        self.columnconfigure(0, weight= 2, uniform= "b")
        self.columnconfigure(1, weight= 1, uniform= "b")
        self.columnconfigure(2, weight= 3, uniform= "b")
        self.columnconfigure(3, weight= 1, uniform= "b")
        self.columnconfigure(4, weight= 2, uniform= "b")
        
        # widgets
        
        # label
        font = ctk.CTkFont(family= FONT, size= INPUT_FONT_SIZE)
        label = ctk.CTkLabel(self, text= '34', text_color= BLACK, font= font)
        label.grid(row = 0, column = 2)
        # buttons
        minus_button = ctk.CTkButton(
            self,
            text= '-',
            fg_color=LIGHT_GRAY,
            font= font,
            text_color=BLACK,
            hover_color= GRAY,
            corner_radius= BUTTON_CORNER_RADIUS
            )
        minus_button.grid(row = 0, column = 0, sticky = 'ns', padx = 8, pady = 8)
        small_minus_button = ctk.CTkButton(
            self,
            text= '-',
            fg_color=LIGHT_GRAY,
            font= font,
            text_color=BLACK,
            hover_color= GRAY,
            corner_radius= BUTTON_CORNER_RADIUS
            )
        small_minus_button.grid(row = 0, column = 1, padx = 4, pady = 4)
        plus_button = ctk.CTkButton(
            self,
            text= '+',
            fg_color=LIGHT_GRAY,
            font= font,
            text_color=BLACK,
            hover_color= GRAY,
            corner_radius= BUTTON_CORNER_RADIUS
            )
        plus_button.grid(row = 0, column = 4, sticky = 'ns', padx = 8, pady = 8)
        small_plus_button = ctk.CTkButton(
            self,
            text= '+',
            fg_color=LIGHT_GRAY,
            font= font,
            text_color=BLACK,
            hover_color= GRAY,
            corner_radius= BUTTON_CORNER_RADIUS
            )
        small_plus_button.grid(row = 0, column = 3, padx = 4, pady = 4)


if __name__ == '__main__':
    App()

    