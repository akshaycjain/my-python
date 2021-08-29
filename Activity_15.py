def get_input():
    length=float(input("Enter length:"))
    bredth=float(input("Enter breadth:"))
    height=float(input("Enter height:"))
    return length,bredth,height
    
def find_volume(length,bredth,height):
    k=(length**2)+(bredth**2)+(height**2)
    v=((bredth**2)*(height**2))/(k**(1/2))
    return v

def find_radius(v):
    r=(((3*v)/(4*3.14159))**(1/3))
    return r

def display(v,r):
    print("Volume of tromboloid is %.3f\nRadius of sphere is %.3f"%(v,r))
    
def main():
    l,b,h=get_input()
    volume_of_tromboloid=find_volume(l,b,h)
    radius_of_sphere=find_radius(volume_of_tromboloid)
    display(volume_of_tromboloid,radius_of_sphere)
main()
