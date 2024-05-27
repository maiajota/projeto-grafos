#Importar biblioteca
from collections import defaultdict

class Grafo:
    #Inicializar o grafo
    def __init__(self):
        self.grafo = defaultdict(list)

    #Adicionar uma aresta de 'u' para 'v'
    def adicionarAresta(self, u, v):
        self.grafo[u].append(v)

    #Criar função auxiliar para visitar todos os vértices adjacentes
    def travessiaProfundidade(self, v, visitado, pilha):
        visitado[v] = True

        for i in self.grafo[v]:
            if not visitado[i]:
                self.travessiaProfundidade(i, visitado, pilha)
        
        #Adiciona o vértice à pilha
        pilha.append(v)

    #Marca os vértices como não visitados
    def ordenacaoTopologica(self):
        visitado = [False] * len(self.grafo)
        
        #Criar pilha vazia
        pilha = []

        #Percorre todos os vértices do grafo
        for i in range(len(self.grafo)):
            if not visitado[i]:
                self.travessiaProfundidade(i, visitado, pilha)

        #Retornar a ordem reversa da pilha
        return pilha[::-1]

#Exemplo de uso
grafo = Grafo()
grafo.adicionarAresta(0, 1)
grafo.adicionarAresta(0, 2)
grafo.adicionarAresta(1, 3)
grafo.adicionarAresta(2, 3)
grafo.adicionarAresta(3, 4)

print("Ordenação topológica do grafo:")
print(grafo.ordenacaoTopologica())
