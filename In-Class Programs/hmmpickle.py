import pickle

infile = open("../In-Class Programs/inputfiles/LargeCitiesDict.dat", 'rb')
cityDict = pickle.load(infile)
infile.close()

for c in cityDict.items(): print(c)