import numpy as np

class play_field():
    def __init__(self, n):
        self.size = n
        self.data = np.zeros((n,n))
        self.iteration = 0

    def set_initial_system(self, x_y_data):
        for (j,i) in x_y_data:
            if i < self.size and j < self.size:
                self.data[j][i] = 1
    
    def alive_neighbours_number(self,i,j):
        count = 0;
        if i-1 >= 0:
            if j-1 >= 0:
                if self.data[i-1][j-1] >= 1: 
                    count+=1
            if j >= 0:
                if self.data[i-1][j] >= 1: 
                    count+=1
            if j+1 < self.size:
                if self.data[i-1][j+1] >= 1: 
                    count+=1 
        if i >= 0 and i < self.size:
            if j-1 >= 0:
                if self.data[i][j-1] >= 1: 
                    count+=1
            if j+1 < self.size:
                if self.data[i][j+1] >= 1: 
                    count+=1
        if i+1 < self.size:
            if j-1 >= 0:
                if self.data[i+1][j-1] >= 1: 
                    count+=1
            if j >= 0:
                if self.data[i+1][j] >= 1: 
                    count+=1
            if j+1 < self.size:
                if self.data[i+1][j+1] >= 1: 
                    count+=1 
        return count
    
    def is_alive(self, i, j):
        number = self.alive_neighbours_number(i,j)
        if self.data[i][j] == 0:
            return number == 3
        else : 
            return  number == 2 or number == 3

    def next_step(self):
        a = self.data.copy()
        for i in range(0,self.size):
            for j in range(0,self.size):
                if self.is_alive(i,j):
                    a[i][j] += 1
                else:
                    a[i][j] = 0
        self.iteration += 1
        self.data = a.copy()
        return self.data

    def get_dim(self):
        return (float(self.size), float(self.size))

"""
        0 0 0 0 0 0     0 0 0 0 0 0
        0 0 0 0 0 0     0 0 0 0 0 0
        0 0 1 0 0 0     0 0 0 0 0 0
        0 0 1 0 0 0 =>  0 1 1 1 0 0
        0 0 1 0 0 0     0 0 0 0 0 0
        0 0 0 0 0 0     0 0 0 0 0 0

"""