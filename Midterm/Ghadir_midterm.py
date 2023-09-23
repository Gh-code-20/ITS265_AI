"""
Ghadir Alfadhl

"""
import random
#import numpy as np
# 1 is the wall
# 0 is room that robot can visit

TaskEnvModel = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]]

class Robot:
    
    def __init__(self, x, y):
        self.positionX = x
        self.positionY = y
        self.EnergyConsumed = 0

        # Sensor values.
        self.LeftSensor = 0
        self.RightSensor = 0
        self.FrontSensor = 0
        self.DirtSensor = 0
        
        self.b=[]
        
        self.Orientation = "North"
        
        self.AllCellsCleaned = False
        self.count = 0
    
    def Perceive(self):
        # Set sensors when robot is facing North
        if self.Orientation == "North":
            self.LeftSensor = TaskEnvModel[self.positionX][self.positionY-1]
            self.RightSensor = TaskEnvModel[self.positionX][self.positionY+1]
            self.FrontSensor = TaskEnvModel[self.positionX-1][self.positionY]
            self.DirtSensor = TaskEnvModel[self.positionX][self.positionY]
            print("\nEnvironment was perceived at position [" + 
                str(self.positionX) + "][" + str(self.positionY) + "]" +
                "\nFront=[" + str(self.positionX) + "][" + 
                str(self.positionY+1) + "]")
            
        elif self.Orientation == "East":
            self.LeftSensor = TaskEnvModel[self.positionX-1][self.positionY]
            self.RightSensor = TaskEnvModel[self.positionX+1][self.positionY]
            self.FrontSensor = TaskEnvModel[self.positionX][self.positionY+1]
            self.DirtSensor = TaskEnvModel[self.positionX][self.positionY]
            print("\nEnvironment was perceived at position [" + 
                str(self.positionX) + "][" + str(self.positionY) + "]" +
                "\nFront=[" + str(self.positionX) + "][" + 
                str(self.positionY+1) + "]")
            
        elif self.Orientation == "South":
            self.LeftSensor = TaskEnvModel[self.positionX][self.positionY+1]
            self.RightSensor = TaskEnvModel[self.positionX][self.positionY-1]
            self.FrontSensor = TaskEnvModel[self.positionX+1][self.positionY]
            self.DirtSensor = TaskEnvModel[self.positionX][self.positionY]
            print("\nEnvironment was perceived at position [" + 
                str(self.positionX) + "][" + str(self.positionY) + "]" +
                "\nFront=[" + str(self.positionX) + "][" + 
                str(self.positionY+1) + "]")
            
        elif self.Orientation == "West":
            self.LeftSensor = TaskEnvModel[self.positionX+1][self.positionY]
            self.RightSensor = TaskEnvModel[self.positionX-1][self.positionY]
            self.FrontSensor = TaskEnvModel[self.positionX][self.positionY-1]
            self.DirtSensor = TaskEnvModel[self.positionX][self.positionY]
            print("\nEnvironment was perceived at position [" + 
                str(self.positionX) + "][" + str(self.positionY) + "]" +
                "\nFront=[" + str(self.positionX) + "][" + 
                str(self.positionY+1) + "]")
            
            
    def MoveRobot(self):
        a = random.randint(1,2)
        # if robot orientation is north.
        if self.Orientation == "North":
            if self.FrontSensor == 0 or self.FrontSensor == 2:
                self.positionX = self.positionX - 1
                self.positionY = self.positionY
                self.Orientation == "North"
                print("Robot moved North to position ["  +  
                      str(self.positionX) + "][" + str(self.positionY) + "]")
                print("Robot Orientation = " + self.Orientation)  
                self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                print("Robot have been moved to follow position = " + str(self.b))
    
            
            elif self.RightSensor == 0 or self.RightSensor == 2:
                self.positionX = self.positionX
                self.positionY = self.positionY+1
                self.Orientation = "East"  # new orientation of robot
                print("Robot moved East to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")
                print("New Robot orientation = " + self.Orientation)     
                self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                print("Robot have been moved to follow position = " + str(self.b))
            
            elif self.LeftSensor == 0 or self.LeftSensor == 2:
                self.positionX = self.positionX
                self.positionY = self.PositionY - 1
                self.Orientation = "West"
                print("Robot moved West to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")
                print("New Robot orientation = " + self.Orientation)      
                self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                print("Robot have been moved to follow position = " + str(self.b))


        # if robot orientation is south
        elif self.Orientation == "South":
            if self.FrontSensor == 0 or self.FrontSensor == 2:
                self.positionX = self.positionX + 1
                self.positionY = self.positionY 
                self.Orientation == "South"
                print("Robot moved South to position ["  +  
                      str(self.positionX) + "][" + str(self.positionY) + "]")
                print("New Robot orientation = " + self.Orientation)                
                self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                print("Robot have been moved to follow position = " + str(self.b))
            
            # if front sensor == 1, test right sensor
            elif self.RightSensor == 0 or self.RightSensor == 2:
                self.positionX = self.positionX 
                self.positionY = self.positionY - 1 
                self.Orientation = "West"
                print("Robot moved West to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")               
                print("New Robot orientation = " + self.Orientation)     
                self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                print("Robot have been moved to follow position = " + str(self.b))
                
            # if front sensor == 1 and right sensor == 1, test left
            elif self.LeftSensor == 0 or self.LeftSensor == 2:
                self.positionX = self.positionX  
                self.positionY = self.PositionY + 1
                self.Orientation = "East"
                print("Robot moved East to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")               
                print("New Robot orientation = " + self.Orientation)       
                self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                print("Robot have been moved to follow position = " + str(self.b))

                
        # if robot orientation is west
        elif self.Orientation == "West":
            if self.FrontSensor == 0 or self.FrontSensor == 2:
                self.positionX = self.positionX
                self.positionY = self.positionY -1
                self.Orientation == "West"
                print("Robot moved West to position ["  +  
                      str(self.positionX) + "][" + str(self.positionY) + "]")
                print("New Robot orientation = " + self.Orientation)   
                self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                print("Robot have been moved to follow position = " + str(self.b))
                
            
            # if front sensor == 1, test right sensor
            elif self.RightSensor == 0 or self.RightSensor == 2:
                self.positionX = self.positionX - 1
                self.positionY = self.positionY
                self.Orientation = "North"
                print("Robot moved North to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")               
                print("New Robot orientation = " + self.Orientation)   
                self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                print("Robot have been moved to follow position = " + str(self.b))
                
            # if front sensor == 1 and right sensor == 1, test left
            elif self.LeftSensor == 0 or self.LeftSensor == 2:
                self.positionX = self.positionX + 1 
                self.positionY = self.PositionY
                self.Orientation = "South"
                print("Robot moved South to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")               
                print("New Robot orientation = " + self.Orientation)  
                self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                print("Robot have been moved to follow position = " + str(self.b))
            
                  
            
        # if robot orientation is east
        elif self.Orientation == "East":
            if self.FrontSensor == 0 and a ==1 or self.FrontSensor == 2 and a ==1:
                self.positionX = self.positionX
                self.positionY = self.positionY + 1
                self.Orientation == "East"
                print("Robot moved East to position ["  +  
                      str(self.positionX) + "][" + str(self.positionY) + "]")
                print("New Robot orientation = " + self.Orientation)      
                self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                print("Robot have been moved to follow position = " + str(self.b))
            
            elif self.FrontSensor == 0 and a ==2 or self.FrontSensor == 2 and a ==2:
                if self.RightSensor == 1:
                    self.positionX = self.positionX
                    self.positionY = self.positionY + 1
                    self.Orientation == "East"
                    print("Robot moved East to position ["  +  
                          str(self.positionX) + "][" + str(self.positionY) + "]")
                    print("New Robot orientation = " + self.Orientation)      
                    self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                    print("Robot have been moved to follow position = " + str(self.b))
                elif self.RightSensor == 0 or self.RightSensor == 2:
                    print("randomly move to the right spot")
                    self.positionX = self.positionX +1
                    self.positionY = self.positionY 
                    self.Orientation == "East"
                    print("Robot moved East to position ["  +  
                          str(self.positionX) + "][" + str(self.positionY) + "]")
                    print("New Robot orientation = " + self.Orientation)     
                    self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                    print("Robot have been moved to follow position = " + str(self.b))
                
                
            
            # if front sensor == 1, test right sensor
            elif self.RightSensor == 0 or self.RightSensor == 2:
                self.positionX = self.positionX + 1
                self.positionY = self.positionY
                self.Orientation = "South"
                print("Robot moved South to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")               
                print("New Robot orientation = " + self.Orientation)    
                self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                print("Robot have been moved to follow position = " + str(self.b))
                
            # if front sensor == 1 and right sensor == 1, test left
            elif self.LeftSensor == 0 or self.LeftSensor == 2:
                self.positionX = self.positionX - 1 
                self.positionY = self.PositionY
                self.Orientation = "North"
                print("Robot moved North to position ["  +  
                    str(self.positionX) + "][" + str(self.positionY) + "]")
                print("New Robot orientation = " + self.Orientation)      
                self.b.append('['+str(self.positionX)+','+str(self.positionY)+']')
                print("Robot have been moved to follow position = " + str(self.b))
                  
        
def main():
    
    # Instantiate Robot object.
    robot1 = Robot(1,1)
    
    
    #while robot1.AllCellsCleaned == False:
    # test for two movements
    while robot1.count <10:
        # Perceive the environment from the robot's initial position.        
        robot1.Perceive()
        # Clean at current position.
        robot1.MoveRobot()
        # count robot movements
        robot1.count = robot1.count + 1
        
    print('when robot is going east and only going to east, it will randomly jump to right by one spot when there is no wall at the right side')
if __name__ == "__main__":
    main()

        
            