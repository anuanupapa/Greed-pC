import numpy as np
import players


def initialize(N):
    adj_mat=np.zeros((N,N))
    player_arr=[]

    for Ind in range(N):
        player_arr.append(players.player())# player initialization is defined inside class
    player_arr=np.array(player_arr).copy()
    
    #player_arr contains array of the player objects
    #adj_mat is the adjacency matrix
    return(adj_mat, player_arr)
