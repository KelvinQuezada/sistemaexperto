# ============================================
# ARCHIVO PRINCIPAL
# ============================================

import tkinter as tk
from interfaz import SistemaExperto

def main():
    ventana = tk.Tk()
    app = SistemaExperto(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()
