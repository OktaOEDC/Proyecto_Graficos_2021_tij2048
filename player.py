import logging;
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class Player:
    def __init__(self, name):
        self.name = name
        self.politica = 0;
        self.educacion = 0;
        self.popularidad = 0;
        self.mascara = 0;
    def change_pol(self, input):

            if (input==True):
                self.politica+=1;
                logging.debug('\n...POLITICA +1\n')
            else:
                self.politica-=0;
                logging.debug('\n...POLITICA -1\n')

    def get_name(self):
        return self.name
    
    def get_pol(self):
        return self.politica

    def get_edu(self):
        return self.educacion

    def get_pop(self):
        return self.popularidad

    def calculate_phil(self):
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


def main():
    print('hello world!')


main()
