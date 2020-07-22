import time

class Boy:
    def one(self):
        self="lad"
        return self
    def two(self):
        self="handsome"
        return self
class Girl:
    def one(self):
        self="lass"
        return self
    def two(self):
        self="beautiful"
        return self
class Blue:
    def berry(self):
        self="Blueberry"
        return self
class Black:
    def berry(self):
        self="Blackberry"
        return self
class Rasp:
    def berry(self):
        self="Raspberry"
        return self
class Bluestone:
    def creature(self):
        self="Unicorn"
        return self
    def color(self):
        self="blue"
        return self
class Redstone:
    def creature(self):
        self="Phoenix"
        return self
    def color(self):
        self="Red"
        return self
class Yellowstone:
    def creature(self):
        self="Dragon"
        return self
    def color(self):
        self="yellow"
        return self

#My favourite lines of code are probably all the print and time.sleep functions due to the fact that they were the easiest to code. :3  
class Calculator:

    def __init__(self):
        self.result=30
        
    def tackle(self):
        self.result = self.result - 5

    def burn(self):
        self.result = self.result - 6

    def stomp(self):
        self.result = self.result - 4

    def Hp(self):
        return self.result

print("WARNING, ALL FORMS OF INPUT MUST BE TYPED EXACTLY AS SHOWN ON THE SCREEN")
time.sleep(2)
print("It's dark, and you don't know where you are")
time.sleep(0.5)
print("Suddenly a ball of light appears in front of you")
time.sleep(0.5)
print("“Greetings um…, what is your gender?” The ball of light says")
time.sleep(0.5)
print ("boy or girl?")

x = input("P I C K  G E N D E R :")
if x == "boy":
    a = Boy()
else:
    a = Girl()
print("'Alrighty good ", a.one(), " you really should wake up, its near noon!'")
time.sleep(0.5)
print("You wake up with a craving for pie")
time.sleep(0.5)
print("You put on your boots, grab your bag, and head to the marketplace")
time.sleep(0.5)
print("The sun is shining")
time.sleep(0.5)
print("The birds are chirping")
time.sleep(0.5)
print("There is a spring in your step")
time.sleep(0.5)
print("You look at the trees, they are a dark green, the canopy above offers shade in your forest dwelling. Light filters through and makes pretty patterns on the forest floor.")
time.sleep(0.5)
print("Once the forest clears, you reach the village. It is lively and many people are selling goods.")
time.sleep(0.5)
print("You buy flour, butter, and sugar however, you are stuck between what filling you should make your pie with.")
time.sleep(0.5)
print("Blueberry, Raspberry, or Blackberry")
x=input("P I C K  B E R R Y:")
if x== "Blueberry":
    b=Blue()
elif x=="Raspberry":
    b=Rasp()
else:
    b=Black()
print("You chose to make a ", b.berry(), "Pie.")
time.sleep(0.5)
print("On the way back to the forest, you pass by a vendor selling colourful stones")
time.sleep(0.5)
print("'There are many different stones here, all of which are expensive, but for a ", a.two()," ", a.one(), " like yourself, I will give you the option to pick one for free'")
time.sleep(0.5)
print("In his stall 3 large stones (red, blue, and yellow) interest you. Which do you choose?")
time.sleep(0.5)
x=input("P I C K  A  S T O N E :")
if x=="red":
    c=Redstone()
elif x=="blue":
    c=Bluestone()
else:
    c=Yellowstone()
print("You picked the ", c.color()," stone!")
time.sleep(0.5)
print("You placed the stone in your bag, it's suprisingly warm.")
time.sleep(0.5)
print("As you pass the creek on your way back, you get hear a very loud growl, and when you find it's source you see a beast staring you down, ready to attack")
time.sleep(0.5)
print("Your egg begins to shake, and soon it explodes into a ", c.creature(), "that is ready to defend you!")
time.sleep(0.5)
print("THE BATTLE IS BEGINNING, YOU CANNOT TAKE ANY DAMAGE, HOWEVER YOU CAN INFLICT DAMAGE. YOU HAVE 3 ATTACKS. STOMP, TACKLE, AND BURN. TO SEE HP OF OPPONENT TYPE, HEALTH, TO END BATTLE TYPE END.")
d=Calculator()
x = input("Type your move:")
if x=="STOMP":
    d.stomp()
    print("You STOMPED the beast")
elif x=="BURN":
    d.burn()
    print("You BURNED the beast")
elif x=="TACKLE":
    d.tackle()
    print("You TACKLED the beast")
elif x=="HEALTH":
    d.Hp()
    print("The beast's HP is ", d.Hp(), "out of 30 HP")
elif x=="END":
    print("The beast is scared away from you and you return home")
else:
    print("Sorry, please type that again, and make sure it is capitalized properly")
x = input("Type your move:")
if x=="STOMP":
    d.stomp()
    print("You STOMPED the beast")
elif x=="BURN":
    d.burn()
    print("You BURNED the beast")
elif x=="TACKLE":
    d.tackle()
    print("You TACKLED the beast")
elif x=="HEALTH":
    d.Hp()
    print("The beast's HP is ", d.Hp(), "out of 30 HP")
elif x=="END":
    print("The beast is scared away from you and you return home")
else:
    print("Sorry, please type that again, and make sure it is capitalized properly")
x = input("Type your move:")
if x=="STOMP":
    d.stomp()
    print("You STOMPED the beast")
elif x=="BURN":
    d.burn()
    print("You BURNED the beast")
elif x=="TACKLE":
    d.tackle()
    print("You TACKLED the beast")
elif x=="HEALTH":
    d.Hp()
    print("The beast's HP is ", d.Hp(), "out of 30 HP")
elif x=="END":
    print("The beast is scared away from you and you return home")
else:
    print("Sorry, please type that again, and make sure it is capitalized properly")
x = input("Type your move:")
if x=="STOMP":
    d.stomp()
    print("You STOMPED the beast")
elif x=="BURN":
    d.burn()
    print("You BURNED the beast")
elif x=="TACKLE":
    d.tackle()
    print("You TACKLED the beast")
elif x=="HEALTH":
    d.Hp()
    print("The beast's HP is ", d.Hp(), "out of 30 HP")
elif x=="END":
    print("The beast is scared away from you and you return home")
else:
    print("Sorry, please type that again, and make sure it is capitalized properly")
x = input("Type your move:")
if x=="STOMP":
    d.stomp()
    print("You STOMPED the beast")
elif x=="BURN":
    d.burn()
    print("You BURNED the beast")
elif x=="TACKLE":
    d.tackle()
    print("You TACKLED the beast")
elif x=="HEALTH":
    d.Hp()
    print("The beast's HP is ", d.Hp(), "out of 30 HP")
elif x=="END":
    print("The beast is scared away from you and you return home")
else:
    print("Sorry, please type that again, and make sure it is capitalized properly")
x = input("Type your move:")
if x=="STOMP":
    d.stomp()
    print("You STOMPED the beast")
elif x=="BURN":
    d.burn()
    print("You BURNED the beast")
elif x=="TACKLE":
    d.tackle()
    print("You TACKLED the beast")
elif x=="HEALTH":
    d.Hp()
    print("The beast's HP is ", d.Hp(), "out of 30 HP")
elif x=="END":
    print("The beast is scared away from you and you return home")
else:
    print("Sorry, please type that again, and make sure it is capitalized properly")
x = input("Type your move:")
if x=="STOMP":
    d.stomp()
    print("You STOMPED the beast")
elif x=="BURN":
    d.burn()
    print("You BURNED the beast")
elif x=="TACKLE":
    d.tackle()
    print("You TACKLED the beast")
elif x=="HEALTH":
    d.Hp()
    print("The beast's HP is ", d.Hp(), "out of 30 HP")
elif x=="END":
    print("The beast is scared away from you and you return home")
else:
    print("Sorry, please type that again, and make sure it is capitalized properly")
x = input("Type your move:")
if x=="STOMP":
    d.stomp()
    print("You STOMPED the beast")
elif x=="BURN":
    d.burn()
    print("You BURNED the beast")
elif x=="TACKLE":
    d.tackle()
    print("You TACKLED the beast")
elif x=="HEALTH":
    d.Hp()
    print("The beast's HP is ", d.Hp(), "out of 30 HP")
elif x=="END":
    print("The beast is scared away from you and you return home")
else:
    print("Sorry, please type that again, and make sure it is capitalized properly")
x = input("Type your move:")
if x=="STOMP":
    d.stomp()
    print("You STOMPED the beast")
elif x=="BURN":
    d.burn()
    print("You BURNED the beast")
elif x=="TACKLE":
    d.tackle()
    print("You TACKLED the beast")
elif x=="HEALTH":
    d.Hp()
    print("The beast's HP is ", d.Hp(), "out of 30 HP")
elif x=="END":
    print("The beast is scared away from you and you return home")
else:
    print("Sorry, please type that again, and make sure it is capitalized properly")
print("Battle has ended.")
print("Once you get home, you and your newfound pet breathe a sigh of releif, for now you can feast upon your ", b.berry(), " pie!!!")
time.sleep(5)
print("The End")
