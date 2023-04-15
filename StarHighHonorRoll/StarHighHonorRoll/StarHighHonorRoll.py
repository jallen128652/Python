#Program: StarHighHonorRoll
#Course: ITSE 1302 7P1
#Author: James Allen
#Description: This program creates 2 files for A and B honor roll

print("Processing student grades...")
#open file
file = open("grades.dat")
#declare lists, counters, variables
aHonors = []
bHonors = []
tcount = 0
aCount = 0
bCount = 0
aPercent = 0
bPercent = 0

#for loop to read file, count students and populate lists
for line in file:
	miniList = line.strip().split(",") 
	name = miniList[0]
	studId = int(miniList[1])
	gpa = int(miniList[2].strip())
	tcount += 1
#control statement to write to each list
	if (gpa >= 90):
		aHonors.append(name)
		aCount += 1
	elif (gpa >= 80 and gpa < 90): #range
		bHonors.append(name)
		bCount += 1
#close read file
file.close()
print("Processing complete\n")

#calculate percentages
aPercent = (aCount * 100) / tcount
bPercent = (bCount * 100) / tcount

#print outputs
print("SUMMARY STATISTICS")
print("-------------------")
print("Total students: " + str(tcount))
print("A Honor Roll Students: " + str(aCount) + " (" + str(round(aPercent, 2)) + "%)")
print("B Honor Roll Students: " + str(bCount) + " (" + str(round(bPercent, 2)) + "%)\n")
#sort lists
aHonors.sort()
bHonors.sort()
#create output file A honors
outputFile = open("AHonorRoll.dat", "wt")
for name in aHonors:
	outputFile.write(name + "\n")
#close write file
outputFile.close()
#create output file B honors
print("AHonorRoll.dat file created...")
outputFile = open("BHonorRoll.dat", "wt")
for name in bHonors:
	outputFile.write(name + "\n")
#close write file
outputFile.close()
print("BHonorRoll.dat file created...\n")
#celebrate!!!!!!
print("End of program.")