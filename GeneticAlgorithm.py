#Importamos random y math
import random;
import math;

#Creamos un individuo
def create_individual():
    #Creamos un individuo que es un array con 10 numeros entre -5.12 y 5.12
    individual = [round (random.uniform(-5.12, 5.12), 2) for _ in range(10)]
    return individual

#Creamos la poblacion a la cual le pasamos el tamaño de la población
def create_population(size):
    #A partir del tamaño que le pasamos creamos la población
    population = [create_individual() for _ in range(size)]
    return population

#Calculamos la aptitud de cada individuo
def fitness(individual):
    #Hacemos un array donde por cada número que hay dentro del individuo hacemos la operación f(−→x ) = 10D + ΣDi=1(x2i − 10cos(2πxi))
    addition = [(i ** 2) - (10 * math.cos(2 * math.pi * i)) for i in individual]
    #Despues de guardar los resultados, multiplicamos 10 por la longitud del individuo y sumamos los resultados de la operación anterior
    fitness = 10 * len(individual) + sum(addition)
    return round(fitness, 2)

#Seleccionamos a los individuos por ruleta
def selection_by_roulette(population):
    #Al buscar los individuos con menor aptitud, los invertimos para que los que tengan menor aptitud tengan mayor probabilidad de ser seleccionados
    fitnesses = [1/fitness(individual) for individual in population]
    #Sumamos las aptitudes
    total_fitness = sum(fitnesses)
    #Creamos una lista con las probabilidades de cada individuo, dividiendo la aptitud de cada individuo entre la aptitud total
    probabilities = [f/total_fitness for f in fitnesses]
    print("Probabilities: ", probabilities)
    #Seleccionamos a los individuos, donde le pasamos la población y las probabilidades, y seleccionamos 2 individuos
    selected = random.choices(population, probabilities, k=2)
    return selected

def main():
    population = create_population(5)
    for individual in population:
        print("Individual: ", individual)
        print("Fitness: ", fitness(individual))
    selected = selection_by_roulette(population)
    print("Selected: ", selected)

if __name__ == "__main__":
    main()