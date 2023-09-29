import tkinter
import tkinter.messagebox
import customtkinter

from DataToCSV.stringsForModifiers import NatureOfRights_mappings

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class ScrollableFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=140, corner_radius=0)
        self.logo_label = customtkinter.CTkLabel(self, text="Scrollable GUI",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.grid_rowconfigure(4, weight=1)

        #scrollable_frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="bottom lhs")
        self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
           switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
           switch.grid(row=i, column=0, padx=10, pady=(0, 20))
           self.scrollable_frame_switches.append(switch)
        self.scrollable_frame_switches[0].select()
        self.scrollable_frame_switches[4].select()