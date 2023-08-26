import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from prettytable import PrettyTable
matplotlib.use('TkAgg')


class Graph:
    def __init__(self, vertices):
        self.V = vertices

    def print_solution(self, reach):
        print("Following matrix transitive closure of the given graph:")
        for i in range(self.V):
            for j in range(self.V):
                print(reach[i][j], end=" ")
            print("\n")

    def transitive_closure(self, graph):
        reach = [i[:] for i in graph]
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
        return reach


def print_final_reachability(initial, final):
    np.matrix(final)

    for i in range(n):
        for j in range(n):
            if final[i][j] == 1 and initial[i][j] == 0:
                print('1*', end=" ")
            elif final[i][j] == 1:
                print('1', end=" ")
            else:
                print('0', end=" ")
        print("\n")


def level_partioning(final):
    common_mat = []
    for i in range(n):
        temp_reach = []
        temp_antec = []
        for j in range(n):
            if final[i][j] == 1:
                temp_reach.append(j)
            if final[j][i] == 1:
                temp_antec.append(j)
        common_mat.append(temp_reach)
        common_mat.append(temp_antec)
    return common_mat


def stop_crit(level):
    for x in level:
        if x == 0:
            return True
    return False


def x_and_y(final):
    driving_power = []
    dependence_power = []

    for i in range(n):
        count_x = 0
        count_y = 0
        for j in range(n):
            if final[i][j] == 1:
                count_x = count_x + 1
            if final[j][i] == 1:
                count_y = count_y + 1
        driving_power.append(count_x)
        dependence_power.append(count_y)
    return driving_power, dependence_power


def find_level(intersection_set, common_mat):
    levels = np.zeros(n, dtype=int)
    count = 1

    while stop_crit(levels):
        store = []
        for i in range(n):
            if len(intersection_set[i]) != 0 and set(intersection_set[i]) == set(common_mat[2 * i]):
                levels[i] = count
                store.append(i)
        count = count + 1
        for x in store:
            for i in common_mat:
                if x in i:
                    i.remove(x)
            for i in intersection_set:
                if x in i:
                    i.remove(x)
    return levels


def plot_it(driving_power, dependence_power):
    fig = plt.figure(figsize=(6, 6), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(dependence_power, driving_power)
    pts = dict()
    for i, txt in enumerate(range(n)):
        t = (dependence_power[i], driving_power[i])
        if t in pts:
            pts[t].append(txt + 1)
        else:
            pts[t] = [txt + 1]

    for i, txt in enumerate(range(n)):
        t = (dependence_power[i], driving_power[i])
        ax.annotate(pts[t], t)

    x1, y1 = [-1, n + 1], [n / 2, n / 2]
    x2, y2 = [n / 2, n / 2], [-1, n + 1]
    ax.plot(x1, y1, x2, y2)

    ax.set_xlim(0, n + 1)
    ax.set_ylim(0, n + 1)
    ax.set_xlabel('Dependence Power')
    ax.set_ylabel('Driving Power')
    ax.set_title('MICMAC Analysis')
    ax.grid()

    plt.show()


n = int(input('Dimension of your Initial Reachability matrix:'))
area = input('Name of Input file:')

graph = np.loadtxt(area, usecols=range(n))

g = Graph(n)
final = g.transitive_closure(graph)
temp = np.loadtxt(area, usecols=range(n))
print_final_reachability(temp, final)
Driving_Power, Dependence_Power = x_and_y(final)

common_mat = level_partioning(final)

intersection_set = []
for i in range(n):
    intersection_set.append(list(set(common_mat[2 * i]) & set(common_mat[2 * i + 1])))

levels = find_level(intersection_set, common_mat)

plot_it(Driving_Power, Dependence_Power)

table = PrettyTable()
table.field_names = ['Variable(Risks)', 'Levels']

for i in range(n):
    table.add_row(['Risk {}'.format(i + 1), levels[i]])

print(table)
