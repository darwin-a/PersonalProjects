## This code will model chaotic scattering in a 3 disk system

from numpy import *
import matplotlib.pyplot as plt
import time as time

#########################################################################################################
###### This Portion Is For The RunTimeWarning Created By Complex Numbers in IntersectTimes Function######
#########################################################################################################
import warnings

warnings.simplefilter("ignore", RuntimeWarning)
    
######################################
######FUNCTIONS FOR PROGRAM###########
######################################

def Intersect(xcoordinates,ycoordinates,paramsr,theta,x0,y0): # This function returns the minimum intersection time and circle hit and intersection points
    
    #########FINDING LEAST TIME###############
    
    numintersects = numdisks * 2 # we intersect at each disk twice
    timeintersect = zeros(numintersects)
    
    
    # Unpack parameters we will be using
    
    r1 = paramsr[0]
    r2 = paramsr[1]
    r3 = paramsr[2]
    
    x1 = xcoordinates[0]
    x2 = xcoordinates[1]
    x3 = xcoordinates[2]

    y1 = ycoordinates[0]
    y2 = ycoordinates[1]
    y3 = ycoordinates[2]
    
    # create a,b,c for quadratic formula for finding time
    
    a1 = cos(theta)**2 + sin(theta)**2
    a2 = a1
    a3 = a1
    
    b1 = 2*x0*cos(theta) + 2*y0*sin(theta) - 2*x1*cos(theta) - 2*y1*sin(theta)
    b2 = 2*x0*cos(theta) + 2*y0*sin(theta) - 2*x2*cos(theta) - 2*y2*sin(theta)
    b3 = 2*x0*cos(theta) + 2*y0*sin(theta) - 2*x3*cos(theta) - 2*y3*sin(theta)
    
    c1 = x0**2 + y0**2 + x1**2 + y1**2 - 2*x1*x0 - 2*y1*y0 - r1**2
    c2 = x0**2 + y0**2 + x2**2 + y2**2 - 2*x2*x0 - 2*y2*y0 - r2**2
    c3 = x0**2 + y0**2 + x3**2 + y3**2 - 2*x3*x0 - 2*y3*y0 - r3**2
    
    #first disk intersect points
    
    timeintersect[0] = (-b1 + sqrt(b1**2 - 4*a1*c1))/(2*a1)
    timeintersect[1] = (-b1 - sqrt(b1**2 - 4*a1*c1))/(2*a1)
    
    #second disk intersect points
    
    timeintersect[2] = (-b2 + sqrt(b2**2 - 4*a2*c2))/(2*a2)
    timeintersect[3] = (-b2 - sqrt(b2**2 - 4*a2*c2))/(2*a2)
    
    #third disk intersect points
    
    timeintersect[4] = (-b3 + sqrt(b3**2 - 4*a3*c3))/(2*a3)
    timeintersect[5] = (-b3 - sqrt(b3**2 - 4*a3*c3))/(2*a3)
    
     # We are only concerned with finding the minimum t to the point we are crossing
     
     # If t is complex, we will change that number to a really large one
     # if t is approximately 0 or negative, we will change that to a really large number
    
    reallylargenumber = 10**8
    reallysmallnumber = 10 ** -8
    
    timeintersect[isnan(timeintersect)] = reallylargenumber 
    timeintersect[timeintersect < reallysmallnumber] = reallylargenumber
    
    IntersectTime = min(timeintersect)
    IntersectCircle = 0
    
    if IntersectTime == timeintersect[0] or IntersectTime == timeintersect[1]:
        IntersectCircle = 1
    if IntersectTime == timeintersect[2] or IntersectTime == timeintersect[3]:
        IntersectCircle = 2
    if IntersectTime == timeintersect[4] or IntersectTime == timeintersect[5]:
        IntersectCircle = 3
    if IntersectTime == reallylargenumber:
        IntersectCircle = 0
    
    #### FIND INTERSECTING POINTS ####
    
    IntersectPointX = LastImpactX + IntersectTime*cos(theta)
    IntersectPointY = LastImpactY + IntersectTime*sin(theta)
    
    IntersectPoints = [IntersectPointX,IntersectPointY]

    return [IntersectTime,IntersectCircle,IntersectPoints]

def flipvectorgettheta(ImpactPoints,LastImpactX,LastImpactY,IntersectCircle): #this function flips the vector and computes our new angle theta
    
    xp = ImpactPoints[0]
    yp = ImpactPoints[1]
    
    x0 = LastImpactX
    y0 = LastImpactY
    
    
    CircleIntersect = IntersectCircle
    
    if CircleIntersect == 1 : # we hit upper disk
        xc = x1
        yc = y1
    
    if CircleIntersect == 2: # we hit right disk
        xc = x2
        yc = y2
        
    if CircleIntersect == 3: # we hit bottom disk
        xc = x3
        yc = y3
    if CircleIntersect == 0: # We Have Not Hit Any Circles, We return 'NaN' because we cant compute it
        return float('NaN')
        
    incomingx = xp-x0
    incomingy = yp-y0
    
    normalx = xp-xc
    normaly = yp-yc
    
    normalmag = sqrt(normalx**2 + normaly**2)
    
    vectorincoming = array([incomingx,incomingy])
    normal_direction = array([(normalx),(normaly)])
    normal_direction = normal_direction/normalmag
    
    vectorreflect = vectorincoming - 2*normal_direction*(dot(vectorincoming,normal_direction))
    
    ycomponent = vectorreflect[1]
    xcomponent = vectorreflect[0]
    
    theta = arctan(ycomponent/xcomponent)
    
    if xcomponent <= 0.0 and ycomponent >= 0.0:
        theta += pi
    elif xcomponent <= 0.0 and ycomponent <= 0.0:
        theta += -pi
        
    return theta
    
#####################
####Create Disks#####
#####################

numdisks = 3

paramsr = zeros(numdisks)

for i in range(numdisks):
    paramsr[i] = 3

d = 5 # distance between disks

# Disk Up #

x1 = -d/6.0 * sqrt(3.0)
y1 = d/2.0

# Disk Right #

x2 = d/3.0 * sqrt(3.0)
y2 = 0

# Disk Left # 

x3 = -d/6.0 * sqrt(3.0)
y3 = -d/2.0

xcoordinates = zeros(numdisks)
ycoordinates = zeros(numdisks)

xcoordinates[0] = x1
xcoordinates[1] = x2
xcoordinates[2] = x3

ycoordinates[0] = y1
ycoordinates[1] = y2
ycoordinates[2] = y3

#####################
####Shoot Particle#####
#####################

# Parameters of Problem #

xp = -4 # starting point of particle
ystart = -0.5 # beginning impact parameter
yend = 0.5 # ending impact parameter
interval = 100000 # points between ystart and yend and how many times we will run the code
impact = linspace(ystart,yend,interval)
theta = 0

# WHAT ARE WE GRAPHING? #
ExitAngle = zeros(interval) # How many exit angles we have is how many times we run the code
BounceCount = zeros(interval) # How Many Times We Bounce For Each Trajectory
TimeSpent = zeros(interval) # Time Spent For Each Trajectory
NumParticles = linspace(0,interval,interval)



##### STARTING ALGORITHM #####
IntersectPointsHeld = zeros([16,2]) # We Use This For Plotting A Single Trajectory
SimulationCounter = 1 # Simulation Counter
Counter = 0 # Initialze Counter For Things We Will Be Graphing
PlotNow = False # This is only used for Plotting A Single Trajectory

for i in impact: 
    exitParticle = False
       
    # Every time we run the code we need to initialize the beginning values #
    LastImpactX = xp
    LastTheta = theta
    LastImpactY = i
    
    
   # if LastImpactY == impact[91]: # scatter number
        #PlotNow = True
        #IntersectPointsHeld[0] = [LastImpactX,LastImpactY]
    #else:
        #PlotNow = False
        #IntersectPointsHeld[15] = IntersectPointsHeld[14]
        

    IntersectArray = Intersect(xcoordinates,ycoordinates,paramsr,LastTheta,LastImpactX,LastImpactY)
    IntersectTime = IntersectArray[0]
    IntersectCircle = IntersectArray[1]
    IntersectPoints = IntersectArray[2]
    
    if IntersectCircle == 0:
        exitParticle = True
        print("We Have Exited")
        timespentthistrajectory = IntersectTime
        
    print("Running Simulation %s" % SimulationCounter)
    
    BounceCounter = 1
    
    timespentthistrajectory = 0
    
    while exitParticle == False:
        
        
        
        print("Projectile has bounced %s times" % BounceCounter) # Sanity Check #
        
        # Use Intersect Function #
        
        IntersectArray = Intersect(xcoordinates,ycoordinates,paramsr,LastTheta,LastImpactX,LastImpactY) 
        
        # Unpack Intersect Function #
        
        IntersectTime = IntersectArray[0]
        IntersectCircle = IntersectArray[1]
        IntersectPoints = IntersectArray[2]
        
        
        
        if PlotNow == True: # IF WE WANT TO PLOT A TRAJECTORY WE USE THIS LINE OF CODE #
            IntersectPointsHeld[BounceCounter] = IntersectPoints
    
        
        if IntersectCircle == 0: # This is our exit condition
            ExitAngle[Counter] = LastTheta
            exitParticle = True
            print("We Have Exited")
            
        
        
        NewAngle = flipvectorgettheta(IntersectPoints,LastImpactX,LastImpactY,IntersectCircle)
        
        LastImpactX = IntersectPoints[0]
        LastImpactY = IntersectPoints[1]
        LastTheta = NewAngle
        
        if exitParticle == False:
            timespentthistrajectory += IntersectTime
        
        
        
        BounceCounter += 1
  
    
    TimeSpent[Counter] = timespentthistrajectory
    
    
    BounceCount[Counter] = BounceCounter
     
    Counter += 1
    SimulationCounter += 1
    
#####################
######Plots##########
#####################


ax=plt.gca()
plt.plot(IntersectPointsHeld[:,0],IntersectPointsHeld[:,1],)
circle1 = plt.Circle((x1,ycoordinates[0]), radius=1, color='g', fill=False)
circle2 = plt.Circle((x2,ycoordinates[1]), radius=1, color='b', fill=False)
circle3 = plt.Circle((x3,ycoordinates[2]), radius=1, color='r', fill=False)
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)
plt.axis('scaled')
plt.title('Trajectory Plot')
plt.show()

plt.figure()
plt.plot(impact,ExitAngle)
plt.xlabel('Impact Parameter (''$\it{b}$)')
plt.ylabel('Exit Angle ('r'$\theta$)')
plt.title('Output ('r'$\theta$) vs Input Ordinate')
plt.show()

plt.figure()
plt.plot(impact,BounceCount)
plt.title("Bounce Count vs Input Ordinate")
plt.xlabel('Impact Parameter (''$\it{b}$)')
plt.ylabel('Number Bounces')
plt.show()

plt.figure()
plt.plot(impact,TimeSpent)
plt.xlabel('Impact Parameter (''$\it{b}$)')
plt.ylabel('Time Spent')
plt.title('Time Spent vs Input Ordinate')
plt.show()