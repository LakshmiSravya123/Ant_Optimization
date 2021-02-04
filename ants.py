# LakshmiSravya, Vedantham, 20142211
# Ramyasree, Vedantham, 20142901
import numpy as np
import random as rand

class Colony:
    class Ant:
        def __init__(self, colony):
            self.colony = colony
            self.pos = rand.randrange(self.colony.n)

            self.mem = np.zeros(self.colony.n)
            self.mem[self.pos] = 1

            self.path = [self.pos]
            self.cost = 0

        def reset(self, colony):
            self.__init__(colony)

        def __str__(self):
            result = " ["
            for n in self.path:
               result+= str(n)+", "
            result +=" ] "
            result+="Cost: "+str(self.cost)+"\n"
            return result

        def __lt__(self, other):
            return self.cost < other.cost

        # Returns city to be travelled to from current position
        def policy(self):
            ##deterministic 
            if rand.random() < self.colony.q_0:
                end=0.0
                s=np.zeros(self.colony.n)
                start=self.pos
                for end in range(self.colony.n):  
                        if (self.mem[end]==0):
                           s[end]+= (self.colony.tau[start][end])*(np.power(self.colony.eta(start,end),self.colony.beta))
                
                end=np.argmax(s)
                
                return end
            # checking probability (stochoistic)
            else:
               denominator=0.0
               prob=0.0
               start=self.pos
               for end in range(self.colony.n):
                 if (start != end):

                   #if ( self.colony.tau[start][end] != 0 and self.colony.adjMat[start][end] != 0):
                      denominator += float(self.colony.tau[start][end] * np.power(self.colony.eta(start,end),self.colony.beta))
                    
                 else:
                   continue

               end=0
               p=0
               while True:
                 if start != end:
                   
                   if (self.mem[end] == 0):# and self.colony.tau[start][end] != 0 and self.colony.adjMat[start][end] != 0):
                          p = (self.colony.tau[start][end] * np.power(self.colony.eta(start,end), self.colony.beta))/denominator
                          if rand.random() < p:
                             break
                   
                 else:
                    end = ((end + 1)%(self.colony.n))
                    continue
                 end = ((end + 1 ) % (self.colony.n))
               
               return end
        # Updates the local pheromones and position of ant
        # while keeping track of total cost and path
        def move(self):
            
            destination = self.policy()   
            
            self.colony.tau[self.pos][destination]=((1-self.colony.alpha)*self.colony.tau[self.pos][destination])+(self.colony.alpha*self.colony.tau_0)
            

            # Change position
            cost = self.colony.adjMat[self.pos][destination]
            self.cost+=cost
            self.pos=destination
            self.mem[destination]=1
            self.path.append(destination)
            

        # Updates the pheromone levels of ALL edges that form 
        # the minimum cost loop at each iteration
        def globalUpdate(self):
            
            for start in range(self.colony.n):
              for end in range(self.colony.n):
                 self.colony.tau[start][end]= ((1-self.colony.alpha)*self.colony.tau[start][end])+(self.colony.alpha/self.cost)
            
                 
            transcript.write(str(self))

    def __init__(self, adjMat, m=10, beta=2, alpha=0.1, q_0=0.9):
        # Parameters: 
        # m => Number of ants
        # beta => Importance of heuristic function vs pheromone trail
        # alpha => Updating propensity
        # q_0 => Probability of making a non-stochastic decision
        # tau_0 => Initial pheromone level

        self.adjMat = adjMat
        self.n = len(adjMat)

        self.tau_0 = 1 / (self.n * self.nearestNearbourHeuristic())
        self.tau = [[self.tau_0 for _ in range(self.n)] for _ in range(self.n)]
        self.ants = [self.Ant(self) for _ in range(m)]

        self.beta = beta
        self.alpha = 0.1
        self.q_0 =q_0

    def __str__(self):
        result="----------------"
        return result
    # Returns the cost of the solution produced by 
    # the nearest neighbour heuristix
    def nearestNearbourHeuristic(self):
        costs = np.zeros(self.n)     
        
        rand1=np.random.choice(self.n)
        #rand2=np.random.choice(self.n)
        
        cost=0
        unvisited=(i for i in range(self.n) if i != rand1)
        start=rand1
        tour=[start]
        while unvisited != []:
           unvisited=list(unvisited)
           near=unvisited[0]
           min=self.adjMat[start,near]
           for i in unvisited[1:]:
              if self.adjMat[start,i]<min:
                 near=i
                 min= self.adjMat[start, near]
           cost+=min
           next=near
           tour.append(next)
           unvisited.remove(next)
           start=next
        

       
        transcript.write("Nearest Nearbour Heuristic Cost :  {} \n".format(cost))
        return float(cost)

    # Heuristic function
    # Returns inverse of smallest distance between r and u
    def eta(self, r, u):
        distance=0.0
        
        distance=self.adjMat[r][u]
        if (distance != 0):
          return (1/float(distance))
        else:
           return 0

    def optimize(self, num_iter):
        for _ in range(num_iter):
            for _ in range(self.n-1):
                for ant in self.ants:
                    ant.move()

            min(self.ants).globalUpdate()

            for ant in self.ants:
                ant.reset(self)
        

if __name__ == "__main__":
    rand.seed(420)

    #file = open('d198')
    file = open('/content/drive/My Drive/Colab Notebooks/dantzig.csv')
    transcript= open('/content/drive/My Drive/Colab Notebooks/result.txt','w')
    adjMat = np.loadtxt(file, delimiter=",")

    ant_colony = Colony(adjMat)
    
    ant_colony.optimize(1000)
