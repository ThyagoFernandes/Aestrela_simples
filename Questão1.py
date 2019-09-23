import sys
import heapq
file_name = sys.argv[1]
map_ = list()
point_B = list()
i = 0

try:
     with open(file_name) as f_open:
         for line in f_open:
             line_split = line.replace('\n','').split(" ")
             print(line_split)
             if('B' in line_split):
                 point_B = [line_split.index('B'),i]
             i = i+1
             map_.append(line_split)
except Exception as e:
    print(e)
print(map_[0][1])
print('\n '+ str(point_B))


    