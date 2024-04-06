from matrix import Matrix, Vector

def test_generate_matrix():
    m1 = Matrix([[1, 2], [3, 4], [5, 6]])
    m2 = Matrix([[5, 6], [7, 8], [9, 10]])
    m3 = Matrix([[1, 2, 3], [4, 5, 6]])
    return m1, m2, m3

def test_generate_vector():
    v1 = Vector([[1, 2, 3]])
    v2 = Vector([[3], [4], [5]])
    #v3 = Vector([[1, 2], [3, 4]])
    return v1, v2

def test_matrix_method(m1, m2, m3):
    print("------------------test matrix methods----------------------")
    # add
    print(m1 + m2)  # radd?
    
    # sub
    print(m1 - m2)
    
    # mult
    print(m1 * m3)
    print(m3.__rmul__(m1))
    print(m1 * 10)
    print(10 * m1)

    # truediv
    # print(m1 / m2)    //TypeError: Only Division by a number is supported
    print(m1 / 2)
    print(m1 / 0.5)
    # print(m2 / 0)
    print(m1.__rtruediv__(10)) # TODO : check fix
    #m1[0][0] = 0
    print(m1.__rtruediv__(0))
    print()

    #.T
    print("-----------transpose-----------")
    print(m1)
    print(m2)
    print(m3)

    print(m1.T())
    print(m2.T())
    print(m3.T())

    print()

def test_vector_method(v1, v2):
    print("------------------test vector methods----------------------")
    v1.__str__()
    v2.__str__()
    print(v1 * v2)  # in fact it is the same as dot i guess..
    print(v1 * 10)
    print(v1 / 2)
    v3 = Vector([[3, 2, 1]])
    print(v1.dot(v3))

    print()

def test_matrix_vector_calculation():
    print("------------------test matrix and vector multiplication----------------------")
    m1 = Matrix([[1, 2, 3],
                [4, 5, 6]]) # 2 * 3
    v1 = Vector([[1], [2], [3]]) # 3 * 1
    v2 = Vector([[3, 2]]) # 1 * 2
    print(m1 * v1)  # why it calls rmul?
    print(v2 * m1)
    #print(v1 * v2) # it should generate Matrix; it is inconsistent with the project's definition..

def test():
    # generate 2 * 3 matrixs and 3 * 2 matrix
    m1, m2, m3 = test_generate_matrix()

    # generate 3 * 1 and 1 * 3 vector
    v1, v2 = test_generate_vector()

    test_matrix_method(m1, m2, m3)
    test_vector_method(v1, v2)
    test_matrix_vector_calculation()

test()