import numpy as np
import players

def measure(AM, pl_arr):
    countercoop=0
    countersat=0
    for pInd in pl_arr:
        countercoop=countercoop+pInd.action
        countersat=countersat+pInd.satisfaction
    return(countercoop/len(pl_arr), countersat/len(pl_arr), np.sum(np.sum(AM))/len(pl_arr))
