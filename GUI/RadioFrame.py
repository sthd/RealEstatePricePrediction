import tkinter
import tkinter.messagebox
import customtkinter as ctk

from DataToCSV.stringsForModifiers import NatureOfRights_mappings

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"





class RadioFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=140, corner_radius=0)

        self.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self, text="Radio GUI", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        #Radio Frame
        self.radiobutton_frame = ctk.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = ctk.CTkLabel(master=self.radiobutton_frame, text="Top rhs:")
        self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")

        self.radio_button_1 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=0, pady=10, padx=20, sticky="n")

        self.radio_button_2 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=0, pady=10, padx=20, sticky="n")

        self.radio_button_3 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=0, pady=10, padx=20, sticky="n")

        self.radio_button_3.configure(state="disabled")
        #self.radio_frame.appearance_mode_optionmenu.set("Dark")
        #self.radio_frame.scaling_optionmenu.set("100%")

    def sidebar_button_event(self):
        print("sidebar_button click")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
