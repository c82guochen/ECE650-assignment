import re
class Vertex:
    def __init__ (self, x, y):
        self.x = float(x)
        self.y = float(y)
    def __str__ (self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

class Edge(object):
    def __init__ (self, src, dst):
        self.src = src
        self.dst = dst
    def __str__(self):
        return '<' + str(self.src) + ',' + str(self.dst) + '>'

class Street :
    streetName = ""
    vertexes=[]  #顶点组
    Lines = [] #顶点组成的边
    def __init__(self,name,inputVertex) :
        self.streetName = name 
        for x in inputVertex :
            self.vertexes.append(x)
        self.calculateLine(self)
    def calculateLine(self) :
        self.Lines = []
        for i in range(0,len(self.vertexes)) :
            singleLine = Edge(self.vertexes[i],self.vertexes[i+1])
            self.Lines.append(singleLine)
    def mod(self,inputVertex):  
        self.vertexes=[]  
        self.Lines = [] 
        for x in inputVertex :
            self.vertexes.append(x)
        self.calculateLine(self)

name_rx = '\".+\"'
num_rx = '-?\d+'
coord_rx = r'\(\s*'+num_rx+'\s*,\s*'+num_rx+'\s*\)'
# cmd_a_rx = '\s*add\s+'+name_rx+'\s+('+coord_rx+'\s*){2,}\s*$'
# cmd_m_rx = '\s*mod\s+'+name_rx+'\s+('+coord_rx+'\s*){2,}\s*$'
# cmd_r_rx = '\s*rm\s+'+name_rx+'\s*$'
# cmd_g_rx = '\s*gg\s*'
# cmd_a_chk = re.compile(cmd_a_rx, re.I)
# cmd_m_chk = re.compile(cmd_m_rx, re.I)
# cmd_r_chk = re.compile(cmd_r_rx, re.I)
# cmd_g_chk = re.compile(cmd_g_rx, re.I)

str1 = 'add "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)'
# str2 = 'add "King Street S" (4,2) (4,8)'
# str3 = 'add "Davenport Road" (1,4) (5,8)'
tuple1 = re.search(name_rx,str1,re.I).span()
# tuple2 = re.search(name_rx,str2,re.I).span()
# tuple3 = re.search(name_rx,str3,re.I).span()
# print(str1[tuple1[0]+1:tuple1[1]-1],str2[tuple2[0]+1:tuple2[1]-1],str3[tuple3[0]+1:tuple3[1]-1])
name = str1[tuple1[0]+1:tuple1[1]-1]
if re.search('\d',name,re.I) != None :
    print('Error!The street name ',name, ' is invalid!(including some numbers)')


tupleV = re.search('('+coord_rx+'\s*){2,}',str1).span() 
vStr = str1[tupleV[0]:tupleV[1]]
vList = []

corrds = re.findall('('+coord_rx+'\s*)',vStr)
print(corrds)
for x in corrds :
    tuplex = re.search(num_rx,x).span()
    Vx = int(x[tuplex[0]:tuplex[1]])
    cropY = x[tuplex[1]+1:]
    tupley = re.search(num_rx,cropY).span()
    Vy = int(cropY[tupley[0]:tupley[1]])
    vertex = Vertex(Vx,Vy)
    vList.append(vertex)
for x  in vList :
    print(x)  

    
# endIndex = 0
# crop = vStr
# tuplePair = re.search('('+coord_rx+'\s*)',crop)
# while tuplePair != None :
#     tuplePair = re.search('('+coord_rx+'\s*)',crop)
#     if tuplePair != None :
#         tuplePair = tuplePair.span()
#         cropPair = crop[tuplePair[0]:tuplePair[1]]
#         tuplex = re.search(num_rx,cropPair).span()
#         Vx = int(cropPair[tuplex[0]:tuplex[1]])
#         cropPairY = crop[tuplex[1]+1:tuplePair[1]]
#         tupley = re.search(num_rx,cropPairY).span()
#         Vy = int(cropPairY[tupley[0]:tupley[1]])
#         vertex = Vertex(Vx,Vy)
#         vList.append(vertex)
#         endIndex = tuplePair[1] - 1
#         crop = crop[endIndex:]
# # street = Street()
# for x  in vList :
#     print(x)

# strNum = '-1'
# tupleNum = re.search('-?\d+',strNum).span() 
# print(type(int(strNum[tupleNum[0]:tupleNum[1]])))

# tuple5 = re.search('('+coord_rx+'\s*){2,}',str2).span()
# print(str2[tuple5[0]:tuple5[1]])
# tuple6 = re.search('('+coord_rx+'\s*){2,}',str3).span()
# print(str3[tuple6[0]:tuple6[1]])