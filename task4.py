import tkinter as tk
from tkinter import ttk

movie_list = [
    {"title": "Leo", "genre": "Action"},
    {"title": "Tik Tik Tik", "genre": "Sci-Fi"},
    {"title": "Love Today", "genre": "Romance"},
    {"title": "Master", "genre": "Action"},
    {"title": "24", "genre": "Sci-Fi"},
    {"title": "Asuran", "genre": "Drama"},
    {"title": "Vikram", "genre": "Action"},
    {"title": "Vinnaithaandi Varuvaayaa", "genre": "Romance"},
    {"title": "Jai Bhim", "genre": "Drama"},
    {"title": "Enthiran", "genre": "Sci-Fi"},
]

book_list = [
    {"title": "Ponniyin Selvan", "genre": "Fiction"},
    {"title": "Hiranyan", "genre": "Fantasy"},
    {"title": "Ennai Aatchidhaan", "genre": "Fiction"},
    {"title": "Mayabogam", "genre": "Fantasy"},
    {"title": "Ungalal Mudiyum", "genre": "Self-Help"},
    {"title": "En Vazhkai", "genre": "Biography"},
    {"title": "Valvil Manithan", "genre": "Self-Help"},
    {"title": "Vikramaditya Kathaigal", "genre": "Fiction"},
    {"title": "C.V.Raman-The Light Warrior", "genre": "Biography"},
    {"title": "Panchatandra Stories", "genre": "Fantasy"},
]

def update_genres(event=None):
    choice = type_choice.get()
    genres = []
    if choice == "Movie":
        for i in movie_list:
            if i["genre"] not in genres:
                genres.append(i["genre"])
    elif choice == "Book":
        for b in book_list:
            if b["genre"] not in genres:
                genres.append(b["genre"])
    genre_box['values'] = genres
    if genres:
        genre_box.set(genres[0])
    else:
        genre_box.set('')

def search_titles():
    selected_type = type_choice.get()
    chosen_genre = genre_choice.get()
    results = []

    if selected_type == "Movie":
        for mv in movie_list:
            if mv["genre"] == chosen_genre:
                results.append(mv["title"])
    elif selected_type == "Book":
        for bk in book_list:
            if bk["genre"] == chosen_genre:
                results.append(bk["title"])

    if results:
        final = "\n".join(results)
        output_lbl.config(text=final)
    else:
        output_lbl.config(text="No matches found.")

win = tk.Tk()
win.title("Explore Books or Movies")
win.geometry("500x430")
win.config(bg="#eaeaea")

tk.Label(win, text="Choose what you want to explore", bg="#eaeaea", font=("Arial", 14)).pack(pady=10)

type_choice = tk.StringVar()
type_box = ttk.Combobox(win, textvariable=type_choice, state="readonly", font=("Arial", 10))
type_box['values'] = ["Book", "Movie"]
type_box.set("Movie")
type_box.pack(pady=5)
type_box.bind("<<ComboboxSelected>>", update_genres)

tk.Label(win, text="Now choose a genre", bg="#eaeaea", font=("Arial", 11)).pack()
genre_choice = tk.StringVar()
genre_box = ttk.Combobox(win, textvariable=genre_choice, state="readonly", font=("Arial", 10))
genre_box.pack(pady=5)
update_genres()
tk.Button(win, text="Show Titles", command=search_titles, bg="#007788", fg="white", font=("Arial", 10)).pack(pady=10)
output_lbl = tk.Label(win, text="", bg="#eaeaea", justify="left", font=("Arial", 10), anchor="w")
output_lbl.pack(padx=20, pady=10, fill='both', expand=True)

win.mainloop()
