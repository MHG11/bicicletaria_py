class Bicicleta:
    
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.mdelo = modelo
        self.ano = ano
        self.valor = valor
        
   
   
    def buzinar(self):
        print("a bicicleta buzinou.")

    def parar(self):
        print("a bicicleta parou.")

    def correr(self):
        print ("a bicicleta correu.")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
   
    
    
caloi = Bicicleta("azul","trilha", "2024", 5000)

print(caloi)


    