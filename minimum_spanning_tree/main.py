

from typing import List, Tuple
import heapq

# notice that, the tree class doesn't store the value of edges
class TreeNode:
    def __init__(self, val, children: List['TreeNode'] = None):
        self.val = val
        self.children: List[TreeNode] = []

# simple implement of Prim Algorithm
# data structure:
# hashtable, binary heap
class PrimGraph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n: int = n
        self.d: List[List[Tuple[int, int]]] = [[] for _ in range(n)]

        for a, b, w in edges:
            self.d[a].append((b, w))
            self.d[b].append((a, w))

        self.mst = None
        self.total_cost = -1

    # time complexity: O(n**2) worst
    # space complexity: O(n**2) worst
    def precalculate(self) -> None:

        # start with any node
        # for example, start with node 0
        # tuple content: (w, a, b)
        #             cost node-a node-b
        touched_edges: List[Tuple[int, int, int]] = [(w, 0, b) for b, w in self.d[0]]
        heapq.heapify(touched_edges)

        nodes = [TreeNode(i) for i in range(self.n)]
        connected = set()
        total_cost = 0

        for _ in range(self.n-1):
            while touched_edges:
                # cost node-a node-b
                w, a, b = heapq.heappop(touched_edges)
                if a not in connected and b not in connected:
                    #
                    nodes[a].children.append(nodes[b])
                    for b_, w_ in self.d[b]:
                        # do not add the edge that was connected yet
                        if b_ == a:
                            continue
                        heapq.heappush(touched_edges, (w_, b, b_))
                    total_cost += w
                    break
            else:
                raise Exception('No any more node can be connected')

        # restore in cache
        self.total_cost = total_cost
        self.mst = nodes[0]

    def get_minimum_spanning_tree(self) -> int:
        if self.mst:
            return self.mst

        self.precalculate()
        return self.mst

    def get_minimum_spanning_tree_cost(self) -> int:
        if self.mst:
            return self.total_cost

        self.precalculate()
        return self.total_cost


# simple implement of Kruskal Algorithm
# data structure:
# hashtable, binary heap
class KruskalGraph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n: int = n
        self.d: List[Tuple[int, int, int]] = [(w, a, b) for a, b, w in edges]
        heapq.heapify(self.d)

        self.mst = None
        self.total_cost = -1

    def precalculate(self) -> None:

        d = self.d.copy()
        nodes = [TreeNode(i) for i in range(self.n)]
        groups = [-1 for _ in range(self.n)]
        group_idx = 0
        cnt = 1
        total_cost = 0
        used_as_child = set()

        while cnt < self.n:   # need n-1 times connection
            if heapq:
                w, a, b = heapq.heappop(d)
            else:
                raise Exception('No any more node can be connected')

            if groups[a] == groups[b]:
                if groups[a] == -1:
                    groups[a] = groups[b] = group_idx
                    group_idx += 1
                    nodes[a].children.append(nodes[b])
                    used_as_child.add(b)
                else:
                    continue # if two node in the same group, then do not add new connection

            elif groups[a] == -1 and groups[b] != -1:
                groups[a] = groups[b]
                nodes[a].children.append(nodes[b])
                used_as_child.add(b)

            elif groups[a] != -1 and groups[b] == -1:
                groups[b] = groups[a]
                nodes[b].children.append(nodes[a])
                used_as_child.add(a)

            else:
                for i in range(self.n):
                    if groups[i] == groups[b]:
                        groups[i] = groups[a]
                nodes[a].children.append(nodes[b])
                used_as_child.add(b)

            total_cost += w
            cnt += 1

        # get the root of tree
        self.mst = nodes[set([i for i in range(self.n)]).difference(used_as_child).pop()]
        self.total_cost = total_cost


    def get_minimum_spanning_tree(self) -> int:
        if self.mst:
            return self.mst

        self.precalculate()
        return self.mst

    def get_minimum_spanning_tree_cost(self) -> int:
        if self.mst:
            return self.total_cost

        self.precalculate()
        return self.total_cost


def test1() -> None:
    n = 4
    edges = [[0, 1, 2], [1, 3, 4], [3, 0, 3], [0, 2, 5], [1, 2, 1]]
    fg = PrimGraph(n, edges)
    fg.precalculate()

    a = fg.get_minimum_spanning_tree()
    print(a)

    b = fg.get_minimum_spanning_tree_cost()
    print(b)

    edges = [[0, 1, 4], [1, 3, 4], [3, 0, 2], [0, 2, 5], [1, 2, 1]]
    fg = KruskalGraph(n, edges)
    fg.precalculate()

    a = fg.get_minimum_spanning_tree()
    print(a)

    b = fg.get_minimum_spanning_tree_cost()
    print(b)



def main() -> None:
    test1()

if __name__ == '__main__':
    main()

