# Sistema Experto para Diagnóstico de Computadoras

Proyecto desarrollado en Python utilizando Tkinter.

## Módulos

- `conocimiento.py`: base de conocimientos y adquisición de nuevas reglas.
- `motor_inferencia.py`: motor que compara síntomas con las reglas.
- `interfaz.py`: interfaz gráfica del usuario.
- `main.py`: archivo principal.

## Requisitos

Python 3.10 o superior.

Tkinter normalmente viene incluido con Python para Windows.

## Ejecución

Abrir PowerShell dentro de esta carpeta y ejecutar:

```powershell
python main.py
```

También puede ejecutarse con:

```powershell
py main.py
```

## Funciones

- Seleccionar síntomas de una computadora.
- Ejecutar un diagnóstico.
- Mostrar porcentaje de coincidencia.
- Mostrar recomendaciones.
- Agregar nuevas reglas mediante el módulo de adquisición del conocimiento.

Las reglas nuevas se mantienen mientras el programa está abierto. Esta versión no utiliza una base de datos.
