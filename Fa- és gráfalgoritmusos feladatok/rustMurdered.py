import os
import sys
from queue import Queue


def rustMurderer(n, roads, s):
    mellek_utak = {i: set() for i in range(1, n + 1)}
    for u, v in roads:
        mellek_utak[u].add(v)
        mellek_utak[v].add(u)

    tavolsagok = [float('inf')] * (n + 1)
    tavolsagok[s] = 0

    q = Queue()
    q.put(s)

    bejaratlan = set(range(1, n + 1))
    bejaratlan.remove(s)

    while not q.empty():
        jelenlegi = q.get()

        komplemens_utak = [node for node in list(bejaratlan) if node != jelenlegi and node  not in mellek_utak[jelenlegi]]

        for node in komplemens_utak:
            tavolsagok[node] = tavolsagok[jelenlegi] + 1
            q.put(node)
            bejaratlan.remove(node)

    return [tavolsagok[i] for i in range(1, n + 1) if tavolsagok[i] != 0 ]


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    with open('input.txt','r') as input_file, open('output.txt', 'w') as fptr:
        t = int(input_file.readline().strip())

        for t_itr in range(t):
            nm = input_file.readline().strip().split()

            n = int(nm[0])

            m = int(nm[1])

            roads = []

            for _ in range(m):
                roads.append(list(map(int, input_file.readline().strip().split())))

            s = int(input_file.readline().strip())

            result = rustMurderer(n, roads,s)

            fptr.write(' '.join(map(str, result)) + '\n')

    fptr.close()
