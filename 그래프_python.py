#자료구조 한옥영 교수님 12주차 실습과제
#그래프 ADT 실습과제
#최종 작성일: 2020.06.07(일)
#2019312481 심규현

class Vertex:
    def __init__(self, data):
        self.data = data
        self.link = None
        self.visited = None
    

class Graph:
    def __init__(self):
        head = Vertex(None)
        self.vertex = []
        self.vertex.append(head) #인덱스 1부터 시작
        self.size = 0
        
    def clear_visited(self):
        for i in range(self.size+1):
            self.vertex[i].visited = None
        return
    
    def position(self, data):
        for i in range(self.size+1):
            if self.vertex[i].data == data:
                return i
        return -1
    
    def insert_vertex(self, data):
        if self.position(data) != -1:
            print("ERROR: Vertex With Such Value Already Exists.")
            return
        new_vertex = Vertex(data)
        self.vertex.append(new_vertex)
        self.size = self.size + 1
        return
    
    def add_edge(self, data1, data2):
        i = self.position(data1)
        j = self.position(data2)
        vi = None
        vj = None
        if i == -1 or j == -1:
            print("ERROR: Can't Find Vertex")
        if i != -1:
            vi = self.vertex[i]
            while(vi.link != None):
                vi = vi.link
        if j != -1:
            vj = self.vertex[j]
            while(vj.link != None):
                vj = vj.link
        new_v1 = Vertex(data2)
        new_v2 = Vertex(data1)
        vi.link = new_v1
        vj.link = new_v2
        
    def degree_of_vertex(self, data):
        cnt = 0
        pos = self.position(data)
        if pos == -1:
            print("ERROR: Can't Find Vertex with Such Value.")
            return -1
        v = self.vertex[pos]
        while(v.link != None):
            cnt = cnt + 1
            v = v.link
        return cnt
        
    def is_empty(self):
        if self.size == 0:
            return 1
        else:
            return 0
            
    def adjacent(self, data):
        pos = self.position(data)
        if pos == -1:
            print("ERROR: Vertex With Such Value Does Not Exist.")
            return
        if self.vertex[pos].link == None:
            print("No Adjacent Vertex.")
            return
        print("{", end="")
        v = self.vertex[pos].link
        while(v.link != None):
            print("%c, "%(v.data), end="")
            v = v.link
        print("%c}"%(v.data))
        return
        
    def path(self, data1, data2):
        pos = self.position(data1)
        tmp = 0
        v = self.vertex[pos]
        orig = self.vertex[pos]
        if v.visited != None:
            if v.visited.data == data2:
                return 1
        if v.data == data2:
            return 1
        while(v.link != None):
            temp_v = self.vertex[self.position(v.link.data)]
            if temp_v.visited == None:
                if v.link.data == data2:
                    orig.visited = self.vertex[self.position(data2)]
                    return 1
            v = v.link
        v = self.vertex[pos]
        while(v.link != None):
            temp_v = self.vertex[self.position(v.link.data)]
            if temp_v.visited == None:
                orig.visited = self.vertex[self.position(v.link.data)]
                tmp = self.path(v.link.data, data2)
                if tmp == 1:
                    return 1
            v = v.link
        return 0
        
    def printpath(self, data1, data2):
        if self.path(data1, data2) == 0:
            print("No Path Between Two Vertex.")
        else:
            pos = self.position(data1)
            v = self.vertex[pos]
            print("PATH: ", end="")
            while(v.visited != None):
                print("%c -> "%(v.data), end="")
                v = v.visited
            print("%c"%(v.data))
        return
        
    def delete_edge(self, data1, data2, mode):
        i = self.position(data1)
        j = self.position(data2)
        vi = None
        vj = None
        edge_i = None
        edge_j = None
        before_edge_i = None
        before_edge_j = None
        if i == -1 or j == -1:
            if mode == 1:
                print("ERROR: Can't Find Vertex")
            return -1
        if i == j:
            if mode == 1:
                print("ERROR: Edge Does Not Exist Between Same Vertex.")
            return -1
        if i != -1:
            if self.vertex[i].link == None:
                if mode == 1:
                    print("ERROR: Edge Does Not Exist.")
                return -1
            vi = self.vertex[i].link
            if vi.data == data2:
                edge_i = vi
                before_edge_i = self.vertex[i]
            else:
                while(vi.link != None):
                    if vi.link.data == data2:
                        edge_i = vi.link
                        before_edge_i = vi
                    vi = vi.link
        if j != -1:
            if self.vertex[j].link == None:
                if mode == 1:
                    print("ERROR: Edge Does Not Exist.")
                return -1
            vj = self.vertex[j].link
            if vj.data == data1:
                edge_j = vj
                before_edge_j = self.vertex[j]
            else:
                while(vj.link != None):
                    if vj.link.data == data1:
                        edge_j = vj.link
                        before_edge_j = vj
                    vj = vj.link
        if edge_i == None or edge_j == None:
            if mode == 1:
                print("ERROR: Edge Does Not Exist.")
            return -1
        before_edge_i.link = edge_i.link
        before_edge_j.link = edge_j.link
        return 1
    
    def delete_vertex(self,data, mode):
        ans = None
        pos = self.position(data)
        if pos == -1:
            print("ERROR: Vertex With Such Value Does Not Exist.")
            return
        v = None
        if mode == 1:
            print("ARE YOU SURE YOU WANT TO DELETE VERTEX %c?"%(data), end="")
            v = self.vertex[pos]
            if v.link != None:
                v = v.link
                print("\nIT HAS EDGE BETWEEN ", end="")
                while(v.link != None):
                    print("%c, "%(v.data), end="")
                    v = v.link
                ans = input("%c. (Y/N) "%(v.data))
            else:
                ans = input("(Y/N) ")
        else:
            ans = "Y"
        if ans == "Y":
            v = self.vertex[pos]
            while(self.vertex[pos].link != None):
                v = self.vertex[pos]
                while(v.link != None):
                    self.delete_edge(data, v.link.data, 0)
            self.vertex.pop(pos)
            self.size = self.size - 1
        elif ans == "N":
            print("DELETE CANCELLED.")
        return
    
    def is_connected(self):
        if self.size == 0:
            return 1
        v1 = self.vertex[1]
        for i in range(self.size+1):
            if i == 0:
                continue
            if self.path(v1.data, self.vertex[i].data) == 0:
                return 0
            self.clear_visited()
        return 1
        
    def num_of_vertex(self):
        return self.size
    
    def num_of_edge(self):
        cnt = 0
        for i in range(self.size+1):
            cnt = cnt + self.degree_of_vertex(self.vertex[i].data)
        cnt = cnt/2
        return cnt
    
    def rename_vertex(self, old, new):
        i = self.position(old)
        j = self.position(new)
        v = None
        if i == -1:
            print("ERROR: Vertex With Such Value Does Not Exist.")
            return
        if j != -1:
            print("ERROR: Vertex With New Value Already Exists.")
            return
        self.vertex[i].data = new
        for k in range(self.size+1):
            if self.vertex[k].data == new:
                continue
            v = self.vertex[k]
            while(v.link != None):
                if v.link.data == old:
                    v.link.data = new
                v = v.link
        return

    def clear_graph(self):
        for i in range(self.size):
            self.delete_vertex(self.vertex[1].data, 0)
        return
        
    def print_edge(self, vertex):
        if vertex.link == None:
            return
        print("(", end="")
        while(vertex.link != None):
            print("%c"%(vertex.link.data), end="")
            if(vertex.link.link != None):
                print(",", end="")
            vertex = vertex.link
        print(")", end="")
        
    def print_graph(self):
        if(self.size == 0):
            print("Empty Graph.")
            return
        print("(", end="")
        for i in range(self.size+1):
            if i == 0:
                continue
            print("%c"%(self.vertex[i].data), end="")
            self.print_edge(self.vertex[i])
            if i != self.size:
                print(", ", end="")
        print(")")

    def is_eular(self):
        count_odd = 0
        tmp = 0
        for i in range(self.size+1):
            if i == 0:
                continue
            tmp = self.degree_of_vertex(self.vertex[i].data)
            if tmp % 2 == 1:
                count_odd = count_odd + 1
            if tmp == 0:
                return 0
        if count_odd == 0 or count_odd == 2:
            return 1
        return 0

    def merge(self, data1, data2):
        i = self.position(data1)
        j = self.position(data2)
        tmp = self.delete_edge(data1, data2, 1)
        tmp_data = None
        if tmp == -1:
            return
        if i == -1 or j == -1:
            return
        vi = self.vertex[i]
        vj = self.vertex[j]
        while(vj.link != None):
            vj = vj.link
            tmp_data = vj.data
            self.delete_edge(data1, tmp_data, 0)
            self.add_edge(data1, tmp_data)
        self.delete_vertex(data2, 0)
        return
    
print("명령문 안내")
print("G: 그래프 생성")
print("+정점의 값: 그래프에 정점 추가")
print("-정점의 값: 그래프에서 정점 제거")
print("E(정점1,정점2): 지정한 두 개의 정점을 잇는 간선 생성")
print("V(값): 현재 정점의 간선 개수 출력")
print("C: 연결 그래프인지를 출력")
print("N: 빈 그래프인지를 출력")
print("A(정점의 값): 해당 정점의 인접 정점 출력")
print("P(정점1,정점2): 정점1부터 정점2로가는 경로의 존재 여부 출력")
print("Q(정점1,정점2): 정점1부터 정점2로가는 경로 출력")
print("X: 그래프의 정점의 수 출력")
print("H: 그래프의 간선의 수 출력")
print("D(정점1,정점2): 지정한 두 개의 정점을 잇는 간선 삭제")
print("R(정점,새로운 값): 지정한 정점의 값을 변경")
print("L: 그래프 출력")
print("U: 오일러 그래프인지를 출력")
print("M(정점1,정점2): 지정한 두 개의 정점을 합병 (값은 정점1의 값을 가짐)")
print("K: 그래프 비우기")
print("&: 프로그램 종료\n")

my_graph = Graph()

while True:
    default_print = 1
    used = 0 #한 명령에서 한 개 이상의 문자를 사용할 경우 중복 입력 방지용 변수

    inp = input("명령어: ") #문자열로 명령어 입력 받기

    if inp[0] == '&': #종료 명령
        break

    for i in range(len(inp)):
        if used > 0:
            used = used - 1
            
        elif inp[i] == 'G': #create의 역할은 이미 위에서 수행
            default_print = 1

        elif inp[i] == '+':
            if i+1 == len(inp)-1:
                used = used + 1
                my_graph.insert_vertex(inp[i+1])
            else:
                print("ERROR: Invalid Input.")
                
        elif inp[i] == '-':
            if i+1 == len(inp)-1:
                used = used + 1
                my_graph.delete_vertex(inp[i+1], 1)
            else:
                print("ERROR: Invalid Input.")
                    
        elif inp[i] == 'L':
            my_graph.print_graph()
            default_print = 0
            
        elif inp[i] == 'E':
            tmp = inp[inp.index('(')+1:inp.index(')')].split(',')
            my_graph.add_edge(tmp[0], tmp[1])
            used = used + (inp.index(')') - inp.index('(') - 1)
            break
            
        elif inp[i] == 'D':
            tmp = inp[inp.index('(')+1:inp.index(')')].split(',')
            my_graph.delete_edge(tmp[0], tmp[1], 1)
            used = used + (inp.index(')') - inp.index('(') - 1)
            break
        
        elif inp[i] == 'V':
            tmp = inp[inp.index('(')+1:inp.index(')')]
            print("%d"%(my_graph.degree_of_vertex(tmp[0])))
            used = used + (inp.index(')') - inp.index('(') - 1)
            default_print = 0
            break
        
        elif inp[i] == 'C':
            if my_graph.is_connected() == 1:
                print("True")
            else:
                print("False")
            default_print = 0
            
        elif inp[i] == 'N':
            if my_graph.is_empty() == 1:
                print("True")
            else:
                print("False")
            default_print = 0
        
        elif inp[i] == 'A':
            tmp = inp[inp.index('(')+1:inp.index(')')]
            my_graph.adjacent(tmp[0])
            used = used + (inp.index(')') - inp.index('(') - 1)
            default_print = 0
            break
            
        elif inp[i] == 'P':
            tmp = inp[inp.index('(')+1:inp.index(')')].split(',')
            if my_graph.path(tmp[0], tmp[1]) == 1:
                print("True")
            else:
                print("False")
            my_graph.clear_visited()
            used = used + (inp.index(')') - inp.index('(') - 1)
            break
        
        elif inp[i] == 'X':
            print("%d"%(my_graph.num_of_vertex()))
            default_print = 0
        
        elif inp[i] == 'H':
            print("%d"%(my_graph.num_of_edge()))
            default_print = 0
            
        elif inp[i] == 'R':
            tmp = inp[inp.index('(')+1:inp.index(')')].split(',')
            my_graph.rename_vertex(tmp[0], tmp[1])
            used = used + (inp.index(')') - inp.index('(') - 1)
            break
        
        elif inp[i] == 'K':
            my_graph.clear_graph()
        
        elif inp[i] == 'Q':
            tmp = inp[inp.index('(')+1:inp.index(')')].split(',')
            my_graph.printpath(tmp[0], tmp[1])
            my_graph.clear_visited()
            used = used + (inp.index(')') - inp.index('(') - 1)
            default_print = 0
            break
            
        elif inp[i] == 'U':
            if my_graph.is_eular() == 1:
                print("True")
            else:
                print("False")
            default_print = 0
        
        elif inp[i] == 'M':
            tmp = inp[inp.index('(')+1:inp.index(')')].split(',')
            my_graph.merge(tmp[0], tmp[1])
            used = used + (inp.index(')') - inp.index('(') - 1)
            break
            
    if default_print == 1:
        my_graph.print_graph()
    else:
        default_print = 1
