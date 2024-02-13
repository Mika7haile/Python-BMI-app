import customtkinter as ctk
from settings import *


class App(ctk.CTk):
    def __init__(self):

        # window setup
        super().__init__(fg_color= GREEN)

        self.mainloop()
App()