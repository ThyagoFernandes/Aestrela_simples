import sys
import heapq
class point:
    def __init__(self, before_point,point_value,x,y):
        self.before_point = before_point
        self.point_value = point_value
        self.x = x
        self.y = y

open_list = list()
closed_list = list()        
file_name = sys.argv[1]
map_ = list()
point_B = list()
point_A = list()

i = 0

try:
     with open(file_name) as f_open:
         for line in f_open:
             line_split = line.replace('\n','').split(" ")
             print(line_split)
             if('B' in line_split):
                 point_B = [line_split.index('B'),i]
             if('A' in line_split):
                 point_A = [line_split.index('A'),i]
             i = i+1
             map_.append(line_split)
except Exception as e:
    print(e)
print(map_[0][1])
p_start = point(None,0,0,0)
open_list.append
print('\n '+ str(point_B))


    