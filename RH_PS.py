import numpy as np
import matplotlib.pyplot as plt
import settings
import players
import update_decide
import PGG
import Measure
import time

[adj_mat, player_arr]=settings.initialize(1000)
n=5000

#Arrays for plots
coop_frac_arr=[]
sat_arr=[]
avgdeg_arr=[]
ttime=[]
tti=time.time()


for i in range(n):
    
    PGG.pgg(adj_mat, player_arr)
    
    update_decide.update_and_decide(adj_mat, player_arr)
    
    [coop,sat,avgdeg]=(Measure.measure(adj_mat, player_arr))
    
    coop_frac_arr.append(coop)
    sat_arr.append(sat)
    avgdeg_arr.append(avgdeg)
    ttime.append(i)
    
    #if i%2490==0:
    print('round :',i)
        
print(time.time()-tti)
plt.plot(ttime, coop_frac_arr)
plt.show()
plt.plot(ttime, sat_arr)
plt.show()
plt.plot(ttime, avgdeg_arr)
plt.show()
