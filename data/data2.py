import pandas as pd
import numpy as np

import json


sequence = pd.read_excel(open('GA.xlsx','rb'), sheet_name='Sequences')
sequence = [[int(x) for x in sequence[lst] if ~np.isnan(x)] for lst in range(52)]
json_sequence = {}
json_sequence['sequence'] = sequence

print(sequence)
print(len(sequence))

with open('GA.json', 'w') as fp:
    json.dump(json_sequence, fp)