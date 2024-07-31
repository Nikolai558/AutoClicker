from customtkinter import CTkToplevel, CTkLabel
from pynput import mouse


class CustomTKCoordinateWindow(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.attributes('-topmost', True)
        self.overrideredirect(True)
        self.geometry("100x25")
        self.label = CTkLabel(self, text="")
        self.label.pack()

        self.selected_coords = None
        self.mouse_listener = None

        # Start the mouse listener
        self.start_mouse_listener()

    def start_mouse_listener(self):
        self.mouse_listener = mouse.Listener(on_move=self.update_position, on_click=self.select_position)
        self.mouse_listener.start()

    def update_position(self, x, y):
        self.geometry(f"100x25+{x}+{y}")
        self.lift()
        self.label.configure(text=f"({x}, {y})")

    def select_position(self, x, y, button, pressed):
        if pressed:
            self.selected_coords = (x, y)
            if self.mouse_listener:
                self.mouse_listener.stop()
            self.destroy()

    def on_press(self, key):
        if key == mouse.Button.esc:
            if self.mouse_listener:
                self.mouse_listener.stop()
            self.destroy()
            print("Selection Cancelled")

    def destroy(self):
        # Ensure the listener stops when the window is destroyed
        if self.mouse_listener:
            self.mouse_listener.stop()
        super().destroy()



