#자료구조 한옥영 교수님 9주차 도전과제
#트리 도전 과제
#최종 작성일: 2020.05.13(수)
#2019312481 심규현

class Node:
    def __init__(self, value): #생성자
        self.data = value #data
        self.left = None
        self.right = None
        self.level = 0
        self.degree = 0
    
class Tree:
    def __init__(self): #생성자
        self.root = None

    def createRoot(self, data):
        if(self.root != None):
            print("ERROR: Root Already Exists.")
        else:
            rootNode = Node(data)
            self.root = rootNode
        return

    def searchValue(self, target):
        position = Node(None)
        left_tree = Tree()
        right_tree = Tree()
        position = self.root
        left_tree.root = self.root.left
        right_tree.root = self.root.right

        while(True):
            if position.data == target:
                return position
            elif (position.left is None) and (position.right is None):
                return None
            else:
                if position.right is None:
                    position = left_tree.searchValue(target)
                elif position.left is None:
                    position = right_tree.searchValue(target)
                else:
                    position = left_tree.searchValue(target)
                    if position is None:
                        position = right_tree.searchValue(target)
                return position

    def isNode(self, target):
        tmp = Node(None)
        tmp = self.searchValue(target)
        if tmp is None:
            return 0
        else:
            return 1

    def InsertNode(self, pNode, data):
        if pNode is None:
            print("ERROR: Parent Node Not Found.")
            return
        n = len(data)
        current = Node(None)
        current = pNode
        if(pNode.left is None):
            current = pNode
        else:
            current = pNode.left
            for i in range((pNode.degree)-1):
                current = current.right
        for i in range(n):
            newNode = Node(data[i])
            newNode.level = (pNode.level) + 1
            if pNode.degree == 0:
                current.left = newNode
            else:
                current.right = newNode
            pNode.degree = (pNode.degree) + 1
            current = newNode
        return
        
    def printTree(self):
        if(self.root is None):
            print("Tree is Empty.", end="")
            return
        left_tree = Tree()
        right_tree = Tree()
        left_tree.root = self.root.left
        right_tree.root = self.root.right
        print("%d"%(self.root.data),end="")
        if left_tree.root != None:
            print("(",end="")
            left_tree.printTree()
            print(")",end="")
        if right_tree.root != None:
            print(",", end="")
            right_tree.printTree()
        return

    def findParent(self, target, parent):
        if self.root.data == target:
            return None
        left_tree = Tree()
        right_tree = Tree()
        position = Node(None)
        tmp = Node(None)
        left_tree.root = self.root.left
        right_tree.root = self.root.right
        position = self.root
        if (position.left is None) and (position.right is None):
            return None
        if (position.left != None) and (position.left.data == target):
            return position
        elif (position.right != None) and (position.right.data == target):
            return parent
        else:
            if position.right is None:
                tmp = left_tree.findParent(target, position)
                return tmp
            elif position.left is None:
                tmp = right_tree.findParent(target, parent)
                return tmp
            else:
                tmp = left_tree.findParent(target, position)
                if tmp is None:
                    tmp = right_tree.findParent(target, parent)
                return tmp

    def getValue(self, node):
        global value
        position = node
        while(position != None):
            value = value + position.data
            position = self.findParent(position.data, self.root)
        return
            

print("명령문 안내")
print("+^(값): 트리의 루트 노드 추가")
print("+(부모노드)[(값1),(값2)...]: 부모노드 아래에 노드 추가")
print("N: 입력 그만 받고 Path 계산하기")
print("&: 프로그램 종료\n") #각 기능별 설명

current_tree = Tree()
value = 0


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
            used = used + 1
            if inp[i+1] == '^':
                used = used + 1
                if i+2 == len(inp)-1: #마지막 원소라면
                    used = used + 1
                    if (ord(inp[i+2])>=ord('0')) and (ord(inp[i+2])<=ord('9')):
                        data = int(inp[i+2])
                        current_tree.createRoot(data)
                    else:
                        print("ERROR: Invalid Input.")
                elif i+3 == len(inp)-1:
                    used = used + 2
                    if (ord(inp[i+2])>=ord('0')) and (ord(inp[i+2])<=ord('9')):
                        if (ord(inp[i+3])>=ord('0')) and (ord(inp[i+3])<=ord('9')):
                            data = int(inp[i+2]+inp[i+3])
                            current_tree.createRoot(data)
                    else:
                        print("ERROR: Invalid Input.")
                else:
                    print("ERROR: Invalid Input.")

            else:
                if (ord(inp[i+1])>=ord('0')) and (ord(inp[i+1])<=ord('9')):
                    if (ord(inp[i+2])>=ord('0')) and (ord(inp[i+2])<=ord('9')):
                        data = int(inp[i+1]+inp[i+2])
                        used = used + 2
                        pNode = data
                        array = []
                        children = inp[inp.index('(')+1:inp.index(')')].split(',')
                        for child in children:
                            array.append(int(child))
                        current_tree.InsertNode(current_tree.searchValue(pNode), array)
                        used = len(inp)-1
                        
                    else:
                        data = int(inp[i+1])
                        used = used + 1
                        pNode = data
                        array = []
                        children = inp[inp.index('(')+1:inp.index(')')].split(',')
                        for child in children:
                            array.append(int(child))
                        current_tree.InsertNode(current_tree.searchValue(pNode), array)
                        used = len(inp)-1
                else:
                    print("ERROR: Invalid Input.")
                    
        elif inp[i] == 'N':
            aim = input("Please Give Value of Node to Calculate the Path in Integer: ")
            int_aim = int(aim)
            if(current_tree.isNode(int_aim)==0):
                print("ERROR: Invalid Input.")
            else:
                value = 0
                current_tree.getValue(current_tree.searchValue(int_aim))
                print("Sum of Path: %d"%value)
                break
            
    if default_print == 1:
        print("(", end="")
        current_tree.printTree()
        print(")")
    else:
        default_print = 1

