Program which implements the k-means clustering algorithm for, at the moment, k=3 only.


Red dots in the picture below represent the randomnly initialized 3 centroid points, while 
the blue represents the data points that I generated in the file.
<img width="585" alt="kMeans1" src="https://user-images.githubusercontent.com/37377528/129717738-b7d0cbe2-32c2-443f-aebb-b461a0d75912.png">

The data points closest to a respective centroid are then placed inside its respective cluster.
<img width="585" alt="kMeans2" src="https://user-images.githubusercontent.com/37377528/129718215-696b5d4d-17f9-4351-8988-347afa80f52c.png">

The centroid's positions are then updated and the distances to each data point calculated again and assigned once again
to their respective clusters. This being the final product my program comes out with.
<img width="585" alt="kMeans3" src="https://user-images.githubusercontent.com/37377528/129718327-a968bc10-929d-405d-87d1-8a55cb6f579f.png">

NOTE: I have not implemented the k-means++ algorithm to help in avoiding the random initialization trap that can come about
if a particular set of initial positions for the centroids are chosen. The result can be a bad clustering of the data points, 
and I have instead decided to just choose new initial points chose which ones worked.


