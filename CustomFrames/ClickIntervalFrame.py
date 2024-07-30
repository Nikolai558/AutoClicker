from customtkinter import CTkFrame, CTkLabel
from CustomWidgets import CustomTKEntry


class CustomClickIntervalFrame(CTkFrame):
    Y_PADDING = (5, 5)
    X_ENTRY_PADDING = (2, 0)
    X_LABEL_PADDING = (10, 0)
    def __init__(self, parent):
        """
        Initializes a frame for user input of the desired click interval.
        This frame allows the user to enter values for Hours, Minutes, Seconds,
        and Milliseconds.

        :param parent: The window that this frame belongs to.
        """
        super().__init__(parent)
        self.grid_rowconfigure(0, weight=1)

        # Labels
        self.hours_label = CTkLabel(self, text="Hours:")
        self.minutes_label = CTkLabel(self, text="Minutes:")
        self.seconds_label = CTkLabel(self, text="Seconds:")
        self.milliseconds_label = CTkLabel(self, text="Milliseconds:")

        # User Entry Fields
        self.hours_entry = CustomTKEntry(self, placeholder_text="0", width=40)
        self.minutes_entry = CustomTKEntry(self, placeholder_text="0", width=40)
        self.seconds_entry = CustomTKEntry(self, placeholder_text="0", width=40)
        self.milliseconds_entry = CustomTKEntry(self, placeholder_text="100", width=40)

        # Placing the elements into the Frame
        self.hours_label.grid(row=0, padx=self.X_LABEL_PADDING, column=0, pady=self.Y_PADDING)
        self.hours_entry.grid(row=0, padx=self.X_ENTRY_PADDING, column=1, pady=self.Y_PADDING)
        self.minutes_label.grid(row=0, padx=self.X_LABEL_PADDING, column=2, pady=self.Y_PADDING)
        self.minutes_entry.grid(row=0, padx=self.X_ENTRY_PADDING, column=3, pady=self.Y_PADDING)
        self.seconds_label.grid(row=0, padx=self.X_LABEL_PADDING, column=4, pady=self.Y_PADDING)
        self.seconds_entry.grid(row=0, padx=self.X_ENTRY_PADDING, column=5, pady=self.Y_PADDING)
        self.milliseconds_label.grid(row=0, padx=self.X_LABEL_PADDING, column=6, pady=self.Y_PADDING)
        self.milliseconds_entry.grid(row=0, padx=self.X_ENTRY_PADDING, column=7, pady=self.Y_PADDING)
