

from typing import List, Tuple, Dict
from collections import deque, defaultdict

# Notice that, network can't be any loop between its nodes
class AOENetwork:
    def __init__(self, n: int, activity_lasting: List[List[int]], start_event: int = -1, end_event: int = -1):
        self.n = n
        self.al = activity_lasting

        #                            et  tm   ->   event_from time
        self.topo_edges: List[List[Tuple[int, int]]]     = [[] for _ in range(n)]
        self.rev_topo_edges: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        self.in_degrees: List[int]                       = [0] * n
        self.out_degrees: List[int]                      = [0] * n

        for ef, et, tm in activity_lasting:
            self.topo_edges[ef].append((et, tm))
            self.rev_topo_edges[et].append((ef, tm))
            self.in_degrees[et] += 1
            self.out_degrees[ef] += 1

        if start_event == -1:
            for i in range(n):
                if self.in_degrees[i] == 0:
                    self.s = i
                    break
            else:
                raise Exception('Can\'t find a node that has zero in-degree as the start event')
        else:
            self.s = start_event

        if end_event == -1:
            for i in range(n):
                if self.out_degrees[i] == 0:
                    self.e = i
                    break
            else:
                raise Exception('Can\'t find a node that has zero out-degree as the end event')
        else:
            self.s = end_event

        # vertex early -> event early -> the most early that you can start this event
        # ve is calculated by topological order of network
        self.ve = [0] * n

        self.fill_in_ve()
        # vertex last  -> event last  -> the most last that you must complete the event
        # vl is calculated by reversed-topological order of network
        # update new vl
        self.vl = [-1] * n
        for i in range(self.n):
            self.vl[i] = self.ve[self.e]

        self.fill_in_vl()


        # calculate e, l
        # where e represents the most early that the activity should be started to do
        # where l represents the most last that the activity should be completely done
        self.es = [0] * len(self.al)
        self.ls = [0] * len(self.al)
        self.fill_in_e()
        self.fill_in_l()


        # then find the key path
        # since both the key path can be more than one
        # so we need use a List[List[int]] to store it
        self.key_paths = []
        self.find_the_key_path()

    # use bfs to implement
    def fill_in_ve(self) -> None:

        # start with self.s -> start event
        dq = deque([self.s])
        in_degrees = self.in_degrees

        while dq:
            for _ in range(len(dq)):
                nd = dq.popleft()
                # process all its sub-node -> other events
                for et, tm in self.topo_edges[nd]:
                    # fill in its sub-node's ve
                    self.ve[et] = max(self.ve[et], self.ve[nd] + tm)
                    # remove this connection for topological ordering
                    in_degrees[et] -= 1
                    if in_degrees[et] == 0:
                        dq.append(et)

    # use bfs to implement
    def fill_in_vl(self) -> None:

        dq = deque([self.e])
        out_degrees = self.out_degrees

        while dq:
            for _ in range(len(dq)):
                nd = dq.popleft()

                for ef, tm in self.rev_topo_edges[nd]:
                    self.vl[ef] = min(self.vl[ef], self.vl[nd]-tm)
                    out_degrees[ef] -= 1
                    if out_degrees[ef] == 0:
                        dq.append(ef)

    def fill_in_e(self) -> None:
        for i, (ef, _, _) in enumerate(self.al):
            self.es[i] = self.ve[ef]

    def fill_in_l(self) -> None:
        for i, (_, et, tm) in enumerate(self.al):
            self.ls[i] = self.vl[et] - tm

    def find_the_key_path(self) -> None:
        non_delay_path = []
        for i, (e, l) in enumerate(zip(self.es, self.ls)):
            if e == l:
                non_delay_path.append(self.al[i])

        edge_dict: Dict[int, List] = defaultdict(list)
        for ef, et, _ in non_delay_path:
            edge_dict[ef].append(et)

        def _search(curr: int, curr_path: List[int]) -> None:
            if curr == self.e:
                self.key_paths.append(curr_path + [curr])
                return

            if curr in edge_dict:
                curr_path.append(curr)
                for nxt in edge_dict[curr]:
                    _search(nxt, curr_path)
                curr_path.pop()

        _search(self.s, [])



def test1() -> None:
    n = 6
    activity_lasting = [[0, 1, 2], [0, 2, 5], [1, 2, 1], [1, 3, 3], [2, 3, 3], [2, 5, 1], [2, 4, 4], [3, 4, 1], [4, 5, 1], [3, 5, 4]]
    aoen = AOENetwork(n, activity_lasting)
    print(aoen.ve)
    print(aoen.vl)
    print(aoen.es)
    print(aoen.ls)

def test2() -> None:
    n = 6
    activity_lasting = [[0, 1, 2], [0, 2, 5], [1, 2, 1], [1, 3, 3], [2, 3, 3], [2, 5, 1], [2, 4, 4], [3, 4, 1], [4, 5, 3], [3, 5, 4]]
    aoen = AOENetwork(n, activity_lasting)
    print(aoen.ve)
    print(aoen.vl)
    print(aoen.es)
    print(aoen.ls)

def main() -> None:
    test1()
    print()
    test2()

if __name__ == '__main__':
    main()
