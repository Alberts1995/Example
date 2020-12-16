def boolean(x, y, operation):
    if operation == "conjunction":
        if x == 0:
            return(0)
        elif y ==  0:
            return(0)
        else:
            return(1)
    elif operation == "disjunction":
        if x == 1:
            return(1)
        elif y ==  1:
            return(1)
        else:
            return(0)
    elif operation == "implication":
        if x == y:
            return(1)
        elif x < y:
            return(1)
        else:
            return(0)
    elif operation == "exclusive":
        if x == y:
            return(0)
        else:
            return(1)
    elif operation == "equivalence":
        if x == y:
            return(1)
        else:
            return(0)


boolean(0, 1, "implication") 

