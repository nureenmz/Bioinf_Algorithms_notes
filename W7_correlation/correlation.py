#This is an example implementation of Euclidean Pearson Correlation
#pip install plotly==4.5.4
#see https://plot.ly/python-api-reference/generated/plotly.graph_objects.Figure.html
#see plot.ly/

# Setup plotting
import plotly.graph_objects as go
import plotly.offline as offline
import csv
import math

#Simple plotting function
def plotme(xx,yy):
    fig = go.Figure(
       data=go.Pointcloud(x=xx, y=yy),
       #data=go.Bar(x=xx, y=yy),
       layout=go.Layout(
          title=go.layout.Title(text="A Scatter Plot"),
          xaxis_title="x title",
          yaxis_title="y titel") # plot as html file
    )
    offline.plot(fig, filename='file.html',auto_open=False)

#load a file- this will contain comma delimited values for correlation
def loadafile(flename):
    mytable = []
    with open(flename) as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        for row in csvReader:
            row = [float(i) for i in row]
            mytable.append(row)
    return mytable
	
#calculate Euclidean distance
def euclidean_distance(element1, element2):
    # Element here is the Gene row
    # Make sure each row has the same number of genes measured
    if(len(element1)!=len(element2)):
        print("values wrong length....")
        return -2
    dist = 0
    # d(p,q) = sqrt((q1-p1)**2 + (q2-p2)**2 ... + (qn-pn)**2)
    # Take each index position of row 1 and row 2, and apply the formula
    for x in range(0, len(element1)):
        dist = dist+(element1[x]-element2[x])**2
    dist = math.sqrt(dist)
    # dist is the euclidean distance between Gene 1 and Gene 2, across all samples
    return dist

#calculate Pearson correlation
def pearson_correlation(element1, element2):
    if (len(element1) != len(element2)):
        print("values wrong length....")
        return -2
    d = 0
    N = len(element1)
    sumXY=0
    sumX=0
    sumY=0
    sumSqX=0
    sumSqY=0
    #
    for x in range(0, N):
       sumX=sumX+element1[x]
       sumY=sumY+element2[x]
       sumXY=sumXY+(element1[x]*element2[x])
       sumSqX=sumSqX+(element1[x]**2)
       sumSqY = sumSqY + (element2[x] ** 2)
    # R is the correlatin coefficient between two elements (genes)
    r=((N*sumXY)-(sumX*sumY))/math.sqrt(((N*sumSqX)-(sumX)**2)*((N*sumSqY)-(sumY)**2))
    return r
	
# Find the most correlated pair of indexes (with the closest Euclidean distance)
def findmostcorrelated(mytable):
    corr = 0.0
    val1 = -1
    val2 = -1
    for x in range(0, len(mytable)):
        for y in range(x+1, len(mytable)):
            mycorr = euclidean_distance(mytable[x], mytable[y])
            # Calculate the elements with the closest Euclidean distance
            if val1 == -1:
                corr = mycorr
                val1 = x
                val2 = y
                continue
            if mycorr < corr:
                corr = mycorr
                val1 = x
                val2 = y
    return val1, val2, corr

# Find the most correlated pair using Pearson cc
def findmostcorrelated_pearson(mytable):
    corr = 0.0
    val1 = -1
    val2 = -1
    for x in range(0, len(mytable)):
        for y in range(x+1, len(mytable)):
            mycorr = pearson_correlation(mytable[x], mytable[y])
            # Convert from correlation (-1 to 1) to distance (0 to 2)
            mycorr = 1-mycorr
            if val1 == -1:
                corr = mycorr
                val1 = x
                val2 = y
                continue
            if mycorr < corr:
                corr = mycorr
                val1 = x
                val2 = y
    return val1, val2, corr

#call the methods as the script loads...

# Processing pipeline
#Test
dd=euclidean_distance([4,5,6,7],[4,5,12,7])
#dd=pearson_correlation([43,21,25,42,57,59],[99,65,79,75,87,81])

#Load files-small file for testing, big file for final search
ed=loadafile("test_bigfile.csv")
#ed=loadafile("test_file1.csv")

#Find most correlated pair
ee=findmostcorrelated(ed)
#ee=findmostcorrelated_pearson(ed)

#print simple results
print("result",dd)
print("result2",ee[0],ee[1],ee[2])

#Plot the winning correlation
plotme(ed[ee[0]],ed[ee[1]])

#The expected answer is index 1 and 49 are 0 distance apart.

#If you load the example file into Excel you can see that these two lines (line 2 and 50 in 1-indexed Excel) have identical rows of values.
# This is why they plot as a straight line and have a Euclidean distance of 0.0!
# For other examples, values may be returned that have distance much greater than 0, we only guarantee to find the closest values in terms of distance compared to the others
#In terms of actual euclidean distance even the closest values might be widely separated in space...

# Euclidean distance is another example of Order n2 (n squared) complexity operation
# Each row has to be compared to every other row so the overall number of comparisons made is the n, the number of rows, times n.
# n is considered  much larger than the number of elements each row that need to be visited to calculate the distance.
# Despite calculating a triangular distance matrix (distAB = distBA), only 50% compute time is saved, but complexity is still O(n2)

# An example using Pearson correlation is provided.
# In this case, a correlation of 1 is returned if the rows being compared are identical.
# Value 0 is returned when the rows are not correlated
# Or -1 if they are anticorrelated
# Use (1-pearson_correlation) to make range from 0 (+ve corr) to 2 (-ve corr) - bounded range makes value interpretation more intuitive

# Spearman correlation uses RANKS of measurements (not actual values) so measures strength of monotonic association (how close the rank order of each pair of measurements match)
# Convert values to ranks, then calculate Pearson correlation of the ranks
# Can find non-linear correlations

# These examples only find the MOST correlated pair
# A complete Correlation Matrix can be built
  # by comparing each row to every other row
  # and export al lthe results as a table
