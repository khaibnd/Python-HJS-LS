# Lot_size Calculation from LHS of chromosome

def lot_sizeCalculation(demand, LHS):
    lot_size = []
    for l in range(len(LHS)):
        lot_size_per_order = []
        base_size = 500
        for ls in range(len(LHS[l])):
            if (sum(LHS[l]) > 0):           
                size_per_sublot = int(base_size * round((demand[l]*LHS[l][ls]/sum(LHS[l])/base_size)))
            else:
                size_per_sublot = 0
            lot_size_per_order.append(size_per_sublot)
        lot_size.append(lot_size_per_order)
    return lot_size
#print(lot_sizeCalculation(demand, LHS))
'''    
demand = [2000, 5000, 14000, 8000, 6000, 4500, 3800, 7000, 9000, 12000]
LHS = [[0.29, 0.18, 0.04], [0.82, 0.78, 0.67, 0.75, 0.1], [0.61, 0.8, 0.08, 0.44, 0.19, 0.5, 0.48], [0.1, 0.33, 0.66, 0.01, 0.0, 0.88], [0.86, 0.85, 0.68, 0.46], [0.47, 0.66], [0.23, 0.09, 0.81, 0.03, 0.0, 0.65, 0.58], [0.24, 0.44, 0.33, 0.11, 0.96, 0.54, 0.54, 0.85, 0.48], [0.44, 0.81, 0.43], [0.68, 0.98, 0.74, 0.26, 0.88]]
new_demand = []
lot_size = lot_sizeCalculation(demand, LHS)
for i in range(len(lot_size)):
    new_demand.append(sum(lot_size[i]))
    
print('old: ', sum(demand), demand)
print('new: ', sum(new_demand), new_demand)

'''