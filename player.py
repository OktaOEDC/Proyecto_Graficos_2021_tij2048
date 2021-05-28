import yaml
import logging
from direct.showbase.ShowBase import ShowBase
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s - %(message)s')


class Player:  
    """Player class.

    Returns:
        [class]: [player class methods and attributes]
    """
    phil_dict = {"Dios": "teologica",
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
    phil_values = {"Dios": "teologica",
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

    def __init__(self, name='username'):
        self.name = name
        self.wallet = 0
        self.vidas = 3
        self.politica = 0
        self.educacion = 0
        self.popularidad = 0
        self.mascara = 0
        self.xx = 0
        self.yy = 0
        self.flags = {'anarquista': False, 'libertariano': False, 'fascista': False,
                      'comunista': False, 'neoliberal': False, 'populista': False, 'autoritario': False}

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
        if change is int:
            self.politica += change
        else:
            logging.debug('change de POLITICA no es entero')

    def change_edu(self, change):
        """Funcion que suma o resta los puntos del atributo educacion
        Args:
            change ([int]): [Numero entero negativo o positivo]
        """
        if change is int:
            self.educacion += change
        else:
            logging.debug('change  de EDUCACION no es entero')

    def change_pop(self, change):
        """Funcion que quita o remueve la mascara del jugador
        Args:
            change ([bool]): [Boolean que indica mascara puesta o no]
        """
        if change is bool:
            self.politica = change
        else:
            logging.debug('change de POP no es boolean')

    def change_pol(self, change):
        """Funcion que suma o resta los puntos del atributo politica
        Args:
            change ([int]): [Numero entero negativo o positivo]
        """
        if change is int:
            self.politica += change
        else:
            logging.debug('change no es entero')

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

    def calculate_phil(self):
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
        with open('player.yaml','w') as file:
            yaml.dump(dictionary,file)

    def savefile(self):
        self.player_to_yaml(self.makedict())
        
    def loadfile(self):
        self.yaml_to_player(self.readyaml())