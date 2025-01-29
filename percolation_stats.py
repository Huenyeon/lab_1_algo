class PercolationStats:
    # perform independent trials on an n-by-n grid
    def __init__(self, n: int, trials: int):
        self.n = n
        self.trials = trials

    # sample mean of percolation threshold
    def mean(self) -> float:
        pass

    # sample standard deviation of percolation threshold
    def stddev(self) -> float:
        pass

    # low endpoint of 95% confidence interval
    def confidence_lo(self) -> float:
        pass

    # high endpoint of 95% confidence interval
    def confidence_hi(self) -> float:
        pass

    # test client (see below)
    @staticmethod
    def main():
        pass

if __name__ == "__main__":
    PercolationStats.main()