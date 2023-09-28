import 'dart:io';

// Directorios de archivos de origen
final directorioPugOrigen = './src_pug';
final directorioStylusOrigen = './src_stylus';
final directorioCoffeeScriptOrigen = './src_coffeescript';

// Directorios de archivos de destino
final directorioHtmlDestino = './build_html';
final directorioCssDestino = './build_css';
final directorioJsDestino = './build_js';

// Comandos para compilar archivos Pug, Stylus y CoffeeScript
final comandoCompilarPug = 'pug {} -o {}';
final comandoCompilarStylus = 'stylus {} -o {}';
final comandoCompilarCoffeeScript = 'coffee -c {} -o {}';

// Función para ejecutar un comando en la línea de comandos
Future<void> ejecutarComando(String comando) async {
  final proceso = await Process.start(comando, [], runInShell: true);
  final stdoutStream = proceso.stdout.transform(Utf8Decoder());
  final stderrStream = proceso.stderr.transform(Utf8Decoder());

  await for (final line in stdoutStream) {
    print(line);
  }

  await for (final line in stderrStream) {
    print(line);
  }
}

// Función para observar cambios en archivos
Future<void> observarCambios() async {
  try {
    while (true) {
      await for (final entity in Directory(directorioPugOrigen).list(recursive: true)) {
        if (entity is File && entity.path.endsWith('.pug')) {
          final rutaArchivo = entity.path;
          await ejecutarComando(comandoCompilarPug
              .replaceAll('{}', rutaArchivo)
              .replaceAll('{}', directorioHtmlDestino));
        }
      }

      await for (final entity in Directory(directorioStylusOrigen).list(recursive: true)) {
        if (entity is File && entity.path.endsWith('.styl')) {
          final rutaArchivo = entity.path;
          await ejecutarComando(comandoCompilarStylus
              .replaceAll('{}', rutaArchivo)
              .replaceAll('{}', directorioCssDestino));
        }
      }

      await for (final entity in Directory(directorioCoffeeScriptOrigen).list(recursive: true)) {
        if (entity is File && entity.path.endsWith('.coffee')) {
          final rutaArchivo = entity.path;
          await ejecutarComando(comandoCompilarCoffeeScript
              .replaceAll('{}', rutaArchivo)
              .replaceAll('{}', directorioJsDestino));
        }
      }

      print('Presiona Enter para continuar...');
      await stdin.readLineSync();
    }
  } on FileSystemException catch (e) {
    print('Error: $e');
  } on ProcessException catch (e) {
    print('Error al ejecutar el comando: $e');
  }
}

void main() {
  print('Observando archivos Pug, Stylus y CoffeeScript...');
  observarCambios();
}
