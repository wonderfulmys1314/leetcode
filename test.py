n,m,c=map(int,input().split())

#构建一个颜色和珠子位置字典，键为颜色，值为颜色出现的位置列表（按递增顺序排列）

color_index={}

for i in range(0,n):

    color=list(map(int,input().split()))

    if(color[0]==0):

        continue

    for c in color[1:]:

        color_index.setdefault(c,[]).append(i)

print(color_index)



def gap(a,b,n):

    #函数：算两个珠子之间的距离(涉及环)

    #n:整串珠子的总数

    if(a<=b):

        return b-a

    else:

        return n+b-a



count=0

#遍历字典中出现的每一种颜色

for cl in color_index.keys():

    gap_l=[]#记录某种颜色的 珠子相邻珠子位置差

    for j in range(0,len(color_index[cl])):

        #前面的和自己的下一个位置比，最后一颗和第一颗比

        if(j<len(color_index[cl])-1):

            gap_l.append(gap(color_index[cl][j],color_index[cl][j+1],n))

        else:

            gap_l.append(gap(color_index[cl][j],color_index[cl][0],n))

    print(gap_l)

    if(min(gap_l)<=m):#只要珠子相邻位置差值小于m,那么这个颜色就不合格了

        count+=1

print(count)