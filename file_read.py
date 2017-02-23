FILE_IN = 'me_at_the_zoo.in'

f = open(FILE_IN, 'r')

first_line = f.readline().strip()
problem_desc_arr = first_line.split(' ')
cache_size = problem_desc_arr[4]
videos_arr = f.readline().strip().split(' ')
# video sizes
videos = dict()
for i in range(0, len(videos_arr)):
    videos[i] = { 'video_size' : videos_arr[i] }

# endpoint latencies to caches
ep = dict()
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
endpoint = dict()
for i in range(0, int(problem_desc_arr[2])):
    endpoint[i] = dict()
    for j in range(0, int(problem_desc_arr[0])):
        endpoint[i][j] = 0

for i in range(0, int(problem_desc_arr[2])):
    vr = f.readline().strip().split(' ')

    print(vr)
    #            ep_idx   video_idx  num_req  
    # endpoints = { 0:       {3:      1500,   0: 1000} }
    endpoint[int(vr[1])][int(vr[0])] += int(vr[2])