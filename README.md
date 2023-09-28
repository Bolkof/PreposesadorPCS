# Observador de Cambios y Compilación

Este programa en Python te permite observar cambios en archivos Pug, Stylus y CoffeeScript en directorios de origen específicos y realizar la compilación correspondiente en directorios de destino. Es útil para automatizar el proceso de desarrollo web cuando trabajas con estos lenguajes y deseas compilarlos automáticamente al realizar modificaciones en tus archivos fuente.

## Requisitos

Asegúrate de tener los siguientes requisitos previos instalados en tu entorno de desarrollo:

- **Python**: Este programa está escrito en Python, por lo que necesitas tener Python 3.10 instalado en tu sistema. 

**Node.js**: Para la compilación de archivos Stylus y CoffeeScript, se utiliza Node.js como plataforma. Puedes descargar Node.js. 
> apt-get install node.js
  
**Pug (Jade)**: Pug es un motor de plantillas para HTML. Puedes instalar la CLI de Pug utilizando el siguiente comando npm:

> sudo apt-get install pug-cli

**Stylus**: Stylus es un preprocesador de CSS. Puedes instalar la CLI de Stylus con el siguiente comando npm:

> sudo apt-get install stylus

**CoffeeScript**: CoffeeScript es un lenguaje que se compila a JavaScript. Puedes instalar la CLI de CoffeeScript utilizando el siguiente comando npm:

>  npm install -g coffee-script

Asegúrate de que todas las dependencias estén correctamente instaladas en tu sistema antes de ejecutar el programa.

## Uso

1. Clona o descarga este repositorio en tu máquina local.

2. Personaliza los directorios de origen y destino:

   Abre el archivo `observador_compilacion.py` y ajusta las siguientes variables para reflejar los directorios donde se encuentran tus archivos fuente y dónde deseas que se generen los archivos compilados:

   ```python
   # Directorios de archivos de origen
   directorio_pug_origen = './src_pug'
   directorio_stylus_origen = './src_stylus'
   directorio_coffeescript_origen = './src_coffeescript'

   # Directorios de archivos de destino
   directorio_html_destino = './build_html'
   directorio_css_destino = './build_css'
   directorio_js_destino = './build_js'
   ```

3. Ejecuta el programa:

   Abre tu terminal, navega al directorio donde se encuentra el archivo `observador_compilacion.py` y ejecuta el siguiente comando:

   ```shell
   python supervisor.py
   ```

   El programa comenzará a observar los cambios en los archivos Pug, Stylus y CoffeeScript en los directorios de origen especificados y realizará las compilaciones correspondientes en los directorios de destino cuando se detecten modificaciones.

4. Para detener el programa, simplemente presiona Ctrl+C en la terminal.

## Personalización

Si deseas agregar o eliminar tipos de archivo o realizar otras personalizaciones, puedes editar el código Python según tus necesidades. Asegúrate de tener las herramientas de compilación adecuadas instaladas en tu sistema para los lenguajes que estás utilizando (Pug, Stylus, CoffeeScript).

## Contribución

Si deseas contribuir a este proyecto o informar sobre problemas, siéntete libre de crear un issue o enviar una solicitud de extracción.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.
