from .ContaLuz import ContaLuz

class Contas:
    def __init__(self) :
        self.__contaLuz = []
        
    def addcontaLuz(self,conta:ContaLuz):
        self.__contaLuz.append(conta)   
        
    def mediaConsumoValor(self):
        media = 0
        for conta in self.__contaLuz:
            media +=conta.getvalorPagar()
        return f"A media das Contas é R${media/len(self.__contaLuz):.2f}"       