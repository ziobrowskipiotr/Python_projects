import numpy as np
import time
import random
import multiprocessing
import matplotlib.pyplot as plt

coords = []


class Plecak:
    def __init__(swoje, height, width):
        swoje.width = int(width)
        swoje.height = int(height)
        swoje.field = np.zeros((swoje.width, swoje.height))
        swoje.value = 0

    def dodaj_rzecz(swoje, rzecz):
        rzecz_width, rzecz_height = rzecz.height, rzecz.width
        for w in range(swoje.width - rzecz_width + 1):
            if w + rzecz_width > swoje.width + 1:
                break
            for h in range(swoje.height - rzecz_height + 1):
                if h + rzecz_height > swoje.height + 1:
                    break
                if np.all(swoje.field[w: w + rzecz_width, h: h + rzecz_height] == 0):
                    swoje.field[w: w + rzecz_width, h: h + rzecz_height] = rzecz._id
                    swoje.value += rzecz.value
                    return True
        # rotation
        rzecz_width, rzecz_height = rzecz_height, rzecz_width
        for w in range(swoje.width - rzecz_width + 1):
            if w + rzecz_width > swoje.width:
                break
            for h in range(swoje.height - rzecz_height + 1):
                if h + rzecz_height > swoje.height + 1:
                    break
                if np.all(swoje.field[w: w + rzecz_width, h: h + rzecz_height] == 0):
                    swoje.field[w: w + rzecz_width, h: h + rzecz_height] = rzecz._id
                    swoje.value += rzecz.value
                    return True
        return False

    def dodaj_rzecz(swoje, rzecz):
        for rzecz in rzecz:
            swoje.dodaj_rzecz(rzecz)

    def display_Plecak(swoje):
        print(swoje.field)

    def podaj_wartość_Plecak(swoje):
        return swoje.value


class rzecz:
    def __init__(swoje, _id, width, height, value):
        swoje._id = _id
        swoje.width = int(width)
        swoje.height = int(height)
        swoje.value = int(value)
        swoje.density = swoje.value / (swoje.width * swoje.height)


def greedy_algorithm(Plecak, rzecz):
    temp_rzecz = rzecz
    temp_rzecz.sort(key=lambda rzecz: rzecz.density, reverse=True)
    for rzecz in temp_rzecz:
        Plecak.dodaj_rzecz(rzecz)


def ocena(Plecak, gene):
    if isinstance(gene[-1], int):
        return 0
    temp_Plecak = Plecak(Plecak.height, Plecak.width)
    for rzecz in gene:
        temp_Plecak.dodaj_rzecz(rzecz)
    return temp_Plecak.podaj_wartość_Plecak()


def population_algorithm(Plecak_arg, rzecz, debug=False):
    p = 100  # population size
    pc = 0.2  # elite percentage
    pm = 0.01  # mutations
    ps = 0.05  # mutation severity
    iterations = 50
    data_for_chart = []
    population = []
    counter = 0
    while counter < iterations:
        counter += 1
        # generate random population
        for i in range(p - len(population)):
            population.append((Plecak_arg, random.sample(rzecz, k=len(rzecz))))

        # multicore ocena
        pool = multiprocessing.Pool()
        result = pool.starmap(ocena, population)
        for i in range(len(population)):
            if not isinstance(population[i][1][-1], int):
                population[i][1].append(result[i])

        # sort according to perceived value 
        population.sort(key=lambda g: -g[1][-1])
        if counter == iterations:
            value = population[0][1][-1]
            data_for_chart.append(value)
            if debug:
                print(counter, value)
            del population[0][1][-1]
            return (population[0][1], value, data_for_chart)
        data_for_chart.append(population[0][1][-1])
        if debug == True:
            print(counter, population[0][1][-1])

        # breed
        for i in range(round(p - 2 * pc * p)):
            b = random.randint(0, pc * p - 1)
            c = random.randint(pc * p, p - 2)
            bc = []
            iter_b = 0
            iter_c = 0
            for j in range(len(rzecz)):
                # randomize gene mixing
                mixer = random.randint(0, 1)
                if mixer:
                    while population[b][1][iter_b] in bc:
                        iter_b += 1

                    if iter_b <= len(rzecz):
                        copy = population[b][1][iter_b]
                        bc.append(copy)
                    else:
                        copy = population[c][1][iter_c]
                        bc.append(copy)

                else:
                    while population[c][1][iter_c] in bc:
                        iter_c += 1

                    if iter_c <= len(rzecz):
                        copy = population[c][1][iter_c]
                        bc.append(copy)
                    else:
                        copy = population[b][1][iter_b]
                        bc.append(copy)

            population.append((Plecak_arg, bc))

        del population[round(pc * p):p]

        # mutate
        for i in range(round(pm * len(population))):
            # pick entity to mutate
            m = random.randint(0, len(population) - 1)
            for j in range(round(ps * len(rzecz))):
                # pick two genes to swap
                m1 = random.randint(0, len(rzecz) - 1)
                m2 = random.randint(0, len(rzecz) - 1)

                temp = population[m][1][m1]
                population[m][1][m1] = population[m][1][m2]
                population[m][1][m2] = temp
                if isinstance(population[m][1][-1], int):
                    del population[m][1][-1]


def new_function(data):
    iterations = list(range(1, 51))
    print(iterations)
    print(data)

    plt.plot(iterations, data)
    plt.xlabel("Iterations")
    plt.ylabel("Values")
    plt.title("Population Algorithm Values and Iterations Chart")
    plt.show()


if __name__ == "__main__":
    with open("./data/packages20.txt", 'r') as file:
        for line in file:
            line = line.strip().split('\n')
            coords.append(line[0].split(','))

    coords.pop(0)
    coords.pop(0)
    rzecz = []

    for cord in coords:
        rzecz.append(rzecz(cord[0], cord[1], cord[2], cord[3]))

    Plecak1 = Plecak(20, 20)

    start_time = time.time()
    greedy_algorithm(Plecak1, rzecz)
    end_time = time.time()
    print("Greedy Algorithm time to execute: " + str(end_time - start_time))
    print("Greedy Algorithm Value: " + str(Plecak1.podaj_wartość_Plecak()))
    print("Greedy Algorithm Plecak Content:")
    Plecak1.display_Plecak()

    Plecak2 = Plecak(20, 20)

    start_time = time.time()
    optimal_set_of_rzecz, value, data_for_chart = population_algorithm(Plecak2, rzecz)
    end_time = time.time()
    print("Population Algorithm time to execute: " + str(end_time - start_time))
    print("Population Algorithm Value: " + str(value))
    print("Population Algorithm Plecak Content: ")
    Plecak2.dodaj_rzecz(optimal_set_of_rzecz)
    Plecak2.display_Plecak()
    new_function(data_for_chart)

    Plecak3 = Plecak(100, 100)
    coords = []
    rzecz = []
    with open("./data/packages100.txt", 'r') as file:
        for line in file:
            line = line.strip().split('\n')
            coords.append(line[0].split(','))
    coords.pop(0)
    coords.pop(0)
    for cord in coords:
        rzecz.append(rzecz(cord[0], cord[1], cord[2], cord[3]))
    start_time = time.time()
    optimal_set_of_rzecz, value, data_for_chart = population_algorithm(Plecak3, rzecz, True)
    end_time = time.time()
    print("Population Algorithm time to execute for 100 elements: " + str(end_time - start_time))
    print("Population Algorithm Value for 100 elements: " + str(value))
    print("Population Algorithm Plecak Content for 100 elements: ")
    Plecak3.dodaj_rzecz(optimal_set_of_rzecz)
    Plecak3.display_Plecak()
    new_function(data_for_chart)