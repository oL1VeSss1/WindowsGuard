import winreg
from tkinter import *
from window import MainWindow


class CheckListAutoRun:
    def __init__(self, window):
        self.parent = window

    def autorun_list(self):
        apps = []
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_READ)
        a = 0
        while True:
            try:
                name, value, _ = winreg.EnumValue(key, a)
                apps.append({"Name": name, "Path": value})
                a +=1
            except (FileNotFoundError, OSError):
                break
        winreg.CloseKey(key)
        return apps

    def result(self):
        data = self.autorun_list()
        for obj in data:
            return f"{obj["Name"]} --> {obj["Path"]}"

    def start_autorun(self):
        ar = Toplevel(self.parent)
        label = Label(ar, text=self.result(), font=("Arial", 15, "bold"))
        ar.title("AutoRun")
        ar.state("zoomed")
        label.pack()

if __name__ == "__main__":
    app = MainWindow()
    autorun_list = CheckListAutoRun(app)
    app.main_window()