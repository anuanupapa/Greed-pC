import numpy as np

#---------------------------------------------------
#Updates the players using the method player.update()
#Followed by player.set_action() and edge addition and deletion
#---------------------------------------------------
def update_and_decide(AM, player_arr):
    AM_static=AM.copy()
    #AM_static will not be changed. Changed will be made directly to AM

    #Updating and recording the satisfactions
    satisfaction_arr=np.ones((len(player_arr),1))
    for pInd in range(len(player_arr)):
        player_arr[pInd].update() #Updating variables of all players
        satisfaction_arr[pInd]=(player_arr[pInd].satisfaction)

    #Loop over the unsatisfied players
    unsatisfied_players=np.where(satisfaction_arr<0)[0]
    print('unsatisfied player indices',unsatisfied_players) ###Comment while RH_PS.py###--------------------------------------------------------
    for unpInd in unsatisfied_players:
        player_arr[unpInd].set_action() #The probability evaluation is inside method

        modify_connections(AM_static, AM, satisfaction_arr[unpInd], unpInd)
#----------------------------------------------------


#----------------------------------------------------
#Edge deletion and edge addition
#----------------------------------------------------
def modify_connections(AM_stat, AM_dyn, sat, index):
    #AM_stat is for reference. Changes will be done on AM_dyn
    #Synchronous updating
    val=np.tanh(np.abs(sat)/8.)
    
    #edge addition using edge_add
    if np.random.random()<val:    #Probability checking for edge addition
        print('player', index, 'wants to add edge')      ###Comment while RH_PS.py###----------------------------------------------------------
        
        add_ind=choose(np.sort(np.setdiff1d(np.where(AM_stat[index]==0)[0],index)))#no self edge
        
        if add_ind=='NaN':        #Do nothing if everyone is a neighbour
            pass
        else:
            AM_dyn[add_ind, index]=1
            AM_dyn[index, add_ind]=1
    else:
        pass
    
    #edge deletion using edge_del
    if np.random.random()<val:    #Probability checking for edge deletion
        print('player', index, 'wants to delete edge')      ###Comment while RH_PS.py###--------------------------------------------------------
        
        del_ind=choose(np.sort(np.where(AM_stat[index]==1)[0]))
        
        if del_ind=='NaN':        #Do nothing if no one is a neighbour
            pass
        else:
            AM_dyn[del_ind, index]=0
            AM_dyn[index, del_ind]=0
    else:
        pass
#------------------------------------------------

#-----------------------------
#Choose random element from ar
def choose(ar):
    if len(ar)!=0:
        return(int(np.random.choice(ar, 1)[0]))
    else:
        return('NaN')
#-----------------------------





if __name__=='__main__':
    import players
    import matplotlib.pyplot as plt
    import networkx as nx
    
    N=15
    adj_mat=np.zeros((N,N))
    player_arr=[]
    
    #Creating Players from players module
    for i in range(N):
        player_arr.append(players.player())
    player_arr=np.array(player_arr).copy()
    
    for i in range(20):
        #setting random payoff
        [player_arr[k].set_payoff(np.random.random()*4) for k in range(N)]
        
        update_and_decide(adj_mat, player_arr)
        
        [print('player', l, 'satisfaction', player_arr[l].satisfaction) for l in range(N)]
        print('\n\n')
        G=nx.from_numpy_matrix(adj_mat)
        nx.draw(G, with_labels=True)
        plt.show()
