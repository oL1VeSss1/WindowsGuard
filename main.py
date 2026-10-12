from window import MainWindow 
import psutil
from tkinter import *

class TaskManager:
    def __init__(self, window):
        self.parent = window


    def task_manager(self):
        result = []
        for process in psutil.process_iter(["name", "pid", "ppid", "status"]):
            try:
                info = process.info
                collect_info = f"{info['name']} -->  PID: {info['pid']}, PPID: {info['ppid']}, Status: {info['status']}"
                result.append(collect_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return result


    def start_task_manager(self):
        tm = Toplevel(self.parent)
        my_frame = Frame(tm)
        my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)
        my_listbox = Listbox(my_frame, yscrollcommand=my_scrollbar.set)
        my_scrollbar.config(command=my_listbox.yview)
        my_scrollbar.pack(expand=True, side=RIGHT, fill=Y)
        my_listbox.pack(expand=True, side=LEFT, fill=BOTH)
        my_frame.pack(fill=BOTH, expand=True)
        tm.state("zoomed")
        result = self.task_manager()
        self.result = result
        for item in result:
            my_listbox.insert(END, item)
        self.update(tm, my_listbox)
        return tm
    

    def update(self, tm, my_listbox):
        result = self.task_manager()
        for item in result:
            if item not in self.result:
                self.result.append(item)
                my_listbox.insert(END, item)
                print("Процесс добавлен")
            else:
                delete_procs = []
                index_procs = []
                listbox_items = my_listbox.get(0, END)

                for item in self.result:
                    if item not in result:
                        delete_procs.append(item)
                        if item in listbox_items:
                            id = listbox_items.index(item)
                            index_procs.append(id)
                            my_listbox.delete(id)  
                            print("Процесс завершен")

        tm.after(1000, self.update, tm, my_listbox)




if __name__ == "__main__":
    app = MainWindow()
    task_manager = TaskManager(app)
    app.main_window()

