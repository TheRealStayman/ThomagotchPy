from ThomagotchPy import Creature

print "Creating a Tamagotchi!"
Tama = Creature("Mametchi")

print "The Tamagotchi's name is \n" + Tama.name

print Tama.name + "'s birthday is " + Tama.birthday
print Tama.name + "'s hunger level is at " + str(Tama.hunger) + " brownie(s)"
print Tama.name + "'s energy level is at " + str(Tama.energy) + " jumping jack(s)"
print Tama.name + "'s health is at " + str(Tama.health) + " heart(s)"

print Tama.getAge()

print "\nChecking " + Tama.name + "'s energy levels"
print "Energy levels at " + str(Tama.getEnergy()) + " jumping jack(s)"
print "Checking " + Tama.name + "'s health levels"
print "Health levels at " + str(Tama.getHealth()) + " heart(s)"

print "\nChecking if " + Tama.name + " is hungry"
if Tama.isHungry() == True:
    print Tama.name + " is hungry. It's time to feed!"
else:
    print Tama.name + " isn't hungry right now."

print "\nChecking if " + Tama.name + " is awake"
if Tama.isAwake() == True:
    print Tama.name + " is wide awake!"
else:
    print Tama.name + " is fast asleep."

print "\nChecking if " + Tama.name + " is alive"
if Tama.isAlive() == True:
    print Tama.name + " is alive and kicking."
else:
    print Tama.name + " is dead. You can't change it. Accept his fate."

print "\nSetting " + Tama.name + "'s hunger to 2 brownie(s)."
print Tama.setHunger(2)

print "\nChecking if " + Tama.name + " is hungry"
if Tama.isHungry() == True:
    print Tama.name + " is hungry. It's time to feed!"
else:
    print Tama.name + " isn't hungry right now."

print "\nPutting " + Tama.name + " to bed."
Tama.sleep()

print "\nChecking if " + Tama.name + " is awake"
if Tama.isAwake() == True:
    print Tama.name + " is wide awake!"
else:
    print Tama.name + " is fast asleep."

print "\nKilling " + Tama.name
Tama.kill()

print "\nChecking if " + Tama.name + " is alive"
if Tama.isAlive() == True:
    print Tama.name + " is alive and kicking."
else:
    print Tama.name + " is dead. You can't change it. Accept his fate."
