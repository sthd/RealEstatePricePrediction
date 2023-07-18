import tkinter
import tkinter.messagebox
import customtkinter as ctk

from DataToCSV.stringsForModifiers import NatureOfRights_mappings

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

from SidebarFrame import SidebarFrame
from RadioFrame import RadioFrame
from CheckboxFrame import CheckboxFrame
from SliderProgressbarFrame import SliderProgressbarFrame
from TabView import TabViewFrame
from TextboxFrame import TextboxFrame

from TextEntries import TextEntriesFrame

class PredictorGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Predict Property Prices in Israel")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = SidebarFrame(self)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.appearance_mode_optionmenu.set("Dark")
        self.sidebar_frame.scaling_optionmenu.set("100%")

        self.textentries_frame = TextEntriesFrame(self)
        self.textentries_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")

        #self.entry_values = []
        #
        #self.entry_labels = []
        #self.entry_boxes = []
        #for i in range(19):
        #    label = ctk.CTkLabel(self, text=f"Value {i+1}:")
        #    label.grid(row=i, column=0, padx=(20, 10), pady=(10, 10), sticky="w")
        #    entry = ctk.CTkEntry(self)
        #    entry.grid(row=i, column=1, padx=(10, 20), pady=(10, 10), sticky="e")
        #    self.entry_labels.append(label)
        #    self.entry_boxes.append(entry)

        #self.radio_frame = RadioFrame(self)
        #self.radio_frame.grid(row=1, column=1, rowspan=4, sticky="nsew")



        #self.entry = ctk.CTkEntry(self, placeholder_text="CTkEntry")
        #self.entry.grid(row=2, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        #self.main_button_1 = ctk.CTkButton(master=self, fg_color="transparent", border_width=2,
        #                                             text_color=("gray10", "#DCE4EE"))
        #self.main_button_1.grid(row=0, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        #
        #self.tabview_frame = TabViewFrame(self)
        #self.tabview_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        #
        #self.slider_progressbar_frame = SliderProgressbarFrame(self)
        #self.slider_progressbar_frame.grid(row=0, column=5, padx=(20, 0), pady=(20, 0), sticky="nsew")
        #
        #self.checkbox_frame = CheckboxFrame(self)
        #self.checkbox_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        #
        #self.textbox_frame = TextboxFrame(self)
        #self.textbox_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")


    def open_input_dialog_event(self):
        dialog = ctk.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())


if __name__ == "__main__":
    predictor_gui = PredictorGUI()
    predictor_gui.mainloop()
