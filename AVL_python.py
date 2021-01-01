#자료구조 한옥영 교수님 11주차 실습과제
#23 트리 ADT 실습 과제
#최종 작성일: 2020.05.31(일)
#2019312481 심규현

#설명해주신대로 위로 계속 만들어나가는 방식이 아니라, 루트 노드일 경우를 따로 분리하여
#자식 노드들을 조정하는 방식으로 구현하였습니다. 실행 결과의 차이는 없습니다.

class Node:
    def __init__(self, value, height, parent=None): #생성자
        self.type = 2 #type 2면 값 1개 자식 2개, type 3이면 값 2개 자식 3개
        self.data = [value, None, None] #최대 3개의 data (나누기 전)
        self.child = [None, None, None, None] #최대 4개의 자식노드 (나누기 전)
        self.height = height
        self.parent = parent

    def push(self, data): #이미 존재하는 노드에 데이터 넣기
        if data == None:
            return
        if self.type == 2:
            self.type = 3
            if self.data[0] == None:
                self.data[0] = data
            else:
                self.data[0], self.data[1] = sorted([data, self.data[0]])
        elif self.type == 3:
            self.type = 4
            if self.data[1] == None:
                self.data[0], self.data[1] = sorted([data, self.data[0]])
            else:
                self.data[0], self.data[1], self.data[2] = sorted([data, self.data[0], self.data[1]])

    def split(self): #노드를 나눠야 하는 경우. 한 노드에 값이 3개 이상일때 실행됨.
        if self.type == 2 or self.type == 3: #나눌 필요 없음
            return
        if self.parent == None: #루트 노드인 경우 (부모노드 없는 경우)
            lChild = Node(self.data[0], (self.height)+1, self)
            rChild = Node(self.data[2], (self.height)+1, self)
            lChild.child[0], lChild.child[1] = self.child[0], self.child[1]
            rChild.child[0], rChild.child[1] = self.child[2], self.child[3]
            if lChild.child[0] != None:
                lChild.child[0].parent = lChild
            if lChild.child[1] != None:
                lChild.child[1].parent = lChild
            if rChild.child[0] != None:
                rChild.child[0].parent = rChild
            if rChild.child[1] != None:
                rChild.child[1].parent = rChild
            self.type = 2
            self.data[0], self.data[1], self.data[2] = self.data[1], None, None
            self.child[0], self.child[1], self.child[2], self.child[3] = lChild, rChild, None, None
            if self.child[0] != None:
                self.child[0].parent = self
            if self.child[1] != None:
                self.child[1].parent = self
        
        elif self.parent.type == 2: #부모노드가 값이 하나인 경우
            if self == self.parent.child[0]: #왼쪽 자식인 경우
                mChild = Node(self.data[2], self.height, self.parent) #가운데 자식 생성
                mChild.child[0], mChild.child[1] = self.child[2], self.child[3]
                if mChild.child[0] != None:
                    mChild.child[0].parent = mChild
                if mChild.child[1] != None:
                    mChild.child[1].parent = mChild
                self.parent.push(self.data[1]) #가운데 값은 올려보내기
                self.parent.child[0], self.parent.child[1], self.parent.child[2] = self.parent.child[0], mChild, self.parent.child[1]
                self.type = 2
                self.child[0], self.child[1], self.child[2], self.child[3] = self.child[0], self.child[1], None, None
                if self.child[0] != None:
                    self.child[0].parent = self
                if self.child[1] != None:
                    self.child[1].parent = self
                self.data[0], self.data[1], self.data[2] = self.data[0], None, None
                
            elif self == self.parent.child[1]:
                mChild = Node(self.data[0], self.height, self.parent)
                mChild.child[0], mChild.child[1] = self.child[0], self.child[1]
                if mChild.child[0] != None:
                    mChild.child[0].parent = mChild
                if mChild.child[1] != None:
                    mChild.child[1].parent = mChild
                self.parent.push(self.data[1])
                self.parent.child[0], self.parent.child[1], self.parent.child[2] = self.parent.child[0], mChild, self.parent.child[1]
                self.type = 2
                self.child[0], self.child[1], self.child[2], self.child[3] = self.child[2], self.child[3], None, None
                if self.child[0] != None:
                    self.child[0].parent = self
                if self.child[1] != None:
                    self.child[1].parent = self
                self.data[0], self.data[1], self.data[2] = self.data[2], None, None
        
        elif self.parent.type == 3:
            if self == self.parent.child[0]: #가장 왼쪽 자식
                newNode = Node(self.data[2], self.height, self.parent) #제일 큰 값 주기
                newNode.child[0], newNode.child[1] = self.child[2], self.child[3]
                if newNode.child[0] != None:
                    newNode.child[0].parent = newNode
                if newNode.child[1] != None:
                    newNode.child[1].parent = newNode
                self.parent.push(self.data[1])
                self.parent.child[0], self.parent.child[1], self.parent.child[2], self.parent.child[3] = self.parent.child[0], newNode, self.parent.child[1], self.parent.child[2]
                self.type = 2
                self.child[0], self.child[1], self.child[2], self.child[3] = self.child[0], self.child[1], None, None
                if self.child[0] != None:
                    self.child[0].parent = self
                if self.child[1] != None:
                    self.child[1].parent = self
                self.data[0], self.data[1], self.data[2] = self.data[0], None, None
                
            elif self == self.parent.child[1]: #가운데 자식
                newNode = Node(self.data[2], self.height, self.parent) #제일 큰 값 주기
                newNode.child[0], newNode.child[1] = self.child[2], self.child[3]
                if newNode.child[0] != None:
                    newNode.child[0].parent = newNode
                if newNode.child[1] != None:
                    newNode.child[1].parent = newNode
                self.parent.push(self.data[1])
                self.parent.child[0], self.parent.child[1], self.parent.child[2], self.parent.child[3] = self.parent.child[0], self.parent.child[1], newNode, self.parent.child[2]
                self.type = 2
                self.child[0], self.child[1], self.child[2], self.child[3] = self.child[0], self.child[1], None, None
                if self.child[0] != None:
                    self.child[0].parent = self
                if self.child[1] != None:
                    self.child[1].parent = self
                self.data[0], self.data[1], self.data[2] = self.data[0], None, None
                
            elif self == self.parent.child[2]: #가장 오른쪽 자식
                newNode = Node(self.data[0], self.height, self.parent) #제일 작은 값 주기
                newNode.child[0], newNode.child[1] = self.child[2], self.child[3]
                if newNode.child[0] != None:
                    newNode.child[0].parent = newNode
                if newNode.child[1] != None:
                    newNode.child[1].parent = newNode
                self.parent.push(self.data[1])
                self.parent.child[0], self.parent.child[1], self.parent.child[2], self.parent.child[3] = self.parent.child[0], self.parent.child[1], newNode, self.parent.child[2]
                self.type = 2
                self.child[0], self.child[1], self.child[2], self.child[3] = self.child[2], self.child[3], None, None
                if self.child[0] != None:
                    self.child[0].parent = self
                if self.child[1] != None:
                    self.child[1].parent = self
                self.data[0], self.data[1], self.data[2] = self.data[2], None, None
        
        
    def insert(self, data):
        if data == None:
            return
        if self.child[0] == None: #자식 없음 = 리프노드
            self.push(data)
            self.split()
        
        elif self.type == 2:
            if data < self.data[0]:
                self.child[0].insert(data)
            else:
                self.child[1].insert(data)
        
        elif self.type == 3:
            if data < self.data[0]:
                self.child[0].insert(data)
            elif data > self.data[1]:
                self.child[2].insert(data)
            else:
                self.child[1].insert(data)

    def insertVal(self, data):
        if data == None:
            return
        self.push(data)
        self.split()
                
    def find(self, data, mode): #mode 1이면 출력
        if self.child[0] == None: #자식 없음 = 리프노드
            if data in self.data:
                return self
            else:
                return None
        
        elif self.type == 2:
            if data in self.data:
                return self
            elif data < self.data[0]:
                if mode == 1:
                    print("-Left", end="")
                return self.child[0].find(data, mode)
            else:
                if mode == 1:
                    print("-Right", end="")
                return self.child[1].find(data, mode)
        
        elif self.type == 3:
            if data in self.data:
                return self
            elif data < self.data[0]:
                if mode == 1:
                    print("-Left", end="")
                return self.child[0].find(data, mode)
            elif data > self.data[1]:
                if mode == 1:
                    print("-Middle", end="")
                return self.child[2].find(data, mode)
            else:
                if mode == 1:
                    print("-Right", end="")
                return self.child[1].find(data, mode)

    def check(self):
        if self.type == 4:
            self.split()
            return
        else:
            return
            
    def deleteValue(self, target):
        if self.data[0] == target:
            self.data[0], self.data[1], self.data[2] = self.data[1], self.data[2], None
        elif self.data[1] == target:
            self.data[0], self.data[1], self.data[2] = self.data[0], self.data[2], None
        if self.type == 3:
            if self.data[2] == target:
                self.data[2] = None
    
class TTT: #two-three tree
    def __init__(self): #생성자
        self.root = None
        
    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False
    
    def searchValue(self, target, mode):
        if self.is_empty() == True:
            return None
        else:
            return self.root.find(target, mode)

    def isNode(self, target):
        tmp = Node(None, 0)
        tmp = self.searchValue(target, 0)
        if tmp is None:
            return False
        else:
            return True

    def checkTree(self):
        if self.is_empty() == True:
            return
        sub_tree1 = TTT()
        sub_tree2 = TTT()
        sub_tree3 = TTT()
        sub_tree1.root = self.root.child[0]
        sub_tree2.root = self.root.child[1]
        sub_tree3.root = self.root.child[2]
        self.root.check()
        if (sub_tree1.root == None) and (sub_tree2.root == None) and (sub_tree3.root == None):
            return
        if sub_tree1.root != None:
            sub_tree1.checkTree()
        if sub_tree2.root != None:
            sub_tree2.checkTree()
        if sub_tree3.root != None:
            sub_tree3.checkTree()
        self.root.check()

    def InsertNode(self, data):
        if self.is_empty() == True:
            self.root = Node(data, 0)
        elif self.isNode(data) == True: #해당 값을 가진 노드가 이미 존재
            print("ERROR: Two Three Tree Cannot Have 2 Nodes With Same Value.")
            return
        else:
            self.root.insert(data)
            self.checkTree()

    def printTree(self):
        if(self.root is None):
            print("Tree is Empty.", end="")
            return
        sub_tree1 = TTT()
        sub_tree2 = TTT()
        sub_tree3 = TTT()
        if self.root.type == 2: #값 1개, 자식 2개
            print("%d"%(self.root.data[0]), end="")
            sub_tree1.root = self.root.child[0]
            sub_tree2.root = None
            sub_tree3.root = self.root.child[1]
        else: #값 2개, 자식 3개
            print("(%d,%d)"%(self.root.data[0], self.root.data[1]), end="")
            sub_tree1.root = self.root.child[0]
            sub_tree2.root = self.root.child[1]
            sub_tree3.root = self.root.child[2]
        if (sub_tree1.root == None) and (sub_tree2.root == None) and (sub_tree3.root == None):
            return
        print("(",end="")
        print("(",end="")
        if sub_tree1.root != None and sub_tree1.root.data[0] != None:
            sub_tree1.printTree()
        print(")",end="")
        print("(",end="")
        if sub_tree2.root != None and sub_tree2.root.data[0] != None:
            sub_tree2.printTree()
        print(")",end="")
        print("(",end="")
        if sub_tree3.root != None and sub_tree3.root.data[0] != None:
            sub_tree3.printTree()
        print(")",end="")
        print(")",end="")
        return
    
    def fixNodeAfterDelete(self, node, parent):
        if node.data[0] != None: #값이 기존에 두개 이상이었으면 수정 불필요
            if node.data[1] == None:
                node.type = 2
            return
        if parent != None: #루트 노드 아닌 경우
            sib, lS, rS, mlS, mrS = None, None, None, None, None
            if (node and node.parent) != None: #leftSibling, rightSibling, mostleftSibling, mostrightSibling 구하기
                if node.parent.type == 2:
                    if node == parent.child[0]:
                        rS = parent.child[1]
                    else:
                        lS = parent.child[0]
                elif node.parent.type == 3:
                    if node == parent.child[0]:
                        rS = parent.child[1]
                        mrS = parent.child[2]
                    elif node == parent.child[1]:
                        lS = parent.child[0]
                        rS = parent.child[2]
                    else:
                        mlS = parent.child[0]
                        lS = parent.child[1]
                        
                redistribute = True
                if lS != None or rS != None:
                    if rS != None and (rS.type == 3 or (rS.type == 2 and mrS != None and mrS.type == 3)):
                        sib = rS
                    elif lS != None and (lS.type == 3 or (lS.type == 2 and mlS != None and mlS.type == 3)):
                        sib = lS
                    elif lS != None and lS.type == 2:
                        sib = lS
                        redistribute = False
                    elif rS != None and rS.type == 2:
                        sib = rS
                        redistribute = False
                
                if redistribute == True: #redistritube 하는 경우
                    if sib == lS: #왼쪽 형제
                        index = 0
                        if node == parent.child[0]:
                            index = 0
                        elif node == parent.child[1]:
                            index = 1
                        elif parent.type == 3 and node == parent.child[2]:
                            index = 2
                        node.data[0] = parent.data[index-1]
                        node.child[1], node.child[2] = node.child[0], node.child[1]
                        node.child[0] = sib.child[2]
                        sib.child[2] = None
                        if node.child[0] != None:
                            node.child[0].parent = node
                        parent.data[index-1] = sib.data[1]
                        sib.data[1] = None
                    elif sib == rS: #오른쪽 형제
                        index = 0
                        if node == parent.child[0]:
                            index = 0
                        elif node == parent.child[1]:
                            index = 1
                        elif parent.type == 3 and node == parent.child[2]:
                            index = 2
                        node.data[0] = parent.data[index]
                        node.child[1] = sib.child[0]
                        sib.child[0], sib.child[1] = sib.child[1], sib.child[2]
                        if node.child[1] != None:
                            node.child[1].parent = node
                        parent.data[index] = sib.data[0]
                        sib.data[0] = sib.data[1]
                        sib.data[1] = None
                        
                    next_node = sib

                else: #merge 하는 경우
                    if parent.type == 2:
                        p_val = parent.data[0]
                    else:
                        if sib == parent.child[0]:
                            p_val = parent.data[0]
                        elif sib == parent.child[1]:
                            if sib == rS:
                                p_val = parent.data[0]
                            if sib == lS:
                                p_val = parent.data[parent.type - 2]
                    child = node.child[0]
                    sib.insertVal(p_val)
                    parent.deleteValue(p_val)
                    
                    if node == parent.child[0]:
                        parent.child[0], parent.child[1], parent.child[2], parent.child[3] = parent.child[1], parent.child[2], parent.child[3], None
                    elif node == parent.child[1]:
                        parent.child[1], parent.child[2], parent.child[3] = parent.child[2], parent.child[3], None
                    elif node == parent.child[2]:
                        parent.child[2], parent.child[3] = parent.child[3], None
                    elif node == parent.child[3]:
                        parent.child[3] = None
                    if parent.type == 3:
                        parent.type = 2
                    
                    if node.child[0] != None:
                        if child != None:
                            index = 0
                            if sib.child is None:
                                sib.child = [None, None, None, None]
                            data = child.data[0]
                            for i in range(sib.type - 1):
                                if i is 0:
                                    if data < sib.data[i]:
                                        index = i
                                else:
                                    if sib.data[i - 1] < data < sib.data[i]:
                                        index = i
                                if i == sib.type - 2:
                                    index = (i+1)
                            if index < sib.type and sib.child[index] == None:
                                sib.child[index] = child
                            else:
                                if index == 0:
                                    sib.child[0],sib.child[1],sib.child[2], sib.child[3] = child, sib.child[0], sib.child[1], sib.child[2]
                                elif index == 1:
                                    sib.child[1], sib.child[2], sib.child[3] = child, sib.child[1], sib.child[2]
                                elif index == 2:
                                    sib.child[2], sib.child[3] = child, sib.child[2]
                                else:
                                    sib.child[3] = child
                                if sib.type == 2:
                                    sib.type = 3
                            child.parent = sib
                    next_node = parent

            self.fixNodeAfterDelete(next_node, next_node.parent)
        
        else: #루트노드인 경우
            self.root = self.root.child[0]
            self.root.parent = None
    
    def recurfindSucc(self, node): #재귀적으로 왼쪽으로 쭉 내려가기
        if node.child[0] == None: #leaf node인 경우
            return node
        else:
            return self.recurfindSucc(node.child[0])
    
    def findInorderSucc(self, target, node): #Inorder Successor 찾기
        if node.child[0] == None: #leaf node 인 경우
            return node
        newNode = node
        if node.type == 2:
            if target+1 < node.data[0]:
                newNode = node.child[0]
            elif node.data[0] < target+1:
                newNode = node.child[1]
        elif node.type == 3:
            if target+1 < node.data[0]:
                newNode = node.child[0]
            elif node.data[0] < target+1 and target+1 < node.data[1]:
                newNode = node.child[1]
            elif node.data[1] < target+1:
                newNode = node.child[2]
        return self.recurfindSucc(newNode)

    def countNode(self):
        if self.root is None:
            return 0
        left_tree = TTT()
        right_tree = TTT()
        mid_tree = TTT()
        left_tree.root = self.root.child[0]
        mid_tree.root = self.root.child[1]
        right_tree.root = self.root.child[2]
        lt = left_tree.countNode()
        mt = mid_tree.countNode()
        rt = right_tree.countNode()
        return (lt+mt+rt+1)
    
    def delete(self, target, node):
        if self.countNode() == 1 and node.data[1] == None:
            if node.data[0] == target:
                self.root = None
                return
        succ = self.findInorderSucc(target, node)
        if node.data[0] == target:
            node.data[0], succ.data[0] = succ.data[0], node.data[0]
        elif node.data[1] == target:
            node.data[1], succ.data[0] = succ.data[0], node.data[1]
        if node.type == 3:
            if node.data[2] == target:
                node.data[2], succ.data[0] = succ.data[0], node.data[2]
        succ.deleteValue(target)
        self.fixNodeAfterDelete(succ, succ.parent)
        
    def getChild(self, node, mode):
        if node == None:
            print("ERROR: Node Does Not Exist.")
            return
        if node.type == 2:
            if mode == 'L':
                if node.child[0] == None:
                    print("NULL")
                else:
                    print("%d"%(node.child[0].data[0]), end="")
                    if node.child[0].data[1] != None:
                        print(", %d"%(node.child[0].data[1]))
                    else:
                        print()
            if mode == 'R':
                if node.child[1] == None:
                    print("NULL")
                else:
                    print("%d"%(node.child[1].data[0]), end="")
                    if node.child[1].data[1] != None:
                        print(", %d"%(node.child[1].data[1]))
                    else:
                        print()
            if mode == 'M':
                print("ERROR: This Node Does Not Have Mid Child.")
        if node.type == 3:
            if mode == 'L':
                if node.child[0] == None:
                    print("NULL")
                else:
                    print("%d"%(node.child[0].data[0]), end="")
                    if node.child[0].data[1] != None:
                        print(", %d"%(node.child[0].data[1]))
                    else:
                        print()
            if mode == 'M':
                if node.child[1] == None:
                    print("NULL")
                else:
                    print("%d"%(node.child[1].data[0]), end="")
                    if node.child[1].data[1] != None:
                        print(", %d"%(node.child[1].data[1]))
                    else:
                        print()
            if mode == 'R':
                if node.child[2] == None:
                    print("NULL")
                else:
                    print("%d"%(node.child[2].data[0]), end="")
                    if node.child[2].data[1] != None:
                        print(", %d"%(node.child[2].data[1]))
                    else:
                        print()
        return

    def heightofTree(self):
        if self.root is None:
            print("ERROR: Invalid Input.")
            return -1
        count = 0
        current = self.root
        while (current.child[0] != None):
            current = current.child[0]
            count = count+1
        return count

    def clearTree(self):
        left_node = None
        left_node = self.root
        while(self.root != None):
            if self.countNode() == 1:
                self.root = None
                return
            left_node = my_TTT.root
            while(left_node.child[0] != None):
                left_node = left_node.child[0]
            self.delete(left_node.data[0], left_node)
        return
        
    def inorderTraversal(self):
        left_tree = TTT()
        mid_tree = TTT()
        right_tree = TTT()
        if self.root.child[0] != None:
            left_tree.root = self.root.child[0]
            left_tree.inorderTraversal()
        print("%d "%(self.root.data[0]), end = "")
        if self.root.type == 3:
            if self.root.child[1] != None:
                mid_tree.root = self.root.child[1]
                mid_tree.inorderTraversal()
            if self.root.data[1] != None:
                print("%d "%(self.root.data[1]), end = "")
            if self.root.child[2] != None:
                right_tree.root = self.root.child[2]
                right_tree.inorderTraversal()
        else:
            if self.root.child[1] != None:
                right_tree.root = self.root.child[1]
                right_tree.inorderTraversal()
        return
        
    def rightrootleftTraversal(self):
        left_tree = TTT()
        right_tree = TTT()
        mid_tree = TTT()
        if self.root.type == 2:
            if self.root.child[1] != None:
                right_tree.root = self.root.child[1]
                right_tree.rightrootleftTraversal()
            print("%d "%(self.root.data[0]), end = "")
            if self.root.child[0] != None:
                left_tree.root = self.root.child[0]
                left_tree.rightrootleftTraversal()
        else:
            if self.root.child[2] != None:
                right_tree.root = self.root.child[2]
                right_tree.rightrootleftTraversal()
            print("%d "%(self.root.data[1]), end = "")
            if self.root.child[1] != None:
                mid_tree.root = self.root.child[1]
                mid_tree.rightrootleftTraversal()
            print("%d "%(self.root.data[0]), end = "")
            if self.root.child[0] != None:
                left_tree.root = self.root.child[0]
                left_tree.rightrootleftTraversal()
        return
    
    def get_min(self):
        tmp = 0
        left_tree = TTT()
        if self.root.child[0] != None:
            left_tree.root = self.root.child[0]
            tmp = left_tree.get_min()
        else:
            return (self.root.data[0])
        return tmp
        
    def get_max(self):
        tmp = 0
        right_tree = TTT()
        if self.root.type == 2:
            if self.root.child[1] != None:
                right_tree.root = self.root.child[1]
                tmp = right_tree.get_max()
            else:
                if self.root.data[1] != None:
                    return (self.root.data[1])
                else:
                    return (self.root.data[0])
            return tmp
        if self.root.type == 3:
            if self.root.child[2] != None:
                right_tree.root = self.root.child[2]
                tmp = right_tree.get_max()
            else:
                if self.root.data[1] != None:
                    return (self.root.data[1])
                else:
                    return (self.root.data[0])
            return tmp
        
    def heightofNode(self, node): #나만의 기능 1
        if (self.root is None) or (node is None):
            print("ERROR: Invalid Input.")
            return -1
        tmp = 0
        while (node.parent != None):
            tmp = tmp + 1
            node = node.parent
        return tmp
        
    def replace(self, node, value):
        left_tree = TTT()
        right_tree = TTT()
        if node.type == 3:
            print("ERROR: Can Only Change Node With One Value.")
            return
        if node.data[0] == value:
            print("ERROR: Cannot Replace With Same Value.")
        elif (node.child[0] == None) and (node.child[1] == None):
            node.data[0] = value
        elif node.child[0] == None:
            right_tree.root = self.root.child[1]
            if right_tree.get_min() > value:
                node.data[0] = value
            else:
                print("ERROR: New Value Has To Meet Conditions of TTT.")
        elif node.child[1] == None:
            left_tree.root = self.root.child[0]
            if left_tree.get_max() > value:
                node.data[0] = value
            else:
                print("ERROR: New Value Has To Meet Conditions of TTT.")
        else:
            right_tree.root = self.root.child[1]
            left_tree.root = self.root.child[0]
            if (left_tree.get_max() < value) and (right_tree.get_min() > value):
                node.data[0] = value
            else:
                print("ERROR: New Value Has To Meet Conditions of TTT.")
        return
        
    def preorderTraversal(self):
        left_tree = TTT()
        right_tree = TTT()
        mid_tree = TTT()
        if self.root.type == 2:
            print("%d "%(self.root.data[0]), end = "")
            if self.root.child[1] != None:
                right_tree.root = self.root.child[1]
                right_tree.preorderTraversal()
            if self.root.child[0] != None:
                left_tree.root = self.root.child[0]
                left_tree.preorderTraversal()
        else:
            if self.root.child[1] != None:
                mid_tree.root = self.root.child[1]
                mid_tree.preorderTraversal()
            print("%d "%(self.root.data[1]), end = "")
            print("%d "%(self.root.data[0]), end = "")
            if self.root.child[2] != None:
                right_tree.root = self.root.child[2]
                right_tree.preorderTraversal()
            if self.root.child[0] != None:
                left_tree.root = self.root.child[0]
                left_tree.preorderTraversal()
        return
            

print("명령문 안내")
print("+값: 이진 트리 탐색 트리의 노드 추가")
print("D값: 해당 노드 삭제")
print("P: 트리 출력")
print("I: Left-Root-Right 방식의 순회 출력")
print("R: Right-Root-Left 방식의 순회 출력")
print("E: Root-Left-Right 방식의 순회 출력")
print("N: 최소값 출력")
print("X: 최대값 출력")
print("F값: 루트부터 해당 노드까지 가기 위한 경로 출력")
print("G(값): 해당 노드의 오른쪽 자식 출력")
print("L(값): 해당 노드의 왼쪽 자식 출력")
print("M(노드의 값들): 해당 노드의 가운데 자식 출력")
print("H: 트리의 높이 출력")
print("O(값): 해당 노드의 높이 출력")
print("A(값): 단일 값을 가지는 노드에 한해 루트의 값 변경")
print("#: 노드 수 센 뒤 출력")
print("C: 트리 초기화")
print("&: 프로그램 종료\n") #각 기능별 설명

my_TTT = TTT()

while True:
    default_print = 1
    used = 0 #한 명령에서 한 개 이상의 문자를 사용할 경우 중복 입력 방지용 변수
    
    inp = input("명령어: ") #문자열로 명령어 입력 받기
    
    if inp[0] == '&': #종료 명령
        break
    
    for i in range(len(inp)):
        if used > 0:
            used = used - 1

        elif inp[i] == '+':
            if i+1 == len(inp)-1:
                used = used + 1
                if (ord(inp[i+1])>=ord('0')) and (ord(inp[i+1])<=ord('9')):
                    data = int(inp[i+1])
                    my_TTT.InsertNode(data)
                else:
                    print("ERROR: Invalid Input.")
            elif i+2 == len(inp)-1:
                used = used + 2
                if (ord(inp[i+1])>=ord('0')) and (ord(inp[i+1])<=ord('9')):
                    if (ord(inp[i+2])>=ord('0')) and (ord(inp[i+2])<=ord('9')):
                        data = int(inp[i+1]+inp[i+2])
                        my_TTT.InsertNode(data)
                else:
                    print("ERROR: Invalid Input.")
            else:
                print("ERROR: Invalid Input.")
                    
        elif inp[i] == 'P':
            print("(", end="")
            my_TTT.printTree()
            print(")")
            default_print = 0
        
        elif inp[i] == 'I':
            my_TTT.inorderTraversal()
            print("")
            default_print = 0
        
        elif inp[i] == 'R':
            my_TTT.rightrootleftTraversal()
            print("")
            default_print = 0
        
        elif inp[i] == 'N':
            print("%d"%(my_TTT.get_min()))
            default_print = 0
            
        elif inp[i] == 'X':
            print("%d"%(my_TTT.get_max()))
            default_print = 0
        
        elif inp[i] == 'F':
            if i+1 == len(inp)-1:
                used = used + 1
                if (ord(inp[i+1])>=ord('0')) and (ord(inp[i+1])<=ord('9')):
                    tmp = int(inp[i+1])
                    if my_TTT.isNode(int(tmp)) == 0:
                        print("ERROR: Node With Such Value Doesn't Exist.")
                    else:
                        print("Root", end="")
                        my_TTT.searchValue(int(tmp), 1)
                        print("")
                    if (int(tmp)<0) or (int(tmp)>99):
                        print("ERROR: Invalid Input.")
                else:
                    print("ERROR: Invalid Input.")
            elif i+2 == len(inp)-1:
                used = used + 2
                if (ord(inp[i+1])>=ord('0')) and (ord(inp[i+1])<=ord('9')):
                    if (ord(inp[i+2])>=ord('0')) and (ord(inp[i+2])<=ord('9')):
                        tmp = int(inp[i+1]+inp[i+2])
                        if my_TTT.isNode(int(tmp)) == 0:
                            print("ERROR: Node With Such Value Doesn't Exist.")
                        else:
                            print("Root", end="")
                            my_TTT.searchValue(int(tmp), 1)
                            print("")
                        if (int(tmp)<0) or (int(tmp)>99):
                            print("ERROR: Invalid Input.")
                else:
                    print("ERROR: Invalid Input.")
            else:
                print("ERROR: Invalid Input.")
            default_print = 0

        elif inp[i] == 'D':
            if i+1 == len(inp)-1:
                used = used + 1
                if (ord(inp[i+1])>=ord('0')) and (ord(inp[i+1])<=ord('9')):
                    data = int(inp[i+1])
                    if my_TTT.root == None:
                        print("ERROR: Tree Is Empty.")
                    elif my_TTT.isNode(data) == False:
                        print("ERROR: Node With Such Value Doesn't Exist.")
                    else:
                        my_TTT.delete(data, my_TTT.searchValue(data, 0))
                else:
                    print("ERROR: Invalid Input.")
            elif i+2 == len(inp)-1:
                used = used + 2
                if (ord(inp[i+1])>=ord('0')) and (ord(inp[i+1])<=ord('9')):
                    if (ord(inp[i+2])>=ord('0')) and (ord(inp[i+2])<=ord('9')):
                        data = int(inp[i+1]+inp[i+2])
                        if my_TTT.root == None:
                            print("ERROR: Tree Is Empty.")
                        elif my_TTT.isNode(data) == False:
                            print("ERROR: Node With Such Value Doesn't Exist.")
                        else:
                            my_TTT.delete(data, my_TTT.searchValue(data, 0))
                    else:
                        print("ERROR: Invalid Input.")
                else:
                    print("ERROR: Invalid Input.")
            
        elif inp[i] == 'H':
            print("%d"%(my_TTT.heightofTree()))
            default_print = 0
        
        elif (inp[i] == 'G') or (inp[i] == 'L') or (inp[i] == 'M'):
            tmp = inp[inp.index('(')+1:inp.index(')')].split(',')
            if my_TTT.isNode(int(tmp[0])) == 0:
                print("ERROR: Node With Such Value Doesn't Exist.")
            else:
                if inp[i] == 'G':
                    my_TTT.getChild(my_TTT.searchValue(int(tmp[0]), 0), 'R')
                if inp[i] == 'L':
                    my_TTT.getChild(my_TTT.searchValue(int(tmp[0]), 0), 'L')
                if inp[i] == 'M':
                    my_TTT.getChild(my_TTT.searchValue(int(tmp[0]), 0), 'M')
            if (int(tmp[0])<0) or (int(tmp[0])>99):
                print("ERROR: Invalid Input.")
            used = used + (inp.index(')') - inp.index('(') - 1)
            default_print = 0
        
        elif inp[i] == 'O': #나만의 기능 1
            tmp = inp[inp.index('(')+1:inp.index(')')]
            if my_TTT.isNode(int(tmp)) == 0:
                print("ERROR: Node With Such Value Doesn't Exist.")
            if (int(tmp)<0) or (int(tmp)>99):
                print("ERROR: Invalid Input.")
            else:
                print("Height: %d"%my_TTT.heightofNode(my_TTT.searchValue(int(tmp), 0)))
            used = used + (inp.index(')') - inp.index('(') - 1)
            default_print = 0
            
        elif inp[i] == 'A': #나만의 기능 2
            tmp = inp[inp.index('(')+1:inp.index(')')]
            if my_TTT.root == None:
                print("ERROR: Cannot Find Tree.")
            elif my_TTT.isNode(int(tmp)) == 1:
                print("ERROR: Node With Such Value Already Exist.")
            else:
                if (int(tmp)<0) or (int(tmp)>99):
                    print("ERROR: Invalid Input.")
                else:
                    my_TTT.replace(my_TTT.root, int(tmp))
            used = used + (inp.index(')') - inp.index('(') - 1)

        elif inp[i] == 'E': #나만의 기능 3
            my_TTT.preorderTraversal()
            print("")
            default_print = 0
        
        elif inp[i] == '#':
            print("%d"%(my_TTT.countNode()))
            default_print = 0
         
        elif inp[i] == 'C':
            my_TTT.clearTree()
            
    if default_print == 1:
        print("(", end="")
        my_TTT.printTree()
        print(")")
    else:
        default_print = 1
