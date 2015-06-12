#/usr/bin/env python

import time
import random
import math

# individuals
def individual(length, min, max):
    'Create a member of the population.'
    return [ random.uniform(min,max) for x in range(length) ]


def population(count, length, min, max):
    """
    Create count number of individuals (i.e. a population).

    count: the number of individuals in the population
    length: the number of values per individual
    min: the minimum possible value in an individual's list of values
    max: the maximum possible value in an individual's list of values

    """
    return [ individual(length, min, max) for x in range(count) ]

def fitness(individual, target):
    """
    Determine the fitness of an individual. Closer is better.

    individual: the individual to evaluate
    target: the target number individuals are aiming for
    """
    sum = individual[0]*target[0]*1. + individual[1]*target[1]*1.
    t = (target[0]+target[1])*1.0
    return abs(t-sum)

def evolve(pop, target, retain=0.4, random_select=0.1, mutate=0.1):
    #for member in pop:
    #    print("[%2.2f, %2.2f]" % (member[0],member[1]))
    #print("  ")
    graded = [ (fitness(x, target), x) for x in pop]
    graded = [ x[1] for x in sorted(graded)]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]
    #for member in graded:
    #    print("[%2.2f, %2.2f]" % (member[0],member[1]))
    #print("  ")
    #print("  ")
    #print("  ")
    #print("  ")
    # randomly add other individuals to
    # promote genetic diversity
    for individual in graded[retain_length:]:
        if random_select > random.uniform(0,1):
            parents.append(individual)
    # mutate some individuals
    for individual in parents:
        if mutate > random.uniform(0,1):
            pos_to_mutate = random.randint(0, len(individual)-1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = random.uniform(0,1.1)
    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = random.randint(0, parents_length-1)
        female = random.randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = int(len(male) / 2)
            if random.randint(0, 2)>1:
                child = male[:half] + female[half:]
            else:
                child = female[:half] + male[half:]
            children.append(child)
    parents.extend(children)
    return parents

# Genetics algoritm
target = 0
p_count = 10
i_length = 2
i_min = 0
i_max = 1.1
# Create the population
p = population(p_count, i_length, i_min, i_max)

# Neural networks
activation=0
# Create random weights
inWeight=[random.uniform(0, 1), random.uniform(0, 1), .99]
#inWeight=[0.0, 0.0, 1]

# Start neuron with no stimuli
inNeuron=[0.0, 0.0]

# Calculate response from neural input
def outNeuron():
        global inNeuron, inWeight, activation
        # compute the activation and return the output
        # activation funtion is a step function
        activation=inNeuron[0]*inWeight[0] + inNeuron[1]*inWeight[1]
        if activation>inWeight[2]:
            return (1/(1+math.exp(-activation)))
            #return 1.0
        else:
            return 0.0

# Display results of test
def display(out, real):
    global inNeuron, inWeight, activation,p
    print("[ %2.2f %2.2f ] - %1.1f/%1.1f - [ %2.2f %2.2f ] -- W = [ %2.2f %2.2f ] p_length %i [ %2.2f %2.2f ]/[ %2.2f %2.2f ]" % (inNeuron[0],inNeuron[1], out,round(out),real[0],real[1],inWeight[0],inWeight[1],len(p), p[0][0],p[0][1],p[9][0],p[9][1] ))

while 1:
        # Loop through each lesson in the learning table
        # Stimulate neurons with test input
        inNeuron[0]=random.uniform(0, 1)
        inNeuron[1]=random.uniform(0, 1)
        target=[round(inNeuron[0]),round(inNeuron[1])]
        # Find weight based on genetic algorithm
        # Use 50 generations
        for j in range(100):
            p = evolve(p, target)
        p = [ (fitness(x, target), x) for x in p]
        p = [ x[1] for x in sorted(p)]
        inWeight[0]=p[0][0]
        inWeight[1]=p[0][1]
        out = outNeuron()
        display(out, target)
        # Adjust weight of neuron #2
        # based on feedback, then display
        #out = outNeuron()
        #inWeight[1]+=rate*(test[i][2]-out)
        #display(out, test[i][2])
        # Delay
        time.sleep(1)
