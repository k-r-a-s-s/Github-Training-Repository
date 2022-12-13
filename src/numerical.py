def bumpy_reduction(x,recursions = 5):
    """Recursive chaos function."""
    if type(recursions) != int or recursions < 0:
        raise NotImplementedError('fib only defined on non-negative integers.')
    if type(recursions) != int or recursions < 0:
        raise NotImplementedError('fib only defined on non-negative integers.')
    elif recursions == 0:
        return x
    else:
        return bumpy_reduction(x/2 + recursions**2, recursions - 1)



    



# write test fucntion



