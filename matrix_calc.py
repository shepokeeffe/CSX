from matrix_class import Matrix

m1 = Matrix([[1,2,3],
            [4,5,6],
            [7,8,9]])

m2 = Matrix([[8,6,7],
            [5,3,0],
            [9,4,1]])

m2.print_matrix(m2.values)

m1.scalarTimesRow(2,1)