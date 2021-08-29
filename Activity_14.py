def input_number():
    num=input("Enter a number:")
    return num
    
def check(num):
    yes=0
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                yes=1
            break
    return yes

def display(v,num):
    if v==1:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

def main():
    num=int(input_number())
    v=check(num)
    display(v,num)
    
main()
