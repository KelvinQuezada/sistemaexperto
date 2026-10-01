# ============================================
# INTERFAZ DE USUARIO
# Sistema Experto para Diagnóstico de PC
# ============================================

import tkinter as tk
from tkinter import ttk, messagebox
from motor_inferencia import diagnosticar
from conocimiento import agregar_regla, obtener_reglas

class SistemaExperto:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema Experto - Diagnóstico de Computadoras")
        self.ventana.geometry("850x650")
        self.ventana.resizable(False, False)
        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self.ventana, text="SISTEMA EXPERTO",
                 font=("Arial", 24, "bold")).pack(pady=10)
        tk.Label(self.ventana, text="Diagnóstico de problemas de computadora",
                 font=("Arial", 14)).pack(pady=5)

        ttk.Separator(self.ventana, orient="horizontal").pack(fill="x", padx=20, pady=10)

        frame = tk.LabelFrame(self.ventana, text="Seleccione los síntomas",
                              font=("Arial", 12, "bold"), padx=15, pady=15)
        frame.pack(padx=20, pady=10, fill="x")

        claves = [
            ("no_enciende", "La computadora no enciende"),
            ("se_apaga", "La computadora se apaga repentinamente"),
            ("se_calienta", "La computadora se calienta demasiado"),
            ("lento", "La computadora está lenta"),
            ("ruidos_disco", "El disco produce ruidos extraños"),
            ("programas_se_cierran", "Los programas se cierran solos"),
            ("sin_internet", "No hay conexión a Internet"),
            ("ventanas_extrañas", "Aparecen ventanas extrañas"),
            ("enciende_sin_imagen", "La computadora enciende pero no muestra imagen"),
            ("teclado_no_funciona", "El teclado no funciona"),
            ("sin_audio", "No hay sonido")
        ]

        self.sintomas = {clave: tk.BooleanVar() for clave, _ in claves}

        for i, (clave, texto) in enumerate(claves):
            tk.Checkbutton(frame, text=texto, variable=self.sintomas[clave],
                           font=("Arial", 10), anchor="w").grid(
                row=i // 2, column=i % 2, sticky="w", padx=10, pady=5)

        botones = tk.Frame(self.ventana)
        botones.pack(pady=10)

        tk.Button(botones, text="REALIZAR DIAGNÓSTICO",
                  font=("Arial", 11, "bold"), command=self.realizar_diagnostico,
                  padx=20, pady=10).grid(row=0, column=0, padx=10)

        tk.Button(botones, text="LIMPIAR", font=("Arial", 11),
                  command=self.limpiar, padx=20, pady=10).grid(row=0, column=1, padx=10)

        tk.Button(botones, text="ADQUIRIR CONOCIMIENTO", font=("Arial", 11),
                  command=self.ventana_conocimiento, padx=20, pady=10).grid(row=0, column=2, padx=10)

        resultado_frame = tk.LabelFrame(self.ventana, text="Resultado del diagnóstico",
                                        font=("Arial", 12, "bold"), padx=10, pady=10)
        resultado_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.resultado = tk.Text(resultado_frame, height=12, font=("Arial", 11), wrap="word")
        self.resultado.pack(fill="both", expand=True)

    def realizar_diagnostico(self):
        seleccionados = [nombre for nombre, variable in self.sintomas.items() if variable.get()]

        if not seleccionados:
            messagebox.showwarning("Advertencia", "Seleccione al menos un síntoma.")
            return

        resultados = diagnosticar(seleccionados)
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, "========== DIAGNÓSTICO ==========\n\n")
        self.resultado.insert(tk.END, "Síntomas seleccionados:\n")
        for sintoma in seleccionados:
            self.resultado.insert(tk.END, f"• {sintoma}\n")
        self.resultado.insert(tk.END, "\n=================================\n\n")

        if not resultados:
            self.resultado.insert(tk.END, "No se encontró una regla que coincida con los síntomas ingresados.\n\n")
            self.resultado.insert(tk.END, "Recomendación: consulte con un técnico especializado.")
            return

        for i, r in enumerate(resultados[:3]):
            self.resultado.insert(tk.END, f"DIAGNÓSTICO {i + 1}\n")
            self.resultado.insert(tk.END, f"Problema: {r['nombre']}\n")
            self.resultado.insert(tk.END, f"Coincidencia: {r['porcentaje']:.0f}%\n\n")
            self.resultado.insert(tk.END, f"Descripción:\n{r['diagnostico']}\n\n")
            self.resultado.insert(tk.END, f"Recomendación:\n{r['solucion']}\n\n")
            self.resultado.insert(tk.END, "---------------------------------\n\n")

    def limpiar(self):
        for variable in self.sintomas.values():
            variable.set(False)
        self.resultado.delete("1.0", tk.END)

    def ventana_conocimiento(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Adquisición del conocimiento")
        ventana.geometry("600x550")

        tk.Label(ventana, text="MÓDULO DE ADQUISICIÓN DEL CONOCIMIENTO",
                 font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(ventana, text="Nombre del problema:").pack()
        entrada_nombre = tk.Entry(ventana, width=60)
        entrada_nombre.pack(pady=5)

        tk.Label(ventana, text="Síntomas asociados separados por coma:").pack()
        entrada_sintomas = tk.Entry(ventana, width=60)
        entrada_sintomas.pack(pady=5)
        tk.Label(ventana, text="Ejemplo: lento, se_calienta",
                 font=("Arial", 9)).pack()

        tk.Label(ventana, text="Diagnóstico:").pack(pady=(15, 0))
        entrada_diagnostico = tk.Entry(ventana, width=60)
        entrada_diagnostico.pack(pady=5)

        tk.Label(ventana, text="Solución recomendada:").pack(pady=(15, 0))
        entrada_solucion = tk.Entry(ventana, width=60)
        entrada_solucion.pack(pady=5)

        def guardar_regla():
            nombre = entrada_nombre.get().strip()
            sintomas_texto = entrada_sintomas.get().strip()
            diagnostico = entrada_diagnostico.get().strip()
            solucion = entrada_solucion.get().strip()

            if not nombre or not sintomas_texto or not diagnostico or not solucion:
                messagebox.showwarning("Advertencia", "Complete todos los campos.")
                return

            sintomas = [s.strip() for s in sintomas_texto.split(",")]
            agregar_regla(nombre, sintomas, diagnostico, solucion)
            messagebox.showinfo("Correcto", "La nueva regla fue agregada correctamente.")

            for entrada in (entrada_nombre, entrada_sintomas, entrada_diagnostico, entrada_solucion):
                entrada.delete(0, tk.END)

            lista.delete(0, tk.END)
            for regla in obtener_reglas():
                lista.insert(tk.END, regla["nombre"])

        tk.Button(ventana, text="AGREGAR REGLA", command=guardar_regla,
                  font=("Arial", 11, "bold"), padx=20, pady=10).pack(pady=20)

        tk.Label(ventana, text="Reglas almacenadas:",
                 font=("Arial", 11, "bold")).pack()

        lista = tk.Listbox(ventana, width=70, height=10)
        lista.pack(padx=10, pady=10)

        for regla in obtener_reglas():
            lista.insert(tk.END, regla["nombre"])
