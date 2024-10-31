
import unittest
from typing import List
import random

from utils.value import *

# A genetic algorithm to solve a problem that named as Traveling Salesman Problem

class Genetic:
    def __init__(self, cities: List[List[int]], times: int = 100) -> None:
        self.n = len(cities)
        self.cities = cities
        self.times = times

        # optional
        self.initialization_function_type = 'random'
        self.pool_size = N

        # initialize the chromosome that represents the order of travelling
        self.chromosome_pool = self.generate_chromosome_pool()
        self.dist = self.get_distance()

    # main function
    def get_the_best_chromosome(self) -> List[int]:
        return self.chromosome_pool[0]

    def iterate(self) -> None:
        for _ in range(self.times):
            self.iterate_one_step()

    def iterate_one_step(self) -> None:

        total_chromosome_pool = []

        for _ in range(self.pool_size):
            chromosome1 = self.chromosome_pool[random.randint(0, self.n-1)]
            chromosome2 = self.chromosome_pool[random.randint(0, self.n-1)]

            new = self.cross_over(chromosome1, chromosome2)
            if random.random() < k:
                new = self.mutate(new)

            total_chromosome_pool.append(new)

        total_chromosome_pool.sort(key=lambda chromosome: self.evaluate(chromosome))

        self.chromosome_pool = total_chromosome_pool[:self.n]


    def cross_over(self, chromosome_give: List[int], chromosome_recv) -> List[int]:

        pos1 = random.randint(0, self.n-1)
        pos2 = random.randint(0, self.n-1)
        if pos1 > pos2:
            pos1, pos2 = pos2, pos1

        subchromosome = chromosome_give[pos1:pos2+1]
        st = set(subchromosome)

        new_chromosome = []
        for i in chromosome_recv:
            if i in st:
                continue
            new_chromosome.append(i)

        new_chromosome.extend(subchromosome)

        return new_chromosome


    def mutate(self, chromosome: List[int]) -> List[int]:

        pos1 = random.randint(0, self.n-1)
        pos2 = random.randint(0, self.n-1)
        if pos1 > pos2:
            pos1, pos2 = pos2, pos1

        subchromosome = chromosome[pos1:pos2+1]
        random.shuffle(subchromosome)

        new_chromosome = chromosome[:pos1] + subchromosome + chromosome[pos2+1:]
        return new_chromosome


    # pre-calculate distance of any two cities
    # we do not use square root to represent in order to save resource
    def get_distance(self) -> List[List[int]]:
        dist = [[0] * self.n for _ in range(self.n)]

        for i in range(1, self.n):
            for j in range(i):
                x1, y1 = self.cities[i]
                x2, y2 = self.cities[j]
                dist[i][j] = dist[j][i] = (x1 - x2) ** 2 + (y1 - y2) ** 2

        return dist

    def evaluate(self, chromosome: List[int]) -> int:  # fitness
        fitness = 0
        for i in range(len(chromosome)-1):
            fitness += self.dist[chromosome[i]][chromosome[i+1]]
        fitness += self.dist[chromosome[-1]][chromosome[0]]
        return fitness

    # initialize
    def generate_chromosome_pool(self) -> List[List[int]]:
        pool = []

        match self.initialization_function_type:
            case RANDOM_:
                for _ in range(self.pool_size):
                    pool.append(self.random_initialize())

        return pool

    def random_initialize(self) -> List[int]:
        r = [i for i in range(self.n)]
        random.shuffle(r)
        return r



class Test(unittest.TestCase):

    def test_cross_over(self):
        cities = [
            [4, 9],  # IV
            [6, 8],  # V
            [5, 0],  # XI
            [9, -2],  # X
            [2, 2],  # I
            [5, 6],  # VI
            [0, -5],  # XII
            [0, 4],  # II
            [9, 5],  # VIII
            [1, 7],  # III
            [8, 8],  # VII
            [10, 2],  # IX
        ]
        g = Genetic(cities)
        chromosome1 = [1, 0, 10, 4, 9, 7, 2, 8, 6, 11, 3, 5]
        chromosome2 = [3, 7, 2, 11, 0, 9, 8, 4, 6, 10, 1, 5]

        new = g.cross_over(chromosome1, chromosome2)
        print(chromosome1)
        print(chromosome2)
        print(new)


    def test_mutate(self):
        cities = [
            [4, 9],  # IV
            [6, 8],  # V
            [5, 0],  # XI
            [9, -2],  # X
            [2, 2],  # I
            [5, 6],  # VI
            [0, -5],  # XII
            [0, 4],  # II
            [9, 5],  # VIII
            [1, 7],  # III
            [8, 8],  # VII
            [10, 2],  # IX
        ]
        g = Genetic(cities)
        chromosome = [1, 0, 10, 4, 9, 7, 2, 8, 6, 11, 3, 5]

        new = g.mutate(chromosome)
        print(chromosome)
        print(new)

    def test1(self) -> None:
        cities = [
            [4, 9],  # IV
            [6, 8],  # V
            [5, 0],  # XI
            [9, -2],  # X
            [2, 2],  # I
            [5, 6],  # VI
            [0, -5],  # XII
            [0, 4],  # II
            [9, 5],  # VIII
            [1, 7],  # III
            [8, 8],  # VII
            [10, 2],  # IX
        ]
        g = Genetic(cities)
        g.iterate()

        best_chromosome = g.get_the_best_chromosome()
        best_evaluation = g.evaluate(best_chromosome)
        for i in best_chromosome:
            print(cities[i], end='->')

        print(best_evaluation)


def main() -> None:
    unittest.main()

if __name__ == '__main__':
    main()

