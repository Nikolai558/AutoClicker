from customtkinter import CTkFrame, CTkRadioButton, CTkLabel, CTkButton


class CustomActionFrame(CTkFrame):
    START_KEY_STR = "F6"

    def __init__(self, parent):
        """
        Initializes a frame for controlling various actions.
        This frame includes buttons to start and stop an action, open hotkey settings,
        and access a record and playback feature. The start and stop actions are associated
        with a predefined hotkey.

        :param parent: The parent window to which this frame belongs.
        """
        super().__init__(parent)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, minsize=210)
        self.columnconfigure(1, weight=1, minsize=210)

        self.start_button = CTkButton(self, text=f"Start ({self.START_KEY_STR})")
        self.stop_button = CTkButton(self, text=f"Stop ({self.START_KEY_STR})")
        self.hotkey_settings_button = CTkButton(self, text=f"Hotkey Setting")
        self.record_playback_button = CTkButton(self, text=f"Record & Playback")

        self.start_button.grid(row=0, column=0, padx=(10, 20))
        self.hotkey_settings_button.grid(row=1, column=0, padx=(10, 20), pady=(0, 10))

        self.stop_button.grid(row=0, column=1, padx=(20, 20))
        self.record_playback_button.grid(row=1, column=1, padx=(20, 20), pady=(0, 10))

