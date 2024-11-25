import numpy as np
import random

class GeneticAlgorithmTSP:
    def __init__(self, cities, population_size=50, generations=1000, mutation_rate=0.01):
        self.cities = cities
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.city_names = list(cities.keys())
        self.population = self.initial_population()

    # Calculate the distance between two cities
    def distance(self, city1, city2):
        x1, y1 = city1
        x2, y2 = city2
        return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # Calculate the total distance of a tour
    def tour_distance(self, tour):
        total_dist = 0
        for i in range(len(tour) - 1):
            total_dist += self.distance(self.cities[tour[i]], self.cities[tour[i + 1]])
        total_dist += self.distance(self.cities[tour[-1]], self.cities[tour[0]])  # Return to starting city
        return total_dist

    # Generate an initial population of random tours
    def initial_population(self):
        population = []
        for _ in range(self.population_size):
            tour = random.sample(self.city_names, len(self.city_names))
            population.append(tour)
        return population

    # Select parents for mating using tournament selection
    def select_parents(self):
        tournament_size = 5
        parents = []
        for _ in range(self.population_size):
            tournament = random.sample(self.population, tournament_size)
            tournament.sort(key=lambda tour: self.tour_distance(tour))
            parents.append(tournament[0])
        return parents

    # Perform crossover (Order 1 crossover)
    def crossover(self, parent1, parent2):
        n = len(parent1)
        start, end = random.sample(range(n), 2)
        if start > end:
            start, end = end, start

        child = [-1] * n
        child[start:end + 1] = parent1[start:end + 1]

        remaining_cities = [city for city in parent2 if city not in child]
        child = [city if city != -1 else remaining_cities.pop(0) for city in child]

        return child

    # Mutate a tour by swapping two cities
    def mutate(self, tour):
        if random.random() < self.mutation_rate:
            idx1, idx2 = random.sample(range(len(tour)), 2)
            tour[idx1], tour[idx2] = tour[idx2], tour[idx1]

    # Run the genetic algorithm
    def run(self):
        for generation in range(self.generations):
            parents = self.select_parents()
            next_generation = []

            while len(next_generation) < self.population_size:
                parent1, parent2 = random.sample(parents, 2)
                child = self.crossover(parent1, parent2)
                self.mutate(child)
                next_generation.append(child)

            self.population = next_generation

        best_tour = min(self.population, key=self.tour_distance)
        return best_tour, self.tour_distance(best_tour)


# Define city coordinates
cities = {
    "A": (100, 300),
    "B": (200, 130),
    "C": (300, 500),
    "D": (500, 390),
    "E": (700, 300),
    "F": (900, 600),
    "G": (800, 950),
    "H": (600, 560),
    "I": (350, 550),
    "J": (270, 350)
}

# Run the optimized genetic algorithm
ga_tsp = GeneticAlgorithmTSP(cities, population_size=50, generations=1000, mutation_rate=0.01)
best_tour, min_distance = ga_tsp.run()

# Display the results
print("Shortest distance value:", min_distance)
print("Best tour:", " -> ".join(best_tour) + f" -> {best_tour[0]}")
