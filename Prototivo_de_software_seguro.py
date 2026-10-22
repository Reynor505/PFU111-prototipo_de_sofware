"""
Prototipo de consola: solicitudes de soporte técnico de estudiantes.
Versión simplificada (listas, funciones y POO).
"""

TIPOS_PERMITIDOS = ["equipo", "software", "conectividad"]
PRIORIDADES_PERMITIDAS = ["bajo", "medio", "alto"]
MIN_DESCRIPCION = 10


# Clase que representa una solicitud
class Solicitud:
    def __init__(self, id, nombre, codigo, tipo, descripcion, prioridad):
        self.id = id
        self.nombre = nombre
        self.codigo = codigo
        self.tipo = tipo
        self.descripcion = descripcion
        self.prioridad = prioridad

    def mostrar(self):
        print(f"#{self.id} | {self.nombre} ({self.codigo}) | {self.tipo} | prioridad {self.prioridad}")
        print(f"     Problema: {self.descripcion}")

# Clase que maneja todo el sistema
class SistemaSoporte:
    def __init__(self):
        self.solicitudes = []   # lista de objetos Solicitud
        self.nombre = ""
        self.codigo = ""
        self.tipo = ""
        self.descripcion = ""
        self.prioridad = ""

    def capturar_datos(self):
        #Pide los datos al usuario y los guarda (sin validar).
        self.nombre = input("Nombre del solicitante: ").strip()
        self.codigo = input("Código de estudiante (formato EST-12345): ").strip().upper()
        self.tipo = input("Tipo de solicitud (equipo/software/conectividad): ").strip().lower()
        self.descripcion = input("Descripción del problema: ").strip()
        self.prioridad = input("Prioridad (bajo/medio/alto): ").strip().lower()
        print("-> Datos capturados. Use la opción 2 para registrar la solicitud.")

    def codigo_es_valido(self):
        #El código debe ser 'EST-' seguido de 5 dígitos (ej. EST-20451).
        if len(self.codigo) != 9:
            return False
        if not self.codigo.startswith("EST-"):
            return False
        if not self.codigo[4:].isdigit():
            return False
        return True

    def validar_datos(self):
        #Devuelve una lista de errores. Lista vacía = datos válidos.
        errores = []

        if self.nombre == "":
            errores.append("El nombre no puede estar vacío.")
        elif any(letra.isdigit() for letra in self.nombre):
            errores.append("El nombre no debe contener números.")

        if not self.codigo_es_valido():
            errores.append("El código debe tener el formato EST-12345 (EST- y 5 dígitos).")

        if self.tipo not in TIPOS_PERMITIDOS:
            errores.append("El tipo no es válido. Opciones: equipo, software o conectividad.")

        if self.descripcion == "":
            errores.append("La descripción no puede estar vacía.")
        elif len(self.descripcion) < MIN_DESCRIPCION:
            errores.append(f"La descripción es muy corta (mínimo {MIN_DESCRIPCION} caracteres).")

        if self.prioridad not in PRIORIDADES_PERMITIDAS:
            errores.append("La prioridad no es válida. Opciones: bajo, medio o alto.")

        return errores

    def registrar(self):
        #Valida los datos y, si son correctos, crea la solicitud.
        errores = self.validar_datos()
        if len(errores) > 0:
            print("\nNO SE REGISTRÓ LA SOLICITUD. Corrija lo siguiente:")
            for error in errores:
                print(f"  x {error}")
            return

        nueva = Solicitud(len(self.solicitudes) + 1, self.nombre, self.codigo,
                          self.tipo, self.descripcion, self.prioridad)
        self.solicitudes.append(nueva)
        print(f"\nSolicitud #{nueva.id} registrada correctamente.")
        self.limpiar()

    def limpiar(self):
        self.nombre = ""
        self.codigo = ""
        self.tipo = ""
        self.descripcion = ""
        self.prioridad = ""

    def consultar(self):
        if len(self.solicitudes) == 0:
            print("\nNo existen solicitudes registradas todavía.")
            return
        print("\n=== SOLICITUDES REGISTRADAS ===")
        for solicitud in self.solicitudes:
            solicitud.mostrar()


