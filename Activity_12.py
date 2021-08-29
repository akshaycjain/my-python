def input_number():
    s=input()
    ns=s.split(' ')
    return ns[0],ns[1],ns[2]

def compare(a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b 
    else:
        return c
        
def display(a, b, c, greatest):
    print('{0} is the greatest number among {1},{2} and {3}'.format(greatest,a,b,c))


def main():
    n1,n2,n3 = input_number()
    greatest_num = compare(n1, n2, n3)
    display(n1, n2, n3, greatest_num)
main()
