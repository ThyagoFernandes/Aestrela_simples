import sys
import heapq
class point:
    before_point= None 
    h = 0
    g = 0 
    j = 0
    i = 0
    content = 0
    def __init__(self, before_point,h,g,i,j,content):
        self.before_point = before_point
        self.g = g
        self.h = h
        self.j = j
        self.i = i
        self.content = content
def find_way():
    point_ = point_B
    path = list()
    path.append([point_.i,point_.j])
    while(point_ != point_A):
        path.append([point_.before_point.j,point_.before_point.i])
        point_ = point_.before_point
    return path
def dist_manhattan(j_point,i_point,j_goal,i_goal,):
    return abs(j_point - j_goal) + abs(i_point - i_goal)
def isgoal(j_point,i_point,j_goal,i_goal):
    return (j_point == j_goal) and (i_point == i_goal)
def find_children_valid(p):
    children_base = [[0,1],[1,0],[0,-1],[-1,0]]
    children_valid = list()
    print(p.i,p.j)
    for child in children_base :
        try:
            if(p.i+child[0] >= 0 and p.j+ child[1]>= 0):
                if((map_[p.i+child[0]][p.j+ child[1]].content == '0' or map_[p.i+child[0]][p.j+ child[1]].content == 'B') and map_[p.i+child[0]][p.j+ child[1]] not in closed_list ):                
                    children_valid.append(map_[p.i+child[0]][p.j+ child[1]])
        except Exception as e:
            pass
    return children_valid

    
open_list = list()
closed_list = list()        
file_name = sys.argv[1]
map_ = list()
point_B = None
point_A = None

i = 0

try:
     with open(file_name) as f_open:
         for line in f_open:
             line_split = line.replace('\n','').split(" ")
             point_list = list()
             j = 0
             #print(line_split)
             for l in line_split:
                
                point_ = point(None,0,0,i,j,l)
                if(point_.content == 'B'):
                     point_B = point_
                if(point_.content == 'A'):
                     point_A = point_
                print(point_.content+' ',end='')
                point_list.append(point_)
                j= j+1
             print('\n')   
             i = i+1           
             map_.append(point_list)
             
except Exception as e:
    print(e)
if(point_A is None):
    print("There is no point A at map, please insert one into it")
    sys.exit()
print()
if(point_B is None):
    print("There is no point B at map, please insert one into it")
    sys.exit()


print(point_A.content+ "f")
open_list.append(point_A)
while (len(open_list)>0):
    open_list.sort(key=lambda p: p.g+p.h)
    p = open_list[0]
    content = [[p.h+p.g,p.content] for p  in open_list]
    open_list.pop(0)

        
    closed_list.append(p)
    children_valid = find_children_valid(p)
    content = [[p.i,p.j] for p in children_valid]
    print(content)
    for child in children_valid:
        child.before_point = p
        child.g = p.g +1
        child.h = dist_manhattan(child.j,child.i,point_B.j,point_B.i)
        open_list.append(child)
if(point_B.before_point is not None):
    print(point_B.before_point.i,point_B.before_point.j,point_B.i,point_B.j)
    path = find_way()
    print(path)
    
else:
    print('There is no path to point B')
