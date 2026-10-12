from window import MainWindow
import psutil
import platform
from tkinter import *

class PcInfo:
    def __init__(self, window):
        self.parent = window

    def collect_info(self):
        info = platform.uname()
        memory = psutil.virtual_memory()
        cpu_freq = psutil.cpu_freq()
        result = {
                'System': info.system,
                'Node': info.node,
                'Release' : info.release,
                'Version' : info.version,
                'Machine' : info.machine,
                'Processor' : info.processor,
                'Total Ram' : f"{memory.total / (1024**3):.2f} GB",
                'Avaliable Ram' : f"{memory.available / (1024**3):.2f} GB",
                'CPU frequency' : f"{cpu_freq.current / 1000:.2f} GHz "
        }
        return "\n".join(f"{key}: {value}" for key, value in result.items()) # возвращаем данные, объединяем ключ и значение


    def start_pc_info(self):
        pi = Toplevel(self.parent)
        label = Label(pi, text=self.collect_info(), font=("Arial", 15, "bold"))
        pi.title("PC INFO")
        pi.state("zoomed")
        label.pack()
        


if __name__ == "__main__":
    app = MainWindow()
    pc_info = PcInfo(app)
    app.main_window()