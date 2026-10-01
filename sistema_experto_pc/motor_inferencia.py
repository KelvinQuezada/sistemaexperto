# ============================================
# MOTOR DE INFERENCIA
# ============================================

from conocimiento import obtener_reglas

def diagnosticar(sintomas_usuario):
    reglas = obtener_reglas()
    resultados = []

    for regla in reglas:
        sintomas_regla = set(regla["sintomas"])
        sintomas_usuario_set = set(sintomas_usuario)
        coincidencias = sintomas_regla.intersection(sintomas_usuario_set)

        if len(coincidencias) > 0:
            porcentaje = (len(coincidencias) / len(sintomas_regla)) * 100
            resultados.append({
                "nombre": regla["nombre"],
                "diagnostico": regla["diagnostico"],
                "solucion": regla["solucion"],
                "coincidencias": len(coincidencias),
                "porcentaje": porcentaje
            })

    resultados.sort(key=lambda x: x["porcentaje"], reverse=True)
    return resultados
