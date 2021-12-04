import numpy as np

Q = [0] * 40
state = 0


class control_learn():

    global Q #each state has two actions: drift/no drift
    global state

    def getQ(self):
        return Q

    def setQ(self,index, value):
        Q[index] = value

    def getState(self,aim):
        if(aim<-0.9):
            return 0
        elif(aim<-0.8):
            return 1
        elif(aim<-0.7):
            return 2
        elif(aim<-0.6):
            return 3
        elif(aim<-0.5):
            return 4
        elif(aim<-0.4):
            return 5
        elif(aim<-0.3):
            return 6
        elif(aim<-0.2):
            return 7
        elif(aim<-0.1):
            return 8
        elif(aim<-0):
            return 9
        elif(aim<0.1):
            return 10
        elif(aim<0.2):
            return 11
        elif(aim<0.3):
            return 12
        elif(aim<0.4):
            return 13
        elif(aim<0.5):
            return 14
        elif(aim<0.6):
            return 15
        elif(aim<0.7):
            return 16
        elif(aim<0.8):
            return 17
        elif(aim<0.9):
            return 18
        else:
            return 19

    def computeQ(self,state):
        if(Q[state*2] < Q[state*2+1]):
            return Q[state*2+1]
        else:
            return Q[state*2]

    def getAction(self,state):
        if(Q[state*2] < Q[state*2+1]):
            return 1
        else:
            return 0
    
    def update(self, action, nextState):
        if(np.abs(nextState - 4.5) < np.abs(state - 4.5)):
            reward = 1
        elif(np.abs(nextState - 4.5) == np.abs(state - 4.5)):
            reward = 0
        else:
            reward = -1

        Q[state*2+action] = Q[state*2+action] + 0.2 * (reward + 0.05*Q[nextState*2 + self.getAction(nextState)] - Q[state*2+action])