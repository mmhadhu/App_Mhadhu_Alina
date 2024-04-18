import calendar
import tkinter as tk
import sqlite3

def show_calendar_with_todo(year, month):
    # Verbindung zur SQLite-Datenbank herstellen oder eine erstellen
    conn = sqlite3.connect('calendar_todo.db')
    c = conn.cursor()

    # Tabelle für Aufgaben erstellen, falls sie noch nicht existiert
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (date TEXT, task TEXT, priority INTEGER)''')

    # Erstelle ein neues Fenster mit Tkinter
    root = tk.Tk()
    root.title("Kalender mit To-Do-Liste")

    # Erstelle einen Kalender für das gegebene Jahr und Monat
    cal_content = calendar.month(year, month)

    # Füge den Kalenderinhalt zu einem Label hinzu
    cal_label = tk.Label(root, text=cal_content, font=("Helvetica", 14))
    cal_label.pack()

    # Anzeige der To-Do-Liste
    todo_label = tk.Label(root, text="To-Do-Liste", font=("Helvetica", 12, "bold"))
    todo_label.pack()

    # Funktion zum Hinzufügen einer Aufgabe zur Datenbank
    def add_task():
        date = f"{year}-{month:02d}-{int(day_var.get()):02d}"
        task = task_entry.get()
        priority = priority_var.get()
        c.execute("INSERT INTO tasks (date, task, priority) VALUES (?, ?, ?)", (date, task, priority))
        conn.commit()
        update_todo_list()

    # Funktion zum Aktualisieren der To-Do-Liste
    def update_todo_list():
        todo_list.delete(0, tk.END)
        for row in c.execute("SELECT * FROM tasks WHERE date=?", (f"{year}-{month:02d}-{int(day_var.get()):02d}",)):
            todo_list.insert(tk.END, f"{row[1]} (Priorität: {row[2]})")

    # Eingabefelder für Aufgaben
    task_entry = tk.Entry(root, width=30)
    task_entry.pack()
    priority_var = tk.IntVar()
    priority_entry = tk.Radiobutton(root, text="Niedrig", variable=priority_var, value=1)
    priority_entry.pack()
    priority_entry = tk.Radiobutton(root, text="Mittel", variable=priority_var, value=2)
    priority_entry.pack()
    priority_entry = tk.Radiobutton(root, text="Hoch", variable=priority_var, value=3)
    priority_entry.pack()

    # Funktion zum Abrufen von Aufgaben für ausgewähltes Datum
    def get_tasks():
        update_todo_list()

    # Liste für To-Do-Liste
    todo_list = tk.Listbox(root, width=50)
    todo_list.pack()

    # Schaltfläche zum Hinzufügen einer Aufgabe
    add_button = tk.Button(root, text="Aufgabe hinzufügen", command=add_task)
    add_button.pack()

    # Starte die Tkinter Hauptloop
    root.mainloop()

# Beispielaufruf der Funktion
show_calendar_with_todo(2024, 4)  # Zeigt den Kalender für April 2024 an
