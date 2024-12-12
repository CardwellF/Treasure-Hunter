#imports
import random
import keyboard

'''
Total classes = 5
1. GameMap | search_room get_room_type
2. Player | damage heal
3. User(player, GameMap) | move_user 
4. Enemy(player, GameMap) |move_enemy
5. Game(User, Enemy, GameMap) | start play finish
'''

'''Player (Parent Class)'''
class Player:
    #class initialisation
    def __init__(self):
        self.health = 100 #player health
        self.inventory={"money": 0, "locate": 0} #player inventory
    #damage message
    def damage(self):
        self.health -= random.randint(10,30)#remove health

'''GameMap (SubClass)'''
class GameMap(Player):
    #class initialisation
    def __init__(self):
        super().__init__()
        #game map
        self.Gmap = [
            [[8,9,"start"],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]]
        ]
    
    #room type method
    def get_room_type(self):
        for x in self.Gmap:#checks rows
            for y in self.Gmap[x]:#checks column positions in row
                if self.Gmap[x][y][2] == False: #checks tile to see if False
                    self.room = random.randint(1,2)#random number
                    if self.room == 1:#checks random number is 1
                        self.Gmap[x][y][2] = "empty_room" #room set to empty on Gmap
                        self.search_room()#search room method
                    elif self.room == 2:#checks random number is 1
                        self.room=random.randint(1,3)#random number
                        if self.room == 1:#checks random number is 1
                            self.Gmap[x][y] = "treasure"#room set to treasure on Gmap
                            self.search_room()#search room method
                        elif self.room ==2:#checks random number is 2
                            self.Gmap[x][y] = "PowerUP"#room set to PowerUP on Gmap
                            self.search_room()#search room method
                        else:#checks random number is 3
                            self.Game[x][y] = "Trap"#room set to Trap on Gmap
                            self.search_room()#search room method
                elif self.Gmap[x][y] != "false":#checks tile to see if not False
                    self.search_room()#search room method
    
    #search room method
    def search_room(self):
         for x in self.Gmap:#checks rows
            for y in self.Gmap[x]:#checks column positions in row
                if self.Gmap[x][y][0] == 8:#check if loaction of player
                    if self.Gmap[x][y][2] == "empty_room":#checks game map index for empty room
                        print("room empty")#print room empty
                    elif self.Gmap[x][y][2] == "treasure":#checks game map index for treasure
                        self.money = random.ranit(100, 150)
                        self.inventory['money'] += self.money#update inventory money value
                        self.Gmap[x][y][2] == "empty_room"#updates GMap as room looted 
                        numberEmptyRooms += 1#number of empty rooms increased
                    elif self.Gmap[x][y][2] == "PowerUP":#checks game map index for PowerUP
                        self.inventory['locate'] += 1#update inventory locate value
                        self.Gmap[x][y][2] == "empty_room"#updates GMap as room looted 
                        numberEmptyRooms += 1#number of empty rooms increased
                    else:#if room is trap room
                        self.damage()#take damage
                elif self.Gmap[x][y][1] == 9:#check if location of enemy player
                    if self.Gmap[x][y][2] == "empty_room":#checks game map index for empty room
                        return "room empty"#return room empty
                    elif self.Gmap[x][y][2] == "treasure":#checks game map index for treasure
                        self.money = random.ranit(100, 150)#generate random amaount of money
                        self.inventory['money'] += self.money#update inventory money value
                        self.Gmap[x][y][2] == "empty_room"#updates GMap as room looted 
                    elif self.Gmap[x][y][2] == "PowerUP":#checks game map index for PowerUP
                        self.inventory['locate'] += 1#update inventory locate value
                        self.Gmap[x][y][2] == "empty_room"#updates GMap as room looted 
                    elif self.Gmap[x][y][2] == "start":# checks game map index for start
                         print("search not posible")# prints error message
                    else:#if room is trap room
                        self.enemy_damage()#if room is trap room

'''User (SubClass)'''
class User(Player, GameMap):
    #class initialisation
    def __init__(self):
        super().__init__()
    
    #get player position
    def get_player_pos(self):
        for x in self.Gmap:
            for y in self.Gmap[x]:
                if self.Gmap[x][y][0] == 8:
                    self.User_position = (x,y)
    
    #move user based on keyboard input
    def move_user(self, direction):
        for x in self.Gmap:
            for y in self.Gmap[x]:
                if x == 0 and self.Gmap[x][y][1] == 8 and direction == "up":
                    print("You are at the top of the map Unable to Move UP")
                    return "Fail"
                elif x != 0 and self.Gmap[x][y][1] == 8 and direction == "up":
                    self.User_position = (x-1, y)
                    self.Gmap[x][y][0] = 0
                    self.Gmap[x-1][y][0] = 8
    
    #use powerup method
    def use_PowerUP(self):
        if self.inventory['locate'] != 0:
            PowerUP = "Active"
            self.inventory['locate'] -= 1
            self.find_none_search()
        else:
            print("you have no locate PowerUP's")
    
    #display inventory method
    def display_inventory(self):
        for key, value in self.inventory:
            print(f"{key} | {value}")
        print("press any 't' to use item")
        if keyboard.is_pressed("t"):
            self.use_PowerUP()
    
    #find enemy method
    def find_none_search(self):
        #start position
        start = self.User_position
        #get end position
        for x in self.Gmap:
            for y in self.Gmap[x]:
                if self.Gmap[x][y][2] == False:
                    end = self.Gmap[x][y]
        #depth first search for shortest path to next identified room
        rows, columns = len(self.Gmap), len(self.Gmap[x])#rows and columns set
        stack = [(self.User_position, [self.User_positiion)]#set up stack
        visited = set()#create visited set
        #while stack 
        while stack:
            (x, y), path = stack.pop()#path set
            #if co-ordinated visited
            if (x, y) in visited:
                continue
            #add co-ordinates to visited
            visited.add((x, y))
            #if co-ordinates = end position
            if (x, y) == end:
                print("path: ", path)#print path
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                    stack.append(((nx, ny), path + [(nx, ny)]))
        print("end not found")

'''Enemy(SubClass)'''
class Enemy(GameMap):
    #class initialisation
    def __init__(self):
        super().__init__()
        self.Ehealth = 100
        self.Einventory={"money": 0, "locate": 0} #enemy inventory
    
    #enemy movement method
    def move_enemy(self):
        z = 1
        for x in self.Gmap:
            for y in self.Gmap[x]:
                if self.Gmap[x][y][z] == 9:
                    self.enemy_position = (x,y)
                    if x == 0:#checks if player at top of map
                        if y == 0:#checks player at left most side of map
                            #checks if trap is south of player and right is clear
                            if self.Gmap[x+1][y][2] == "Trap" and self.Gmap[x][y+1][2]!= "Trap":
                                    #updates enemy position right
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if trap is right of player and south is clear
                            elif self.Gmap[x][y+1][2] == "Trap" and self.Gmap[x+1][y][2] != "Trap":
                                    #updates enemy position south
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x+1][y][1] = 9
                                    self.enemy_position = (x+1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is south of player and right is explored
                            elif self.Gmap[x+1][y][2] == False and self.Gmap[x][y+1][2] != False:
                                    #updates enemy position south
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x+1][y][1] = 9
                                    self.enemy_position = (x+1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is right of player and south is explored
                            elif self.Gmap[x][y+1][2] == False and self.Gmap[x+1][y][2] != False:
                                    #updates enemy position right
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if all moveable sides are trapped
                            elif self.Gmap[x+1][y][2] == "Trap" and self.Gmap[x][y][2] == "Trap":
                                    #updates enemy position right
                                    self.gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #enemy damage method
                                    a = self.enemy_damage()
                                    return a
                            #anything else move right
                            else:
                                    #updates enemy position right
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                        elif y == 9:#checks if user right most side of map
                            #checks if trap is south of player and left is clear
                            if self.Gmap[x+1][y][2] == "Trap" and self.Gmap[x][y-1][2]!= "Trap":
                                    #updates enemy position left
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if trap is left of player and south is clear
                            elif self.Gmap[x][y-1][2] == "Trap" and self.Gmap[x+1][y][2] != "Trap":
                                    #updates enemy position south
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x+1][y][1] = 9
                                    self.enemy_position = (x+1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is south of player and left is explored
                            elif self.Gmap[x+1][y][2] == False and self.Gmap[x][y-1][2] != False:
                                    #updates enemy position south
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x+1][y][1] = 9
                                    self.enemy_position = (x+1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is left of player and south is explored
                            elif self.Gmap[x][y-1][2] == False and self.Gmap[x+1][y][2] != False:
                                    #updates enemy position left
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if all moveable sides are trapped
                            elif self.Gmap[x+1][y][2] == "Trap" and self.Gmap[x][y][2] == "Trap":
                                    #updates enemy position left
                                    self.gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #enemy damage method
                                    a = self.enemy_damage()
                                    return a
                            #anything else move left
                            else:
                                    #updates enemy position left
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                        else:
                             #checks if trap is south of player and right is clear
                            if self.Gmap[x+1][y][2] == "Trap" and self.Gmap[x][y+1][2]!= "Trap":
                                    #updates enemy position right
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if trap is right of player and south is clear
                            elif self.Gmap[x][y+1][2] == "Trap" and self.Gmap[x+1][y][2] != "Trap":
                                    #updates enemy position south
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x+1][y][1] = 9
                                    self.enemy_position = (x+1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is south of player and right is explored
                            elif self.Gmap[x+1][y][2] == False and self.Gmap[x][y+1][2] != False:
                                    #updates enemy position south
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x+1][y][1] = 9
                                    self.enemy_position = (x+1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is right of player and south is explored
                            elif self.Gmap[x][y+1][2] == False and self.Gmap[x+1][y][2] != False:
                                    #updates enemy position right
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if all moveable sides are trapped
                            elif self.Gmap[x+1][y][2] == "Trap" and self.Gmap[x][y][2] == "Trap":
                                    #updates enemy position right
                                    self.gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #enemy damage method
                                    a = self.enemy_damage()
                                    return a
                            #checks if trap is south of player and left is clear
                            elif self.Gmap[x+1][y][2] == "Trap" and self.Gmap[x][y-1][2]!= "Trap":
                                    #updates enemy position left
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if trap is left of player and south is clear
                            elif self.Gmap[x][y-1][2] == "Trap" and self.Gmap[x+1][y][2] != "Trap":
                                    #updates enemy position south
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x+1][y][1] = 9
                                    self.enemy_position = (x+1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is south of player and left is explored
                            elif self.Gmap[x+1][y][2] == False and self.Gmap[x][y-1][2] != False:
                                    #updates enemy position south
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x+1][y][1] = 9
                                    self.enemy_position = (x+1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is left of player and south is explored
                            elif self.Gmap[x][y-1][2] == False and self.Gmap[x+1][y][2] != False:
                                    #updates enemy position left
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if all moveable sides are trapped
                            elif self.Gmap[x+1][y][2] == "Trap" and self.Gmap[x][y][2] == "Trap":
                                    #updates enemy position left
                                    self.gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #enemy damage method
                                    a = self.enemy_damage()
                                    return a
                            #anything else move left
                            else:
                                    #updates enemy position left
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                    if x == 9:#checks if enemy at bottom of map
                        if y == 0:#checks player at left most side of map
                            #checks if trap is north of player and right is clear
                            if self.Gmap[x-1][y][2] == "Trap" and self.Gmap[x][y+1][2]!= "Trap":
                                    #updates enemy position right
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if trap is right of player and north is clear
                            elif self.Gmap[x][y+1][2] == "Trap" and self.Gmap[x-1][y][2] != "Trap":
                                    #updates enemy position north
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x-1][y][1] = 9
                                    self.enemy_position = (x-1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is north of player and right is explored
                            elif self.Gmap[x-1][y][2] == False and self.Gmap[x][y+1][2] != False:
                                    #updates enemy position north
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x-1][y][1] = 9
                                    self.enemy_position = (x-1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is right of player and north is explored
                            elif self.Gmap[x][y+1][2] == False and self.Gmap[x-1][y][2] != False:
                                    #updates enemy position right
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if all moveable sides are trapped
                            elif self.Gmap[x-1][y][2] == "Trap" and self.Gmap[x][y][2] == "Trap":
                                    #updates enemy position right
                                    self.gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #enemy damage method
                                    a = self.enemy_damage()
                                    return a
                            #anything else move right
                            else:
                                    #updates enemy position right
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                        elif y == 9:#checks if user right most side of map
                            #checks if trap is north of player and left is clear
                            if self.Gmap[x-1][y][2] == "Trap" and self.Gmap[x][y-1][2]!= "Trap":
                                    #updates enemy position left
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if trap is left of player and north is clear
                            elif self.Gmap[x][y-1][2] == "Trap" and self.Gmap[x-1][y][2] != "Trap":
                                    #updates enemy position north
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x-1][y][1] = 9
                                    self.enemy_position = (x-1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is north of player and left is explored
                            elif self.Gmap[x-1][y][2] == False and self.Gmap[x][y-1][2] != False:
                                    #updates enemy position north
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x-1][y][1] = 9
                                    self.enemy_position = (x-1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is left of player and north is explored
                            elif self.Gmap[x][y-1][2] == False and self.Gmap[x-1][y][2] != False:
                                    #updates enemy position left
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if all moveable sides are trapped
                            elif self.Gmap[x+1][y][2] == "Trap" and self.Gmap[x][y][2] == "Trap":
                                    #updates enemy position left
                                    self.gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #enemy damage method
                                    a = self.enemy_damage()
                                    return a
                            #anything else move left
                            else:
                                    #updates enemy position left
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                        else:
                             #checks if trap is north of player and right is clear
                            if self.Gmap[x-1][y][2] == "Trap" and self.Gmap[x][y+1][2]!= "Trap":
                                    #updates enemy position right
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if trap is right of player and north is clear
                            elif self.Gmap[x][y+1][2] == "Trap" and self.Gmap[x-1][y][2] != "Trap":
                                    #updates enemy position north
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x-1][y][1] = 9
                                    self.enemy_position = (x-1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is north of player and right is explored
                            elif self.Gmap[x-1][y][2] == False and self.Gmap[x][y+1][2] != False:
                                    #updates enemy position north
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x-1][y][1] = 9
                                    self.enemy_position = (x-1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is right of player and north is explored
                            elif self.Gmap[x][y+1][2] == False and self.Gmap[x-1][y][2] != False:
                                    #updates enemy position right
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if all moveable sides are trapped
                            elif self.Gmap[x-1][y][2] == "Trap" and self.Gmap[x][y][2] == "Trap":
                                    #updates enemy position right
                                    self.gmap[x][y][1] = 0
                                    self.Gmap[x][y+1][1] = 9
                                    self.enemy_position = (x, y+1)
                                    #enemy damage method
                                    a = self.enemy_damage()
                                    return a
                            #checks if trap is north of player and left is clear
                            elif self.Gmap[x-1][y][2] == "Trap" and self.Gmap[x][y-1][2]!= "Trap":
                                    #updates enemy position left
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if trap is left of player and north is clear
                            elif self.Gmap[x][y-1][2] == "Trap" and self.Gmap[x-1][y][2] != "Trap":
                                    #updates enemy position north
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x-1][y][1] = 9
                                    self.enemy_position = (x-1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is north of player and left is explored
                            elif self.Gmap[x-1][y][2] == False and self.Gmap[x][y-1][2] != False:
                                    #updates enemy position north
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x-1][y][1] = 9
                                    self.enemy_position = (x-1, y)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if Unexplored(False) is left of player and north is explored
                            elif self.Gmap[x][y-1][2] == False and self.Gmap[x-1][y][2] != False:
                                    #updates enemy position left
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
                            #checks if all moveable sides are trapped
                            elif self.Gmap[x+1][y][2] == "Trap" and self.Gmap[x][y][2] == "Trap":
                                    #updates enemy position left
                                    self.gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #enemy damage method
                                    a = self.enemy_damage()
                                    return a
                            #anything else move left
                            else:
                                    #updates enemy position left
                                    self.Gmap[x][y][1] = 0
                                    self.Gmap[x][y-1][1] = 9
                                    self.enemy_position = (x, y-1)
                                    #gets room type method
                                    self.get_room_type()
                                    return True
    #enemy damage method
    def enemy_damage(self):
        self.new_Ehealth = self.Ehealth - random.randint(10,30)#creates temporary health variable
        if self.new_Ehealth <= 0:
            return "Enemy loses"
        else:
            self.Ehealth = self.new_Ehealth #sets Ehealth to the temporary health variable
            return True
                            
'''game (SubClass)'''
class game(Enemy, User, GameMap):
    #class initalising
    def __init__(self):
        super().__init__()
        self.specific_key = "c" #sets 'hot-key' to c
        self.setup = keyboard.read_event() #read events
        self.turn = 1#sets initial turn
        self.moved  = False#sets moved to false
        self.controls = {"up": "w", "down": "s", "left": "a", "right": "d", "inventory": "e", "controls": "c", "search": "r", "return": "b"}#controls dictionary
        self.map_reset = [#map reset
            [[8,9,"start"],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]],
            [[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False],[0,0,False]]
        ]
    
    #start game method
    def start_game(self):
        self.Gmap = self.map_reset#sets map to the reset map
        print("press c to view controls else press any other key")#start instructions
        if self.setup.event_type == keyboard.KEY_DOWN and self.setup.name != self.specific_key:#checks what key is pressed
            self.play()#play method called
        else:
            self.view_controls("start")
    
    #view controls method
    def view_controls(self, area):
        for key, value in self.controls:
            print(f"{key} | {value}")
        #checks if back button presses
        if keyboard.is_pressed("b"):
            if area == "player":
                self.PlayerTurn()
            else:
                self.start_game()    
    
    #PlayerTurn method
    def PlayerTurn(self):
        while self.moved == False and self.turn % 2 != 0:
            if keyboard.is_pressed("e"):#e is presses
                self.display_inventory("player")#display inventory
            if keyboard.is_pressed("c"):#c is presses
                self.view_controls("player")#display controls
            if keyboard.is_pressed("r"):#r is presses
                self.get_room_type()#search rooms after assigning room a type
            if keyboard.is_pressed("w"):#w is presses
                self.moved = self.move_user("up")#move player up
                if self.moved == True:
                    self.turn += 1
            if keyboard.is_pressed("s"):#s is presses
                self.moved = self.move_user("down")#move player down
                if self.moved == True:
                    self.turn += 1
            if keyboard.is_pressed("a"):#a is presses
                self.moved = self.move_user("left")#move player left
                if self.moved == True:#checks if move is good
                    self.turn += 1#adds one to turn
            if keyboard.is_pressed("d"):#d is presses
                self.moved = self.move_user("right")#move player right
                if self.moved == True:#checks if move is good
                    self.turn += 1#adds one to turn
            if self.moved == "player_lose":#checks if player lost during move
                self.check_victory()#calls for lose message
    
    #EnemyTurn method
    def EnemyTurn(self):
        self.Emoved = False # enemy make move false
        while self.Emoved == False and self.turn % 2 == 0:#while move not made and enemy turn is true
            self.Emoved = self.move_enemy()#enemy moves
            if self.Emoved == "enemy_lose":#checks if enemy lost during move
                self.check_victory()#call for victory message
    
    #Play method
    def play(self):
        global numberEmptyRooms
        numberEmptyRooms = 0 #sets empty room to 0
        #checks if any empty rooms exist
        for x in self.Gmap:
            for y in self.Gmap[x]:
                #if empty room exist
                if self.Gmap[x][y][2] == "empty_room":
                    numberEmptyRooms+=1#add 1 to empty rooms
        while self.turns<=100 and numberEmptyRooms != 99:
            self.PlayerTurn()
            self.EnemyTurn()
    
    #check victory method
    def check_victory(self):
        if self.Emoved == "enemy_lose" or self.inventory.get('money') > self.Einventory.get('money'):
            print("YOU WIN")
            self.turn = 1
            self.start()
        elif self.moved == "player_lose" or self.inventory.get('money') < self.Einventory.get('money'):
            print("YOU LOSE")
            self.turn = 1
            self.start()
        else:
            print("DRAW")
            self.turn = 1
            self.start()
        
