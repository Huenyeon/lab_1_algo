from lib.weighted_quick_union_uf import WeightedQuickUnionUF

class Percolation:
    # creates n-by-n grid, with all sites initially blocked
    def __init__(self, n: int): #20
        self.n = n
        self.arr = [[False ] * self.n for _ in range(self.n)]
        self.open_sites = 0
        self.uf = WeightedQuickUnionUF(n * n + 1)
        self.top = n * n
        

    # opens the site (row, col) if it is not open already
    def open(self, row: int, col: int) -> None: #(1,2)
        if not self.is_open(row, col): #gina open ang site if inde pa open
            self.arr[row-1][col-1] = True
            self.open_sites += 1

            index = (row - 1) * self.n + (col -1)

            if row == 1: #connect to the top if its ara sa first row
                self.uf.union(index, self.top)

            #idk if need pa ni but in case lang
            directions = [(-1, 0), (1, 0), (0, -1),(0, 1)] #directions sang site na i-open (up, down, left, right)
            for change_row, change_col in directions: #gina check which direction sang current site ang open para ma connect
                new_row, new_col = row + change_row, col + change_col
                if 1 <= new_row <= self.n and 1 <= new_col <= self.n and self.is_open(new row, new_col):
                    self.uf.union(index, (new_row - 1) * self.n + (new_col - 1))

    # is the site (row, col) open?
    def is_open(self, row: int, col: int) -> bool:
        return self.arr[row-1][col-1] == True
        

    # is the site (row, col) full?
    def is_full(self, row: int, col: int) -> bool:
        return self.is_open(row, col) and self.uf.connected((row - 1) * self.n + (col - 1), self.top)

        
    # returns the number of open sites
    def number_of_open_sites(self) -> int:
        return self.open_sites

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
