# import modul tkinter untuk GUI
import tkinter as tk
# membuat window utama,judul, dan deskripsi
app = tk.Tk()
app.title("Menghitung Luas Jajargenjang")
judul = tk.Label(app, text="Bangun Geometri", font=("Comic Sans MS", 18, "bold"))
judul.pack(pady=10)
desk = tk.Label(
    app,
    text="Menghitung luas jajargenjang\nParameter: Alas dan Tinggi"
)
desk.pack(pady=5)

# fungsi menghitung luas
def hitung_luas():
    a = float(entry_alas.get())       # ambil nilai alas dari entry
    t = float(entry_tinggi.get())     # ambil nilai tinggi dari entry
    luas = a * t                      # rumus luas jajargenjang
    label_hasil.config(text=f"Luas = {luas:.0f}")  # tampilkan hasil
# frame parameter
frame = tk.Frame(app)
frame.pack(pady=10)
# label dan entry parameter alas dan tinggi
tk.Label(frame, text="Alas").grid(row=0, column=0, padx=10, pady=5)
entry_alas = tk.Entry(frame)
entry_alas.grid(row=0, column=1, padx=10, pady=5)
tk.Label(frame, text="Tinggi").grid(row=1, column=0, padx=10, pady=5)
entry_tinggi = tk.Entry(frame)
entry_tinggi.grid(row=1, column=1, padx=10, pady=5)

# tombol "Hitung Luas"
btn = tk.Button(app, text="Hitung Luas", command=hitung_luas, width=15, bg="#87CEFA")
btn.pack(pady=10)
# label hasil
label_hasil = tk.Label(app, text="Luas = ", font=("Comic Sans MS", 14))
label_hasil.pack(pady=10)

# menjalankan aplikasi
app.mainloop()