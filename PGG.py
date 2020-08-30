import numpy as np
from scipy.sparse import lil_matrix

#This function is used for testing players.py
def demo_game(r1,r2):
    payoff_mat=np.array([[3,0],[4,1]])
    p1=payoff_mat[1-r1,1-r2]
    p2=payoff_mat[1-r2,1-r1]
    return(p1,p2)



#------------------------------------------------
#pgg: updates the payoff after the game is played
#------------------------------------------------
def pgg(AdjMat, pl_arr, r=4):
    #Setting up action array of the players
    player_res=[]
    for pl in pl_arr:
        player_res.append(pl.action)
    player_response=np.array(player_res)
    
    payoff_update(game(AdjMat, player_response, r), pl_arr)
#------------------------------------------------
    
#------------------------------------------------
#payoff_update: updates the attribute 'payoff' of the players
#------------------------------------------------
def payoff_update(payoff, p_arr):
    N=len(p_arr)

    for i in range(N):
        p_arr[i].set_payoff(payoff[i])

    ###Comment while RH_PS.py###-------------------------------------------------------------------------------------
    [print('player',i,p_arr[i].payoff) for i in range(N)]
#-------------------------------------------------

    
#-------------------------------------------------
#game : 1 round of PGG over the entire network for all nodes
#-------------------------------------------------
def game(AM, pRes, r):#pRes:Player Response AM:Adjacency Matrix
    N=np.shape(AM)[0]

    #network on which the PGG will be played
    net_each_pgg=AM+np.eye(N,N)

    #number of players participating in 'i'th PGG is player_count
    player_count=np.reshape(np.sum(net_each_pgg, axis=1), (N,1))

    net_each_pgg_sparse=lil_matrix(net_each_pgg)
    pRes=np.reshape(pRes,(N,1))

    #PGG: Total PG for the game around 'i'th node is stored.
    #C=1 D=0, thus dot product works.
    PG_accumulated=r*net_each_pgg_sparse.dot(pRes)

    #PG obtained by 'row'th player due to 'column'th PGG
    #is stored in payoff_obtained_per_pgg
    PG_obtained=np.reshape(np.divide(PG_accumulated, player_count), (N,))
    payoff_obtained_per_pgg=net_each_pgg*PG_obtained[np.newaxis,:]

    #Final payoff after summing all the contributions and subtracting cost 
    payoff_obtained=np.reshape(np.sum(payoff_obtained_per_pgg, axis=1),(N,1))
    final_payoff=payoff_obtained-np.multiply(player_count, pRes) #FCPG
    
    return(final_payoff)
#-----------------------------------------------------





if __name__=='__main__':
    from players import player
    import networkx as nx
    import matplotlib.pyplot as plt

    '''
    #1st config
    p1=player(action=1)
    p2=player(action=0)
    p3=player(action=1)
    p4=player(action=0)
    player_arr=np.array([p1,p2,p3,p4])
    adj_mat=np.array([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
    '''

    #2nd config
    p1=player(action=1)
    p2=player(action=0)
    p3=player(action=1)
    p4=player(action=0)
    p5=player(action=0)
    player_arr=np.array([p1,p2,p3,p4,p5])
    adj_mat=np.array([[0,1,0,1,1],[1,0,1,0,1],[0,1,0,1,1],[1,0,1,0,1],[1,1,1,1,0]])

    pgg(adj_mat,player_arr)

    G=nx.from_numpy_matrix(adj_mat)
    col_map=[]
    for p in player_arr:
        if p.action==1:
            col_map.append('blue')
        else:
            col_map.append('red')
    nx.draw(G, node_color=col_map, with_labels=True, pos=nx.fruchterman_reingold_layout(G))
    plt.show()
