import datetime

class Creature(object):

    def __init__(self, name):
        self.name = name

    birthday = datetime.datetime.now().strftime("%Y/%m/%d")
    birthyear = datetime.datetime.now().strftime("%Y")
    birthmonth = datetime.datetime.now().strftime("%m")
    hunger = 5 #On a scale of 0-5 brownies where 5 brownies is full. (Based on Sir Burton)
    energy = 175 #On a scale of 0-90 jumping jacks where 175 is how many jumping jacks you have left before you are tired. (Based on Sir Burton)
    health = 10 #On a scale of 0-10 where 10 is full health.

    alive = True
    sleeping = False
    
    def getAge(self):
        age_years = int(datetime.datetime.now().strftime("%Y")) - int(self.birthyear)
        age_months = int(datetime.datetime.now().strftime("%m")) - int(self.birthmonth)
        return str(self.name) + " is " + str(age_years) + " year(s) " + str(age_months) + " month(s) old."

    def getEnergy(self):
        return self.energy

    def isHungry(self):
        if self.hunger <= 2:
            return True
        else:
            return False

    def isAlive(self):
        if self.alive == True:
            return True
        else:
            return False

    def isAwake(self):
        if self.sleeping == False:
            return True
        else:
            return False

    def getHealth(self):
        return self.health

    def setHunger(self, val):
        self.hunger = val
        return "You have set hunger to " + str(val) + " brownie(s)."

    def sleep(self):
        self.sleeping = True

    def kill(self):
        self.alive = False
        self.energy = 0
        self.health = 0
