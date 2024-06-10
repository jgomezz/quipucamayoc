import math

# Angle in degrees
angle = 30
angle_radians = math.radians(angle)

lens = [84,175.5,264.5,353.5]

for len in lens:
   x1 = round(len * math.cos(angle_radians) \
        -  21.5 * math.sin(angle_radians),1)
   x2 = round(len * math.cos(angle_radians) \
        +  21.5 * math.sin(angle_radians),1)
   
   y1 = 400 - round(len * math.sin(angle_radians) \
        + 21.5 * math.cos(angle_radians),1)
   y2 = 400 - round(len * math.sin(angle_radians) \
        -  21.5 * math.cos(angle_radians),1)
   
   print(f"({x1},{y1} )  ({x2}, {y2})") 
   #print(len) 


