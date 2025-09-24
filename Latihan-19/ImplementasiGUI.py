import tkinter as tk
import requests
from threading import Thread


def fetch_random_quote(label, root):
    def worker():
        try:
            r = requests.get("https://api.quotable.io/random", timeout=6)
            r.raise_for_status()
            d = r.json()
            text = f'"{d["content"]}"\n— {d.get("author", "Unknown")}'
        except Exception:
            text = "Gagal mengambil quote."
        # update GUI di main thread:
        root.after(0, lambda: label.config(text=text))

    Thread(target=worker, daemon=True).start()


root = tk.Tk()
root.title("Quote Fetcher")
lbl = tk.Label(
    root, text="Tekan tombol untuk mendapat quote", wraplength=400, justify="left"
)
lbl.pack(padx=10, pady=10)
btn = tk.Button(root, text="Ambil Quote", command=lambda: fetch_random_quote(lbl, root))
btn.pack(pady=5)
root.mainloop()
