from lib.std_stats import StdStats 
from percolation import Percolation
import random
from math import sqrt

class PercolationStats:
    # perform independent trials on an n-by-n grid
    def __init__(self, n: int, trials: int):

        self.treshold = []
        try:
            self.n = n
            self.trials = trials
            if n <= 0 or trials<= 0:
                raise ValueError
        
        except ValueError as e:
            print(e)

        for _ in range(self.trials):
            percolation = Percolation(self.n)
            
            
            while not percolation.percolates():
                row = random.randint(1, n)
                col = random.randint(1,n)
                if not percolation.is_open(row,col):
                    percolation.open(row,col)
                    
                
        
            values = percolation.number_of_open_sites()/ (self.n**2)
            self.treshold.append(values)

    # sample mean of percolation threshold
    def mean(self) -> float:
        return StdStats.mean(self.treshold)
        
        

    # sample standard deviation of percolation threshold
    def stddev(self) -> float:
        return StdStats.stddev(self.treshold)

    # low endpoint of 95% confidence interval
    def confidence_lo(self) -> float:
        return self.mean() - (1.96* (self.stddev()/ self.trials ** 0.5)) 

    # high endpoint of 95% confidence interval
    def confidence_hi(self) -> float:
        return self.mean() + (1.96* (self.stddev()/ self.trials ** 0.5))

    # test client (see below)
    @staticmethod
    def main():
        import sys
        if len(sys.argv) != 3:
            print("Usage: python percolation_stats.py <n> <trials>")
            return
        n = int(sys.argv[1])
        trials = int(sys.argv[2])
        stats = PercolationStats(n, trials)
        print(f"mean                    = {stats.mean()}")
        print(f"stddev                  = {stats.stddev()}")
        print(f"95% confidence interval = [{stats.confidence_lo()}, {stats.confidence_hi()}]")

if __name__ == "__main__":
    PercolationStats.main()
