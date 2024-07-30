# [AutoClicker](https://github.com/Nikolai558/AutoClicker) Copyright (C) 2024 [Nikolai558](https://github.com/Nikolai558)


from customtkinter import CTkEntry


class CustomTKEntry(CTkEntry):
    def __init__(self, parent, *args, **kwargs):
        CTkEntry.__init__(self, parent, *args, **kwargs)

    def get_value(self):
        current_value = self.get()
        if current_value and current_value != "":
            return self.get()
        else:
            return self.cget("placeholder_text")
