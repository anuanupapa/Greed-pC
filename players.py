import numpy as np

<<<<<<< HEAD

=======
>>>>>>> 7bb108783e2256362ad1ff8e19552e8007ca021e
class player:

    
    def __init__(self, greed=0.65, memory=0.01, action=0, sd=0.1):
        self.aspiration = 0
        self.satisfaction = 0
        self.greed = greed
        self.paymax = 0
        self.paymin = 0
        self.memory = memory
        self.payoff = 0
        self.action = action
        self.tremble = sd
        
    def set_payoff(self,Payoff): #Payoff is set after the PGG
        self.payoff=Payoff
        
    def set_paymin(self): #Minimum Payoff
        self.paymin = self.payoff-(1-self.memory)*(self.payoff-self.paymin)*int(self.payoff>=self.paymin)
        

    def set_paymax(self): #Maximum Payoff
        self.paymax = self.payoff+(1-self.memory)*(self.paymax-self.payoff)*int(self.paymax>=self.payoff)
            
    def set_aspiration(self):
        self.aspiration=self.greed*self.paymax+(1-self.greed)*self.paymin

    def set_satisfaction(self):
        self.satisfaction = self.payoff - self.aspiration + np.random.normal(0,self.tremble,1)[0]

    def update(self): # Updates 'satisfaction' based on the current 'payoff'
        self.set_paymin()
        self.set_paymax()
        self.set_aspiration()
        self.set_satisfaction()
        
    
    def set_action(self): # changes action based on the probability dictated by satisfaction
        if self.satisfaction<0:
            self.action=(self.action+int(np.random.random()<np.tanh(np.abs(self.satisfaction)/8.)))%2
        else:
            pass

 
if __name__=='__main__':
    from PGG import demo_game
    import matplotlib.pyplot as plt
    #demo_game is specifically written to test this class
    
    n=20000
    coopfrac1_arr=[]
    coopfrac2_arr=[]
    gr_arr=[]
    wind=2000 #Window averaging
    
<<<<<<< HEAD
    for gr in np.arange(0,1.002,0.025): #greed array
        print(gr)
=======
    for gr in np.linspace(0,1,50): #greed array
>>>>>>> 7bb108783e2256362ad1ff8e19552e8007ca021e
        p1 = player(greed=gr, sd=0.1)
        p2 = player(greed=gr, sd=0.1)
        counter1=0
        counter2=0
        for t in range(n):
            
            [Pay1, Pay2]=demo_game(p1.action,p2.action)
            
            p1.set_payoff(Pay1)
            p2.set_payoff(Pay2)
            p1.update()
            p2.update()
            p1.set_action()
            p2.set_action()
            
            if t>n-wind:
                counter1=counter1+p1.action
                counter2=counter2+p2.action
        
        coopfrac1_arr.append(counter1/wind)
        coopfrac2_arr.append(counter2/wind)
        gr_arr.append(gr)
    
    plt.plot(gr_arr, coopfrac1_arr,'.-',label='p1')
    plt.plot(gr_arr, coopfrac2_arr,'*-', label='p2')
    plt.legend()
    plt.xlabel('greed')
    plt.ylabel('cooperation fraction averaged last '+str(wind)+' rounds')
    plt.title('cooperation fraction VS greed t='+str(n)+'rounds')
<<<<<<< HEAD
    plt.savefig('2player_greedVScoop.png')
=======
    #plt.savefig('2player_greedVScoop.png')
>>>>>>> 7bb108783e2256362ad1ff8e19552e8007ca021e
    plt.show()
