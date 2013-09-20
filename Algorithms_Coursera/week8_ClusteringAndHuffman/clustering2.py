
'''
In this programming problem and the next you'll code up the clustering algorithm from lecture for computing a max-spacing k-clustering. Download the text file here. This file describes a distance function (equivalently, a complete graph with edge costs). It has the following format:

[number_of_nodes]
[edge 1 node 1] [edge 1 node 2] [edge 1 cost]
[edge 2 node 1] [edge 2 node 2] [edge 2 cost]
...
There is one edge (i,j) for each choice of 1≤i<j≤n, where n is the number of nodes. For example, the third line of the file is "1 3 5250", indicating that the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. You can assume that distances are positive, but you should NOT assume that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number k of clusters is set to 4. What is the maximum spacing of a 4-clustering?

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum! '''
#This page gives me a lot of help https://class.coursera.org/algo2-002/forum/thread?thread_id=106

theFile = open("clustering1.txt",'r')
lines = theFile.readlines()
numberNones = int(lines[0])
lines = lines[1:]
edges = [[int(line.split()[0]),int(line.split()[1]),int(line.split()[2])] for line in lines]
edges = sorted(edges,key = lambda x:x[2])
clusters = {k:[k] for k in range(numberNones+1)}
pointCluster = [k for k in range(numberNones+1)]
NextStop = False
for edge in edges:
    p1 = edge[0]
    p2 = edge[1]
    if NextStop and not pointCluster[p1] == pointCluster[p2]:
        print "The space is:",edge  
        break
    #p1 and p2 not in the same cluster
    if not pointCluster[p1] == pointCluster[p2]:
        if pointCluster[p1]  < pointCluster[p2]:
            clusters[pointCluster[p1]] += clusters[pointCluster[p2]] 
            temp = pointCluster[p2]
            for p in clusters[pointCluster[p2]] :
                pointCluster[p] = pointCluster[p1]
            del clusters[temp]
        else:
            clusters[pointCluster[p2]] += clusters[pointCluster[p1]]
            temp = pointCluster[p1]
            for p in clusters[pointCluster[p1]]:
                pointCluster[p] = pointCluster[p2]
            del clusters[temp]
    if len(clusters.items()) == 5:
        NextStop = True

for c in clusters.items():
    print(c)

            