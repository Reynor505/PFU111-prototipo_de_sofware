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


