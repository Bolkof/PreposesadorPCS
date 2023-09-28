const fs = require('fs');
const { exec } = require('child_process');

// Directorios de archivos de origen
const directorioPugOrigen = './src_pug';
const directorioStylusOrigen = './src_stylus';
const directorioCoffeeScriptOrigen = './src_coffeescript';

// Directorios de archivos de destino
const directorioHtmlDestino = './build_html';
const directorioCssDestino = './build_css';
const directorioJsDestino = './build_js';

// Comandos para compilar archivos Pug, Stylus y CoffeeScript
const comandoCompilarPug = 'pug {} -o {}';
const comandoCompilarStylus = 'stylus {} -o {}';
const comandoCompilarCoffeeScript = 'coffee -c {} -o {}';

// Función para ejecutar un comando en la línea de comandos
function ejecutarComando(comando, callback) {
    exec(comando, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error al ejecutar el comando: ${error}`);
            return;
        }
        callback(stdout);
    });
}

// Función para observar cambios en archivos
function observarCambios() {
    try {
        fs.watch(directorioPugOrigen, { recursive: true }, (eventType, filename) => {
            if (filename.endsWith('.pug')) {
                const comando = comandoCompilarPug.replace('{}', `${directorioPugOrigen}/${filename}`).replace('{}', directorioHtmlDestino);
                ejecutarComando(comando, (resultado) => {
                    if (resultado) {
                        console.log(resultado);
                    } else {
                        console.log(`Compilado: ${filename} -> ${directorioHtmlDestino}`);
                    }
                });
            }
        });

        fs.watch(directorioStylusOrigen, { recursive: true }, (eventType, filename) => {
            if (filename.endsWith('.styl')) {
                const comando = comandoCompilarStylus.replace('{}', `${directorioStylusOrigen}/${filename}`).replace('{}', directorioCssDestino);
                ejecutarComando(comando, (resultado) => {
                    if (resultado) {
                        console.log(resultado);
                    } else {
                        console.log(`Compilado: ${filename} -> ${directorioCssDestino}`);
                    }
                });
            }
        });

        fs.watch(directorioCoffeeScriptOrigen, { recursive: true }, (eventType, filename) => {
            if (filename.endsWith('.coffee')) {
                const comando = comandoCompilarCoffeeScript.replace('{}', `${directorioCoffeeScriptOrigen}/${filename}`).replace('{}', directorioJsDestino);
                ejecutarComando(comando, (resultado) => {
                    if (resultado) {
                        console.log(resultado);
                    } else {
                        console.log(`Compilado: ${filename} -> ${directorioJsDestino}`);
                    }
                });
            }
        });

        console.log('Observando archivos Pug, Stylus y CoffeeScript...');
        console.log('Presiona Ctrl+C para salir.');
    } catch (error) {
        console.error(`Error: ${error}`);
    }
}

observarCambios();
