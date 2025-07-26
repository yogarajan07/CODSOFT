import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime
import json
import threading
import random
import requests


TASK_FILE = "tasks.json"

quotes = [
    "The future depends on what you do today. – Mahatma Gandhi",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Don’t wait for opportunity. Create it."
]


def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add new task
def add_task():
    task = simpledialog.askstring("New Task", "Enter your task:")
    if task:
        tasks.append({"task": task})
        save_tasks(tasks)
        messagebox.showinfo("Task Added", f"'{task}' added to your list.")

# Show all tasks
def show_tasks():
    if not tasks:
        messagebox.showinfo("Tasks", "No tasks added.")
    else:
        task_text = "\n".join([f"- {t['task']}" for t in tasks])
        messagebox.showinfo("Your Tasks", task_text)

# Show motivational quote
def show_quote():
    quote = random.choice(quotes)
    display_message(f"{quote}")


# You can replace this with a real API call
def show_weather():
    from tkinter import simpledialog
    city = simpledialog.askstring("Weather", "Enter your city name:")
    if not city:
        return

    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            display_message(f"🌦 {response.text}")
        else:
            display_message("Could not retrieve weather.")
    except Exception as e:
        display_message("❌ Network error.")
# Chatbot response logic
def handle_input():
    user_input = input_box.get()
    chat_log.insert(tk.END, f"You: {user_input}")

    user_input = user_input.lower()

    if "add task" in user_input or "reminder" in user_input:
        add_task()
    elif "show task" in user_input:
        show_tasks()
    elif "motivate" in user_input or "quote" in user_input:
        show_quote()
    elif "weather" in user_input:
        show_weather()
    elif "hello" in user_input or "hi" in user_input:
        display_message("Hello! How can I help you today?")
    elif "time" in user_input:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        display_message(f"rrent time is {now}")
    elif "date" in user_input:
        today = datetime.date.today().strftime("%B %d, %Y")
        display_message(f"day is {today}")
    elif "bye" in user_input:
        display_message("Goodbye! Have a great day")
    else:
        display_message("I didn't understand that. Try asking about weather, tasks, or quotes.")

    input_box.delete(0, tk.END)

# Helper to display message
def display_message(msg):
    chat_log.insert(tk.END, f"Bot: {msg}")

# GUI Setup
root = tk.Tk()
root.title("Day-to-Day Life Assistant")
root.geometry("500x500")
root.config(bg="#f0f0f0")

chat_log = tk.Listbox(root, width=70, height=20, bg="white", font=("Arial", 10))
chat_log.pack(pady=10)

input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=5)

input_box = tk.Entry(input_frame, width=40, font=("Arial", 12))
input_box.pack(side=tk.LEFT, padx=5)

send_btn = tk.Button(input_frame, text="Send", command=handle_input, bg="#4caf50", fg="white")
send_btn.pack(side=tk.LEFT)

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Task", command=add_task, width=15).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Show Tasks", command=show_tasks, width=15).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Motivate Me", command=show_quote, width=15).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Weather", command=show_weather, width=15).grid(row=1, column=1, pady=5)

tasks = load_tasks()
root.mainloop()
