from tkinter import IntVar
from customtkinter import CTkFrame, CTkRadioButton, CTkLabel, CTkButton
from CustomWidgets import CustomTKEntry


class CustomCursorPositionFrame(CTkFrame):
    def __init__(self, parent):
        """
        Initializes a frame for setting cursor position options.
        This frame provides options for selecting the cursor's current location
        or specifying a custom location by picking coordinates.

        :param parent: The parent window to which this frame belongs.
        """
        super().__init__(parent)
        self.radio_var = IntVar(value=1)

        self.grid_rowconfigure(0, weight=1, pad=0)
        self.grid_columnconfigure(0, weight=1, pad=0)

        self.current_location_radio_button = CTkRadioButton(self, text="Current Location", variable=self.radio_var, value=1)
        self.pick_location_radio_button = CTkRadioButton(self, text="", variable=self.radio_var, value=2, width=10)

        self.pick_location_button = CTkButton(self, text="Pick Location", width=100)

        self.x_label = CTkLabel(self, text="X")
        self.x_entry = CustomTKEntry(self, placeholder_text="0", width=40)

        self.y_label = CTkLabel(self, text="Y")
        self.y_entry = CustomTKEntry(self, placeholder_text="0", width=40)

        self.current_location_radio_button.grid(row=0, column=0, padx=(10, 0), pady=(0, 0), sticky="w")
        self.pick_location_radio_button.grid(row=0, column=1, padx=(10, 0), pady=(0, 0), sticky="e")
        self.pick_location_button.grid(row=0, column=2, padx=(10, 0), pady=(0, 0), sticky="e")
        self.x_label.grid(row=0, column=3, padx=(10, 0), pady=(0, 0), sticky="e")
        self.x_entry.grid(row=0, column=4, padx=(10, 0), pady=(0, 0), sticky="e")
        self.y_label.grid(row=0, column=5, padx=(10, 0), pady=(0, 0), sticky="e")
        self.y_entry.grid(row=0, column=6, padx=(10, 6), pady=(0, 0), sticky="e")
