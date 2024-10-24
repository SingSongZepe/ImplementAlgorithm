

from typing import List
from collections import deque

class GraphForTraverse:
    # n is count of nodes, root is the node for traversing
    # if root is absent, then we need to calculate, which node our traversal starts with, we can traverse all node
    def __init__(self, n: int, edges: List[List[int]], directly: bool = True,  root: int = -1):
        self.n = n
        self.d = [[] for _ in range(self.n)]

        if directly:
            for f, t in edges:
                self.d[f].append(t)
        else:
            for f, t in edges:
                self.d[f].append(t)
                self.d[t].append(f)

        if not directly:
            root = 0

        if root == -1:
            self.root = self.search_root()
        else:
            self.root = root

    # even sometimes that starts with any node, you can't traverse all node
    # but this function will find the node that starts with we can traverse nodes as many as possible
    def search_root(self) -> int:
        max_included = 0
        max_included_i = -1

        visited = set()

        def dfs(curr: int) -> int:
            included = 0
            for t in self.d[curr]:
                included += dfs(t)

            return included + 1

        # test all node as start node
        for i in range(self.n):
            visited.clear()
            cincluded = dfs(i)

            if cincluded > max_included:
                max_included = cincluded
                max_included_i = i

            if cincluded == self.n:
                return max_included_i

        return max_included_i

    # depth first search, for short DFS
    def traverse_DFS(self):

        visited = set()

        def dfs(curr: int):
            # functional expression
            print(f'{curr}->', end='')

            for t in self.d[curr]:
                if t not in visited:
                    visited.add(t)
                    dfs(t)

        return dfs(self.root)

    # breadth first search, for short BFS
    def traverse_BFS(self):

        visited = set()

        dq = deque([self.root])

        while dq:

            for _ in range(len(dq)):
                curr = dq.popleft()

                # functional expression
                print(f'{curr}->', end='')

                for t in self.d[curr]:
                    if t not in visited:
                        dq.append(t)

                visited.add(curr)


def test1() -> None:

    # direct-graph
    n = 5
    edges = [[0, 1], [0, 3], [3, 2], [2, 1], [2, 4], [1, 4]]
    gft = GraphForTraverse(n, edges, True, 0)
    gft.traverse_DFS()
    print()
    gft.traverse_BFS()
    print()

    # direct-graph
    n = 5
    edges = [[0, 1], [0, 3], [3, 2], [2, 1], [2, 4], [1, 4]]
    gft_1 = GraphForTraverse(n, edges)
    print()
    
    # indirect-graph
    dgft = GraphForTraverse(n, edges, False)
    dgft.traverse_BFS()
    print()
    dgft.traverse_DFS()
    print()


def main() -> None:
    test1()

if __name__ == '__main__':
    main()
