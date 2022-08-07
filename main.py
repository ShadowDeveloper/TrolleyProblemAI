import random
import json
from utils import *
memory = json.load(open("memory.json", 'r'))
mode = "ai"
humanCount = 2
humans = []
#m.write()
for _ in range(humanCount):
    gender = random.choices(["male", "female", "non-binary"], weights=[48,47,5])[0]
    minorAgeWeights = [1 for _ in range(1, 19)]
    adultAgeWeights = [2 for _ in range(19, 61)]
    elderlyAgeWeights = [1 for _ in range(61, 110)]
    ageWeights = []
    for x in minorAgeWeights:
        ageWeights.append(x)
    for x in adultAgeWeights:
        ageWeights.append(x)
    for x in elderlyAgeWeights:
        ageWeights.append(x)
    age = random.choices(range(1, 110), weights=ageWeights)[0]

    humanTypes = []
    humanTypes.append("stranger")
    humanTypes.append("relative")
    if age > 9:
        humanTypes.append("friend")
    if age > 18:
        humanTypes.append("doctor")
        humanTypes.append("criminal")
    typeWeights = [10, 2, 2, 3, 3]
    usedWeights = []
    i = 0
    for _ in humanTypes:
        usedWeights.append(typeWeights[i])
        i += 1
    weightsSum = sum(usedWeights)
    i = 0
    for x in usedWeights:
        usedWeights[i] = x/weightsSum
        i += 1
    humanType = random.choices(humanTypes, weights=usedWeights)[0]
    humans.append(Human(gender, age, humanType))
choiceOne = humans[:int((len(humans)/2))]
choiceTwo = humans[int((len(humans)/2)):]

print("Choice One:\n")
for human in choiceOne:
    print(human.format())
print()
print("Choice Two:\n")
for human in choiceTwo:
    print(human.format())

if mode != "ai":
    choice = input("Input 1 to save Choice One, or 2 to save Choice Two")
    if choice == "1":
        for x in choiceOne:
            memory["saved"].append({"gender" : x.gender,
                                    "age" : x.age,
                                    "type" : x.type})
    if choice == "2":
        for x in choiceOne:
            memory["saved"].append({"gender": x.gender,
                                    "age": x.age,
                                    "type": x.type})

    memoryWrite = open("memory.json", 'w')
    memoryWrite.write(str(memory).replace("\'", "\""))
if mode == "ai":
    malesSaved = 0
    femalesSaved = 0
    nbsSaved = 0
    strangersSaved = 0
    relativesSaved = 0
    friendsSaved = 0
    doctorsSaved = 0
    criminalsSaved = 0
    minorsSaved = 0
    adultsSaved = 0
    elderliesSaved = 0
    aiGenderToSave = ""
    aiAgeToSave = ""
    for humanSaved in memory['saved']:
        savedGender = humanSaved['gender']
        savedAge = humanSaved['age']
        savedType = humanSaved['type']
        if savedGender == "male":
            malesSaved += 1
        if savedGender == "female":
            femalesSaved += 1
        if savedGender == "non-binary":
            nbsSaved += 1
        if savedType == "stranger":
            strangersSaved += 1
        if savedType == "relative":
            relativesSaved += 1
        if savedType == "friend":
            friendsSaved += 1
        if savedType == "doctor":
            doctorsSaved += 1
        if savedType == "criminal":
            criminalsSaved += 1
        if savedAge <= 18:
            minorsSaved += 1
        elif savedAge <= 60:
            adultsSaved += 1
        else:
            elderliesSaved += 1
    def roll():
        aiGenderWeights = [malesSaved, femalesSaved, nbsSaved]
        aiGenderToSave = random.choices(["male", "female", "non-binary"], weights=aiGenderWeights)[0]
        aiTypeWeights = [strangersSaved, relativesSaved, friendsSaved, doctorsSaved, criminalsSaved]
        aiTypeToSave = random.choices(["stranger", "relative", "friend", "doctor", "criminal"], weights=aiTypeWeights)[0]
        aiAgeWeights = [minorsSaved, adultsSaved, elderliesSaved]
        aiAgeToSave = random.choices(["minor", "adult", "elderly"], weights=aiAgeWeights)[0]
        aiAgeToSaveRange = []
        if aiAgeToSave == "minor":
            aiAgeToSaveRange = range(1, 19)
        elif aiAgeToSave == "adult":
            aiAgeToSaveRange = range(19, 61)
        elif aiAgeToSave == "elderly":
            aiAgeToSaveRange = range(61, 110)
        choiceOneConditionsMet = 0
        choiceTwoConditionsMet = 0
        for choiceOneHuman in choiceOne:
            if aiGenderToSave == choiceOneHuman.gender:
                choiceOneConditionsMet += 1
            if aiTypeToSave == choiceOneHuman.type:
                choiceOneConditionsMet += 1
            if choiceOneHuman.age in aiAgeToSaveRange:
                choiceOneConditionsMet += 1

        for choiceTwoHuman in choiceTwo:
            if aiGenderToSave == choiceTwoHuman.gender:
                choiceTwoConditionsMet += 1
            if aiTypeToSave == choiceTwoHuman.type:
                choiceTwoConditionsMet += 1
            if choiceTwoHuman.age in aiAgeToSaveRange:
                choiceTwoConditionsMet += 1

        if choiceOneConditionsMet > choiceTwoConditionsMet:
            print("Saving Choice One")
        elif choiceTwoConditionsMet > choiceOneConditionsMet:
            print("Saving Choice Two")
        else:
            print("Saving Choice One")
    roll()
'''
TODO: add "AI".
Sum each type and age, then use these as weights
'''