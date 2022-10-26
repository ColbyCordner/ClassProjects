import maya.cmds as cmds

#//Creates Cup
cmds.polyCylinder(sx=16, sy=1, sz=1, h=6, rcp=0, cuv=3, ch=1, r=3)
cmds.move(0, 3, 0)



#//Creates Handle
cmds.polyTorus(radius=2,sectionRadius=0.5,twist=0,subdivisionsX=20,subdivisionsY=10,createUVs=1,constructionHistory=1,ax=[0,1,0])
cmds.rotate(0,0,90, relative=1,worldSpace=1,forceOrderXYZ=1)
cmds.move(0, 2.85, -2.8)

#//Creates Eyes
cmds.polySphere(radius=1,subdivisionsX=20,subdivisionsY=20,createUVs=2,constructionHistory=1)
cmds.move(-1.5,3.146,2.622, absolute=1)
cmds.scale(0.288,1.138,0.288,relative=1)
cmds.duplicate(returnRootsOnly=1)
cmds.move(1.031, 3.146, 2.736, absolute=1)
cmds.move(0.132939,0,0,relative=1)

#//Create Legs
cmds.polyCylinder(ax=(0,1,0),r=1,h=2,sx=16,sy=1,sz=1,rcp=0,cuv=3,ch=1)
cmds.scale(0.5,0.5,0.5,relative=1)
cmds.rotate(90,50,0,relative=1,worldSpace=1,forceOrderXYZ=1)
cmds.move(2.602,-0.264,2.565,absolute=1)
cmds.scale(1, 4.038883, 1, relative=1)
cmds.polySphere(ax=(0,1,0),r=1,sx=20,sy=20,cuv=2,ch=1)
cmds.move(4.169, -0.263, 3.876, absolute=1)
cmds.scale(0.486, 0.486, 0.486, relative=1)

#//I'm well aware there's an easier way to do this, but I couldn't for the life
#//of me figure out how to duplicate so this is what you get.
cmds.polyCylinder(ax=(0,1,0),r=1,h=2,sx=16,sy=1,sz=1,rcp=0,cuv=3,ch=1)
cmds.scale(0.5,0.5,0.5,relative=1)
cmds.scale(1, 4.038883, 1,relative=1)
cmds.move(-2.268, -0.264, 2.394, absolute=1)
cmds.rotate(90,-42.52,0,worldSpace=1,forceOrderXYZ=1,relative=1)
cmds.polySphere(ax=(0,1,0),r=1,sx=20,sy=20,cuv=2,ch=1)
cmds.move(-3.622, -0.263, 3.876, absolute=1)
cmds.scale(0.486,0.486, 0.486, relative=1)

#//Create Toes
cmds.polySphere(ax=(0,1,0),r=1,sx=20,sy=20,cuv=2,ch=1)
cmds.scale(0.23, 0.882,0.23,relative=1)
cmds.move(-4.563, 0.413, 3.653,absolute=1)
cmds.rotate(-14.523, 16.464, 16.498, relative=1, worldSpace=1, forceOrderXYZ=1)
cmds.duplicate(returnRootsOnly=1)
cmds.move(-4.255,0.413,3.975,absolute=1)
cmds.rotate(0.483, 9.063, 1.169, absolute=1, worldSpace=1, forceOrderXYZ=1)
cmds.duplicate(returnRootsOnly=1)
cmds.move(-3.889, 0.404, 4.334,absolute=1)
cmds.rotate(22.43, 2.857, -23.229, absolute=1,worldSpace=1,forceOrderXYZ=1)

cmds.polySphere(ax=(0, 1, 0),r=1,sx=20,sy=20,cuv=2,ch=1)
cmds.scale(0.23, 0.882, 0.23, relative=1)
cmds.move(3.169,0.442,4.188, absolute=1)
cmds.rotate( 9.609, 28.483, 42.066, relative=1,worldSpace=1,forceOrderXYZ=1)
cmds.duplicate(returnRootsOnly=1)
cmds.move(3.6, 0.413, 3.873, absolute=1)
cmds.rotate(-2.653, 55.874, -0.201, absolute=1, worldSpace=1, forceOrderXYZ=1)
cmds.duplicate(returnRootsOnly=1)
cmds.move(4.067, 0.304, 3.661,absolute=1)
cmds.rotate(-20.833, -15.902, -26.366,absolute=1,worldSpace=1,forceOrderXYZ=1)
