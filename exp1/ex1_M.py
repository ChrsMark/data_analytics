import os, sys
import numpy 
import time
from math import radians, cos, sin, asin, sqrt

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
            res.append((lat, long))
    return res
             
def readFile_two(filename):
    res = []
    with open(filename) as f:
        for line in f:
            lat = float(line.split("|")[3])
            long = float(line.split("|")[4])
            res.append((lat, long))
    return res

def run_experiment(h_range, M, hotels, rests):
    scores = []
    R = 100
    start_time = time.time()
    for hotel in hotels[:h_range]:
        good_rests = 0
        for rest in rests[:M]:
           dist = calc_distance(hotel, rest)
           if dist <= R:
               good_rests = good_rests + 1
        scores.append(good_rests)
    elapsed_time = time.time() - start_time
    mean_score = numpy.mean(scores)
    best_score = max(scores)
    with open("test_results_M_mean_score.txt", "a") as myfile:
      myfile.write("{}\t{}\t{}\n".format(h_range, M, mean_score))
    with open("test_results_M_max_score.txt", "a") as myfile:
      myfile.write("{}\t{}\t{}\n".format(h_range, M, best_score))
    with open("test_results_M_time.txt", "a") as myfile:
      myfile.write("{}\t{}\t{}\n".format(h_range, M, elapsed_time))


if __name__ == "__main__":
    
    hotels = readFile('./hotels.txt')
    print(len(hotels))

    rests = readFile_two('./restaurants.txt')
    print(len(rests))
    h_range = [50, 100, 500, 1000, 5000, 10000, len(hotels)-1]
    Ms = [50, 100, 500, 1000, 5000, 10000, len(rests) -1]
    count = 0 
    all_ = len(h_range) * len(Ms)
    for r in h_range:
        for m in Ms:
            count += 1
            run_experiment(r, m, hotels, rests)
            print("{} out of {}".format(count, all_))
