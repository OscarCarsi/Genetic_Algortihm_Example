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
    probabilities = [round(f/total_fitness,2) for f in fitnesses]
    #Seleccionamos a los individuos, donde le pasamos la población y las probabilidades, y seleccionamos 2 individuos
    selected = random.choices(population, probabilities, k=2)
    return selected

#Cruzamos los padres con blx_alpha
def blx_alpha_crossover(parent1, parent2, alpha=0.5):
    child1, child2 = [], [] #se crean los arrays para los hijos
    for p1, p2 in zip(parent1, parent2): #Se itera sobre los valores de cada padre
        cmin = max(min(p1, p2) - alpha * abs(p1 - p2), -5.12) #Se calcula el valor mínimo
        cmax = min(max(p1, p2) + alpha * abs(p1 - p2), 5.12) #Se calcula el valor máximo
        child1.append(round(random.uniform(cmin, cmax),2)) #Se añade un valor aleatorio entre el mínimo y el máximo al hijo 1
        child2.append(round(random.uniform(cmin, cmax),2)) #Se añade un valor aleatorio entre el mínimo y el máximo al hijo 2
    return child1, child2 

def replacement_with_elitism(population, parents, children):
    # Convierte children en una lista 
    children = list(children)
    # Combina los padres y los hijos
    combined = parents + children
    
    # Calcula la aptitud de cada individuo con los padres y los hijos
    fitnesses = [(individual, fitness(individual)) for individual in combined]

    # Ordena los individuos por aptitud en orden ascendente
    sorted_by_fitness = sorted(fitnesses, key=lambda x: x[1])

    # Selecciona los dos mejores individuos
    best_two = [individual for individual, _ in sorted_by_fitness[:2]]

    # Reemplaza los padres en la población original con los dos mejores individuos
    for i in range(len(population)):
        if population[i] in parents:
            population[i] = best_two.pop(0)
            if not best_two:
                break

    return population

def main():
    population = create_population(5)
    parents = selection_by_roulette(population)
    children = blx_alpha_crossover(parents[0], parents[1])
    new_population = replacement_with_elitism(population, parents, children)


if __name__ == "__main__":
    main()