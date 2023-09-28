fs = require 'fs'
exec = require 'child_process').exec

# Directorios de archivos de origen
directorioPugOrigen = './src_pug'
directorioStylusOrigen = './src_stylus'
directorioCoffeeScriptOrigen = './src_coffeescript'

# Directorios de archivos de destino
directorioHtmlDestino = './build_html'
directorioCssDestino = './build_css'
directorioJsDestino = './build_js'

# Comandos para compilar archivos Pug, Stylus y CoffeeScript
comandoCompilarPug = 'pug {} -o {}'
comandoCompilarStylus = 'stylus {} -o {}'
comandoCompilarCoffeeScript = 'coffee -c {} -o {}'

# Función para ejecutar un comando en la línea de comandos
ejecutarComando = (comando, callback) ->
  exec comando, (error, stdout, stderr) ->
    if error
      console.error "Error al ejecutar el comando: #{error}"
      return
    callback stdout

# Función para observar cambios en archivos
observarCambios = ->
  try
    fs.watch directorioPugOrigen, recursive: true, (eventType, filename) ->
      if filename.endsWith('.pug')
        comando = comandoCompilarPug.replace '{}', "#{directorioPugOrigen}/#{filename}".replace '{}', directorioHtmlDestino
        ejecutarComando comando, (resultado) ->
          if resultado
            console.log resultado
          else
            console.log "Compilado: #{filename} -> #{directorioHtmlDestino}"

    fs.watch directorioStylusOrigen, recursive: true, (eventType, filename) ->
      if filename.endsWith('.styl')
        comando = comandoCompilarStylus.replace '{}', "#{directorioStylusOrigen}/#{filename}".replace '{}', directorioCssDestino
        ejecutarComando comando, (resultado) ->
          if resultado
            console.log resultado
          else
            console.log "Compilado: #{filename} -> #{directorioCssDestino}"

    fs.watch directorioCoffeeScriptOrigen, recursive: true, (eventType, filename) ->
      if filename.endsWith('.coffee')
        comando = comandoCompilarCoffeeScript.replace '{}', "#{directorioCoffeeScriptOrigen}/#{filename}".replace '{}', directorioJsDestino
        ejecutarComando comando, (resultado) ->
          if resultado
            console.log resultado
          else
            console.log "Compilado: #{filename} -> #{directorioJsDestino}"

    console.log 'Observando archivos Pug, Stylus y CoffeeScript...'
    console.log 'Presiona Ctrl+C para salir.'
  catch error
    console.error "Error: #{error}"

observarCambios()
