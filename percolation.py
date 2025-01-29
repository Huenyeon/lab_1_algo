from lib.weighted_quick_union_uf import WeightedQuickUnionUF


class Percolation:
    # creates n-by-n grid, with all sites initially blocked
    def __init__(self, n: int): #20
        self.n = n
        self.arr = [[False ] * self.n for _ in range(self.n)]
        self.opened_sites = 0



    # opens the site (row, col) if it is not open already
    def open(self, row: int, col: int) -> None: #(1,2)
        
        self.arr[row - 1][col - 1] = True
        print(self.arr)
        print(self.arr[row])


    # is the site (row, col) open?
    def is_open(self, row: int, col: int) -> bool:
        return self.arr[row-1][col-1] == True
        


    # is the site (row, col) full?
    def is_full(self, row: int, col: int) -> bool:
        pass
        
    # returns the number of open sites
    def number_of_open_sites(self) -> int:
        # return self.opened_sites
        return self.opened_sites

    # does the system percolate?
    def percolates(self) -> bool:
        #if maka agi na sya from top to botton
        pass

    # test client (optional)
    @staticmethod
    def main():
        pass


if __name__ == "__main__":
    Percolation.main()
    percolation= Percolation(4)

    percolation.open(2,1)
