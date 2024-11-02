noteFirstContest = float(input("What's the note of the first contest?: "))
noteSecondContest = float(input("What's the note of the second contest?: "))
noteLab = float(input("What's the note of lab?: "))

desiredFinalNote = 60

requiredAverage = (desiredFinalNote - (noteLab * 0.3)) / 0.7

noteThirdContest = (requiredAverage * 3) - (noteFirstContest + noteSecondContest)

print(f"The note required in the third contest to pass is: {noteThirdContest:.2f}.")