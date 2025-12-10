class Matrix:

    def __init__(self, values):
        self.values = values
        self.rows = len(values)
        self.cols = len(values[0])

    def print_matrix(self):
        for row in self.values:
            print(row)

    def plus(self, other):
        for self.rows in self.values:
            for self.cols in self.rows:
                add_result = self.values[row][col] + other.values[row][col]

    def times(self, other):
        return

    def scalarTimesRow(self, scalar, rownumber):
        target_row = self.values[rownumber]
        for i in target_row:
            i = i*scalar
        return
    
print("eureka!")
