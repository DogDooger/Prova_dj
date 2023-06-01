class ContaLuz:
    def __init__(self,numero,numeroLeitura,valorPagar):
        self.__numero = numero
        self.__numeroLeitura = numeroLeitura
        self.__valorPagar = valorPagar
        
    def getvalorPagar(self):
        return self.__valorPagar    