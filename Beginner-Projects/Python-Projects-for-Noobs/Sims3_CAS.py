import random

print("")
print("Sims 3 Random Face Generator")
print("For use with NRAAS Master Controller Integration")
print("Written by Pleasant Sims")
print("Inspired by chemtale's Sims 2 randomizer")
print("") 

min_val = -256
max_val = 256

# Roll head
head = input("Roll head? ")
if head.lower() in ['yes', 'y', '']:
    print("")
    print("Face Height: " + str(random.randint(min_val, max_val)))
    print("Face Profile: " + str(random.randint(min_val, max_val)))
    print("Head Width: " + str(random.randint(-256, 0)))
    print("")

# Roll chin
chin = input("Roll chin? ")
if chin.lower() in ['yes', 'y', '']:
    print("")
    print("Chin Depth: " + str(random.randint(0, 150)))
    print("Chin Height: " + str(random.randint(-150, 256)))
    print("Chin Scale: " + str(random.randint(-175, 100)))
    print("Chin Underlip Depth: " + str(random.randint(-100, 150)))
    print("")

# Roll jaw
jaw = input("Roll jaw? ")
if jaw.lower() in ['yes', 'y', '']:
    print("")
    print("Jaw Depth: " + str(random.randint(-80, 150)))
    print("Jaw Height: " + str(random.randint(-175, 175)))
    print("Jaw Shape: " + str(random.randint(-175, 125)))
    print("Jaw Underbite: " + str(random.randint(0, 75)))
    print("Jaw Width: " + str(random.randint(-256, 175)))
    print("")

# Roll cheek
cheek = input("Roll cheek? ")
if cheek.lower() in ['yes', 'y', '']:
    print("")
    print("Cheek Bone Height: " + str(random.randint(min_val, max_val)))
    print("Cheek Bone Shape: " + str(random.randint(-175, 175)))
    print("Cheek Fullness: " + str(random.randint(-150, 150)))
    print("Cheek Jowls: " + str(random.randint(0, 156)))
    print("Nasolabial Crease: " + str(random.randint(0, 200)))
    print("")

# Roll ears
ears = input("Roll ears? ")
if ears.lower() in ['yes', 'y', '']:
    print("")
    print("Ears Orbit: " + str(random.randint(-120, 256)))
    print("Ears Point: " + str(random.randint(0, 20)))
    print("Ears Rotate: " + str(random.randint(-256, 0)))
    print("Ears Scale: " + str(random.randint(-100, 0)))
    print("")

# Roll eyes
eyes = input("Roll eyes? ")
if eyes.lower() in ['yes', 'y', '']:
    print("")
    print("Eye Depth: " + str(random.randint(min_val, max_val)))
    print("Eye Distance: " + str(random.randint(-256, 100)))
    print("Eye Height: " + str(random.randint(-150, 150)))
    print("Eye Scale: " + str(random.randint(-175, 100)))
    print("Eye Socket Height: " + str(random.randint(-125, 125)))
    print("Rotate Eyes: " + str(random.randint(-100, 100)))
    print("")

# Roll eye shape
eyeshape = input("Roll eye shape? ")
if eyeshape.lower() in ['yes', 'y', '']:
    print("")
    print("Eye Apex: " + str(random.randint(-175, 175)))
    print("Eye Corner Height: " + str(random.randint(-100, 100)))
    print("Eye Inner Corner Height: " + str(random.randint(-150, 150)))
    print("Eye Shape: " + str(random.randint(-100, 256)))
    print("Eye Apex Lower: " + str(random.randint(-150, 100)))
    print("")

# Roll eyelids
eyelids = input("Roll eyelids? ")
if eyelids.lower() in ['yes', 'y', '']:
    print("")
    print("Eyelid Height: " + str(random.randint(-100, 100)))
    print("Eyes Lower Lid Height: " + str(random.randint(0, 256)))
    print("Eyes Upper Lid Height: " + str(random.randint(0, 125)))
    print("")  

# Roll brow
brow = input("Roll brow? ")
if brow.lower() in ['yes', 'y', '']:
    print("")
    print("Brow Curve: " + str(random.randint(-175, 175)))
    print("Brow Definition: " + str(random.randint(0, 100)))
    print("Brow Height: " + str(random.randint(-175, 175)))
    print("Brow Rotation: " + str(random.randint(-175, 50)))
    print("")  

# Roll nose
nose = input("Roll nose? ")
if nose.lower() in ['yes', 'y', '']:
    print("")
    print("Nose Definition: " + str(random.randint(-175, 256)))
    print("Nose Height: " + str(random.randint(-100, 150)))
    print("Nose Length: " + str(random.randint(-175, 50)))
    print("Nose Mass: " + str(random.randint(0, 175)))
    print("Nose Rotate: " + str(random.randint(-150, 125)))
    print("Nose Scale: " + str(random.randint(-175, 75)))
    print("Nose Width: " + str(random.randint(-200, 110)))
    print("")  

# Roll nostril
nostril = input("Roll nostril? ")
if nostril.lower() in ['yes', 'y', '']:
    print("")
    print("Nostril Definition: " + str(random.randint(-100, 150)))
    print("Nostril Height: " + str(random.randint(-150, 175)))
    print("Nostril Rotate: " + str(random.randint(-125, 150)))
    print("Nostril Scale: " + str(random.randint(-125, 150)))
    print("")  

# Roll tip
tip = input("Roll tip? ")
if tip.lower() in ['yes', 'y', '']:
    print("")
    print("Nose Tip Depth: " + str(random.randint(-35, 135)))
    print("Nose Tip Rotate: " + str(random.randint(-125, 150)))
    print("Nose Tip Scale: " + str(random.randint(-125, 175)))
    print("")

# Roll bridge
bridge = input("Roll bridge? ")
if bridge.lower() in ['yes', 'y', '']:
    print("")
    print("Bridge Depth: " + str(random.randint(-100, 200)))
    print("Bridge Height: " + str(random.randint(-130, 130)))
    print("Bridge Rotate: " + str(random.randint(-100, 175)))
    print("Bridge Width: " + str(random.randint(-150, 100)))
    print("")

# Roll mouth
mouth = input("Roll mouth? ")
if mouth.lower() in ['yes', 'y', '']:
    print("")
    print("Mouth Corner Depth: " + str(random.randint(-175, 150)))
    print("Mouth Corners Rotate: " + str(random.randint(-150, 150)))
    print("Mouth Curve: " + str(random.randint(-100, 175)))
    print("Mouth Definition: " + str(random.randint(-100, 175)))
    print("Mouth Depth: " + str(random.randint(-175, 150)))
    print("Mouth Height: " + str(random.randint(-200, 175)))
    print("Mouth Width: " + str(random.randint(-150, 150)))
    print("")

# Roll lower lip
lowerlip = input("Roll lower lip? ")
if lowerlip.lower() in ['yes', 'y', '']:
    print("")
    print("Lower Lip Shape: " + str(random.randint(-175, 175)))
    print("Lower Lip Thickness: " + str(random.randint(-100, 200)))
    print("Lower Lip Width: " + str(random.randint(-175, 175)))
    print("")

# Roll upper lip
upperlip = input("Roll upper lip? ")
if upperlip.lower() in ['yes', 'y', '']:
    print("")
    print("Upper Lip Shape: " + str(random.randint(50, 200)))
    print("Upper Lip Thickness: " + str(random.randint(-256, 170)))
    print("Upper Lip Width: " + str(random.randint(-100, 100)))
    print("")
