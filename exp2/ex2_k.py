import os, sys
import numpy 
import time
from math import radians, cos, sin, asin, sqrt
from sklearn.neighbors import NearestNeighbors

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

def calc_distance(point1, point2):
    return haversine(point1[0], point1[1], point2[0], point2[1])

def readFile(filename):
    res = []
    with open(filename) as f:
        for line in f:
            lat = float(line.split("|")[4])
            long = float(line.split("|")[5])
            res.append([lat, long])
    return res
             
def readFile_two(filename):
    res = []
    with open(filename) as f:
        for line in f:
            lat = float(line.split("|")[3])
            long = float(line.split("|")[4])
            res.append([lat, long])
    return res

def run_experiment(k, M, hotels, rests):
    scores = []
    start_time = time.time()
    for hotel in hotels:
        good_rests = 0
        array_set = numpy.array([hotel] + rests[:M])
        dist = calc_k_neis_max_dist(k, array_set)
        scores.append(dist)
    elapsed_time = time.time() - start_time
    mean_score = numpy.mean(scores)
    best_score = min(scores)
    print(mean_score, best_score)
    with open("test_results_k_meanscore_big5.txt", "a") as myfile:
      myfile.write("{}\t{}\t{}\n".format(k, M, mean_score))
    with open("test_results_k_bestscore_big5.txt", "a") as myfile:
      myfile.write("{}\t{}\t{}\n".format(k, M, best_score))
    with open("test_results_k_elapsedtime_big5.txt", "a") as myfile:
      myfile.write("{}\t{}\t{}\n".format(k, M, elapsed_time))

def calc_k_neis_max_dist(k, array_set):
    nbrs = NearestNeighbors(n_neighbors=k+1, algorithm='ball_tree').\
        fit(array_set)
    distances, indices = nbrs.kneighbors(array_set)
    return max(distances[0])

if __name__ == "__main__":
    
    hotels = readFile('./hotels.txt')
    print(len(hotels))

    rests = readFile_two('./restaurants.txt')
    print(len(rests))
    K = [1, 5, 10, 50, 100, 500]
    Ms = [50, 100, 500, 1000, 5000]
    # Ms = [100]
    count = 0
    # run_experiment(100, 100, hotels, rests, 3)
    all_ = len(K) * len(Ms) 
    for k in K:
         for m in Ms:
             count += 1
             print("{} out of {}".format(count, all_))
             if k > m:
                 continue
             run_experiment(k, m, hotels, rests)
