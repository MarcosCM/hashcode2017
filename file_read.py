import operator
FILE_IN = 'kittens.in'
FILE_IN = 'me_at_the_zoo.in'
FILE_IN = 'trending_today.in'
FILE_IN = 'videos_worth_spreading.in'

f = open(FILE_IN, 'r')

cacheServer = {}
numberCache= {}
first_line = f.readline().strip()
problem_desc_arr = first_line.split(' ')
cache_size = int(problem_desc_arr[4])
videos_arr = f.readline().strip().split(' ')
ep = dict()
endpoint = dict()
videos = dict()
total = 0

def top():
    for i,j in cacheServer.items():
        iter_ = 0
        tmp = cache_size
        for k in j:
            try:
                x, _ = k
                tmp = tmp - int(videos[x]['video_size'])
                if tmp < 1:
                    tmp = tmp + int(videos[x]['video_size'])
                    break
                iter_ += 1
            except:
                break
        numberCache[i] = iter_
'''
Insert a request in cache server
'''
def insert(servidor, request, num):
    if servidor in cacheServer:
        if request in cacheServer[servidor]:
            cacheServer[servidor][request] = cacheServer[servidor][request] + num
        else:
            cacheServer[servidor][request] = num
    else:
        cacheServer[servidor] = {}
        cacheServer[servidor][request] = num

def sort_():
    global total
    for i in range(0, len(cacheServer)):
        try:
            cacheServer[i] = sorted(cacheServer[i].items(), \
                key=operator.itemgetter(1), reverse = True)
            total += 1
        except KeyError:
            print("Not used")

def output():
    global total
    with open("subv", "w+") as f:
        f.write(str(total) + "\n")
        for i, m in cacheServer.items():
            if numberCache[i] is 0:
                continue
            f.write(str(i) + " ")
            for j in range(0, numberCache[i]):
                x, _ = m[j]
                f.write(str(x) + " ")
            f.write("\n")

def parse():
    # video sizes
    for i in range(0, len(videos_arr)):
        videos[i] = { 'video_size' : videos_arr[i] }

    # endpoint latencies to caches
    for i in range(0, int(problem_desc_arr[1])):
        ep_info = f.readline().strip().split(' ')
        ep[i] = dict()
        ep[i]['dc_latency'] = ep_info[0]
        ep[i]['caches'] = dict()
        for j in range(0, int(ep_info[1])):
            ep_to_cache_info = f.readline().strip().split(' ')
            arr = []
            arr.append(int(ep_to_cache_info[0]))
            arr.append(int(ep_to_cache_info[1]))
            ep[i]['caches'][int(ep_to_cache_info[0])] = int(ep_to_cache_info[1])

    # video request for video from endpoint
    for i in range(0, int(problem_desc_arr[1])):
        endpoint[i] = dict()
        for j in range(0, int(problem_desc_arr[0])):
            endpoint[i][j] = 0

    for i in range(0, int(problem_desc_arr[2])):
        vr = f.readline().strip().split(' ')

        #            ep_idx   video_idx  num_req  
        # endpoints = { 0:       {3:      1500,   0: 1000} }
        endpoint[int(vr[1])][int(vr[0])] += int(vr[2])

def minLate(ep_):
    min_ = -1
    iter_ = 0
    for i, j in ep_['caches'].items():
        if min_ is -1:
            min_ = j 
            iter_ = i
        elif min_ > j:
            min_ = ep_['caches'][i]
            iter_= i
    return iter_ 

if __name__ == "__main__":
    parse()
    for i, j in endpoint.items():
        min_ = minLate(ep[i])
        for k, l in j.items():
            insert(min_, k, l)
    sort_()
    top()
    output()
