
from typing import List

class FloydGraph:
    def __init__(self, n: int, edges: List[List[int]], disable_precalculate: bool = False):
        self.n = n
        self.d = [[float('inf')] * n for _ in range(n)]
        self.disable_precalculate = disable_precalculate

        # all value in diagonal set to 0
        for i in range(n):
            self.d[i][i] = 0

        # get adjacent matrix
        for f, t, w in edges:
            self.d[f][t] = w

        self.cd = None
        self.cp = None

        if not self.disable_precalculate:
            self.precalculate()

    # time complexity: O(1)
    # space complexity: O(1)
    # receive a 3-length array
    def add_edge(self, edge: List[int]) -> bool:
        f, t, w = edge
        if f == t:
            print('add a self-reference path has no sense')
            return False

        if f >= self.n or t >= self.n:
            raise Exception('node can\'t larger or equal than total node count n ')

        self.d[f][t] = w

        if not self.disable_precalculate:
            self.precalculate()

    # time complexity: O(1)
    # space complexity: O(1)
    # receive a 2-length array
    def remove_edge(self, edge: List[int]) -> bool:
        f, t = edge
        if f == t:
            print('add a self-reference path has no sense')
            return False

        if f >= self.n or t >= self.n:
            raise Exception('node can\'t larger or equal than total node count n ')

        self.d[f][t] = float('inf')

        if not self.disable_precalculate:
            self.precalculate()

    # utils function
    def set_ability_precalculate(self, ability: bool):
        self.disable_precalculate = ability
        print(f'set auto precalculate D and P option to {ability}')

    # time complexity: O(n**3)
    # space complexity: O(n**2)
    # if graph not change by adding or removing an edge,
    # you just need calculate once.
    # Once graph is changed, then repre-calculate
    def precalculate(self) -> None:
        # initialize adjacent matrix D and previous node P
        curr_d = self.d
        curr_p = [[-1] * self.n for _ in range(self.n)]

        for r in range(self.n):
            for c in range(self.n):
                if r == c or curr_d[r][c] == float('inf'):
                    continue
                curr_p[r][c] = r

        # update D and P for each node from 0 to n-1
        # new_d = curr_d.copy()
        for nd in range(self.n):
            for r in range(self.n):

                # the nd-th row
                if r == nd:
                    continue
                for c in range(self.n):
                    # the nd-th column and the diagonal don't need to be updated
                    if c == nd or r == c:
                        continue

                    # update
                    new_v = curr_d[r][nd] + curr_d[nd][c]
                    if new_v < curr_d[r][c]:
                        curr_d[r][c] = new_v
                        curr_p[r][c] = nd

            # store the result for later-calling
            self.cd = curr_d
            self.cp = curr_p

    # time complexity: O(1)
    # space complexity: O(1)
    # return the shortest distance if path exists
    # otherwise return -1
    def get_shortest_distance(self, f: int, t: int) -> int:
        if self.cd:
            return -1 if self.cd[f][t] == float('inf') else self.cd[f][t]

        raise Exception('haven\' pre-calculate D and P')


    # time complexity: O(n)
    # space complexity: O(n)
    # return a list representing the path from node f to node t if there is a path exists
    # otherwise return -1 representing there is no path exists
    def get_shortest_path(self, f: int, t: int) -> List[int]:
        path = [t]

        curr = t

        while curr != f and curr != -1:
            curr = self.cp[f][curr]
            path.append(curr)

        path.reverse()
        return path


# the edges don't give the weight of duplicate path [1, 0, A], [1, 0, B] (the former will be replaced by the latter one)
# the edges don't give the self-reference path list [1, 1, any]
def test1() -> None:
    n = 4
    edges = [[0, 1, 2], [1, 3, 4], [3, 0, 3], [0, 3, 3], [0, 2, 5], [1, 2, 1]]
    fg = FloydGraph(n, edges)

    d = fg.get_shortest_distance(3, 2)
    print(d)
    assert d == 6

    path = fg.get_shortest_path(3, 2)
    print(path)
    assert path == [3, 0, 1, 2]

    fg.add_edge([3, 2, 1])
    d = fg.get_shortest_distance(3, 2)
    print(d)
    assert d == 1

    fg.remove_edge([3, 2])
    d = fg.get_shortest_distance(3, 2)
    print(d)

    p = fg.get_shortest_path(3, 2)
    print(p)


def main() -> None:
    test1()

if __name__ == '__main__':
    main()

