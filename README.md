# mygraphtools

**mygraphtools** é uma biblioteca para trabalhar com grafos
de forma rápida e fácil escrita em Python.

## Instalação
```sh
pip install mygraphtools
```

## Criando um grafo
Importamos a class Graph da nossa biblioteca
```sh 
 from mygraphtools import Graph 
``` 
Criamos uma instância, repare que é necessário informar se o grafo é: [Dirigido](https://pt.wikipedia.org/wiki/Grafo_orientado), [Ponderado](https://pt.wikipedia.org/wiki/Grafo_valorado#:~:text=Um%20grafo%20valorado%20ou%20grafo,arestas%20a%20conjunto%20de%20n%C3%BAmeros.) e [Conexo](https://www.pucsp.br/~jarakaki/grafos/Aula4.pdf)
```sh
myGraph = Graph(directed=False, weighted=True, connected=True)
``` 
## Atributos
Um objeto da classe `Graph()` possuirá os seguintes atributos públicos:

| Atributo | Descrição |
| ------ | ------ |
| weighted | Atributo booleano que indica se o grafo é ponderado |
| directed | Atributo booleano que indica se o grafo é dirigido |
| connected | Atributo booleano que indica se o grafo é conexo |
| edges | Lista das arestas do grafo |
| vertices | Lista dos vértices |

Para acessar o atributo, use `Object.attribute`

## Métodos
Com um grafo criado podemos usar algumns métodos para manipulá-lo:

* `addedge()` - Método usado para adicionar arestas ao seu grafo e por consequência os vértices também, os parâmetros são: no mínimo dois vértices e o custo relacionado à aresta em casos de grafos ponderados
    * Criando uma aresta entre os vértices 0 e 1:
        ```sh
        myGraph.addedge(0, 1)
        ```
    * Criando uma aresta entre os vértices 0 e 1 com custo 10    
        ```sh
        myGraph.addedge(0, 1, 10)
        ```
 
* `cost()` - Método que retorna o custo total do grafo, obviamente para grafos ponderados
    ```sh    
    cost = myGraph.cost()
    ```
* `numedges()` - Método que retorna o número de arestas do grafo
    ```sh   
    edges = myGraph.numedges()  
    ```

* `numvertices()` - Método que retorna o número de vértices do grafo
    ```sh
    vertices = myGraph.numvertices()
    ```
* `degree(vertex)` - Método que recebe um vértice V e retorna o [grau](https://pt.wikipedia.org/wiki/Grau_(teoria_dos_grafos)) de V
    ```sh
    degree = myGraph.degree(0)
    ```

* `adjacentvertices(vertex)` - Método que recebe um vértice V e retorna uma lista de todos os vértices que são [adjacentes](https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/graphs.html#neighbour) a V
    ```sh
    adjacencyList = myGraph.adjacentvertices(0)
    ```
* `adjacentedges` - Método que recebe um vértice V e retorna uma lista com as arestas que formam o leque de saída de V, isto é, as arestas que ligam V a seus adjacentes.
    ```sh
    adjacencyList = myGraph.adjacentedges(0)
    ```
## Algoritmos da Teoria de Grafos
Com os métodos e atributos descritos acima, é possível modelar um grafo para implementar alguns algoritmos com mais facilidade, mas para quem necessita de agilidade temos os algoritmos implementados na nossa classe.

* #### Árvore Geradora Mínima (Minimum Spanning Tree)
    Para calcular a [Minimum Spanning Tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree) (MST) do seu grafo, basta fazer uma chamada do método `calculatemst()`, que retorna uma lista com as arestas que formam a MST.

    ```sh
    mst = myGraph.calculatemst()
    ```
    Grafos ponderados possuem os atributos `myGraph.mst` e `myGraph.mstcost` que representam respectivamente as arestas que formam a MST e o custo da mesma.