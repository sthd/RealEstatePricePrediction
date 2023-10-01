import tkinter
import tkinter.messagebox
import customtkinter as ctk

from DataToCSV.stringsForModifiers import NatureOfRights_mappings

#ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
#ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class CheckboxFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=140, corner_radius=0)

        self.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self, text="Checkbox GUI", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.checkbox_slider_frame = ctk.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=0, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_2 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_3 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_3.grid(row=2, column=0, pady=20, padx=20, sticky="n")

        #self.sidebar_frame.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
        #self.checkbox_3.configure(state="disabled")
        #self.checkbox_1.select()


    def sidebar_button_event(self):
        print("sidebar_button click")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
