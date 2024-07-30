from tkinter import IntVar
from customtkinter import CTkFrame, CTkRadioButton, CTkLabel
from CustomWidgets import CustomTKEntry


class CustomClickRepeatFrame(CTkFrame):
    def __init__(self, parent):
        """
        Initializes a frame for user input of repeat click options.
        This frame allows the user to choose between a fixed number of repeats or
        repeating the action until stopped. The options include setting the number of
        times to repeat the action or selecting an option to continue indefinitely.

        :param parent: The window that this frame belongs to.
        """
        super().__init__(parent)
        self.grid_rowconfigure(0, weight=1, pad=0)
        self.grid_columnconfigure(0, weight=1)

        self.radio_var = IntVar(value=2)

        self.repeat_radio_button = CTkRadioButton(self, text="Repeat:", variable=self.radio_var, value=1)
        self.repeat_times_entry = CustomTKEntry(self, placeholder_text="1", width=38)
        self.repeat_times_label = CTkLabel(self, text=" Times")
        self.until_stopped_radio_button = CTkRadioButton(self, text="Repeat Until Stopped", variable=self.radio_var, value=2)

        self.repeat_radio_button.grid(row=0, column=0, padx=(10, 0), sticky="w")
        self.repeat_times_entry.grid(row=0, column=1)
        self.repeat_times_label.grid(row=0, column=2, padx=(0, 10), sticky="e")

        self.until_stopped_radio_button.grid(row=1, column=0, padx=(10, 0), pady=18, columnspan=3, sticky="w")
