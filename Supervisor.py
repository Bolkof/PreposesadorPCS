import subprocess
import os

# Directorios de archivos de origen
directorio_pug_origen = './src_pug'
directorio_stylus_origen = './src_stylus'
directorio_coffeescript_origen = './src_coffeescript'

# Directorios de archivos de destino
directorio_html_destino = './build_html'
directorio_css_destino = './build_css'
directorio_js_destino = './build_js'

# Comandos para compilar archivos Pug, Stylus y CoffeeScript
comando_compilar_pug = 'pug {} -o {}'
comando_compilar_stylus = 'stylus {} -o {}'
comando_compilar_coffeescript = 'coffee -c {} -o {}'

# Función para ejecutar un comando en la línea de comandos
def ejecutar_comando(comando):
    proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proceso.communicate()
    return stdout, stderr

# Función para observar cambios en archivos
def observar_cambios():
    try:
        while True:
            for raiz, carpetas, archivos in os.walk(directorio_pug_origen):
                for archivo in archivos:
                    ruta_archivo = os.path.join(raiz, archivo)
                    extension = os.path.splitext(ruta_archivo)[1][1:]  # Obtener la extensión del archivo
                    if extension == 'pug':
                        stdout, stderr = ejecutar_comando(comando_compilar_pug.format(ruta_archivo, directorio_html_destino))
                        if stderr:
                            print(f'Error al compilar {ruta_archivo}: {stderr.decode("utf-8")}')
                        else:
                            print(f'Compilado: {ruta_archivo} -> {directorio_html_destino}')

            for raiz, carpetas, archivos in os.walk(directorio_stylus_origen):
                for archivo in archivos:
                    ruta_archivo = os.path.join(raiz, archivo)
                    extension = os.path.splitext(ruta_archivo)[1][1:]  # Obtener la extensión del archivo
                    if extension == 'styl':
                        stdout, stderr = ejecutar_comando(comando_compilar_stylus.format(ruta_archivo, directorio_css_destino))
                        if stderr:
                            print(f'Error al compilar {ruta_archivo}: {stderr.decode("utf-8")}')
                        else:
                            print(f'Compilado: {ruta_archivo} -> {directorio_css_destino}')

            for raiz, carpetas, archivos in os.walk(directorio_coffeescript_origen):
                for archivo in archivos:
                    ruta_archivo = os.path.join(raiz, archivo)
                    extension = os.path.splitext(ruta_archivo)[1][1:]  # Obtener la extensión del archivo
                    if extension == 'coffee':
                        stdout, stderr = ejecutar_comando(comando_compilar_coffeescript.format(ruta_archivo, directorio_js_destino))
                        if stderr:
                            print(f'Error al compilar {ruta_archivo}: {stderr.decode("utf-8")}')
                        else:
                            print(f'Compilado: {ruta_archivo} -> {directorio_js_destino}')
                            
            input("Presiona Enter para continuar...")
    except KeyboardInterrupt:
        print("Salida del programa")

if __name__ == "__main__":
    print('Observando archivos Pug, Stylus y CoffeeScript...')
    observar_cambios()
