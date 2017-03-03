import numpy as np
import matplotlib.pyplot as plt

p = np.mat([[0.8, 0.1, 0.1],
            [0.2, 0.0, 0.8],
            [0.4, 0.4, 0.2]])

# Verify by simulation recurrent and transient states
x = np.mat([1.0, 0.0, 0.0])


def step(p, state):
    """
    Simulate cat Leo behaviour based on current state's next state probability.
    :param p: transient matrix
    :param state: current state - index of array, 0 based
    :return: next step state - index of array, 0 based
    """
    temp = []
    for j in range(p.shape[1]):
        sum = 0
        for k in range(j + 1):
            sum += p[state, k]
        temp.append(sum)
    key = np.random.rand()
    for j_next in range(p.shape[1]):
        if key <= temp[j_next]:
            return j_next


def final_state_distribution(p, init_state, num_of_steps):
    """
    Simulates random walk an generate final states distribution
    :param p: transient matrix
    :param init_state: initial state
    :param num_of_steps: number of steps in simulation
    :return:
    """
    i = init_state
    counter = [0] * p.shape[0]
    for _ in range(num_of_steps):
        counter[i] += 1
        i = step(p, i)
    for index in range(len(counter)):
        counter[index] /= num_of_steps
    return counter

init_states_list = []
for i in range(p.shape[0]):
    init_states_list.append(i)
num_of_steps_list = [50, 100, 1000]

init_state = init_states_list[0]
num_of_steps = num_of_steps_list[0]
plt.figure(1)
plt.subplot(311)
counter = final_state_distribution(p, init_state, num_of_steps)
print(counter)
plt.plot(counter, 'ro')

num_of_steps = num_of_steps_list[1]
plt.subplot(312)
counter = final_state_distribution(p, init_state, num_of_steps)
print(counter)
plt.plot(counter, 'ro')

num_of_steps = num_of_steps_list[2]
plt.subplot(313)
counter = final_state_distribution(p, init_state, num_of_steps)
print(counter)
plt.plot(counter, 'ro')

init_state = init_states_list[1]
num_of_steps = num_of_steps_list[0]
plt.figure(2)
plt.subplot(311)
counter = final_state_distribution(p, init_state, num_of_steps)
print(counter)
plt.plot(counter, 'ro')

num_of_steps = num_of_steps_list[1]
plt.subplot(312)
counter = final_state_distribution(p, init_state, num_of_steps)
print(counter)
plt.plot(counter, 'ro')

num_of_steps = num_of_steps_list[2]
plt.subplot(313)
counter = final_state_distribution(p, init_state, num_of_steps)
print(counter)
plt.plot(counter, 'ro')

plt.figure(3)
init_state = init_states_list[2]
num_of_steps = num_of_steps_list[0]
plt.subplot(311)
counter = final_state_distribution(p, init_state, num_of_steps)
print(counter)
plt.plot(counter, 'ro')

num_of_steps = num_of_steps_list[1]
plt.subplot(312)
counter = final_state_distribution(p, init_state, num_of_steps)
print(counter)
plt.plot(counter, 'ro')

num_of_steps = num_of_steps_list[2]
plt.subplot(313)
counter = final_state_distribution(p, init_state, num_of_steps)
print(counter)
plt.plot(counter, 'ro')


plt.xlabel("Initial state")
plt.ylabel("Number of iterations")
plt.show()