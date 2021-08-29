def start_input():
    s=input("Enter the start number:")
    return s

def stop_input():
    e=input("Enter the stop number:")
    return e
    
def display(s,e):
    while s<e:
        print(s,end=', ')
        s=s+2
    print(s)

def main():
    start=int(start_input())
    stop=int(stop_input())
    if(start%2==0):
        start=start+1
    if(stop%2==0):
        stop=stop-1
    display(start, stop)
main()
