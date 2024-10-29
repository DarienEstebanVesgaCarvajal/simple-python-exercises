noteFirstContest = float(input("What's the note of the first cerxam?: "))
noteSecondContest = float(input("What's the note of the second cerxam?: "))
noteLab = float(input("What's the note of lab?: "))

desiredFinalNote = 60

requiredAverage = (desiredFinalNote - (noteLab * 0.3)) / 0.7

noteThirdContest = (requiredAverage * 3) - (noteFirstContest + noteSecondContest)

print(f"The note required to pass is: {noteThirdContest}")