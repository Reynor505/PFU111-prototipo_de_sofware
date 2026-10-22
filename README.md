# Prototipo de Software Seguro y Validado

## PFU-111 - Semana 12 - Grupo 2

### Descripción del proyecto

Este proyecto consiste en un prototipo de consola desarrollado en Python para registrar y administrar solicitudes de soporte técnico de estudiantes universitarios. El programa permite ingresar datos, validarlos antes del registro, consultar solicitudes almacenadas y limpiar los campos.

### Objetivo

Desarrollar un programa que permita gestionar solicitudes de soporte técnico mediante funciones, programación orientada a objetos y validaciones de datos, evitando el registro de información incompleta o incorrecta.

### Tecnologías utilizadas

- **Lenguaje:** Python 3.
- **Editor recomendado:** Visual Studio Code.
- **Interfaz:** Consola.
- **Conceptos aplicados:** Clases, objetos, listas, funciones, condicionales, ciclos y validación de datos.

### Funcionalidades

El sistema cuenta con las siguientes opciones:

1. **Ingresar datos:** solicita el nombre, código de estudiante, tipo de solicitud, descripción y prioridad.
2. **Registrar solicitud:** valida los datos y registra la solicitud únicamente si son correctos.
3. **Limpiar campos:** borra los datos ingresados para comenzar un nuevo registro.
4. **Consultar solicitudes:** muestra las solicitudes registradas o informa si todavía no existen.
5. **Salir:** finaliza la ejecución del programa.

### Validaciones implementadas

- **Nombre:** no puede estar vacío ni contener números.
- **Código de estudiante:** debe cumplir el formato `EST-12345`.
- **Tipo de solicitud:** acepta únicamente `equipo`, `software` o `conectividad`.
- **Descripción:** no puede estar vacía y debe contener al menos 10 caracteres.
- **Prioridad:** acepta únicamente `bajo`, `medio` o `alto`.

Los datos de texto se limpian de espacios sobrantes mediante `strip()`. El código se convierte a mayúsculas y el tipo de solicitud y la prioridad a minúsculas para facilitar su validación.

### Estructura del código

El programa utiliza dos clases principales:

- **`Solicitud`:** representa una solicitud registrada y contiene sus datos, identificador y método para mostrar la información.
- **`SistemaSoporte`:** administra la captura, validación, registro, limpieza y consulta de solicitudes.

La función `mostrar_menu()` presenta las opciones disponibles y la función `main()` controla el funcionamiento del programa mediante un ciclo `while`.

### Requisitos

- Tener Python 3 instalado.
- Contar con un editor de código o una terminal para ejecutar el programa.

### Cómo ejecutar el programa

1. Clonar o descargar este repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code o una terminal.
3. Ejecutar el siguiente comando:

```bash
python solicitudes_soporte_simple.py
```

Si tu sistema utiliza el comando `python3`, puedes ejecutar:

```bash
python3 solicitudes_soporte_simple.py
```

4. Seleccionar una opción del menú e ingresar los datos solicitados.

### Almacenamiento de datos

Las solicitudes se almacenan temporalmente en una lista de objetos mientras el programa está en ejecución. El código actual no implementa almacenamiento permanente en archivos o bases de datos.

### Integrantes

- Ronald Cruz Chino
- Denilson Davis Machaca Flores
- Daniel Wilfredo Pomarez Huaranca

### Conclusión

Este prototipo permite gestionar solicitudes de soporte técnico mediante una interfaz de consola sencilla. La aplicación de validaciones y la organización del código en clases contribuyen a mejorar la estructura del programa y a reducir los errores en el ingreso de información.

**Proyecto académico — PFU-111, Semana 12, Grupo 2.**

La Paz, Bolivia.
