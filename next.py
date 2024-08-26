import random
#room of 4*4 
room =[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
#function to display rooms
def display_room(room):
 for row in room:
  print(row)
  print("initially all rooms are dirty")
  display_room(room)
  #introduce dirt[0] clean[1]
  for x in range(4):
   for y in range (4):
    room [x][y]= random.choice([0,1])
    #modelling the vaccum cleaner
    dirt_rooms=0
    for x in range(4):
     for y in range(4):
      if room[x][y]==1:
       print("cleaning the room")
       room[x][y]=0
       dirt_rooms +=1
       #calculate performance
       performance=(100-(dirt_rooms/16))*1000
       print(f"performance:{performance}")
       print("\nFinal room status after cleaning:")
       display_room(room)
       