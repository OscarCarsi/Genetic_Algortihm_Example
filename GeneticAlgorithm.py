import random;
import math;

def create_individual():
    individual = []
    for _ in range(10):
        individual.append(round(random.uniform(-5.12, 5.12), 2))
    return individual

def create_population(size):
    population = []
    for _ in range(size):
        population.append(create_individual())
    return population

def fitness(individual):
    addition = []
    for i in individual:
        addition.append((i ** 2) - (10 * math.cos(2 * math.pi * i)))
    fitness = 10 * len(individual) + sum(addition)
    return fitness

def main():
    population = create_population(2)
    for individual in population:
        print("Individual: ", individual)
        print("Fitness: ", fitness(individual))

if __name__ == "__main__":
    main()