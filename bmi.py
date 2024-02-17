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

        # data
        self.metric_bool = ctk.BooleanVar(value= True)
        self.height_int = ctk.IntVar(value= 154)
        self.weight_float = ctk.DoubleVar(value= 65)
        self.bmi_string = ctk.StringVar()
        self.update_bmi()

        # interactive slider
        self.height_int.trace('w', self.update_bmi)
        self.weight_float.trace('w', self.update_bmi)
        self.metric_bool.trace('w', self.change_units)
        # widgets
        ResultText(self, self.bmi_string)
        self.weight_input = WeightInput(self, self.weight_float, self.metric_bool)
        self.height_input = HeightInput(self, self.height_int, self.metric_bool)
        UnitSwitcher(self, self.metric_bool)
        self.mainloop()
    def change_units(self, *args):
        self.height_input.update_text(self.height_int.get())
        self.weight_input.update_weight()

    def update_bmi(self, *args):
        height = self.height_int.get()/ 100
        weight = self.weight_float.get() 
        resultText = round(weight / height** 2, 2)
        self.bmi_string.set(resultText)

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
    def __init__(self, parent, bmi_string):
        font = ctk.CTkFont(family = FONT, size= MAIN_TEXT_SIZE, weight= 'bold')
        super().__init__(
            master = parent,
            textvariable = bmi_string,
            text = 34.4,
            font = font,
            text_color = WHITE)
        self.grid(row = 0, column = 0, rowspan = 2, sticky = 'nwes')
class WeightInput(ctk.CTkFrame):
    def __init__(self, parent,weight_float, metric_bool):
        super().__init__(parent, fg_color= WHITE)
        self.grid(row = 2, column = 0, sticky = 'nsew', padx = 10, pady = 10)
        self.weight_float = weight_float
        self.metric_bool = metric_bool


        # layout 
        self.rowconfigure(0, weight= 1, uniform= "b")
        self.columnconfigure(0, weight= 2, uniform= "b")
        self.columnconfigure(1, weight= 1, uniform= "b")
        self.columnconfigure(2, weight= 3, uniform= "b")
        self.columnconfigure(3, weight= 1, uniform= "b")
        self.columnconfigure(4, weight= 2, uniform= "b")

        # data (output logic)
        self.weight_text = ctk.StringVar(value= f"{weight_float.get()} Kg")
        self.update_weight()
        # widgets
        
        # label
        font = ctk.CTkFont(family= FONT, size= INPUT_FONT_SIZE)
        label = ctk.CTkLabel(
            self,
            text_color= BLACK,
            font= font,
            textvariable = self.weight_text)
        label.grid(row = 0, column = 2)
        # buttons
        minus_button = ctk.CTkButton(
            self,
            text= '-',
            fg_color=LIGHT_GRAY,
            font= font,
            text_color=BLACK,
            hover_color= GRAY,
            corner_radius= BUTTON_CORNER_RADIUS,
            command = lambda: self.update_weight(('minus', 'large')) 
            )
        minus_button.grid(row = 0, column = 0, sticky = 'ns', padx = 8, pady = 8)
        small_minus_button = ctk.CTkButton(
            self,
            text= '-',
            fg_color=LIGHT_GRAY,
            font= font,
            text_color=BLACK,
            hover_color= GRAY,
            corner_radius= BUTTON_CORNER_RADIUS,
            command = lambda: self.update_weight(('minus', 'small')) 
            )
        small_minus_button.grid(row = 0, column = 1, padx = 4, pady = 4)
        plus_button = ctk.CTkButton(
            self,
            text= '+',
            fg_color=LIGHT_GRAY,
            font= font,
            text_color=BLACK,
            hover_color= GRAY,
            corner_radius= BUTTON_CORNER_RADIUS,
            command = lambda: self.update_weight(('plus', 'large'))
            )
        plus_button.grid(row = 0, column = 4, sticky = 'ns', padx = 8, pady = 8)
        small_plus_button = ctk.CTkButton(
            self,
            text= '+',
            fg_color=LIGHT_GRAY,
            font= font,
            text_color=BLACK,
            hover_color= GRAY,
            corner_radius= BUTTON_CORNER_RADIUS,
            command = lambda: self.update_weight(('plus', 'small'))
            )
        small_plus_button.grid(row = 0, column = 3, padx = 4, pady = 4)
    def update_weight(self, info = None):
        if info:
            if self.metric_bool.get():
                amount = 1 if info[1] == 'large' else 0.1
            else:
                 amount = 0.453592 if info[1] == 'large' else 0.453592 / 16   
            if info[0] == 'plus':
                self.weight_float.set(self.weight_float.get() + amount)
            else:
                self.weight_float.set(self.weight_float.get() - amount)
        if self.metric_bool.get():   
            self.weight_text.set(f'{round(self.weight_float.get(), 1)} Kg')
        else:
            raw_ounces = self.weight_float.get() * 2.20462 * 16
            pounds, ounces = divmod(int(raw_ounces), 16)
            self.weight_text.set(f'{pounds} Lb {ounces} Oz')
class HeightInput(ctk.CTkFrame):
    def __init__(self, parent, height_int, metric_bool):
        super().__init__(parent, fg_color = WHITE)
        self.grid(row = 3, column = 0, sticky = 'nswe', padx = 10, pady = 10)
        # passed attribute
        self.metric_bool = metric_bool

        # widget and layout(pack)

        slider = ctk.CTkSlider(
            self,
            variable = height_int,
            button_color= GREEN,
            button_hover_color= GRAY,
            progress_color= GREEN,
            fg_color= LIGHT_GRAY,
            from_= 100,
            to=250,
            command= self.update_text
            )
        slider.pack(side = 'left', expand = True, fill = 'x', padx = 10, pady = 10)

        self.output_string = ctk.StringVar()
        self.update_text(height_int.get())
        output_text = ctk.CTkLabel(
            self,
            textvariable = self.output_string,
            text_color= BLACK,
            font = ctk.CTkFont(family= FONT, size= INPUT_FONT_SIZE)
            )
        output_text.pack(side= 'left', padx = 20)

    def update_text(self, amount):
        if self.metric_bool.get():
            text_string = str(int(amount))
            meter = text_string[0]
            cm = text_string[1:]
            self.output_string.set(f'{meter}.{cm}m')
        else:
            feet, inches = divmod(amount / 2.54, 12)
            self.output_string.set(f'{int(feet)}\'{int(inches)}\'')
class UnitSwitcher(ctk.CTkLabel):
    def __init__(self, parent, metric_bool):
        super().__init__(
            parent,
            text = 'Metric',
            text_color= DARK_GREEN,
            font= ctk.CTkFont(family= FONT, size = SWITCH_FONT_SIZE)
            )
        self.place(relx = 0.98, rely = 0.01, anchor = 'ne')
        self.metric_bool = metric_bool
        self.bind('<Button>', self.change_units)
        
    def change_units(self, event):
        self.metric_bool.set(not self.metric_bool.get())
        if self.metric_bool.get():
            self.configure(text = 'Metric')
        else:
            self.configure(text = 'Imperial')
if __name__ == '__main__':
    App()