from scipy.spatial import kdtree, KDTree 
from scipy.spatial.distance import euclidean, cityblock, cosine, hamming

points = [(1,-1),(2,3),(-2,3),(2,-3),(4,5)]

kdt = KDTree(points)
print( 'Nearest Point to (1,1) in the given set of points is : ' + str(kdt.query((1,1))))

p1 = (1, 0)
p2 = (10, 2)
p3 = (11,12)


print("Euclidean Distance between p1 p2 and p3 is : " + str(euclidean(p1, p2, p3)))
print("Manhattan Distance between p1 p2 and p3 is : " + str(cityblock(p1, p2, p3)))
print("Cosine Distance between p1 p2 and p3 is : " + str(cosine(p1, p2, p3)))

p4 = (True,False,True,True)
p5 = (False,True,True,False)

print("Hamming Distance [Binary Sequence Distance] between p4 and p5 is : " + str(hamming(p4, p5)))