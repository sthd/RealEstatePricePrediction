import tkinter
import tkinter.messagebox
import customtkinter as ctk
import pandas as pd

from DataToCSV.stringsForModifiers import NatureOfRights_mappings

#ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
#ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class TextEntriesFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=140, corner_radius=0)

        self.grid_rowconfigure(4, weight=1)
        #self.logo_label = ctk.CTkLabel(self, text="TextEntries GUI", font=ctk.CTkFont(size=20, weight="bold"))
        #self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.checkbox_entries = []
        self.option_menus = []

        # Define options for the option menus
        option_lists = [
            ["Option 1", "Option 2", "Option 3"],
            ["Option A", "Option B", "Option C"],
            ["Choice X", "Choice Y", "Choice Z"],
            ["Item I", "Item II", "Item III"]
        ]

        for i in range(19):
            # Create a title label
            title_label = ctk.CTkLabel(self, text=f"Title {i + 1}", width=40, height=1)

            title_label.grid(row=1, column=i, padx=10, pady=10)

            # Create a text entry
            entry = ctk.CTkEntry(self, width=40, height=10)
            entry.grid(row=2, column=i, padx=10, pady=10)
            self.checkbox_entries.append(entry)

        #right_hand_side_list = list(NatureOfRights_mappings.values())
        #self.optionmenu_1 = ctk.CTkOptionMenu(self, values=right_hand_side_list)
        #self.optionmenu_1.grid(row=1, column=20, padx=20, pady=(20, 10))
        #
        #self.optionmenu_2 = ctk.CTkOptionMenu(self, values=["nio", "pod"])
        #self.optionmenu_2.grid(row=1, column=21, padx=20, pady=(20, 10))

        for j in range(4):
            # Create an option menu
            option_menu = ctk.CTkOptionMenu(self, values=option_lists[j])
            option_menu.grid(row=1, column=19+j, padx=10, pady=10)
            self.option_menus.append(option_menu)

        self.save_button = ctk.CTkButton(self, text="Save", command=self.save_entries, width=40, height=1)
        self.save_button.grid(row=3, column=0, pady=(10, 10))



    def save_entries(self):
        # Get the values from the entries
        entry_values = [entry.get() for entry in self.checkbox_entries]

        # Get the selected options from the option menus
        #option_values = [option.get() for option in self.option_menus]

        # Create a DataFrame with the entry values
        df = pd.DataFrame({'Entries': entry_values})#, 'Options': option_values})

        # Display the DataFrame
        print(df)
        df.to_csv(f"entries.csv")




        #for j in range(20, 24):
        #    # Create an option menu
        #    option_menu = ctk.CTkOptionMenu(self, option_lists[j % 20])
        #    option_menu.grid(row=2, column=j, padx=10, pady=10)
        #    self.option_menus.append(option_menu)


        #for i in range(19):
        #    # Create a title label
        #    title_label = ctk.CTkLabel(self.checkbox_slider_frame, text=f"Title {i+1}")
        #    title_label.grid(row=i//19, column=i%19, padx=10, pady=10)
        #
        #    # Create a text entry
        #    entry = ctk.CTkEntry(self.checkbox_slider_frame, width=10, height=1)
        #    entry.grid(row=(i//19)+1, column=i%19, padx=10, pady=10)
        #
        #    self.checkbox_entries.append(entry)

        #right_hand_side_list = list(NatureOfRights_mappings.values())
        #print(f" the rhs is {right_hand_side_list}")
        #self.tabview = ctk.CTkTabview(self, width=250)
        #self.tabview.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        #self.tabview.add("CTkTabview")
        #self.optionmenu_1 = ctk.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
        #                                      values=right_hand_side_list)
        #self.optionmenu_1.grid(row=1, column=20, padx=20, pady=(20, 10))
        ## Create a button to save the entries