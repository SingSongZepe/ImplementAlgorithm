

from typing import List
from collections import deque

# notice that the graph are surely guaranteed to be that, there is no loop in the graph
# like
#    0  ----> 1
#    ^        |
#    |        |
#    |        V
#    3 <----- 2
# no such loop in graph
class DirectedGraphForTopoSort:
    # n is the count of nodes, if you don't want to explicitly give, there is a function to calculate it
    # root is the one or more node (normally, a graph has only one root) that its in-degree is 0
    # edges is the List of edges, format of edge is [f, t], where f is from_node, t is to_node
    def __init__(self, n: int, edges: List[List[int]], root: List[int] = None):
        self.n = n
        self.d: List[List[int]] = [[] for _ in range(n)]
        self.in_degrees: List[int] = [0] * n
        for f, t in edges:
            self.d[f].append(t)
            self.in_degrees[t] += 1

        # if root is not explicitly given
        if not root:
            self.roots = [i for i, degree in enumerate(self.in_degrees) if degree == 0]
        else:
            self.roots = root

    # get any result of topological sorting
    # so just use self.root[0] as root
    # use dfs to implement it
    def any_topological_sort(self) -> List[int]:
        
        visited = [False] * self.n
        res = []
        
        def dfs(curr_in_degree):
            for i, d in enumerate(curr_in_degree):
                if d == 0 and not visited[i]:
                    visited[i] = True
                    res.append(i)

                    for nd in self.d[i]:
                        curr_in_degree[nd] -= 1

                    dfs(curr_in_degree)
                    break

        dfs(self.in_degrees[:])
        return res

    # implement by bfs
    def any_topological_sort_bfs(self) -> list[int]:
        in_degrees = self.in_degrees[:]
        queue = deque([i for i, degree in enumerate(in_degrees) if degree == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for t in self.d[node]:
                in_degrees[t] -= 1
                if in_degrees[t] == 0:
                    queue.append(t)

        if len(result) != self.n:
            return []

        return result

    # get all topological sorts
    # use dfs to implement it
    def all_topological_sorts(self) -> List[List[int]]:
        all_sorts = []
        visited = [False] * self.n
        
        #        path
        def dfs(curr_sort, curr_in_degrees):
            if len(curr_sort) == self.n:
                all_sorts.append(curr_sort.copy())
                return

            zeros_in_degree = [i for i, degree in enumerate(curr_in_degrees) if degree == 0 and not visited[i]]
            for nd in zeros_in_degree:
                visited[nd] = True
                next_in_degrees = curr_in_degrees[:]
                
                curr_sort.append(nd)
                for t in self.d[nd]:
                    next_in_degrees[t] -= 1
                    
                dfs(curr_sort, next_in_degrees)
                
                curr_sort.pop()
                visited[nd] = False

        dfs([], self.in_degrees[:])
        return all_sorts


#
def test1() -> None:
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [0, 2], [0, 4], [4, 3]]
    root = [0]

    dgts = DirectedGraphForTopoSort(n, edges)  # if root not given it will be auto-calculated
    any_res = dgts.any_topological_sort()
    print(any_res)

    all_res = dgts.all_topological_sorts()
    print(all_res)

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [0, 2], [4, 2], [4, 3]]

    dgts = DirectedGraphForTopoSort(n, edges)  # if root not given it will be auto-calculated
    any_res = dgts.any_topological_sort()
    print(any_res)

    all_res = dgts.all_topological_sorts()
    print(all_res)

    any_res_bfs = dgts.any_topological_sort_bfs()
    print(any_res_bfs)


def main() -> None:
    test1()

if __name__ == '__main__':
    main()

