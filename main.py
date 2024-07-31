# [AutoClicker](https://github.com/Nikolai558/AutoClicker) Copyright (C) 2024 [Nikolai558](https://github.com/Nikolai558)
# Automate mouse clicks and key presses with customizable intervals, repetition, and cursor positions.
import time

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# [AutoClicker](https://github.com/Nikolai558/AutoClicker) Copyright (C) 2024 [Nikolai558](https://github.com/Nikolai558)


import keyboard
import pyautogui
import customtkinter
from CustomFrames import CustomClickIntervalFrame, CustomClickOptionFrame, CustomClickRepeatFrame, CustomCursorPositionFrame, CustomActionFrame
from CustomWidgets import CustomTKCoordinateWindow


class App(customtkinter.CTk):
    HEIGHT = "350"
    WIDTH = "460"

    def __init__(self):
        super().__init__()
        keyboard.add_hotkey('F6', self.toggle_action)
        self._is_running = False
        self._task_id = None

        self.title('Personal AutoClicker')
        self.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.attributes('-topmost', True)

        self.create_frames()
        self.place_frames()
        self.configure_button_commands()

    def create_frames(self):
        self.click_interval_frame = CustomClickIntervalFrame(self)
        self.click_option_frame = CustomClickOptionFrame(self)
        self.click_repeat_frame = CustomClickRepeatFrame(self)
        self.cursor_position_frame = CustomCursorPositionFrame(self)
        self.action_frame = CustomActionFrame(self)

    def place_frames(self):
        self.click_interval_frame.grid(column=0, row=0, padx=10, pady=5, ipadx=10, ipady=10, columnspan=2)
        self.click_option_frame.grid(column=0, row=1, padx=(10, 0), pady=5, ipadx=10, ipady=10, sticky="w")
        self.click_repeat_frame.grid(column=1, row=1, padx=(0, 10), pady=5, ipadx=10, ipady=10, sticky="ne")
        self.cursor_position_frame.grid(column=0, row=2, padx=(10, 0), pady=5, ipadx=10, ipady=10, sticky="nw", columnspan=2)
        self.action_frame.grid(column=0, row=3, padx=(10, 0), pady=5, ipadx=10, ipady=10, columnspan=2, sticky="nsw")

    def configure_button_commands(self):
        self.action_frame.start_button.configure(command=self.start)
        self.action_frame.stop_button.configure(command=self.stop)
        self.cursor_position_frame.pick_location_button.configure(command=self.pick_location)

    def pick_location(self):
        self.cursor_position_frame.radio_var.set(2)
        coord_window = CustomTKCoordinateWindow(self)
        self.wait_window(coord_window)  # Wait until the coordinate window is closed
        if coord_window.selected_coords:
            x, y = coord_window.selected_coords
            # Update your main application with the selected coordinates
            self.cursor_position_frame.x_entry.configure(placeholder_text=str(x))
            self.cursor_position_frame.y_entry.configure(placeholder_text=str(y))

    def start(self):
        self._is_running = True

        # Disable the start button
        self.action_frame.start_button.configure(state='disabled')

        # Enable the Stop Button
        self.action_frame.stop_button.configure(state='normal')

        # Get all information from User input/selections
        interval = self.click_interval_frame.get_total_interval()
        mouse_button = self.click_option_frame.mouse_button_dropdown.get().upper()
        click_type = self.click_option_frame.click_type_dropdown.get()
        repeat_duration = -1 if self.click_repeat_frame.radio_var.get() == 2 else self.click_repeat_frame.repeat_times_entry.get_value()
        location = None if self.cursor_position_frame.radio_var.get() == 1 else (self.cursor_position_frame.x_entry.get_value(), self.cursor_position_frame.y_entry.get_value())

        if click_type != "Key Press":
            self.auto_click(interval, repeat_duration, 2 if click_type == "Double" else 1, mouse_button, location)
        else:
            # TODO - Implement key press feature call here.
            self.stop()

    def auto_click(self, interval, amount, click_amt, click_button, click_pos=None):
        if self._is_running and (amount > 0 or amount == -1):
            if amount > 0:
                amount = amount - 1

            if click_pos:
                pyautogui.click(clicks=click_amt, button=click_button, x=click_pos[0], y=click_pos[1])
            else:
                pyautogui.click(clicks=click_amt, button=click_button)

            self._task_id = self.after(interval, self.auto_click, interval, amount, click_amt, click_button, click_pos)
        elif self._is_running and amount == 0:
            self.stop()


    def stop(self):
        self._is_running = False

        # Disable the stop Button
        self.action_frame.stop_button.configure(state='disabled')

        # Enable the Start Button
        self.action_frame.start_button.configure(state='normal')

        if self._task_id:
            self.after_cancel(self._task_id)
            self._task_id = None

    def toggle_action(self):
        if self._is_running:
            self.stop()
        else:
            self.start()

    def on_closing(self):
        if self._is_running:
            self.stop()
        keyboard.unhook_all_hotkeys()
        self.destroy()


def main():
    app = App()
    app.protocol('WM_DELETE_WINDOW', app.on_closing)
    try:
        app.mainloop()
    except KeyboardInterrupt:
        app.on_closing()


if __name__ == '__main__':
    main()
