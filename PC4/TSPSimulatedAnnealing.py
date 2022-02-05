import numpy
import matplotlib.pyplot as plt

cost_matrix = []


class Coordinate:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    @staticmethod
    def get_distance(a, b):
        # return numpy.sqrt(numpy.abs(a.x-b.x)+numpy.abs(a.y-b.y))
        return cost_matrix[a.label][b.label]

    @staticmethod
    def get_total_distance(coords):
        dist = 0
        for first, second in zip(coords[:-1], coords[1:]):
            dist += Coordinate.get_distance(first, second)
        dist += Coordinate.get_distance(coords[0], coords[-1])
        return dist


if __name__ == '__main__':
    # Crearemos las coordenadas
    coords = []
    for i in range(10):
        coords.append(Coordinate(numpy.random.uniform(),
                      numpy.random.uniform(), i))

    cost_matrix = numpy.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            if(i <= j):
                p = numpy.random.uniform()
                if(p > 0.2):
                    cost_matrix[i][j] = numpy.random.uniform()*50
                else:
                    cost_matrix[i][j] = numpy.inf
            else:
                cost_matrix[i][j] = cost_matrix[j][i]

    # graficos
    fig = plt.figure(figsize=(10, 10))
    gs = fig.add_gridspec(2, 2)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])
    costx = []
    costy = []
    tempx = []
    tempy = []
    probx = []
    proby = []

    # Simulated annealing algorithm
    cost0 = Coordinate.get_total_distance(coords)
    T = 1000.0  # Temperatura inicial
    factor = 0.99  # factor de decrecimiento

    for i in range(700):
        # graficando
        costx.append(i)
        costy.append(cost0)
        tempx.append(i)
        tempy.append(T)
        # actualizando grafico solucion
        ax1.cla()
        ax1.set_title('Ruta {}'.format(i+1))
        for first, second in zip(coords[:-1], coords[1:]):
            ax1.plot([first.x, second.x], [first.y, second.y], 'b')
        ax1.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
        for c in coords:
            ax1.plot(c.x, c.y, 'ro')
            ax1.annotate(c.label,(c.x, c.y))
        ax1.axis([0, 1, 0, 1])
        # actualizando grafico del costo
        ax2.cla()
        ax2.plot(costx, costy)
        ax2.set_title('Distancia total (costo)')
        ax2.set_xlabel('iteracion')
        ax2.set_ylabel('Distancia')
        ax2.text(400, 350, r'Costo = {:4f}'.format(cost0))
        ax2.axis([0, 700, 0, 400])
        # actualizando grafico de la temperatura
        ax4.cla()
        ax4.plot(tempx, tempy)
        ax4.set_title('Temperatura')
        ax4.set_xlabel('iteracion')
        ax4.set_ylabel('Temperatura')
        ax4.text(250, 700, r'Temperatura = {:4f}'.format(T))
        ax4.axis([0, 700, 0, 1000])
        p = 1
        t_p = 1

        for j in range(150):
            # Generando una nueva solución
            c1, c2 = numpy.random.randint(0, len(coords), size=2)
            while(True):
                temp = coords[c1]
                coords[c1] = coords[c2]
                coords[c2] = temp

                # Calculando el nuevo costo
                cost1 = Coordinate.get_total_distance(coords)
                if(cost1 < numpy.inf):
                    break
                else:
                    temp = coords[c1]
                    coords[c1] = coords[c2]
                    coords[c2] = temp
                    c1, c2 = numpy.random.randint(0, len(coords), size=2)

            if cost1 < cost0:
                cost0 = cost1
            else:
                r = numpy.random.uniform()
                p = numpy.exp((cost0-cost1)/T)
                if r < p:
                    cost0 = cost1
                    t_p = p
                else:
                    temp = coords[c1]
                    coords[c1] = coords[c2]
                    coords[c2] = temp
        T = T*factor

        probx.append(i)
        proby.append(t_p)
        # actualizando grafico de probabilidad de aceptacion
        ax3.cla()
        ax3.plot(probx, proby, ls=' ', marker='.', alpha=0.3)
        ax3.set_title('Probabilidad de aceptación')
        ax3.set_xlabel('iteracion')
        ax3.set_ylabel('Probabilidad de aceptación')
        ax3.axis([0, 700, 0, 1])
        plt.draw()
        plt.pause(0.015)

    for cord in coords:
        print(cord.label, end=" ,")
    plt.show()
