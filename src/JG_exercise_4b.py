# JG
# September 29, 2024
# The program contains several lines of code from the book

def avg(units, *args):
    print (sum(args) / len(args), units)

def pr_named_vals(**kwargs):
    for k in kwargs:
        print(k, ':', kwargs[k])

def pr_vals_2(*args, **kwargs):
    for i in args:
        print(i)
    for k in kwargs:
        print(k, ':', kwargs[k])

def main():
    avg('inches', 11, 22, 33)
    print(10, 20, 30, end='.', sep=',')
    pr_named_vals(a=10, b=20, c=30)
    pr_vals_2(1, 2, 3, -4, a=10, b=200)

main()
