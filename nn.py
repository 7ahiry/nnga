#/usr/bin/env python

import time
import random

# Learning rate:
# Lower  = slower
# Higher = less precise
rate=.1
activation=0
# Create random weights
inWeight=[random.uniform(0, 1), random.uniform(0, 1), 1]
#inWeight=[random.uniform(0, 1), random.uniform(0, 1), .5]

# Start neuron with no stimuli
inNeuron=[0.0, 0.0]

# Learning table (or gate)
test =[[0.0, 0.0, 0.0]]
test+=[[0.0, 1.0, 1.0]]
test+=[[1.0, 0.0, 1.0]]
test+=[[1.0, 1.0, 1.0]]

# Calculate response from neural input
def outNeuron():
        global inNeuron, inWeight, activation
        # compute the activation and return the output
        # activation funtion is a step function
        activation=inNeuron[0]*inWeight[0] + inNeuron[1]*inWeight[1]
        if activation>inWeight[2]:
                return 1.0
        else:
                return 0.0

# Display results of test
def display(out, real):
    global inNeuron, inWeight, activation
    if out == real:
        print("[",str(inNeuron[0])," ",str(inNeuron[1]) ,"]",str(out),"should be **TRUE**", str(activation),"[",str(inWeight[0])," ",str(inWeight[1]) ,"]")
    else:
        print("[",str(inNeuron[0])," ",str(inNeuron[1]) ,"]",str(out),"should be", str(real),"[",str(inWeight[0])," ",str(inWeight[1]) ,"]")

while 1:
        # Loop through each lesson in the learning table
        for i in range(len(test)):
                # Stimulate neurons with test input
                inNeuron[0]=test[i][0]
                inNeuron[1]=test[i][1]
                #inNeuron[0]=random.uniform(0, 1)
                #inNeuron[1]=random.uniform(0, 1)
                # Adjust weight of neuron #1
                # based on feedback, then display
                out = outNeuron()
                inWeight[0]+=rate*(test[i][2]-out)
                inWeight[1]+=rate*(test[i][2]-out)
                display(out, test[i][2])
                # Adjust weight of neuron #2
                # based on feedback, then display
                #out = outNeuron()
                #inWeight[1]+=rate*(test[i][2]-out)
                #display(out, test[i][2])
                # Delay
                time.sleep(1)
