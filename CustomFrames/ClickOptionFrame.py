from customtkinter import CTkFrame, CTkLabel, CTkOptionMenu


class CustomClickOptionFrame(CTkFrame):
    def __init__(self, parent):
        """
        Initializes a frame for user input of mouse click options.
        This frame allows the user to select the mouse button (Left, Middle, Right)
        and/or the type of click (Single, Double, Key Press).
        If Key Press is selected, the program will act as the keyboard button press.

        :param parent: The window that this frame belongs to.
        """
        super().__init__(parent)
        self.grid_rowconfigure(0, weight=1, pad=0, minsize=10)
        self.grid_columnconfigure(0, weight=1, minsize=75)

        self.mouse_button_label = CTkLabel(self, text="Mouse Button:")
        self.click_type_label = CTkLabel(self, text="Click Type:")

        self.mouse_button_dropdown = CTkOptionMenu(self,
                                                   width=100,
                                                   values=["Left", "Middle", "Right"])
        self.click_type_dropdown = CTkOptionMenu(self,
                                                 width=100,
                                                 values=["Single", "Double", "Key Press"])

        self.mouse_button_label.grid(row=0, column=0, pady=(0, 10), padx=(10, 0), sticky="w")
        self.click_type_label.grid(row=1, column=0, pady=10, padx=(10, 0), sticky="w")
        self.mouse_button_dropdown.grid(row=0, column=1, pady=(0, 10), padx=(0, 10), sticky="e")
        self.click_type_dropdown.grid(row=1, column=1, pady=(0, 10), padx=(0, 10), sticky="e")

