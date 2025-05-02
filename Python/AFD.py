from enum import Enum

tipo_estado = Enum('tipo_estado', 'INICIAL FINAL INICIAL_FINAL COMUM')

class tipo_estado(Enum):
    INICIAL = 1
    FINAL = 2
    INICIAL_FINAL = 3
    COMUM = 4

class estado:
    def __init__(self, tipo:tipo_estado, id, transicao:dict):
        self.tipo = tipo
        self.id = id
        self.transicao = transicao

class AFD:
    def __init__(self, alfabeto):
        print(__name__)
        self.estados = []
        self.alfabeto = alfabeto
        self.estado_inicial = None

    def cria_estado(self, id, tipo, transicao):
        if tipo == tipo_estado.INICIAL or tipo == tipo_estado.INICIAL_FINAL:
                self.estado_inicial = estado(tipo, id, transicao)
                self.estados.append(self.estado_inicial)
        else:
            self.estados.append(estado(tipo, id, transicao))

    def busca_estado(self, id):
        for i in range(len(self.estados)):
            if self.estados[i].id == id:
                return i
        return -1
    
    def leitura(self, cadeia):
        estado_atual = self.estado_inicial
        for simbolo in cadeia:
            if not simbolo in self.alfabeto:
                print(f"Simbolo {simbolo} não pertence ao alfabeto")
                return False, estado_atual
            if simbolo in estado_atual.transicao:
                indice = self.busca_estado(estado_atual.transicao[simbolo])
                if indice != -1:
                    estado_atual = self.estados[indice]
                else:
                    print(f"Estado {estado_atual.transicao[simbolo]} não encontrado")
                    return False, estado_atual
            else:
                print(f"Simbolo {simbolo} não tem transição definida no estado {estado_atual.id}")
                return False, estado_atual
        if estado_atual.tipo == tipo_estado.FINAL or estado_atual.tipo == tipo_estado.INICIAL_FINAL:
            return True, estado_atual
        return False, estado_atual