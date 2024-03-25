###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    
    f = open(filename, 'r')
    name_dict = {}
    
    for line in f.readlines():
        store = line.split(",")
        name_dict[store[0]] = store[1].strip("\n")
        
    f.close()
    
    return name_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_sorted = sorted(list(cows.items()), key = lambda x: float(x[1]), reverse = True)
    num_cows_left = len(cows_sorted)
    trip = []
    while num_cows_left > 0:
        this_trip = []
        accu_w = 0
        i = 0
        while i < len(cows_sorted):
            accu_w += float(cows_sorted[i][1])
            if accu_w > limit:
                break
            else:
                this_trip.append(cows_sorted[i][0])
                i += 1
        trip.append(this_trip)
        cows_sorted = cows_sorted[i:]
        num_cows_left = len(cows_sorted)
    
    return trip       

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    cow_list = list(cows.items())
    best_trip = list()
    partitions = []
    # All partition:
    for partition in get_partitions(cow_list):
        partitions.append(partition)
    partitions.sort(key = lambda x: len(x))
    for partition in partitions:
        i = 0
        while i < len(partition):
            accu_w = 0
            for part in partition[i]:
                accu_w += int(part[1])
            if accu_w > limit:
                break
            i += 1
        if i == len(partition):
            for t in range(len(partition)):
                trip = list()
                for part in partition[t]:
                    trip.append(part[0])
                best_trip.append(trip)
            break
    return best_trip
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows('ps1_cow_data.txt')
    print('Cows:', cows)
    
    print()
    
    start = time.time()
    result = greedy_cow_transport(cows)
    end = time.time()
    print('Greedy result:', result)
    print('Greedy executing time:', end-start)
    
    print()
    start = time.time()
    result = brute_force_cow_transport(cows)
    end = time.time()
    print('Brute force result:', result)
    print('Brute force executing time:', end-start)
    
compare_cow_transport_algorithms()

















