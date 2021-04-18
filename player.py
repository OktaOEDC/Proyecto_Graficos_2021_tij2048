import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Player:
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

    def __init__(self, name):
        self.name = name
        self.wallet = 0
        self.politica = 0
        self.educacion = 0
        self.popularidad = 0
        self.mascara = 0
        self.xx = 0
        self.yy = 0
        self.flags = {'anarquista': False, 'libertariano': False, 'fascista': False,
                      'comunista': False, 'neoliberal': False, 'populista': False}

    def pri_gang(self):
        """CHECA Y HACE AL JUGADOR PRIISTA
        """
        if self.name == 'Ulises':
            self.flags['neoliberal'] = True

        if self.flags['neoliberal'] == True:
            self.wallet = 1000
            print('Bienvenido al PRI compadre')
            self.name('Carlos S')

    def amlo_mode(self):
        """CHECA Y HACE AL JUGADOR POBRE
        """
        if self.name == 'Julio':
            self.flags['populista'] = True
        if self.flags['populista'] == True:
            self.wallet = 0
            self.nombre = 'Andres Manuel'
            print('MORENA!')
            print('HORA DE HACER UN TREN PLEBE')

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

    def calculate_phil(self):
        print('beep bop')


def main():
    print('hello world!')


main()
