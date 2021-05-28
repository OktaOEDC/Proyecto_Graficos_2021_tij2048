import math
import yaml
import logging
import numpy as np
from direct.showbase.ShowBase import ShowBase
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s - %(message)s')


class Player:
    """Player class.

    Returns:
        [class]: [player class methods and attributes]
    """

    def __init__(self, name='username', wallet=0, vidas=3, politica=0, educacion=0, popularidad=0, mascara=0, xx=0, yy=00):
        self.name = name
        self.wallet = wallet
        self.vidas = vidas
        self.politica = politica
        self.educacion = educacion
        self.popularidad = popularidad
        self.mascara = mascara
        self.xx = xx
        self.yy = yy
        self.flags = {'anarquista': False, 'libertariano': False, 'fascista': False,
                      'comunista': False, 'neoliberal': False, 'populista': False, 'autoritario': False}
        self.phil_dict = {"Dios": "teologica",
                          "'Griegos'": "naturalista",
                          "Democrito": "democratico",
                          "Odin": "Mitologica",
                          "Socrates": "socratico",
                          "Platon": "platonico",
                          'Papa': 'Edad Media',
                          "Davinci": "Renacimiento",
                          "Descartes": "Dualista",
                          "Locke": "Liberalimo",
                          "Berkeley": "inmaterialismo",
                          "Kant": "idealismo",
                          "Schelling": "Romaticismo",
                          "Hegel": "idealismo aleman",
                          "Kierkegaard": "existencialismo",
                          "Marx": "socialismo",
                          "Darwin": "Evolutismo",
                          "Freud": "proto fenomenologia",
                          "Foucalt": "post estructuralista",
                          "Rand": "Objetivismo",
                          "Chomsky": "Medios",
                          "Magon": "Anarquismo"}
        self.phil_values = {"Dios": [2, 1, 7, 1],
                            "'Griegos'": [5, 5, 3, 0],
                            "Democrito": [10, 8, 5, 1],
                            "Odin": [0, 9, 5, 0],
                            "Socrates": [5, 10, 3, 0],
                            "Platon": [2, 2, 9, 0],
                            'Papa': [10, 1, 4, 0],
                            "Davinci": [4, 9, 2, 1],
                            "Descartes": [4, 4, 4, 0],
                            "Locke": [3, 7, 10, 1],
                            "Berkeley": [0, 0, 1, 1],
                            "Kant": [9, 7, 8, 0],
                            "Schelling": [6, 8, 6, 1],
                            "Hegel": [7, 5, 7, 0],
                            "Kierkegaard": [7, 5, 7, 0],
                            "Marx": [0, 10, 1, 1],
                            "Darwin": [9, 10, 9, 1],
                            "Freud": [7, 9, 4, 0],
                            "Foucalt": [1, 4, 7, 1],
                            "Rand": [3, 8, 6, 1],
                            "Chomsky": [9, 10, 5, 1],
                            "Magon": [5, 9, 4, 1]}
        self.statements = []
        self.mode_amlo()
        self.mode_mexico()
        self.mode_pri()

    def mode_pri(self):
        """CHECA Y HACE AL JUGADOR PRIISTA
        """
        if self.name == 'Ulises':
            self.flags['neoliberal'] = True

        if self.flags['neoliberal'] == True:
            self.wallet = 1000
            logging.debug('Bienvenido al PRI compadre')
            self.name = 'Carlos S'

    def mode_amlo(self):
        """CHECA Y HACE AL JUGADOR POBRE
        """
        if self.name == 'Julio':
            self.flags['populista'] = True
        if self.flags['populista'] == True:
            self.wallet = 0
            self.name = 'Andres Manuel'
            logging.debug('MORENA!')
            logging.debug('HORA DE HACER UN TREN PLEBE')

    def mode_mexico(self):
        """MODO MEXICO
        """
        self.vidas = 1
        self.wallet = 0
        logging.debug('bienvenido a Mexico, F en el chat...')

    def change_pol(self, change):
        """Funcion que suma o resta los puntos del atributo politica
        Args:
            change ([int]): [Numero entero negativo o positivo]
        """
        if type(change) == int:
            self.politica += change
        else:
            logging.debug('change de POLITICA no es entero')

    def change_edu(self, change):
        """Funcion que suma o resta los puntos del atributo educacion
        Args:
            change ([int]): [Numero entero negativo o positivo]
        """
        if type(change) == int:
            self.educacion += change
        else:
            logging.debug('change  de EDUCACION no es entero')

    def change_pop(self, change):
        """Funcion que quita o remueve la mascara del jugador
        Args:
            change ([bool]): [Boolean que indica mascara puesta o no]
        """
        if type(change) == int:
            self.politica = change
        else:
            logging.debug('change de POP no es int')

    def change_mascara(self, change):
        """Funcion que quita o remueve la mascara del jugador
        Args:
            change ([bool]): [Boolean que indica mascara puesta o no]
        """
        if type(change) == bool:
            self.mascara = change
        else:
            logging.debug('change de POP no es int')

    def get_name(self):
        return self.name

    def get_pol(self):
        return self.politica

    def get_edu(self):
        return self.educacion

    def get_pop(self):
        return self.popularidad

    def get_mascara(self):
        return self.mascara

    def edge_cases(self):
        """Aun no he terminado las auxiliares
        """
        # --------------edge cases -----------
        # Autoritario
        if self.get_pop() <= 0:
            self.flags['autoritario'] = True
            logging.debug('El jugador es Autoritario')
        # populista
        if self.get_pop() >= 10:
            self.flags['populista'] = True
            logging.debug('El jugador es Populista')
        # anarquismo
        if (self.get_pol() <= 0) and (self.get_mascara > 0):  # tal vez pongo un trap question
            self.flags['anarquista']
        # fascismo
        # falta un criterio que sera un trap question
        if (self.get_pol() >= 10 and (self.get_pop() > 5) and (self.get_edu() > 5)):
            self.flags['fascista']
            logging.debug('El jugador es Fascista')

    def get_phil(self):
        self.edge_cases()
        values = [self.get_pol(), self.get_edu(), self.get_edu(),
                  self.get_mascara()]
        diferences = [0, 0, 0, 0]
        temp_dif = [0, 0, 0, 0]
        bestdif = 0
        dif = 0

        for key in self.flags:
            if key == True:
                self.statements.append(self.name, 'eres', key)
                print((self.name, 'eres', key))

        for key, value in self.phil_values.items():
            for index in range(len(values)):
                temp_dif[index] = (value[index]-(values[index]))

            dif = (temp_dif[0])+(temp_dif[1])+(temp_dif[2])+(temp_dif[2])
            if dif < bestdif:
                bestdif = dif
                diferences = temp_dif
                dif = 0
            print('diferences are', diferences, 'total:', bestdif)
            if value == values:
                self.statements.append(
                    ('Pareces acercarte al perfil de', key, 'como', value))
                print((
                    'Pareces acercarte al perfil de', key, 'como', value))
                # worst case: no case
        if len(self.statements) < 1:
            self.statements.append((
                self.name, 'pareces no tener afilicion politica'))
        return self.statements

    def readyaml(self):
        """SAVEFILE GENERATOR
        """
        file = open("./player.yaml", 'r')
        dictionary = yaml.load(file)
        for key, value in dictionary.items():
            print(key, ":", str(value))
        return dictionary

    def makedict(self):
        dictionary = {'name': self.name, 'wallet': self.wallet,
                      'vidas': self.vidas, 'politica': self.politica,
                      'educacion': self.educacion, 'popularidad': self.popularidad, 'mascara': self.mascara, 'xx': self.xx, 'yy': self.yy, 'flags': {
                          'anarquista': self.flags['anarquista'],
                          'libertariano': self.flags['libertariano'],
                          'fascista': self.flags['fascista'],
                          'comunista': self.flags['comunista'],
                          'neoliberal': self.flags['populista'],
                          'autoritario': self.flags['autoritario']
                      }
                      }
        return dictionary

    def yaml_to_player(self, dictionary):
        self.name = dictionary.get('name')
        self.wallet = dictionary['wallet']
        self.vidas = dictionary['vidas']
        self.politica = dictionary['politica']
        self.educacion = dictionary['educacion']
        self.popularidad = dictionary['popularidad']
        self.mascara = dictionary['mascara']

    def player_to_yaml(self, dictionary):
        with open('player.yaml', 'w') as file:
            yaml.dump(dictionary, file)

    def savefile(self):
        self.player_to_yaml(self.makedict())

    def loadfile(self):
        self.yaml_to_player(self.readyaml())
