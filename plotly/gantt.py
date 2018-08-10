
import pandas as pd
import numpy as np
import plotly
import plotly.plotly as py
import plotly.figure_factory as ff
from src.fitnessCalculation.startDate import start_date
plotly.tools.set_credentials_file(username='khaibnd', api_key='tpPcfBEzxRZX56T9d3GK')

start_date = start_date()

def gantt(demand, RHS, processing_time, sequence, lot_size, run_time, c):    
    j_keys=[item[:2] for item in RHS]
    m_keys=[item[2:] for item in RHS]
    
    df=[]
    for j, m in zip(j_keys, m_keys):
            exl = [i for i in (j + m)]
            l1 = RHS.index(exl)
            r = run_time(l1, lot_size, RHS, sequence, processing_time)
            finish = c[l1] + start_date
            finish1 = pd.to_datetime(finish, unit='s')
            start =  finish - r
            start1 = pd.to_datetime(start, unit='s')
          
            df.append(dict(Task='Machine %s'%(m), Start='%s'%(str(start1)), Finish='%s'%(str(finish1)),Resource='Job_%s'%(j[0])))
            
    color = {'Job_%s'%(k):'rgb'+str(tuple(np.random.choice(range(256), size=3))) for k in range(len(demand))}
    
    fig = ff.create_gantt(df, index_col='Resource',colors=color, show_colorbar=True, group_tasks=True, showgrid_x=True, title='Job shop Schedule')
    return py.plot(fig, filename='GA_job_shop_scheduling', world_readable=True)
