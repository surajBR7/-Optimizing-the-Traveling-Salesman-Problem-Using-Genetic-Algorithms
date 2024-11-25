# Optimizing-the-Traveling-Salesman-Problem-Using-Genetic-Algorithms
# Traveling Salesperson Problem (TSP) Solutions

This repository contains various implementations of the Traveling Salesperson Problem (TSP) using Genetic Algorithms and graph theory concepts. The TSP is a classic optimization problem where the objective is to find the shortest possible route that visits a set of cities exactly once and returns to the origin city.

---

## Contents

### 1. **Graph Implementation**
- **File:** `graph.py`
- **Description:** Implements a `Graph` class for handling vertices, edges, and adjacency relationships. Includes utilities to:
  - Add vertices and edges with weights.
  - Retrieve adjacent vertices and calculate path costs.
- **Key Features:**
  - Easy graph construction.
  - Path cost evaluation for any given route.
- **Usage Example:**
  ```python
  graph = Graph()
  graph.setAdjacent('a', 'b', 4)
  graph.setAdjacent('a', 'c', 4)
  path = 'abc'
  print(graph.getPathCost(path))
  ```
### 2. Genetic Algorithm for TSP (Version 1)
- **File:** `TSP.py`
- **Description:** Solves the TSP using a Genetic Algorithm approach, optimizing for minimal route cost.
- **Key Features:**
  - Population generation with random routes.
  - Tournament selection for parent selection.
  - Order-1 crossover for genetic recombination.
  - Mutation to introduce variation.
  - Includes elitism to preserve the best routes.
- **Usage Example:**
  ```python
  ga_tsp = GeneticAlgorithmTSP(generations=20, population_size=7, mutationRate=0.2, elitismRate=0.1)
  optimal_path, path_cost = ga_tsp.optimize(graph)
  print(f"Optimal Path: {optimal_path}, Cost: {path_cost}")
  ```
  ### 3. Genetic Algorithm for TSP (Version 2)
- **File:** `TSP1.py`
- **Description:** Another implementation of the TSP using Genetic Algorithms. This version focuses on cities with 2D coordinates and includes:
  - Distance calculations based on city coordinates.
  - Randomized initial population generation.
  - Tournament selection and mutation for optimization.
- **Key Features:**
  - Returns the shortest route and its distance.
  - Configurable parameters like mutation rate and population size.
- **Usage Example:**
  ```python
  cities = {
      "A": (100, 300),
      "B": (200, 130),
      "C": (300, 500)
  }
  ga_tsp = GeneticAlgorithmTSP(cities, population_size=50, generations=1000, mutation_rate=0.01)
  best_tour, min_distance = ga_tsp.run()
  print(f"Shortest Distance: {min_distance}, Route: {best_tour}")
  ```
  ### 4. Graph Visualization
- **File:** `graph.py`
- **Description:** Provides utilities to visualize graphs and debug TSP solutions.
- **Key Features:**
  - Can be integrated with graphical tools to visualize routes and nodes.

---

## Requirements

To run the scripts, you need the following Python libraries:
- `numpy`
- `matplotlib` (for visualization)
- `random` (standard Python library)

Install required libraries using:
```bash
pip install numpy matplotlib
```

## Usage
 Clone the repository:

```bash
git clone https://github.com/your_username/TSP_Solutions.git
```
Navigate to the directory:
```bash
cd TSP_Solutions
```
Run the scripts:

```bash
python graph.py
python TSP.py
python TSP1.py
```

## Features
- Graph Construction: Create graphs with weighted edges.
- Optimization: Find optimal TSP routes using genetic algorithms.
- Visualization: Visualize and debug routes with ease.

## Author
Suraj B Rajolad
