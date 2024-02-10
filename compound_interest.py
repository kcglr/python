principal = int(input("enter the initial amount: "))
rate = float(input("enter the interest rate: "))
numyears = int(input("enter the number of years you are planning on investing: "))
year = 1

while year <= numyears:
    principal = principal * (1 + rate) 
    print(f'{year:>3d} {principal:0.2f}')
    ### F-STRING ###
    #'0.2f' means a floating-point number with two decimal places of accuracy.
    #'>3d' means a three-digit decimal number, right aligned.
    year += 1

