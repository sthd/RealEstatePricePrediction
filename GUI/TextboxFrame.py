import tkinter
import tkinter.messagebox
import customtkinter as ctk

from DataToCSV.stringsForModifiers import NatureOfRights_mappings

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class TextboxFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=140, corner_radius=0)

        self.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self, text="TabView GUI", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        #self.radiobutton_frame = ctk.CTkFrame(self)
        #self.radiobutton_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.textbox = ctk.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", "How to use this predictor\n\n" +
                            "In order to use the predictor you need to enter all the values requested by the model.\n\n")