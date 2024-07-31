import pyautogui
import threading
from queue import Queue
from customtkinter import CTk, CTkLabel


class MouseTrackerApp(CTk):
    def __init__(self, result_queue):
        super().__init__()
        self._task_id = None
        self.result_queue = result_queue

        self.attributes('-topmost', True)
        self.title = 'Mouse Tracker'
        self.geometry("200x100")

        self.position_lable = CTkLabel(self, text="X: 0, Y: 0")
        self.position_lable.pack(pady=20)

        self.bind("<Escape>", self.on_escape_key)
        self.bind("<Button-1>", self.on_mouse_click)

        self.current_position = None
        self.running = True

        self.update_position()

    def on_escape_key(self, event):
        self.save_and_close()

    def on_mouse_click(self, event):
        self.save_and_close()

    def update_position(self):
        if self.running:
            x, y = pyautogui.position()
            self.position_lable.configure(text=f"X: {x}, Y: {y}")
            self.current_position = (x, y)
            self._task_id = self.after(100, self.update_position)

    def save_and_close(self):
        self.running = False
        self.after_cancel(self._task_id)
        if self.current_position:
            self.result_queue.put(self.current_position)
        self.destroy()


def run_mouse_tracker(result_queue):
    app = MouseTrackerApp(result_queue)
    app.mainloop()


def get_mouse_position():
    result_queue = Queue()
    tracker_thread = threading.Thread(target=run_mouse_tracker, args=(result_queue,))
    tracker_thread.start()

    # Wait for the thread to complete and get the result
    tracker_thread.join()
    if not result_queue.empty():
        return result_queue.get()
    return 0, 0


if __name__ == "__main__":
    position = get_mouse_position()
    print(f"Final mouse position: {position}")
