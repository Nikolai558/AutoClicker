import customtkinter
from CustomFrames import CustomClickIntervalFrame, CustomClickOptionFrame, CustomClickRepeatFrame, CustomCursorPositionFrame, CustomActionFrame
from CustomWidgets import CustomTKEntry


class App(customtkinter.CTk):
    HEIGHT = "350"
    WIDTH = "460"

    def __init__(self):
        super().__init__()
        self.title('Personal AutoClicker')
        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.attributes('-topmost', True)

        self.click_interval_frame = CustomClickIntervalFrame(self)
        self.click_interval_frame.grid(column=0, row=0, padx=10, pady=5, ipadx=10, ipady=10, columnspan=2)

        self.click_option_frame = CustomClickOptionFrame(self)
        self.click_option_frame.grid(column=0, row=1, padx=(10, 0), pady=5, ipadx=10, ipady=10, sticky="w")

        self.click_option_frame = CustomClickRepeatFrame(self)
        self.click_option_frame.grid(column=1, row=1, padx=(0, 10), pady=5, ipadx=10, ipady=10, sticky="ne")

        self.cursor_position_frame = CustomCursorPositionFrame(self)
        self.cursor_position_frame.grid(column=0, row=2, padx=(10, 0), pady=5, ipadx=10, ipady=10, sticky="nw", columnspan=2)

        self.action_frame = CustomActionFrame(self)
        self.action_frame.grid(column=0, row=3, padx=(10, 0), pady=5, ipadx=10, ipady=10, columnspan=2, sticky="nsw")


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
