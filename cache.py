#!/usr/local/bin/python3
import operator

cacheServer = {}
cacheCapacity = {}
videoSize = {}
numberCache= {}

def initCacheCapacity(server, capacity):
    cacheCapacity[server] = capacity

def initSize(video, size):
    videoSize[video] = size

def top():
    for i in range(1, len(cacheServer) + 1):
        num = 0
        for (j, k) in cacheServer[i]:
            if (cacheCapacity[i] < videoSize[i]):
                numberCache[i] = num + 1
                break
            cacheCapacity[i] = cacheCapacity[i] - videoSize[j]
            num = num + 1
'''
Insert a request in cache server
'''
def insert(servidor, request):
    if servidor in cacheServer:
        if request in cacheServer[servidor]:
            cacheServer[servidor][request] = cacheServer[servidor][request] + 1
        else:
            cacheServer[servidor][request] = 0
    else:
        cacheServer[servidor] = {}
        cacheServer[servidor][request] = 0

def sort_():
    for i in range(1, len(cacheServer) + 1):
        cacheServer[i] = sorted(cacheServer[i].items(), \
                key=operator.itemgetter(1), reverse = True)

def output():
    with open("sub", "w+") as f:
        for i in range(1, len(cacheServer) + 1):
            for j in numberCache:
                for k in range(0, j + 1):
                    x, _ = cacheServer[i][k]
                    f.out(x)

if __name__ == "__main__":
    # Test simple operation
    insert(1, 2)
    insert(1, 1)
    insert(1, 1)
    sort_()
    output()
