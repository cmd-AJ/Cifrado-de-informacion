Repositorio: https://github.com/cmd-AJ/Cifrado-de-informacion.git


## Descripción

Este proyecto contiene un conjunto de implementaciones en Python orientadas al estudio de conceptos básicos de criptografía y representación de la información. El código se encuentra desarrollado en un archivo Jupyter Notebook (`main.ipynb`) y tiene fines educativos.

Se abordan los siguientes temas:

Parte 1
- Cifrado César

Parte 2
- Conversión de texto ASCII a binario
- Codificación Base64
- Relación entre codificación y representación binaria

---

## Contenido del Proyecto

### 1. Diccionario ASCII

Se define un diccionario que asocia cada letra minúscula del alfabeto con su valor ASCII correspondiente.

**Propósito**
- Mostrar explícitamente la relación entre caracteres y valores ASCII
- Facilitar la comprensión del cifrado a bajo nivel

---

### 2. Cifrado César

El cifrado César es un cifrado por sustitución simple que desplaza cada letra del texto un número fijo de posiciones dentro del alfabeto.

#### Función principal
```python
cifrado_cesar(texto, desplazamiento)
```

#### Funcionamiento
- Recorre cada carácter del texto
- Convierte letras minúsculas a su valor ASCII
- Aplica el desplazamiento usando aritmética modular (mod 26)
- Convierte nuevamente el valor numérico a carácter
- Mantiene sin cambios los caracteres que no son letras

#### Ejemplo
```python
mensaje = "hola mundo"
print(cifrado_cesar(mensaje, 3))
```

---

### 3. Conversión de Texto ASCII a Binario

Se convierte un texto a una lista de valores ASCII y posteriormente a su representación binaria.

#### Pasos
1. El texto se convierte en una lista de caracteres
2. Cada carácter se transforma en su valor ASCII usando `ord()`
3. Cada valor decimal se convierte a binario mediante una función personalizada

#### Función
```python
decimal_a_binario(n)
```

Esta función:
- Divide sucesivamente el número entre 2
- Construye el número binario a partir de los residuos
- Devuelve la representación binaria como una cadena

---

### 4. Codificación Base64

Se realiza la codificación de un texto en formato Base64 utilizando la librería estándar de Python.

#### Proceso
- El texto se codifica a bytes
- Se transforma a Base64
- Cada carácter del resultado Base64 se convierte a su valor ASCII
- Dichos valores se representan en binario utilizando la función anterior

#### Ejemplo
```python
text = "krnwenwrmxbjlroamxb"
text_in_base64 = base64.b64encode(text.encode()).decode()
```

---

## Requisitos

- Python 3.x
- Jupyter Notebook
- Librería estándar `base64`

---

## Objetivo Académico

Este proyecto tiene como finalidad:
- Comprender el funcionamiento del cifrado César
- Analizar la relación entre texto, ASCII y binario
- Introducir el concepto de codificación Base64
- Reforzar el uso de funciones y estructuras básicas en Python

---

## Licencia

Este proyecto se proporciona con fines educativos.
Su uso es libre para estudio y aprendizaje.
