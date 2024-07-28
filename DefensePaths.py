import math, random
from panda3d.core import *


def DrawCloud(radius = 7):
    x = 2 * random.random() - 1 #creates random x
    y = 2 * random.random() - 1 #creates random y
    z = 2 * random.random() - 1 #creates random z

    unitVec = Vec3(x, y, z) #creates a vector3 position called unitVec using x y z
    #unitVec.Normalize() #normalizes unitVec to fix math mistakes
    unitVecReturn = unitVec * radius
    return unitVecReturn #returns value 

def BaseballSeams(step, numSeams, B, F = 1):
    time = step / float(numSeams) * 2 * math.pi

    F4 = 0
    R = 1

    xxx = math.cos(time) - B * math.cos(3 * time)
    yyy = math.sin(time) + B * math.sin(3 * time)
    zzz = F * math.cos(2 * time) + F4 * math.cos(4 * time)

    rrr = math.sqrt(xxx ** 2 + yyy ** 2 + zzz ** 2)
    
    x = R * xxx / rrr
    y = R * yyy / rrr
    z = R * zzz / rrr

    xyz = Vec3(x, y, z)
   

    return xyz

def XSeams(step, numSeams, B, F = 1, radius = 1):
    time = step / float(numSeams) * 2 * math.pi

    xxx = math.cos(time) - B * math.cos(3 * time)
    yyy = math.sin(time) + B * math.sin(3 * time)
    zzz = 0

    #rrr = math.sqrt(xxx ** 2 + yyy ** 2 + zzz ** 2)
    
    x = radius * xxx 
    y = radius * yyy 
    z = radius * zzz 

    xyz = Vec3(x, y, z)
   
    return xyz

def YSeams(step, numSeams, B, F = 1, radius = 1):
    time = step / float(numSeams) * 2 * math.pi

    zzz = math.cos(time) - B * math.cos(3 * time)
    xxx = math.sin(time) + B * math.sin(3 * time)
    yyy = 0

    #rrr = math.sqrt(xxx ** 2 + yyy ** 2 + zzz ** 2)
    
    x = radius * xxx 
    y = radius * yyy 
    z = radius * zzz 

    xyz = Vec3(x, y, z)
   
    return xyz

def ZSeams(step, numSeams, B, F = 1, radius = 1):
    time = step / float(numSeams) * 2 * math.pi

    yyy = math.cos(time) - B * math.cos(3 * time)
    zzz = math.sin(time) + B * math.sin(3 * time)
    xxx = 0

    #rrr = math.sqrt(xxx ** 2 + yyy ** 2 + zzz ** 2)
    
    x = radius * xxx 
    y = radius * yyy 
    z = radius * zzz 

    xyz = Vec3(x, y, z)
   
    return xyz