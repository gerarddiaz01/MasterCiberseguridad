Documentos de Referencia: "FSL Clase 12 – Scripting básico en bash.pdf"

# Informe Técnico: Scripting Básico en Bash

## 1\. Resumen Ejecutivo

Este informe cubre los fundamentos del **scripting en Bash**, una herramienta esencial para la administración de sistemas y la automatización de tareas en entornos Linux. Se exploran las ventajas de usar scripts para el fortalecimiento de servidores (hardening), la sintaxis básica de los comandos, el uso de variables, operadores, estructuras de control de flujo y funciones. Se presentan ejemplos prácticos para ilustrar estos conceptos y se analizan las mejores prácticas de seguridad. Finalmente, se demuestra la aplicación de estos conocimientos a través de una prueba de concepto que automatiza el escaneo de puertos con **Nmap**.

-----

## 2\. Conceptos Fundamentales

  * **Bash (Born Again SHell)**: Es el intérprete de comandos por defecto en la mayoría de las distribuciones Linux. Bash proporciona una interfaz de usuario para interactuar con el sistema operativo y es ampliamente utilizado para la administración de sistemas y la automatización de tareas.
  * **Script en Bash**: Es un archivo de texto que contiene una serie de comandos de Bash que se ejecutan secuencialmente. La primera línea de un script, conocida como **shebang** (`#!/bin/bash`), especifica el intérprete que debe usarse para ejecutar el archivo.
  * **Sintaxis Básica de Comandos**: Los comandos de Bash siguen la estructura `comando [opciones] [argumentos]`.
      * **Comando**: Es la instrucción principal para el intérprete.
      * **Opciones**: Modifican el comportamiento del comando.
      * **Argumentos**: Proporcionan información adicional al comando.
  * **Variables y Tipos de Datos**: Las variables en Bash se utilizan para almacenar datos. Pueden ser de tipo:
      * **Cadena de texto (`string`)**: Se asignan entre comillas dobles.
      * **Numérico (`integer` o `float`)**: No requieren caracteres especiales, solo el número. Para referenciar una variable se usa el símbolo de dólar (`$`) seguido del nombre de la variable.
  * **Comentarios**: Se usan para documentar el código y se inician con el símbolo de almohadilla (`#`).
  * **Operadores y Expresiones**: Los operadores se usan para realizar operaciones matemáticas y lógicas, mientras que las expresiones son combinaciones de variables, operadores y valores. Para realizar una operación aritmética, se utiliza la sintaxis `$((expresión))`.
  * **Estructuras de Control de Flujo**: Permiten controlar y modificar el orden de ejecución de los comandos.
      * **Condicionales**: `if`, `else`, `elif`. Permiten ejecutar un bloque de código si una condición es verdadera.
      * **Bucles**: `for`, `while`, `until`. Permiten ejecutar un bloque de código repetidamente mientras una condición se cumpla.
  * **Funciones**: Son bloques de código reutilizables. Se definen con un nombre, paréntesis `()`, y el código dentro de llaves `{}`. Los parámetros se pasan como variables numeradas, por ejemplo `$1` para el primer parámetro.
  * **Redirección de Entrada/Salida**: Permite cambiar la forma en que los scripts interactúan con la entrada y salida estándar. Los operadores comunes son `>` (redirige la salida a un archivo, sobrescribiendo), `>>` (redirige la salida y la añade al final del archivo), y `<` (redirige la entrada desde un archivo).
  * **Tuberías (`Pipelines`)**: Permiten enviar la salida de un comando como entrada para otro comando. Se representan con el símbolo `|`. Esto es útil para encadenar operaciones complejas.

-----

## 3\. Procedimientos Prácticos

### 3.1. Prueba de Concepto: Automatización de Hardening Básico

Este procedimiento demuestra cómo crear un script para actualizar automáticamente el sistema, lo que representa una tarea de **hardening**.

1.  **Crear el archivo del script**:
      * **Comando**: `nano automation.sh`
      * **Propósito**: Crea y abre un nuevo archivo llamado `automation.sh` en el editor `nano`.
2.  **Escribir el script**:
      * **Contenido**:
        ```bash
        #!/bin/bash
        apt-get update
        apt-get upgrade
        echo "Update and upgrade finished"
        ```
      * **Explicación**: El `shebang` indica que es un script de Bash. `apt-get update` actualiza la lista de paquetes disponibles. `apt-get upgrade` instala las nuevas versiones de los paquetes. `echo` muestra un mensaje de confirmación al usuario.
3.  **Ejecutar el script**:
      * **Comando**: `sudo sh automation.sh`
      * **Propósito**: Se usa `sudo` porque los comandos de actualización requieren privilegios de administrador.
      * **Resultado**: El script se ejecuta, actualiza la lista de paquetes, instala las actualizaciones y muestra el mensaje final.

-----

### 3.2. Prueba de Concepto: Escaneo de Puertos con Nmap

Este procedimiento automatiza el escaneo de puertos abiertos con **Nmap** y genera un informe en un archivo de texto.

1.  **Crear el archivo del script**:

      * **Comando**: `nano solution.sh`
      * **Propósito**: Crear y abrir el archivo del script.

2.  **Escribir el script**:

      * **Contenido**:
        ```bash
        #!/bin/bash
        open_ports=$(nmap -sT -A localhost | grep -E "open" | awk '{print $1}')
        echo "**Open ports report**" > port_report.txt
        for port in $open_ports; do
            echo "- $port" >> port_report.txt
        done
        echo "An open ports report has been generated in port_report.txt"
        ```
      * **Explicación de los comandos**:
          * `open_ports=$(...)`: Almacena el resultado de la expresión entre paréntesis en la variable `open_ports`.
          * `nmap -sT -A localhost`: Escanea la máquina local (`localhost`). `-sT` realiza un escaneo TCP Connect para encontrar puertos abiertos. `-A` activa la detección del sistema operativo y las versiones de los servicios.
          * `| grep -E "open"`: La tubería (`|`) envía la salida de `nmap` a `grep`. `grep` filtra las líneas que contienen la palabra "open".
          * `| awk '{print $1}'`: La tubería envía el resultado a `awk`, que se utiliza para procesar y formatear la salida. `'{print $1}'` imprime la primera columna de cada línea, que corresponde al puerto abierto.
          * `echo "**Open ports report**" > port_report.txt`: Crea el archivo `port_report.txt` y añade el encabezado, sobrescribiendo cualquier contenido previo.
          * `for port in $open_ports; do ... done`: Itera sobre cada puerto almacenado en la variable `open_ports`.
          * `echo "- $port" >> port_report.txt`: En cada iteración, agrega la información del puerto al final del archivo `port_report.txt` sin sobrescribirlo, gracias al operador `>>`.
          * `echo "An open ports report...`: Muestra un mensaje final al usuario con el nombre del informe generado.

3.  **Ejecutar y verificar**:

      * **Comando**: `sh solution.sh`
      * **Verificación**: Se ejecuta el script, que genera el informe. Usando `ls`, se comprueba la existencia del archivo `port_report.txt`. Con `cat port_report.txt`, se visualiza el contenido del informe, que muestra los puertos abiertos.
      * **Comando**: `nmap -sT -A localhost`
      * **Verificación**: Se ejecuta el comando `nmap` directamente en la terminal y se compara su salida con el informe. El resultado del script coincide con la información filtrada manualmente, confirmando el correcto funcionamiento del script.

-----

## 4\. Conclusiones y Puntos Clave

### 4.1. Importancia y Beneficios de Seguridad

El **scripting en Bash** es fundamental para el fortalecimiento de servidores GNU/Linux. Permite automatizar tareas de seguridad recurrentes como la aplicación de actualizaciones y la configuración de firewalls, lo que ahorra tiempo y esfuerzo y reduce el riesgo de errores humanos. Los scripts también facilitan la **monitorización** del sistema y el registro de eventos, lo que es esencial para la detección de actividades sospechosas y la auditoría. Las prácticas de seguridad, como la validación de la entrada del usuario y la minimización de privilegios, son cruciales para evitar vulnerabilidades como la **inyección de comandos** y la exposición de información sensible.

### 4.2. Puntos de Aprendizaje Clave

  * **Fundamentos del Scripting**: Se aprendieron conceptos esenciales como variables, operadores, expresiones y estructuras de control de flujo (`if`, `for`, `while`), que son la base para crear scripts funcionales.
  * **Estructuras Avanzadas**: Se exploraron funcionalidades avanzadas como las **funciones**, la **redirección de entrada/salida** (`>`, `>>`) y las **tuberías** (`|`), que permiten escribir scripts más complejos, modulares y eficientes.
  * **Prácticas de Seguridad**: Se destacó la importancia de validar la entrada del usuario, minimizar los privilegios de ejecución de los scripts y utilizar herramientas como `shellcheck` para detectar vulnerabilidades.
  * **Uso de Herramientas**: Se demostró cómo integrar herramientas de ciberseguridad como **Nmap** en scripts para automatizar procesos de detección y generar informes.

### 4.3. Relevancia Técnica

Los procedimientos aprendidos tienen una alta relevancia en la administración de sistemas. La capacidad de automatizar tareas repetitivas y compartir scripts mejora la **eficiencia y la productividad**. La integración con APIs para obtener información en tiempo real y el uso de tuberías y filtros como `grep` y `awk` son habilidades técnicas valiosas para el procesamiento de datos y la automatización de flujos de trabajo. El ejercicio de **Nmap** es un ejemplo práctico de cómo el scripting en Bash se convierte en una herramienta indispensable para los profesionales de la ciberseguridad, permitiendo automatizar la detección de vulnerabilidades de manera programática.