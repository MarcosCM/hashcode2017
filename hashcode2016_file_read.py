FILE_IN = 'me_at_the_zoo.in'

f = open(FILE_IN, 'r')

first_line = f.readline().strip()
problem_desc_arr = first_line.split(' ')
videos_arr = f.readline().strip().split(' ')
# video sizes
for i in range(0, len(videos_arr)):
    videos_arr.append({ 'video_size' : videos_arr[i] })

# endpoint latencies to caches
for i in range(0, int(problem_desc_arr[1])):
    ep = f.readline().strip().split(' ')
    latency = ep[0]
    caches = []
    for j in range(0, int(ep[1])):
        cache_info = f.readline().strip().split(' ')
        arr = []
        arr.append(int(cache_info[0]))
        arr.append(int(cache_info[1]))
        caches.append(arr)
        print(caches[j])

# video request for video from endpoint
endpoint = dict()
for i in range(0, int(problem_desc_arr[2])):
    vr = f.readline().strip().split(' ')

    #            ep_idx   video_idx  num_req  
    # endpoints = { 0:       {3:      1500,   0: 1000} }
    current_keys = endpoint.keys()
    if not int(vr[1]) in current_keys:
        endpoint[int(vr[1])] = dict()
    endpoint[int(vr[1])][int(vr[0])] = int(vr[2])
    print(int(vr[1]))
    print(endpoint[int(vr[1])])