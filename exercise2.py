
def teilbar(x, y):
    if y==0:
        print("es ist nicht möglich durch Null zu teilen") # erste Bedingung die geprüft wird, sind im
    elif y ==x:
        print("x und y sind gleich") 
    else:
        if x%y == 0:
            print("x ist durch y teilbar")
        else:
            print ("x ist nicht durch y teilbar")
            
            
teilbar(x=4, y=2)
