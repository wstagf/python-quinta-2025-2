class Carro:        # Classe
  cor = ""          # Atributo
  modelo = 0        # Atributo
  ano = 0           # Atributo
  tipoRoda = ""     # Atributo
  __renavam = ""    # Atributo PRIVADO, somente a classe tem acesso
  __tank = 0        # Atributo PRIVADO, somente a classe tem acesso

  def __init__(self, cor, mod, ano, tipoRoda, renavam): # Construtor com parametros
      self.cor = cor
      self.modelo = mod
      self.ano = ano
      self.tipoRoda = tipoRoda
      self.__renavam = renavam

  def mostrarDetalhes(self):  # Metodo, sem parametros, e SEM retorno
      print("Eu sou um carro")
      print("Cor: " + self.cor )
      print("Ano: " + str( self.ano))
      print("Modelo: " + str( self.modelo))

  def lerRenavam(self):  # Metodo, sem parametros, e COM retorno
      return self.__renavam
  
  def abastecer(self, quantidade): # Metodo, COM parametros, e SEM retorno 
      self.__tank = self.__tank + quantidade

  def painelGasolina(self): # Metodo, SEM parametros, e COM retorno
      return self.__tank
      
  



def main():
     print("Orientacao a Objetos")
     brasilia = Carro("Amarelo", 2020, 
                      2021, "Gauchas",
                      "RENAVAM1") # Instanciar um ojeto chamado
                      # brasilia do tipo Carro 
                      # e não passou parametro
                      # nenhum para o contrutor
     brasilia.mostrarDetalhes()
     print(brasilia.tipoRoda)
     print(brasilia.lerRenavam())
     print("O tank esta com " + str(brasilia.painelGasolina()))
     brasilia.abastecer(100)
     print("O tank esta com " + str(brasilia.painelGasolina()))


     print("    -   -   -   -   -    ")
     print("    -   -   -   -   -    ")
     print("    -   -   -   -   -    ")


     gol = Carro("Vermelho", 2010, 2010, 
                  "Liga Leve", "RENAVAM2")
      
     gol.mostrarDetalhes()
     print(gol.tipoRoda)
     print(gol.lerRenavam())
     print("O tank esta com " + str(gol.painelGasolina()))
     gol.abastecer(50)
     print("O tank esta com " + str(gol.painelGasolina()))


if __name__ == "__main__":
    main()
    
  


 
