

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    #grado = None
    grado = "grado 12"

    #def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
    def __init__(self, grupo="Grupo de estudiantes: ", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo
        #cadena = self._grupo+"grupo predeterminado"  
        #cadena = self._grupo +" "+self._asignaturas+" "+self.listadoAlumnos
        #return cadena
    
    #def listadoAsignaturas(self, **kwargs):
    def listadoAsignaturas(self, **kwargs):       
        self._asignaturas = []
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

        
    def agregarAlumno(self, alumno, lista=None):
        #if(lista is None):
         #   lista.append(alumno)
         #   self.listadoAlumnos = self.listadoAlumnos + lista
        #else:
        #    self.listadoAlumnos = [alumno]
        #if lista is None:
        #    lista = []
        #lista.append(alumno)
        #return lista
        if (lista is not None):
            lista.append(alumno)
            self.listadoAlumnos = lista
        else:
            self.listadoAlumnos = [alumno]


    # @ classmethod
    #def asignarNombre(cls, nombre="Grado 10"):
    #    cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 4"):
     #   cls.grado = nombre
