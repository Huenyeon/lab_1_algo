from lib.weighted_quick_union_uf import WeightedQuickUnionUF

class Percolation:
    # creates n-by-n grid, with all sites initially blocked
    def __init__(self, n: int): #20
        self.n = n
        self.arr = [[False ] * self.n for _ in range(self.n)]
        self.opened_sites = 0
        self.uf = WeightedQuickUnionUF(self.n*self.n + 2)
        self.top = n*n 
        self.bottom = n*n + 1


    # opens the site (row, col) if it is not open already
    def open(self, row: int, col: int) -> None:  
        index = (row - 1) * self.n + (col - 1)  #formula to get the index of row col

        if self.arr[row - 1][col - 1] == False:  
            self.arr[row - 1][col - 1] = True
            self.opened_sites += 1

            # If open ang the top row, connect it to the imaginary top node
            if row == 1:
                self.uf.union(index, self.top)
            # If open ang bottom row, connect it to the imaginary bottom node
            if row == self.n:
                self.uf.union(index, self.bottom)
            
            # Check left and right nga open sites
            if col > 1 and self.arr[row - 1][col - 2] == True: 
                left_site = (row - 1) * self.n + (col - 2)
                self.uf.union(index, left_site)

            if col < self.n and self.arr[row - 1][col] == True:  
                right_site = (row - 1) * self.n + col
                self.uf.union(index, right_site)

            # Check up and down nga open sites
            if row > 1 and self.arr[row - 2][col - 1] == True:  
                up_site = (row - 2) * self.n + (col - 1)
                self.uf.union(index, up_site)

            if row < self.n and self.arr[row][col - 1] == True: 
                down_site = row * self.n + (col - 1)
                self.uf.union(index, down_site)



    # is the site (row, col) open?
    def is_open(self, row: int, col: int) -> bool:
        return self.arr[row-1][col-1] == True
        

    # is the site (row, col) full?
    def is_full(self, row: int, col: int) -> bool:

        row_col_index = (row - 1) * self.n + (col - 1)
        
        if not self.arr[row-1][col-1]:
            return False
        
        return self.uf.find(self.top) == self.uf.find(row_col_index)
        


            
        
    # returns the number of open sites
    def number_of_open_sites(self) -> int:
        return self.opened_sites



    # does the system percolate?
    def percolates(self) -> bool:
        return self.uf.find(self.top) == self.uf.find(self.bottom)

    # test client (optional)
    @staticmethod
    def main():
        pass


if __name__ == "__main__":
    Percolation.main()

