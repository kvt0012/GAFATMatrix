import numpy as np
from GAFATMatrix import FAT
import GAInit as GA
import GAFATMatrix as GAM
import loopLable as loop
import math as Math
import random
n = 20  # size of individual (chromosome)
m = 10  # size of population
n_generations = 100 # number of generations
n_epoch= 500
MUTATION_PROBABILITY = 0.25
NUMBER_BEST_AGAIN_LIMIT = 20
# để vẽ biểu đồ quá trình tối ưu
# fitnesses = []
# def compute_fitness(individual):
#     return sum(gen for gen in individual)
fats = []
def create_individual():
    # print([generate_random_value() for _ in range(n)])
    # return [generate_random_value() for _ in range(n)]
    print(np.random.randint(2, size=(4, 4)) )
    print("~~~~~~~~~~~~~~~~~")
    return np.random.randint(2, size=(4, 4))
for i in range(0,n_generations):
    temp = np.random.randint(2, size=(4, 4))
    fatMatrix = FAT(temp)
    fats.append(fatMatrix)
    # print(fatMatrix.fitnessScore)
def run():

    bestFatScore = fats[0].fitnessScore
    countFat = 0
    epoch = 0
    while epoch < n_epoch:
        i=0
        while i < n_generations/4:
            motherIndex = Math.floor(random.random() * (n_generations/ 2 - 1))
            fatherIndex = Math.floor(random.random() * (n_generations / 2 - 1))
            [offspring1, offspring2] = fats[motherIndex].mate(fats[fatherIndex])
            offspring1 = FAT(offspring1)
            offspring2 = FAT(offspring2)
            if (random.random() < MUTATION_PROBABILITY):
                offspring1.mutate_swap()
            if (random.random() < MUTATION_PROBABILITY):
                offspring2.mutate_swap()
            fats.append(offspring1)
            fats.append(offspring2)
            fats.sort()
            print("lan thu",epoch+1)
            if bestFatScore == fats[0].fitnessScore:
                countFat +=1
                if (countFat ==NUMBER_BEST_AGAIN_LIMIT):
                    print("~~~~~~~~~~~~~~~~~~~~~~")
                    return
                else:
                    bestFatScore = fats[0].fitnessScore
                    countFat = 0
            i += 1
            epoch += 1

        print("THE BEST CHOICE: \n ", fats[0].FAT)
        print("The fitness score", fats[0].fitnessScore)




run()
# matplotlib.pyplot.figure()
#         matplotlib.pyplot.plot(self.best_solutions_fitness)
#         matplotlib.pyplot.title(title)
#         matplotlib.pyplot.xlabel(xlabel)
#         matplotlib.pyplot.ylabel(ylabel)
#         matplotlib.pyplot.show()
def crossover(individual1, individual2, crossover_rate=0.9):
    individual1_new = individual1.copy()
    individual2_new = individual2.copy()

    for i in range(n):
        if random.random() < crossover_rate:
            individual1_new[i] = individual2[i]
            individual2_new[i] = individual1[i]

    return individual1_new, individual2_new


def mutate(individual, mutation_rate=0.05):
    individual_m = individual.copy()

    for i in range(n):
        if random.random() < mutation_rate:
            individual_m[i] = np.random.randint(2, size=(4, 4))

    return individual_m


def selection(sorted_old_population):
    index1 = random.randint(0, m - 1)
    while True:
        index2 = random.randint(0, m - 1)
        if (index2 != index1):
            break

    individual_s = sorted_old_population[index1]
    if index2 > index1:
        individual_s = sorted_old_population[index2]

    return individual_s


def create_new_population(old_population, elitism=2, gen=1):
    sorted_population = sorted(old_population, key=GA.evaluteFAT())

    # if gen % 1 == 0:
    #     # fitnesses.append(compute_fitness(sorted_population[m - 1]))
    #     # print("BEST:", compute_fitness(sorted_population[m - 1]))

    new_population = []
    while len(new_population) < m - elitism:
        # selection
        individual_s1 = selection(sorted_population)
        individual_s2 = selection(sorted_population)  # duplication

        # crossover
        individual_c1, individual_c2 = crossover(individual_s1, individual_s2)

        # mutation
        individual_m1 = mutate(individual_c1)
        individual_m2 = mutate(individual_c2)

        new_population.append(individual_m1)
        new_population.append(individual_m2)

    for ind in sorted_population[m - elitism:]:
        new_population.append(ind.copy())

    return new_population

