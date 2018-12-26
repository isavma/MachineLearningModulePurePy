import LinearAlgebraPurePython as la 
import sys

class Least_Squares:
    def __init__(self, tol=1):
        self.order = order
        self.tol = tol

    def __format_data_correctly(self, D):
        if not isinstance(D[0],list): 
            return [D]
        else:
            return D

    def __orient_data_correctly(self, D):
        if len(D) < len(D[0]): 
            return la.transpose(D)
        else:
            return D

    def __condition_input_data(self, X):
        X = self.__format_data_correctly(X)
        X = self.__orient_data_correctly(X)
        
        num_rows_of_X = len(X)
        num_of_Xs = len(X[0])

        if self.order > 1:
            for row_num in range(num_rows_of_X):
                temp_row = []
                for i_of_x in range(num_of_Xs):
                    for order in range(self.order):
                        temp_row.append(X[row_num][i_of_x] ** (order+1.0))
                X[row_num] = temp_row

        for i in range(len(X)): 
            X[i] = [1.0] + X[i]

        if len(X) < len(X[0]):
            raise ArithmeticError('Inadequate number of inputs for model solution.')

        return X

    def __condition_output_data(self, Y):
        Y = self.__format_data_correctly(Y)
        Y = self.__orient_data_correctly(Y)

        return Y

    def fit(self, X, Y):
        self.X = self.__condition_input_data(X)
        self.Y = self.__condition_output_data(Y)

        AT = la.transpose(self.X)
        ATA = la.matrix_multiply(AT, self.X)
        ATB = la.matrix_multiply(AT, self.Y)
        self.coefs = la.solve_equations(ATA,ATB,tol=self.tol)

    def predict(self, X_test):
        self.X_test = self.__condition_input_data(X_test)

        return la.matrix_multiply(self.X_test, self.coefs)
