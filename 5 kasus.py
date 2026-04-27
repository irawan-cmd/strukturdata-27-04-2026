# pyhthon 5 kasus queue visualizer dashboard(pyhton)
import customtkinter as ctk
from collections import deque

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Queue Visualizer Modern UI")
app.geometry("1000x600")

# ======================
# SIDEBAR
# ======================

frame_sidebar = ctk.CTkFrame(app, width=200)
frame_sidebar.pack(side="left", fill="y")

frame_main = ctk.CTkFrame(app)
frame_main.pack(side="right", expand=True, fill="both")

title = ctk.CTkLabel(frame_sidebar, text="Queue Menu", font=("Arial", 18))
title.pack(pady=20)

# ======================
# GLOBAL STATE
# ======================

printer_q = deque()
hotpotato_q = deque()
hospital_q = []
airport_q = deque()

# ======================
# CLEAR FRAME
# ======================

def clear_frame():
    for widget in frame_main.winfo_children():
        widget.destroy()

# ======================
# 1 PRINTER
# ======================

def show_printer():
    clear_frame()

    ctk.CTkLabel(frame_main, text="Printer Queue", font=("Arial",20)).pack(pady=10)

    entry = ctk.CTkEntry(frame_main)
    entry.pack()

    listbox = ctk.CTkTextbox(frame_main, height=200)
    listbox.pack(pady=10)

    def update():
        listbox.delete("0.0", "end")
        for i in printer_q:
            listbox.insert("end", i+"\n")

    def enqueue():
        if entry.get():
            printer_q.append(entry.get())
            entry.delete(0,"end")
            update()

    def dequeue():
        if printer_q:
            printer_q.popleft()
            update()

    ctk.CTkButton(frame_main, text="Enqueue", command=enqueue).pack(pady=5)
    ctk.CTkButton(frame_main, text="Print", command=dequeue).pack(pady=5)

# ======================
# 2 HOT POTATO
# ======================

def show_hotpotato():
    clear_frame()

    ctk.CTkLabel(frame_main, text="Hot Potato", font=("Arial",20)).pack(pady=10)

    entry = ctk.CTkEntry(frame_main)
    entry.pack()

    listbox = ctk.CTkTextbox(frame_main, height=200)
    listbox.pack(pady=10)

    def update():
        listbox.delete("0.0", "end")
        for p in hotpotato_q:
            listbox.insert("end", p+"\n")

    def add():
        if entry.get():
            hotpotato_q.append(entry.get())
            entry.delete(0,"end")
            update()

    def rotate():
        if len(hotpotato_q)>1:
            hotpotato_q.rotate(-1)
            update()

    def eliminate():
        if hotpotato_q:
            hotpotato_q.popleft()
            update()

    ctk.CTkButton(frame_main, text="Tambah", command=add).pack(pady=5)
    ctk.CTkButton(frame_main, text="Oper", command=rotate).pack(pady=5)
    ctk.CTkButton(frame_main, text="Eliminasi", command=eliminate).pack(pady=5)

# ======================
# 3 RUMAH SAKIT
# ======================

def show_hospital():
    clear_frame()

    ctk.CTkLabel(frame_main, text="Rumah Sakit (Priority)", font=("Arial",20)).pack(pady=10)

    entry = ctk.CTkEntry(frame_main)
    entry.pack()

    priority = ctk.CTkOptionMenu(frame_main, values=["1","2","3"])
    priority.pack()

    listbox = ctk.CTkTextbox(frame_main, height=200)
    listbox.pack(pady=10)

    def update():
        listbox.delete("0.0", "end")
        for p,n in hospital_q:
            listbox.insert("end", f"{n} (P{p})\n")

    def add():
        if entry.get():
            hospital_q.append((int(priority.get()), entry.get()))
            hospital_q.sort()
            entry.delete(0,"end")
            update()

    def call():
        if hospital_q:
            hospital_q.pop(0)
            update()

    ctk.CTkButton(frame_main, text="Tambah Pasien", command=add).pack(pady=5)
    ctk.CTkButton(frame_main, text="Panggil", command=call).pack(pady=5)

# ======================
# 4 BFS
# ======================

def show_bfs():
    clear_frame()

    ctk.CTkLabel(frame_main, text="BFS Traversal", font=("Arial",20)).pack(pady=10)

    output = ctk.CTkTextbox(frame_main, height=200)
    output.pack(pady=10)

    graph = {
        "A":["B","C"],
        "B":["D","E"],
        "C":["F"],
        "D":[],
        "E":[],
        "F":[]
    }

    def run():
        visited=[]
        q=deque(["A"])

        while q:
            node=q.popleft()
            if node not in visited:
                visited.append(node)
                for n in graph[node]:
                    q.append(n)

        output.delete("0.0","end")
        for v in visited:
            output.insert("end", v+" -> ")

    ctk.CTkButton(frame_main, text="Run BFS", command=run).pack(pady=5)

# ======================
# 5 BANDARA
# ======================

def show_airport():
    clear_frame()

    ctk.CTkLabel(frame_main, text="Bandara Queue", font=("Arial",20)).pack(pady=10)

    entry = ctk.CTkEntry(frame_main)
    entry.pack()

    listbox = ctk.CTkTextbox(frame_main, height=200)
    listbox.pack(pady=10)

    def update():
        listbox.delete("0.0", "end")
        for p in airport_q:
            listbox.insert("end", p+"\n")

    def add():
        if entry.get():
            airport_q.append(entry.get())
            entry.delete(0,"end")
            update()

    def serve():
        if airport_q:
            airport_q.popleft()
            update()

    ctk.CTkButton(frame_main, text="Tambah", command=add).pack(pady=5)
    ctk.CTkButton(frame_main, text="Layani", command=serve).pack(pady=5)

# ======================
# MENU BUTTON
# ======================

ctk.CTkButton(frame_sidebar, text="Printer", command=show_printer).pack(pady=10)
ctk.CTkButton(frame_sidebar, text="Hot Potato", command=show_hotpotato).pack(pady=10)
ctk.CTkButton(frame_sidebar, text="Rumah Sakit", command=show_hospital).pack(pady=10)
ctk.CTkButton(frame_sidebar, text="BFS", command=show_bfs).pack(pady=10)
ctk.CTkButton(frame_sidebar, text="Bandara", command=show_airport).pack(pady=10)

# default
show_printer()

app.mainloop()
