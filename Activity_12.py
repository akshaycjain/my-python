def input_numbers():
    s=input()
    ns=s.split(' ')
    return ns

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
    n1,n2,n3 = input_numbers()
    greatest_num = compare(n1, n2, n3)
    display(n1, n2, n3, greatest_num)
main()
