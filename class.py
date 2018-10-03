
import copy

class story:
	#the basics of a story
	def __init__ (self, genre):
		self.genre = genre
		self.startScene = []



	def createStory(self,beatnumber,scenenumber, startbeat):
		startscene = Scene(beatnumber,"start",startbeat,"Start")
		secondAct = []
		thirdAct = []
		for beat in startscene.scenepotential:
			secondAct.append(Scene(beatnumber,scenetype,beat,startScene))
		for scene in secondAct:
			for beat in scene.scenepotential:
			thirdAct.append(Scene(beatnumber,scenetype,beat,scene))
		

	


		




class Subject:
	def __init__(self,name):
		self.name = name



class Person(Subject):
	def __init__(self, name, alignment, location):
		self.name = name
		self.alignment = alignment
		self.location = location



class Location:
	def __init__ (self, name, locationType):
	    self.name = name
	    self.type = locationType


class Beat:
	def __init__ (self, sequence, rule, actor, target, location,suspense,parent):
		self.sequence = sequence
		self.rule = rule
		self.actor = actor
		self.target = target		
		self.location = location
		self.children = []
		self.parent = parent
		self.suspense = suspense

	def add_child(self,child):
		self.children.append(child)

	def branch(self,tokenDict):
		for key in tokenDict:
             # lookup the function to call for each line
   			 functionToCall = tokenDict[key]

            # and call it
   			 functionToCall(self)


class Scene:
	def __init__ (self, beatnumber, scenetype, startbeat, previousscene):
		self.previousscene = previousscene 
		self.beatnumber = beatnumber
		self.scenetype = scenetype
		self.startbeat = [startbeat]
		self.scenepotential = []
		beatlist = self.startbeat
		for _ in range(self.beatnumber):
			newlist = []
			for beat in beatlist:
				beat.branch(tokenDict)
				newlist = newlist + beat.children
				
			beatlist = newlist
			self.scenepotential = beatlist
			#print(self.scenepotential)
	def returnpotential(self):
		return(scenepotential)


	def printscenes(self):

		for beat in self.scenepotential:
			tempbeat = beat
			tempscene = [beat]
			while tempbeat.parent != []:
				tempscene = [tempbeat.parent] + tempscene
				tempbeat = tempbeat.parent
			print("Scene Start")
			for child in tempscene:
				print(child.rule)
				print(child.location.name)
				print(child.suspense)
			
class rule(self):

	def checkValidity(self):



	def creatBeat(self,beat):
		newBeat 
		return newBeat








seedybar = Location('SeedyBar', 'Bar')
office = Location('Office', 'Office')
sil = Person('Sil', 'Villain', seedybar)
ben = Person('Ben', 'Hero', office)






#class moveList:
	#Adef __init__ (self)





def shoot(beat):
	suspenseChange = 20
	if (beat.actor.location == beat.target.location):
		print ("samelocation")
		if (beat.actor.alignment == "Hero" and beat.target.alignment == "Villain"):
			beat.add_child(Beat(beat.sequence + 1,"Shoot",beat.actor, beat.target, beat.location, beat.suspense - suspenseChange, beat))
		if beat.actor.alignment == "Villain" and beat.target.alignment == "Hero":
			beat.add_child(Beat(beat.sequence + 1,"Shoot",beat.actor, beat.target, beat.location, beat.suspense + suspenseChange, beat))
	else:
		print("noscene")

def follow(beat):
    suspenseChange = 10
    if  beat.actor.alignment == "Hero" and beat.target.alignment == "Villain" :
    		locationchange = copy.copy(beat.actor)
    		locationchange.location = beat.target.location
    		beat.add_child(Beat(beat.sequence + 1,"Follow",locationchange,beat.target,beat.target.location, beat.suspense + suspenseChange, beat ))
    if beat.actor.alignment == "Villain" and beat.target.alignment == "Hero":
    		locationchange = copy.copy(beat.actor)
    		locationchange.location = beat.target.location
    		beat.add_child(Beat(beat.sequence + 1,"Follow",locationchange,beat.target,beat.target.location, beat.suspense + suspenseChange, beat ))

tokenDict = {1: follow,
			2: shoot }


start = Beat(0, "start", ben, sil, office, 0, [])


startscene = Scene(3, "test", start)
startscene.createscene()
startscene.printscenes()