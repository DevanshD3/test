locations={
    0:"you are studying python in your computer",
    1:"you are standing on the road before a small brick building",
    2:"you are at the top of a hill",
    3:"you are inside the building",
    4:"you are in a valley behind the stream",
    5:"you are in a forest"
}

exits={
    0:  {"Q":0}, #the changes need not be made in the code since the list index was same as the dictionary key
    1:  {"W":2,"E":3,"N":5,"S":4,"Q":0},
    2:  {"N":5,"Q":0},
    3:  {"W":1,"Q":0},
    4:  {"N":1,"W":2,"Q":0},
    5:  {"S":1,"W":2,"Q":0}
}

vocab={"QUIT": "Q",
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W"
    }

loc=1
while True:
    avail=", ".join(exits[loc].keys())
    if loc==0:
        break
    # for direction in exits[loc].keys(): #direction takes the value of W E N S Q
    #     avail+=direction + "," #this simply means avail=avail+direction+"," and then change allot the value
    direction=input("Enter the direction, the availaible exits are "+avail+" ").upper() #upper is used to convert the input in upper case
    #WE NEED TO PASS THE INPUT IF NECESSARY
    if len(direction)>1:
        for word in vocab.keys():
            if word in direction: # if we wrote word==direction then only NORTH would have worked , here even GO NORTH works
                direction=vocab[word] #if NORTH is typed it allots the value of N to the direction variable
    print()
    if direction in exits[loc]:
        loc=exits[loc][direction] #this allots the value in the loc.
        print(locations[loc])
    else:
        print("no such location exists")
    