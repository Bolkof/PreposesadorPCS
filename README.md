# archivo ASCII_color
Darle color a las palabras en la terminal con escapes ascii

## descargar repositorii

Puedes utilizar el comando `git clone` en Linux y git bash para descargar este repositorio de GitHub.

```bash
https://github.com/Bolkof/ASCIIcolor/tree/main
```

## que es esta carpeta

El código proporcionado parece estar relacionado con la manipulación de colores de texto en la terminal utilizando códigos de escape ANSI. Aquí tienes algunas variables adicionales que podrían ser útiles:

Estos códigos de color te permitirán cambiar el color del texto en la terminal a rojo, verde y azul respectivamente. Puedes agregar más colores siguiendo el mismo patrón, cambiando el número de código ANSI para el color deseado. Recuerda también tener una variable `reset_color` como la que ya proporcionaste para restaurar el color original del texto cuando sea necesario.

## contenido del archivo

Secuencias de escape ANSI para cambiar el color del texto, guardado en variables

```
rojo = "\033[91m"
cyan = "\033[96m"
magenta = "\033[95m"
blanco = "\033[97m"
verde = "\033[92m"
azul = "\033[94m"
amarillo = "\033[93m"
negro = "\033[90m"

reset_color = "\033[0m"
subrayado = "\033[4m"
parpadeante = "\033[5m"
invertido = "\033[7m"
tachado = "\033[9m"

amarillo_brillante = "\033[93;1m"
rojo_brillante = "\033[91;1m"
verde_brillante = "\033[92;1m"
azul_brillante = "\033[94;1m"
magenta_brillante = "\033[95;1m"
cyan_brillante = "\033[96;1m"
blanco_brillante = "\033[97;1m"
```




## ejemplo de codigo
Claro, aquí te proporcionaré ejemplos de cómo imprimir texto en los lenguajes Lua, Dart y JavaScript utilizando las variables de formato de color definidas en tu código:

Lua:
```lua
print(rojo .. "Este es un texto rojo en Lua" .. reset_color)
```

Python:
```
print(f"{rojo}{subrayado}Este texto es rojo y subrayado{reset_color}")
```

Dart (asumiendo que estás en un entorno que admite códigos ANSI para colores en la consola, de lo contrario, esto podría no funcionar):
```dart
print("$rojoEste es un texto rojo en Dart$reset_color");
```

JavaScript (en un entorno de consola que admite códigos ANSI para colores, como Node.js):
```javascript
console.log(`${rojo}Este es un texto rojo en JavaScript${reset_color}`);
```

Ten en cuenta que la capacidad de mostrar colores en la consola puede variar según el entorno y la configuración específicos, por lo que es posible que debas ajustar el código según tu situación.

## importar
Claro, aquí tienes ejemplos de cómo importar el archivo "colores_ascii" desde la carpeta "funciones" en diferentes lenguajes de programación: Lua, Dart, Python y JavaScript.

Lua:
```lua
dofile("funciones/colores_ascii.lua")

-- Ahora puedes usar las variables definidas en colores_ascii
print(rojo .. "Este texto es rojo" .. reset_color)
```

Dart:
```dart
import 'funciones/colores_ascii.dart';

// Ahora puedes usar las variables definidas en colores_ascii
print(rojo + "Este texto es rojo" + reset_color);
```

Python:
```python
from funciones.colores_ascii import *

# Ahora puedes usar las variables definidas en colores_ascii
print(rojo + "Este texto es rojo" + reset_color)
```

JavaScript (Node.js):
```javascript
const { rojo, reset_color } = require('./funciones/colores_ascii');

// Ahora puedes usar las variables definidas en colores_ascii
console.log(rojo + "Este texto es rojo" + reset_color);
```

Asegúrate de que el archivo "colores_ascii" esté ubicado en la carpeta "funciones" del directorio actual en cada uno de estos lenguajes para que las importaciones funcionen correctamente.
