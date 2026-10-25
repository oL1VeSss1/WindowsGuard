from window import MainWindow 
import psutil
from tkinter import *
from tkinter import ttk

class TaskManager:
    def __init__(self, window):
        self.parent = window


    def task_manager(self):
        result = []
        for process in psutil.process_iter(["name", "pid", "ppid", "status"]):
            try:
                info = process.info
                result.append({
                   'Name': info['name'],
                    'PID': info['pid'],
                    'PPID': info['ppid'],
                    'Status': info['status']
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return result


    def start_task_manager(self):
        tm = Toplevel(self.parent)
        tm.geometry("500x500")

        my_frame = Frame(tm)
        my_tree = ttk.Treeview(my_frame)
        my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

        my_scrollbar.pack(expand=True, side=RIGHT, fill=Y)
        my_frame.pack(fill=BOTH, expand=True)
        my_tree.configure(yscrollcommand=my_scrollbar.set)
        my_scrollbar.configure(command=my_tree.yview)

        my_tree['columns'] = ("Name", "PID", "PPID", "Status")
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Name", anchor=W, width=120)
        my_tree.column("PID", anchor=CENTER, width=80)
        my_tree.column("PPID", anchor=W, width=120)
        my_tree.column("Status", anchor=W, width=120)

        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Name", text="Name", anchor=W)
        my_tree.heading("PID", text='PID', anchor=CENTER)
        my_tree.heading("PPID", text="PPID", anchor=W)
        my_tree.heading("Status", text="Status", anchor=W)

        result = self.task_manager()
        for record in result:
            my_tree.insert(parent="", index='end', iid=str(record['PID']), text="", values=(record['Name'], record['PID'], record['PPID'], record['Status']))
        my_tree.pack(fill=BOTH, expand=True)
        tm.after(1000, self.update, tm, my_tree)
        return tm, my_tree
    

    def update(self, tm, my_tree):
        current_pids = self.task_manager()
        existing_pids = my_tree.get_children()

        current_pids_info = {str(item['PID']) for item in current_pids}
        existing_pids_info = set(existing_pids)

        dead_pids = existing_pids_info - current_pids_info

        for pid in dead_pids:
            if my_tree.exists(pid):
                my_tree.delete(pid)
                print(f"Процесс {pid} удален")

        for record in current_pids:
            pids = str(record['PID'])
            values = (record['Name'], record['PID'], record['PPID'], record['Status'])
            if my_tree.exists(pids):
                my_tree.item(pids, values=values)
            else:
                my_tree.insert(parent="", index='end', iid=pids, text="", values=values)
                print(f"Процесс {pids} добавлен")

        tm.after(1000, self.update, tm, my_tree)




if __name__ == "__main__":
    app = MainWindow()
    task_manager = TaskManager(app)
    app.main_window()

