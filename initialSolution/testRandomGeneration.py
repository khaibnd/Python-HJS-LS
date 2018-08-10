import random

a = [3, 5, 7, 6, 4, 2, 7, 9, 3, 5]
b = [10, 10, 10, 10, 10, 8, 10, 10, 10, 10]
c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

job_count = 10
max_sublot = [3, 5, 7, 6, 4, 2, 7, 9, 3, 5]

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

job_list = [[k, i, j] for k in range(len(a)) for i in range(a[k]) for j in range(b[k])]
random.shuffle(job_list)
print(job_list)
print(len(job_list))
print(sum([i*j for i, j in zip(a, b)]))
print('*********************************************************************************')


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
           
        #sorted_temp_value = sorted(temp_value, key=lambda word: (word[2]))
        #print(temp_position)
        #print(sorted_temp_value)
        for j in range(len(job_list)):
            for t in temp_position:
                z = temp_position.index(t)
                if j == t:
                    job_list[j] =  sorted_temp_value[z]
       
print(job_list)


