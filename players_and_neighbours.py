import numpy as np
import settings


class player:
    
    def __init__(self, Neighbours, greed=0.65, memory=0.01, action=0):
        self.aspiration = 0
        self.satisfaction = 0
        self.greed = greed
        self.paymax = 0
        self.paymin = 0
        self.memory = memory
        self.payoff = 0
        self.action = action
        self.neigh=Neighbours
            

            
    def set_payoff(self,Payoff):
        self.payoff=Payoff
        
    def set_paymin(self):
        if self.paymin>self.payoff:
            self.paymin = self.payoff
        else:
            self.paymin=self.paymin + self.memory*(self.payoff - self.paymin)

    def set_paymax(self):
        if self.paymax<self.payoff:
            self.paymax = self.payoff
        else:
            self.paymax=self.paymax + self.memory*(self.payoff - self.paymax)
            
    def set_aspiration(self):
        self.aspiration=self.greed*self.paymax+(1-self.greed)*self.paymin

    def set_satisfaction(self):
        self.satisfaction = self.payoff - self.aspiration + np.random.normal(0,0.1,1)[0]

    def set_action(self):
        self.action=(self.action+int(bool(np.random.random()<np.tanh(np.abs(self.satisfaction)/8.))))%2

    def edge_add(self):
        self.neigh=np.concatenate((np.choice(setdiff1d(settings.N_arr, self.neigh),1),self.neigh), axis=None)

    def edge_del(self):
        self.neigh=np.setdiff1d(self.neigh, np.random.choice(self.neigh, 1))
        
    def set_neighbours(self):
        if np.random.random()<np.tanh(np.abs(self.satisfaction/8.)):
            neigh1=self.edge_add()
        else:
            pass
        if np.random.random()<np.tanh(np.abs(self.satisfaction/8.)):
            neigh2=self.edge_del()
        else:
            pass
        self.neigh=np.unique(np.concatenate((neigh1,neigh2),axis=None))

    @classmethod
    def update(self):
        self.set_paymin()
        self.set_paymax()
        self.set_aspiration()
        self.set_satisfaction()

    @classmethod
    def decide(self):
        if self.satisfaction<0:
            self.set_action()
            self.set_neighbour()

 
if __name__=='__main__':
    from PGG import demo_game

    p1 = player()
    p2 = player()
    p1.paymax=4
    p1.paymin=0
    p2.paymax=3
    p2.paymin=1
    print(type(p1))
    for i in range(10000):
        [Pay1, Pay2]=demo_game(p1.action,p2.action)
        p1.set_payoff(Pay1)
        p2.set_payoff(Pay2)
        p1.update()
        p2.update()
        print(p1.payoff,p2.payoff)
