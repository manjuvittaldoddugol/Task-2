import tkinter as tk
import random

# -----------------------------
# RANDOM QUOTE GENERATOR
# CodeAlpha - Task 2
# -----------------------------

quotes = [
    ("The best way to predict the future is to create it.", "Peter Drucker"),
    ("Success is not final, failure is not fatal.", "Winston Churchill"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("Great things are done by a series of small things.", "Vincent van Gogh"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("Success comes from hard work and dedication.", "Unknown"),
    ("Learning never exhausts the mind.", "Leonardo da Vinci")
]

# Create window
root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("400x500")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="Random Quote Generator",
    font=("Arial", 20, "bold")
)
title.pack(pady=30)

# Quote display
quote_label = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    wraplength=330,
    justify="center"
)
quote_label.pack(pady=50)

# Author display
author_label = tk.Label(
    root,
    text="",
    font=("Arial", 13, "italic")
)
author_label.pack(pady=10)


# Function to generate quote
def new_quote():
    quote, author = random.choice(quotes)

    quote_label.config(
        text='"' + quote + '"'
    )

    author_label.config(
        text="- " + author
    )


# New Quote button
new_button = tk.Button(
    root,
    text="New Quote",
    command=new_quote,
    font=("Arial", 14, "bold"),
    padx=30,
    pady=10
)
new_button.pack(pady=40)


# Show quote when app opens
new_quote()

# Run application
root.mainloop()