def Fibonacci(seq):
    if type(seq) != int:
        raise ValueError("Expecting integer")

    if seq==0 or seq == -1: 
        return 0

    if seq == 1:
        return 1

    return Fibonacci(seq-2) + Fibonacci(seq-1)
