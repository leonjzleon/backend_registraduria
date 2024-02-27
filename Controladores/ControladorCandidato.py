from Modelos.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido


"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()


    def index(self):
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        nuevoCandidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        CandidatoActual = Candidato(self.repositorioCandidato.findById(id))
        CandidatoActual.cedula = infoCandidato["cedula"]
        CandidatoActual.numero_resolucion = infoCandidato["numero_resolucion"]
        CandidatoActual.nombre = infoCandidato["nombre"]
        CandidatoActual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(CandidatoActual)

    def delete(self, id):
        return self.repositorioCandidato.delete(id)

    """
        Relación Partido y Candidato
        """

    def asignarPartido(self, id, id_Partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_Partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)