import math
import random

def radToPoint(rad):
	return [math.cos(rad), math.sin(rad)]

def pointsToLine(ptA, ptB):
	m = (ptB[1] - ptA[1])/(ptB[0] - ptA[0])
	b = (ptA[1] - m*ptA[0])
	return [m, b]

def Intersect(linA, linB):
	xVal = (linB[1] - linA[1])/(linA[0] - linB[0])
	yVal = linA[0]*xVal + linA[1]
	return 1 if math.sqrt(xVal**2 + yVal**2) < 1 else 0

Cuts      = 3
Dict      = {}
MaxSlices = (Cuts**2 + Cuts + 2)/2

for iC in range(Cuts + 1, MaxSlices + 1):
	Dict[iC] = 0.0

for iX in xrange(1000000):
	Lines = []
	Sum = 0

	for iN in xrange(Cuts):
		PtA  = radToPoint(random.uniform(0, 2*math.pi))     # Generate a random point on the unit circle
		PtB  = radToPoint(random.uniform(0, 2*math.pi))     # Generate another random point on the unit circle
		Lines.append(pointsToLine(PtA, PtB))                # Use Algebra I to find the line running through 2 points

	for iNA in xrange(Cuts - 1):                            # Iterate through every cut...
		for iNB in range(iNA + 1, len(Lines)):              # ...against every OTHER cut to see if there is an intersection.
			Sum += Intersect(Lines[iNA], Lines[iNB])        # If there is an intersection (inside the unit circle), there
                                                            # must be one additional piece.
	Dict[Cuts + 1 + Sum] += 1

Avg = 0.0

for iD in Dict:
	Avg += iD*Dict[iD]

print Avg/iX
print Dict



