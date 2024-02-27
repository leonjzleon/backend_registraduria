from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorResultado():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """

    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()
        print("Creando ControladorResultado")

    def index(self):
        print("Listar todas los Resultados")
        return self.repositorioResultado.findAll()

    def create(self, infoResultado, id_candidato, id_mesa):
        nuevaResultado = Resultado(infoResultado)
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevaResultado.candidato = elCandidato
        nuevaResultado.mesa = laMesa
        return self.repositorioResultado.save(nuevaResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    """
    Modificación de inscripción (estudiante y materia)  
    """

    def update(self, id, infoResultado, id_candidato, id_mesa):
        laResultado = Resultado(self.repositorioResultado.findById(id))
        laResultado.numero_mesa = infoResultado["numero_mesa"]
        laResultado.id_partido = infoResultado["id_partido"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        laResultado.candidato = elCandidato
        laResultado.mesa = laMesa
        return self.repositorioResultado.save(laResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)