class Matrix:
    __data: list
    __shape: tuple

    # def __init__(self, data: list, shape: tuple) -> Matrix: #Matrix or None?
    #     if data is None and shape is None:
    #         raise TypeError("Matrix must be initialized with data or shape")
    #     if data and shape:
    #         if len(data) != shape[0] or len(data[0]) != shape[1]:
    #             raise ValueError("Shape and data dimensions mismatch")
    #     if data:
    #         self.__shape[0] = len(data)
    #         self.__shape[1] = len(data[0])
    #         for i in data:
    #             if len(i) != shape[1]:
    #                 raise ValueError("Data is inconsistent")
    #         self.__data = data
    #     else:
    #         self.__shape = shape
    #         self.__data = [[0 for _ in range(shape[1])] for _ in range(shape[0])]
    #     return self

    def __init__(self, input: list | tuple):
        if isinstance(input, list):
            for i in input:
                if not isinstance(i, list) or len(i) != len(input[0]):
                    raise ValueError("Data is inconsistent")
            if not all(isinstance(input[i][j], (int, float)) for i in range(len(input)) for j in range(len(input[0]))):
                raise ValueError("Data is not a list of numbers")
            self.__data = input
            self.__shape = (len(input), len(input[0]))
        elif isinstance(input, tuple):
            if len(input) == 2:
                self.__data = [[0 for _ in range(input[1])] for _ in range(input[0])]
                self.__shape = input
            else:
                raise ValueError("Tuple must be of length 2")   # or maybe i can make vector if the length is 1
        else:
            raise TypeError("Input must be a list or a tuple")

    def __add__(self, other):
        if self.__shape != other.__shape:
            raise ValueError("Matrices have different shapes")
        return Matrix([[self.__data[i][j] + other.__data[i][j] for j in range(self.__shape[1])] for i in range(self.__shape[0])])
    
    def __radd__(self, other):
        return other.__add__(self)

    def __sub__(self, other):
        if self.__shape != other.__shape:
            raise ValueError("Matrices have different shapes")
        return Matrix([[self.__data[i][j] - other.__data[i][j] for j in range(self.__shape[1])] for i in range(self.__shape[0])])
    
    def __rsub__(self, other):
        return other.__sub__(self)

    def  __truediv__(self, divisor):  #why truediv?--> magic method
        if not isinstance(divisor, (int, float)):
            raise TypeError("Only Division by a number is supported")
        if divisor == 0:
            raise ZeroDivisionError("Division by zero")
        return Matrix([[self.__data[i][j] / divisor for j in range(self.__shape[1])] for i in range(self.__shape[0])])
    
    #TODO : fix
    def __rtruediv__(self, divisor):
        if ((self.data[i][j] == 0 for j in range(self.__shape[1])) for i in range(self.__shape[0])):
            raise ZeroDivisionError("Division by zero")
        return Matrix([[divisor / self.__data[i][j] for j in range(self.__shape[1])] for i in range(self.__shape[0])])
    
    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.__shape[1] != other.__shape[0]:
                raise ValueError("Matrices have incompatible shapes")
            return Matrix([[sum(self.__data[i][k] * other.__data[k][j] for k in range(self.__shape[1])) for j in range(other.__shape[1])] for i in range(self.__shape[0])])
        elif isinstance(other, Vector):
            if self.__shape[1] != len(other):
                raise ValueError("Vector and Matrix have incompatible shapes")
            return Vector([[sum(self.__data[i][k] * other[k] for k in range(self.__shape[1]))] for i in range(self.__shape[0])])
        elif isinstance(other, (int, float)):
            return Matrix([[self.__data[i][j] * other for j in range(self.__shape[1])] for i in range(self.__shape[0])])
    
    def __rmul__(self, other):
        if isinstance(other, Matrix):
            return other.__mul__(self)
        elif isinstance(other, Vector):
            if other.__shape[1] != len(self):
                raise ValueError("Vector and Matrix have incompatible shapes")
            return Vector([[sum(other[k] * self.__data[i][k] for k in range(self.__shape[1]))] for i in range(self.__shape[0])])
        elif isinstance(other, (int, float)):
            return self.__mul__(other)

    def __str__(self) -> str:
        return f"Matrix({self.__data}, {self.__shape})"

    #def __repr__(self) -> str:
    #    return f"Matrix({self.__data}, {self.__shape})"

    def T(self): #check
        return Matrix([[self.__data[j][i] for j in range(self.__shape[1])] for i in range(self.__shape[0])])

class Vector(Matrix):
    def __init__(self, input: list | tuple):
        if isinstance(input, list):
            if not (len(input) == 1 or len(input[0]) == 1):
                raise ValueError("Vector must be a 1D list")
        elif isinstance(input, tuple):
            if not (input[0] == 1 or input[1] == 1):
                raise ValueError("Vector must be a 1D tuple")
        super().__init__(input)
    
    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Only vectors can be dot producted")
        if self.__shape != other.__shape:
            raise ValueError("Vectors have different shapes")
        return sum([[self.__data[i][j] * other.__data[j][i] for i in range(self.__shape[0])] for j in range(self.__shape[1])])