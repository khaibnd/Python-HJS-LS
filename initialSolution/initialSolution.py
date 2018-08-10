
import random
import numpy as np
'''
population_size = 20
job_count = 10
max_sublot = [3, 5, 7, 6, 4, 2, 7, 9, 3, 5]
mc_op = [6, 14, 8, 5, 6, 9, 4, 6, 7, 2]
demand = [2000, 5000, 14000, 8000, 6000, 4500, 3800, 7000, 9000, 12000]

sequence = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
[0, 2, 4, 9, 3, 1, 6, 5, 7, 8], 
[1, 0, 3, 2, 8, 5, 7, 6, 9, 4], 
[1, 2, 0, 4, 6, 8, 7, 3, 9, 5], 
[2, 0, 1, 5, 3, 4, 8, 7, 9, 6], 
[2, 1, 5, 3, 7, 4, 0, 6], 
[1, 0, 3, 2, 6, 5, 9, 8, 7, 4], 
[2, 0, 1, 5, 4, 6, 8, 9, 7, 3], 
[0, 1, 3, 5, 2, 9, 6, 7, 4, 8], 
[1, 0, 2, 6, 8, 9, 5, 3, 4, 7]]
'''

def gen_population(population_size, max_sublot, mc_op, job_count, sequence):
    return tuple({'LHS': [gen_lhs(length) for length in max_sublot],
                  'RHS': gen_rhs(np.dot([len(i) for i in sequence], max_sublot), max_sublot, mc_op,job_count, sequence)} for _ in range(population_size))


def gen_lhs(length):
    return [round(np.random.uniform(0,1),2) for _ in range(length)]

def gen_rhs(length, max_sublot, mc_op,job_count, sequence):
    ret = []
    job_list = [[k, i, j] for k in range(len(max_sublot)) for i in range(max_sublot[k]) for j in range([len(i) for i in sequence][k])]
    random.shuffle(job_list)

    for i in range(job_count):
        for k in range(max_sublot[i]):
            temp_value = []
            temp_position = []
            for j in range(len(job_list)):
                if job_list[j][0:2]  == [i,k]:
                    temp_position.append(j)
                    temp_value.append(job_list[j])
                    
            temp_value_ind = {c: [b, a, c] for (b, a, c) in temp_value}
            sorted_temp_value = [temp_value_ind[c] for c in sequence[i]]

            for j in range(len(job_list)):
                for t in temp_position:
                    z = temp_position.index(t)
                    if j == t:
                        job_list[j] =  sorted_temp_value[z]    
        
    for i in range(length):
        new = []
        a1 = job_list[i][0]
        a2 = job_list[i][1]
        a3 = job_list[i][2]          
        a4 = random.randint(0, mc_op[a3]-1)    
        new.append(a1) # job
        new.append(a2) # sub-lot
        new.append(a3) # operation
        new.append(a4) # machine
        ret.append(new)
    return ret

#print(gen_population(population_size, max_sublot, mc_op, job_count, sequence))


