import streamlit as st
import sqlite3

# Funktion zum Anzeigen des Kalenders mit der To-Do-Liste
def show_calendar_with_todo(year, month):
    # Verbindung zur SQLite-Datenbank herstellen oder eine erstellen
    conn = sqlite3.connect('calendar_todo.db')
    c = conn.cursor()

    # Tabelle für Aufgaben erstellen, falls sie noch nicht existiert
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (date TEXT, task TEXT, priority INTEGER)''')

    # Erstelle einen Kalender für das gegebene Jahr und Monat
    cal_content = calendar.month(year, month)

    # Zeige den Kalenderinhalt an
    st.markdown(cal_content)

    # Anzeige der To-Do-Liste
    st.subheader("To-Do-Liste")

    # Eingabefelder für Aufgaben
    task = st.text_input("Aufgabe", "")
    priority = st.selectbox("Priorität", ["Niedrig", "Mittel", "Hoch"])

    # Schaltfläche zum Hinzufügen einer Aufgabe
    if st.button("Aufgabe hinzufügen"):
        date = f"{year}-{month:02d}-{st.date_input('Datum', min_value=1, max_value=31)}"
        priority_map = {"Niedrig": 1, "Mittel": 2, "Hoch": 3}
        c.execute("INSERT INTO tasks (date, task, priority) VALUES (?, ?, ?)", (date, task, priority_map[priority]))
        conn.commit()

        # Aktualisiere die To-Do-Liste
        update_todo_list(c, year, month)

# Funktion zum Aktualisieren der To-Do-Liste
def update_todo_list(c, year, month):
    selected_date = st.date_input('Datum auswählen', min_value=1, max_value=31, value=1)
    st.write("Aufgaben für ausgewähltes Datum:")

    # Abrufen und Anzeigen der Aufgaben für das ausgewählte Datum
    tasks = c.execute("SELECT * FROM tasks WHERE date=?", (f"{year}-{month:02d}-{selected_date:02d}",))
    for row in tasks:
        st.write(f"- {row[1]} (Priorität: {row[2]})")

# Hauptfunktion der Streamlit-App
def main():
    # Verbindung zur SQLite-Datenbank herstellen oder eine erstellen
    conn = sqlite3.connect('calendar_todo.db')
    c = conn.cursor()

    # Seitentitel und Beschreibung
    st.title("Kalender mit To-Do-Liste")
    st.write("Fügen Sie Aufgaben hinzu und sehen Sie sie im Kalender.")

    # Jahr und Monat auswählen
    year = st.number_input("Jahr", min_value=1900, max_value=2100, value=2024)
    month = st.number_input("Monat", min_value=1, max_value=12, value=4)

    # Anzeigen des Kalenders und der To-Do-Liste
    show_calendar_with_todo(year, month)

if __name__ == "__main__":
    main()
