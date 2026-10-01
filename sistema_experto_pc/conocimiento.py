# ============================================
# BASE DE CONOCIMIENTOS
# Sistema Experto para Diagnóstico de PC
# ============================================

reglas = [
    {
        "nombre": "Problema de alimentación",
        "sintomas": ["no_enciende"],
        "diagnostico": "La computadora presenta un posible problema de alimentación.",
        "solucion": "Verifique que el cable de alimentación esté correctamente conectado. Pruebe otro tomacorriente y revise la fuente de poder."
    },
    {
        "nombre": "Sobrecalentamiento",
        "sintomas": ["se_apaga", "se_calienta"],
        "diagnostico": "La computadora puede estar presentando sobrecalentamiento.",
        "solucion": "Limpie los ventiladores, retire el polvo y revise que el sistema de refrigeración funcione correctamente."
    },
    {
        "nombre": "Problema de almacenamiento",
        "sintomas": ["lento", "ruidos_disco"],
        "diagnostico": "Puede existir un problema con el disco duro.",
        "solucion": "Realice una copia de seguridad de sus archivos y revise el estado del disco duro o SSD."
    },
    {
        "nombre": "Falta de memoria RAM",
        "sintomas": ["lento", "programas_se_cierran"],
        "diagnostico": "La computadora puede tener poca memoria RAM disponible.",
        "solucion": "Cierre programas innecesarios, revise el consumo de memoria y considere ampliar la memoria RAM."
    },
    {
        "nombre": "Problema de conexión a Internet",
        "sintomas": ["sin_internet"],
        "diagnostico": "Existe un posible problema de conexión a Internet.",
        "solucion": "Verifique el cable de red o la conexión Wi-Fi. Reinicie el router y compruebe la configuración de red."
    },
    {
        "nombre": "Problema de malware",
        "sintomas": ["lento", "ventanas_extrañas"],
        "diagnostico": "La computadora podría estar afectada por software malicioso.",
        "solucion": "Realice un análisis completo con un antivirus actualizado y elimine programas sospechosos."
    },
    {
        "nombre": "Problema de pantalla",
        "sintomas": ["enciende_sin_imagen"],
        "diagnostico": "La computadora enciende pero no muestra imagen.",
        "solucion": "Verifique el cable HDMI/DisplayPort, pruebe otro monitor y revise la tarjeta gráfica o memoria RAM."
    },
    {
        "nombre": "Problema de teclado",
        "sintomas": ["teclado_no_funciona"],
        "diagnostico": "El teclado puede presentar un problema de conexión o hardware.",
        "solucion": "Desconecte y vuelva a conectar el teclado. Pruebe otro puerto USB o utilice otro teclado."
    },
    {
        "nombre": "Problema de audio",
        "sintomas": ["sin_audio"],
        "diagnostico": "Existe un posible problema con el sistema de audio.",
        "solucion": "Compruebe el volumen, los dispositivos de salida y los controladores de sonido."
    }
]

def agregar_regla(nombre, sintomas, diagnostico, solucion):
    nueva_regla = {
        "nombre": nombre,
        "sintomas": sintomas,
        "diagnostico": diagnostico,
        "solucion": solucion
    }
    reglas.append(nueva_regla)
    return nueva_regla

def obtener_reglas():
    return reglas
