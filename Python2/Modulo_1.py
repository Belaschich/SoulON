'''
Crie uma classe animal com atributos e métodos, posteriormente, crie uma classe que herde seus atributos, 
 e possua os seus atributos próprios. 
Crie dois objetos da classe filha.
'''
class animal():
    def __init__(self, especie, genero, familia, ordem, classe, filo):
        self.especie = especie
        self.genero = genero
        self.familia = familia
        self.ordem = ordem
        self.classe = classe
        self.filo = filo

class hebivoro(animal):
    def __init__(self, especie, genero, familia, ordem, classe, filo, classe_alimento):
        super(). __init__(especie, genero, familia, ordem, classe, filo)
        self.classe_alimento = classe_alimento

c = animal("C. lupus", "Canis", "Canidae", "Carnivora", "Mamalia", "Chordata")
t = hebivoro("Multi-especie", "Multi-genero", "Ramphastidae", "Piciformes", "Aves", "Chordata", "frugívoros")
v = hebivoro("B. taurus", "Bos", "Bovidae", "Artiodactyla", "Mammalia", "Chordata", "ruminante")

print(vars(c))
print(vars(t))
print(vars(v))