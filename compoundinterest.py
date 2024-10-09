def compound_interest(p, t, r):
    print("The principal amount is:", p)
    print("The time period is:", t)
    print("The rate of interest is:", r)
    
    Amount = p*(pow(1 + r / 100, t))
    ci = Amount - p

    print("The compound interest is", ci)
    return ci 


compound_interest(1000, 5, 10.25)   
