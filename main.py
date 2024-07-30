import customtkinter
from CustomFrames import CustomClickIntervalFrame
from CustomWidgets import CustomTKEntry


class App(customtkinter.CTk):
    HEIGHT = "350"
    WIDTH = "460"

    def __init__(self):
        super().__init__()
        self.title('Personal AutoClicker')
        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')

        self.click_interval_frame = CustomClickIntervalFrame(self)
        self.click_interval_frame.grid(column=0, row=0, padx=10, pady=10, ipadx=10, ipady=10, columnspan=2)


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
