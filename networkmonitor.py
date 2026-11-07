from window import MainWindow
import psutil
from tkinter import ttk
from tkinter import *

class NetworkMonitor:
    def __init__(self, window):
        self.parent = window

    def format_address(self, address):
        if address:
            return f"{address.ip}:{address.port}"
        return "N/A"
    def network_monitor(self):
        result = []
        for process in psutil.process_iter(["name", "pid", "status"]):
            try:
                connections = process.net_connections()
                info = process.info
                if connections:
                    for idx, conn in enumerate(connections):
                        result.append({
                            "Name":info['name'],
                            "PID":info['pid'],
                            "Status":info['status'],
                            "Laddr":self.format_address(conn.laddr),
                            "Raddr":self.format_address(conn.raddr),
                            "Index": idx
                        })
                        
                else:
                    result.append({
                        "Name":info['name'],
                        "PID":info['pid'],
                        "Status":info['status'],
                        "Laddr":"N/A",
                        "Raddr": "N/A",
                        "Index": 0
                    })   
            except (psutil.ZombieProcess, psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return result



    def start_network_monitor(self):
        nm = Toplevel(self.parent)
        nm.geometry("500x500")

        my_frame = Frame(nm)
        my_tree = ttk.Treeview(my_frame)
        my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

        my_scrollbar.pack(expand=True, side=RIGHT, fill=Y)
        my_frame.pack(fill=BOTH, expand=True)
        my_tree.configure(yscrollcommand=my_scrollbar.set)
        my_scrollbar.configure(command=my_tree.yview)

        my_tree['columns'] = ("Name", "PID", "Status", "Laddr", "Raddr")
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Name", anchor=W, width=120)
        my_tree.column("PID", anchor=CENTER, width=80)
        my_tree.column("Status", anchor=W, width=120)
        my_tree.column("Laddr", anchor=W, width=120)
        my_tree.column("Raddr", anchor=W, width=120)

        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Name", text="Name", anchor=W)
        my_tree.heading("PID", text='PID', anchor=CENTER)
        my_tree.heading("Status", text="Status", anchor=W)
        my_tree.heading("Laddr", text="Local Address", anchor=W)
        my_tree.heading("Raddr", text="Remote Address", anchor=W)
        result = self.network_monitor()
        for record in result:
            uniq_id = f"{record['PID']}_{record['Index']}"
            my_tree.insert(parent="", index='end', iid=uniq_id, text="", values=(record['Name'], record['PID'], record['Status'], record['Laddr'], record['Raddr'] ))
        my_tree.pack(fill=BOTH, expand=True)

        return nm, my_tree



if __name__ == "__main__":
    app = MainWindow()
    net_monitor = NetworkMonitor(app)
    app.main_window()
