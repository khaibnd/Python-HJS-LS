import json

from src.data.data import load_data
from src.initialSolution.initialSolution import gen_population
from src.fitnessCalculation.LHS import lot_sizeCalculation
from src.fitnessCalculation.RHS2 import lot_finished_timeCalculation, run_time, makespan_timeCalculation
from src.plotly.gantt import gantt
from src.selection.selection2 import chros_selection
from src.crossover.crossover import chros_crossover
from src.mutation.mutation import chros_mutation

import cProfile
import pstats
import io

def main():
    
    a = r'C:\Users\khai.bui\Desktop\Operations\5. Eclipse\Python HJS-LS\src\GA.xlsx'
    b = r'C:\Users\khai.bui\Desktop\Operations\5. Eclipse\Python HJS-LS\src\GA.json'
    nhap = input('Nhap file dau vao: ') or a
    xuat = input('Nhap file dau ra: ') or b
    job = input('Nhap so luong job: ')
    load_data(nhap, xuat, job)
    
    # Import parameters from 'data.txt' file
    with open('GA.json') as f:
        parameters = json.load(f)
    
    population_size = int(parameters['population_size'])
    num_iteration = int(parameters['num_iteration'])
    job_count = int(parameters['job_count'])
    max_sublot = parameters['max_sublot']
    mc_op = parameters['mc_op']
    demand = parameters['demand']
    #priority = parameters['priority']
    sequence = parameters['sequence']
    processing_time = parameters['processing_time']
    setup_time = parameters['setup_time']
    k_way = int(parameters['k_way'])
    
    SPC_1_rate = parameters['SPC_1_rate']
    SPC_2_rate = parameters['SPC_2_rate']
    OMAC_rate = parameters['OMAC_rate']
    JLOSC_rate = parameters['JLOSC_rate']
    SLOSC_rate = parameters['SLOSC_rate']
    
    SStM = parameters['SStM']
    SSwM = parameters['SSwM']
    SSD = parameters['SSD']             # Parameter maximum sublot removal in SSD
    ROAM = parameters['ROAM']
    IOAM = parameters['IOAM']
    OSSM = parameters['OSSM']
    
    theta_max = parameters['theta_max'] # Parameter maximum change rate in SStM
      
    print('Load data done.')
    print('population_size', population_size)
    print('num_iteration', num_iteration)
    
    
    # Generate initial population list with size = 'population_size' (check the 'initialSolution.py')
    print('Verify initial solution')
    population_list = gen_population(population_size, max_sublot, mc_op, job_count, sequence)
    print('initial population: ', population_list)
    best_list = []
    best_span = 99999999999999999
    for iteration in range(num_iteration):
        print('Iteration: ', iteration)
        #total_chromosome = population_list
        #offspring_list = []
        
        # k-way tournament selection operator
        print('Start selection')
        population_list = chros_selection(k_way,population_size,  population_list, demand, setup_time, processing_time, sequence, mc_op)
        print('Selection done')
        
        # crossover
        population_list = chros_crossover(population_list, max_sublot, SPC_1_rate, SPC_2_rate, OMAC_rate, JLOSC_rate, SLOSC_rate)
        
        print('Crossover done')
        # mutation
        population_list = chros_mutation(population_list,sequence, mc_op, max_sublot, theta_max, SStM, SSwM, SSD, ROAM, IOAM, OSSM)
        
        print('Mutation done')
        #print('new: ',population_list)
        # Fitness initial population ( can dieu chinh do day tinh theo makespan chu ko phai Tardiness)
        local_makespan_list = [makespan_timeCalculation(lot_sizeCalculation(demand, population_list[pop]['LHS']), population_list[pop]['RHS'], setup_time, processing_time, sequence, mc_op) for pop in range(population_size)]
        local_best_span = min(local_makespan_list)
        if local_best_span < best_span:
            best_span = local_best_span
            best_list = population_list[local_makespan_list.index(best_span)]
        
        print('Iteration: ', iteration,' ,best span: ', best_span)
        print('Best list: ', best_list)
        
    print('Makespan', best_span)
    
    # Show Gantt Chart
    RHS = best_list['RHS']
    LHS = best_list['LHS']
    lot_size = lot_sizeCalculation(demand, LHS)
    makespan, max_c, completion_time= lot_finished_timeCalculation(lot_size, RHS, setup_time, processing_time, sequence, mc_op)
    print(gantt(demand, RHS, processing_time, sequence, lot_size, run_time, completion_time))

    
pr = cProfile.Profile()
pr.enable()
my_result = main()
pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
ps.print_stats()

with open('log.txt', 'w+') as f:
    f.write(s.getvalue())