-- Módulo para ejecutar comandos en la línea de comandos
function ejecutarComando(comando)
    local handle = io.popen(comando)
    local resultado = handle:read("*a")
    handle:close()
    return resultado
end

-- Directorios de archivos de origen
local directorioPugOrigen = './src_pug'
local directorioStylusOrigen = './src_stylus'
local directorioCoffeeScriptOrigen = './src_coffeescript'

-- Directorios de archivos de destino
local directorioHtmlDestino = './build_html'
local directorioCssDestino = './build_css'
local directorioJsDestino = './build_js'

-- Comandos para compilar archivos Pug, Stylus y CoffeeScript
local comandoCompilarPug = 'pug {} -o {}'
local comandoCompilarStylus = 'stylus {} -o {}'
local comandoCompilarCoffeeScript = 'coffee -c {} -o {}'

-- Función para observar cambios en archivos
function observarCambios()
    while true do
        for archivo in io.popen('find ' .. directorioPugOrigen):lines() do
            if string.match(archivo, "%.pug$") then
                local comando = string.format(comandoCompilarPug, archivo, directorioHtmlDestino)
                local resultado = ejecutarComando(comando)
                if resultado ~= "" then
                    print(resultado)
                else
                    print(string.format('Compilado: %s -> %s', archivo, directorioHtmlDestino))
                end
            end
        end

        for archivo in io.popen('find ' .. directorioStylusOrigen):lines() do
            if string.match(archivo, "%.styl$") then
                local comando = string.format(comandoCompilarStylus, archivo, directorioCssDestino)
                local resultado = ejecutarComando(comando)
                if resultado ~= "" then
                    print(resultado)
                else
                    print(string.format('Compilado: %s -> %s', archivo, directorioCssDestino))
                end
            end
        end

        for archivo in io.popen('find ' .. directorioCoffeeScriptOrigen):lines() do
            if string.match(archivo, "%.coffee$") then
                local comando = string.format(comandoCompilarCoffeeScript, archivo, directorioJsDestino)
                local resultado = ejecutarComando(comando)
                if resultado ~= "" then
                    print(resultado)
                else
                    print(string.format('Compilado: %s -> %s', archivo, directorioJsDestino))
                end
            end
        end

        print("Presiona Enter para continuar...")
        io.read()
    end
end

print('Observando archivos Pug, Stylus y CoffeeScript...')
observarCambios()
