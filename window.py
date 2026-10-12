from tkinter import *
from tkinter import Tk
import secrets, string


class MainWindow:

    def random_title(self):
        letters = string.ascii_letters
        result = ''.join(secrets.choice(letters) for _ in range(20))
        return result

    def main_window(self):
        window = Tk()
        window.title(self.random_title())
        window.geometry("600x400+450-350")
        window.resizable(False, False)
        buttons = TaskManagerButton(window)
        buttons.task_manager_button()   
        buttons1 = PcInfoButton(window)
        buttons1.pc_info_button()
        buttons2 = AutoRunListButton(window)
        buttons2.auto_run_list_button()
        window.mainloop()

class TaskManagerButton:
    def __init__(self, parent_window):
        self.window = parent_window

    def task_manager_button(self):
        tm_button = Button(self.window, text="Task Manager")
        tm_button.config(font=("Arial", 30, "bold"), command=self.open_task_manager)
        tm_button.pack()

    def open_task_manager(self):
        from main import TaskManager

        task_manager = TaskManager(self.window)
        task_manager.start_task_manager()

class PcInfoButton:
    def __init__(self, parent_window):
        self.window = parent_window

    def pc_info_button(self):
        pc_info_button = Button(self.window, text="PC INFO")
        pc_info_button.config(font=("Arial", 30, "bold"), command=self.open_pc_info)
        pc_info_button.pack()

    def open_pc_info(self):
        from pc_info import PcInfo

        pc_info = PcInfo(self.window)
        pc_info.start_pc_info()

class AutoRunListButton:
    def __init__(self, parent_window):
        self.window = parent_window

    def auto_run_list_button(self):
        auto_run_list_button = Button(self.window, text="AutoRun")
        auto_run_list_button.config(font=("Arial", 30, "bold"), command=self.open_auto_run_list)
        auto_run_list_button.pack()

    def open_auto_run_list(self):
        from autorun import CheckListAutoRun
        autorun_list = CheckListAutoRun(self.window)
        autorun_list.start_autorun()




if __name__ == "__main__":
    app = MainWindow()
    app.main_window()







