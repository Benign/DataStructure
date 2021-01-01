#자료구조 한옥영 교수님 10주차 실습과제
#이진 탐색 트리 ADT 실습 과제
#최종 작성일: 2020.06.19(금)
#2019312481 심규현

class Node:
    def __init__(self, value): #생성자
        self.data = value #data
        self.left = None
        self.right = None
        self.height = 0
    
class BST:
    def __init__(self): #생성자
        self.root = None

    def createRoot(self, data):
        if(self.root != None):
            print("ERROR: Root Already Exists.")
        else:
            rootNode = Node(data)
            self.root = rootNode
        return

    def searchValue(self, target, mode):
        position = Node(None)
        sub_tree = BST()
        position = self.root
        if position.data == target:
            return position
        elif position.data > target:
            if self.root.left == None:
                return None
            sub_tree.root = self.root.left
            if mode == 1:
                print(" > Left", end="")
            position = sub_tree.searchValue(target, mode)
        elif position.data < target:
            if self.root.right == None:
                return None
            sub_tree.root = self.root.right
            if mode == 1:
                print(" > Right", end="")
            position = sub_tree.searchValue(target, mode)
        return position

    def isNode(self, target):
        tmp = Node(None)
        tmp = self.searchValue(target, 0)
        if tmp is None:
            return 0
        else:
            return 1

    def InsertNode(self, data):
        done = 0
        count = 0
        if self.root == None:
            print("ERROR: Tree Not Found.")
            return
        if my_BST.isNode(data) == 1: #해당 값을 가진 노드가 이미 존재
            print("ERROR: Binary Search Tree Cannot Have 2 Nodes With Same Value.")
            return
        current = Node(None)
        current = self.root
        while(done == 0):
            if current.data > data:
                if current.left == None:
                    done = 1 #우 부트리
                else:
                    current = current.left
            elif current.data < data:
                if current.right == None:
                    done = 2 #좌 부트리
                else:
                    current = current.right
            count = count + 1
        newNode = Node(data)
        newNode.height = count
        if done == 1:
            current.left = newNode
        elif done == 2:
            current.right = newNode
        return
        
    def printTree(self):
        if(self.root is None):
            print("Tree is Empty.", end="")
            return
        left_tree = BST()
        right_tree = BST()
        left_tree.root = self.root.left
        right_tree.root = self.root.right
        print("%d"%(self.root.data),end="")
        if (left_tree.root == None) and (right_tree.root == None):
            return
        print("(",end="")
        if left_tree.root != None:
            left_tree.printTree()
        print(",", end="")
        if right_tree.root != None:
            right_tree.printTree()
        print(")",end="")
        return

    def findParent(self, target):
        if self.root.data == target:
            return None
        left_tree = BST()
        right_tree = BST()
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
            return position
        else:
            if position.right is None:
                tmp = left_tree.findParent(target)
                return tmp
            elif position.left is None:
                tmp = right_tree.findParent(target)
                return tmp
            else:
                tmp = left_tree.findParent(target)
                if tmp is None:
                    tmp = right_tree.findParent(target)
                return tmp

    def deleteNode(self, node, mode):
        root = 0
        if node is None:
            print("ERROR: Invalid Input.")
            return
        if node.data == self.root.data:
            root = 1
        parent = Node(None)
        if root == 0:
            parent = self.findParent(node.data)
        if (node.left == None) and (node.right == None): #leaf node
            if root == 0:
                if parent.left == node:
                    parent.left = None
                    return
                elif parent.right == node:
                    parent.right = None
                    return
            elif root == 1: #유일한 노드
                my_BST.root = None
                return
        elif node.left == None:
            if root == 0:
                if parent.left == node:
                    parent.left = node.right
                    return
                elif parent.right == node:
                    parent.right = node.right
                    return
            elif root == 1:
                self.root = node.right
                return
        elif node.right == None:
            if root == 0:
                if parent.left == node:
                    parent.left = node.left
                    return
                elif parent.right == node:
                    parent.right = node.left
                    return
            elif root == 1:
                self.root = node.left
                return
        else:
            temp = 0
            heir = Node(None) #후계자
            if mode == 'L':
                heir = node.left
                while (heir.right != None):
                    heir  = heir.right
                temp = node.data
                node.data = heir.data
                heir.data = temp
                self.deleteNode(heir, 'L')
            elif mode == 'R':
                heir = node.right
                while (heir.left != None):
                    heir = heir.left
                temp = node.data
                node.data = heir.data
                heir.data = temp
                self.deleteNode(heir, 'R')
            else:
                print("ERROR: Cannot Choose Heir")
                return

    def getChild(self, node, mode):
        if node == None:
            print("ERROR: Node Does Not Exist.")
            return
        if mode == 'L':
            if node.left == None:
                print("NULL")
            else:
                print("%d"%(node.left.data))
        if mode == 'R':
            if node.right == None:
                print("NULL")
            else:
                print("%d"%(node.right.data))
        return

    

    def heightofTree(self, max):
        if self.root is None:
            print("ERROR: Invalid Input.")
            return -1
        tmp1 = 0
        tmp2 = 0
        left_tree = BST()
        right_tree = BST()
        left_tree.root = self.root.left
        right_tree.root = self.root.right
        if (self.root.left is None) and (self.root.right is None):
            return self.root.height
        else:
            if left_tree.root != None:
                tmp1 = left_tree.heightofTree(max)
            if right_tree.root != None:
                tmp2 = right_tree.heightofTree(max)
        if tmp1>tmp2:
            return tmp1
        else:
            return tmp2

    def countNode(self):
        if self.root is None:
            return 0
        left_tree = BST()
        right_tree = BST()
        left_tree.root = self.root.left
        right_tree.root = self.root.right
        lt = left_tree.countNode()
        rt = right_tree.countNode()
        return (lt+rt+1)

    def clearTree(self):
        left_node = Node(None)
        left_node = self.root
        while(self.root != None):
            left_node = my_BST.root
            while(left_node.left != None):
                left_node = left_node.left
            self.deleteNode(left_node, 'L')
        return
        
    def inorderTraversal(self):
        left_tree = BST()
        right_tree = BST()
        if self.root.left != None:
            left_tree.root = self.root.left
            left_tree.inorderTraversal()
        print("%d "%(self.root.data), end = "")
        if self.root.right != None:
            right_tree.root = self.root.right
            right_tree.inorderTraversal()
        return
        
    def rightrootleftTraversal(self):
        left_tree = BST()
        right_tree = BST()
        if self.root.right != None:
            right_tree.root = self.root.right
            right_tree.rightrootleftTraversal()
        print("%d "%(self.root.data), end = "")
        if self.root.left != None:
            left_tree.root = self.root.left
            left_tree.rightrootleftTraversal()
        return
    
    def get_min(self):
        tmp = 0
        left_tree = BST()
        if self.root.left != None:
            left_tree.root = self.root.left
            tmp = left_tree.get_min()
        else:
            return (self.root.data)
        return tmp
        
    def get_max(self):
        tmp = 0
        right_tree = BST()
        if self.root.right != None:
            right_tree.root = self.root.right
            tmp = right_tree.get_min()
        else:
            return (self.root.data)
        return tmp
        
    def heightofNode(self, node): #나만의 기능 1
        if (self.root is None) or (node is None):
            print("ERROR: Invalid Input.")
            return -1
        tmp = 0
        tmp = (node.height) - (self.root.height)
        return tmp
        
    def replace(self, node, value):
        left_tree = BST()
        right_tree = BST()
        if node.data == value:
            print("ERROR: Cannot Replace With Same Value.")
        elif (node.left == None) and (node.right == None):
            node.data = value
        elif node.left == None:
            right_tree.root = self.root.right
            if right_tree.get_min() > value:
                node.data = value
            else:
                print("ERROR: New Value Has To Meet Conditions of BST.")
        elif node.right == None:
            left_tree.root = self.root.left
            if left_tree.get_max() > value:
                node.data = value
            else:
                print("ERROR: New Value Has To Meet Conditions of BST.")
        else:
            right_tree.root = self.root.right
            left_tree.root = self.root.left
            if (left_tree.get_max() < value) and (right_tree.get_min() > value):
                node.data = value
            else:
                print("ERROR: New Value Has To Meet Conditions of BST.")
        return
        
    def preorderTraversal(self):
        left_tree = BST()
        right_tree = BST()
        print("%d "%(self.root.data), end = "")
        if self.root.left != None:
            left_tree.root = self.root.left
            left_tree.preorderTraversal()
        if self.root.right != None:
            right_tree.root = self.root.right
            right_tree.preorderTraversal()
        return
            

print("명령문 안내")
print("+값: 이진 트리 탐색 트리의 노드 추가")
print("-값: 해당 노드 삭제")
print("P: 트리 출력")
print("I: Left-Root-Right 방식의 순회 출력")
print("R: Right-Root-Left 방식의 순회 출력")
print("E: Root-Left-Right 방식의 순회 출력")
print("N: 최소값 출력")
print("X: 최대값 출력")
print("F값: 루트부터 해당 노드까지 가기 위한 경로 출력")
print("G(값): 해당 노드의 오른쪽 자식 출력")
print("L(값): 해당 노드의 왼쪽 자식 출력")
print("H: 트리의 높이 출력")
print("O(값): 해당 노드의 높이 출력")
print("A(값): 루트의 값 변경")
print("#: 노드 수 센 뒤 출력")
print("C: 트리 초기화")
print("&: 프로그램 종료\n") #각 기능별 설명

my_BST = BST()
heir = 'L'
print("좌-부트리에서 후계자 선택: L")
print("우-부트리에서 후계자 선택: R")
print("기본설정: 좌-부트리")
heir_mode = input("입력: ")
if heir_mode[0] == 'L':
    heir = 'L'
elif heir_mode[0] == 'R':
    heir = 'R'

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
                    if my_BST.root == None:
                        my_BST.createRoot(data)
                    else:
                        my_BST.InsertNode(data)
                else:
                    print("ERROR: Invalid Input.")
            elif i+2 == len(inp)-1:
                used = used + 2
                if (ord(inp[i+1])>=ord('0')) and (ord(inp[i+1])<=ord('9')):
                    if (ord(inp[i+2])>=ord('0')) and (ord(inp[i+2])<=ord('9')):
                        data = int(inp[i+1]+inp[i+2])
                        if my_BST.root == None:
                            my_BST.createRoot(data)
                        else:
                            my_BST.InsertNode(data)
                else:
                    print("ERROR: Invalid Input.")
            else:
                print("ERROR: Invalid Input.")
                    
        elif inp[i] == 'P':
            print("(", end="")
            my_BST.printTree()
            print(")")
            default_print = 0
        
        elif inp[i] == 'I':
            my_BST.inorderTraversal()
            print("")
            default_print = 0
        
        elif inp[i] == 'R':
            my_BST.rightrootleftTraversal()
            print("")
            default_print = 0
        
        elif inp[i] == 'N':
            print("%d"%(my_BST.get_min()))
            default_print = 0
            
        elif inp[i] == 'X':
            print("%d"%(my_BST.get_max()))
            default_print = 0
        
        elif inp[i] == 'F':
            if i+1 == len(inp)-1:
                used = used + 1
                if (ord(inp[i+1])>=ord('0')) and (ord(inp[i+1])<=ord('9')):
                    tmp = int(inp[i+1])
                    if my_BST.isNode(int(tmp)) == 0:
                        print("ERROR: Node With Such Value Doesn't Exist.")
                    else:
                        print("ROOT", end="")
                        my_BST.searchValue(int(tmp), 1)
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
                        if my_BST.isNode(int(tmp)) == 0:
                            print("ERROR: Node With Such Value Doesn't Exist.")
                        else:
                            print("ROOT", end="")
                            my_BST.searchValue(int(tmp), 1)
                            print("")
                        if (int(tmp)<0) or (int(tmp)>99):
                            print("ERROR: Invalid Input.")
                else:
                    print("ERROR: Invalid Input.")
            else:
                print("ERROR: Invalid Input.")
            default_print = 0

        elif inp[i] == '-':
            if i+1 == len(inp)-1:
                used = used + 1
                if (ord(inp[i+1])>=ord('0')) and (ord(inp[i+1])<=ord('9')):
                    data = int(inp[i+1])
                    if my_BST.root == None:
                        print("ERROR: Tree Is Empty.")
                    elif my_BST.isNode(data) == 0:
                        print("ERROR: Node With Such Value Doesn't Exist.")
                    else:
                        my_BST.deleteNode(my_BST.searchValue(data, 0), heir)
                else:
                    print("ERROR: Invalid Input.")
            elif i+2 == len(inp)-1:
                used = used + 2
                if (ord(inp[i+1])>=ord('0')) and (ord(inp[i+1])<=ord('9')):
                    if (ord(inp[i+2])>=ord('0')) and (ord(inp[i+2])<=ord('9')):
                        data = int(inp[i+1]+inp[i+2])
                        if my_BST.root == None:
                            print("ERROR: Tree Is Empty.")
                        elif my_BST.isNode(data) == 0:
                            print("ERROR: Node With Such Value Doesn't Exist.")
                        else:
                            my_BST.deleteNode(my_BST.searchValue(data, 0), heir)
                    else:
                        print("ERROR: Invalid Input.")
                else:
                    print("ERROR: Invalid Input.")
            
        elif inp[i] == 'H':
            print("%d"%(my_BST.heightofTree(0)))
            default_print = 0
        
        elif (inp[i] == 'G') or (inp[i] == 'L'):
            tmp = inp[inp.index('(')+1:inp.index(')')]
            if my_BST.isNode(int(tmp)) == 0:
                print("ERROR: Node With Such Value Doesn't Exist.")
            else:
                if inp[i] == 'G':
                    my_BST.getChild(my_BST.searchValue(int(tmp), 0), 'R')
                if inp[i] == 'L':
                    my_BST.getChild(my_BST.searchValue(int(tmp), 0), 'L')
            if (int(tmp)<0) or (int(tmp)>99):
                print("ERROR: Invalid Input.")
            used = used + (inp.index(')') - inp.index('(') - 1)
            default_print = 0
        
        elif inp[i] == 'O': #나만의 기능 1
            tmp = inp[inp.index('(')+1:inp.index(')')]
            if my_BST.isNode(int(tmp)) == 0:
                print("ERROR: Node With Such Value Doesn't Exist.")
            if (int(tmp)<0) or (int(tmp)>99):
                print("ERROR: Invalid Input.")
            else:
                print("Height: %d"%my_BST.heightofNode(my_BST.searchValue(int(tmp), 0)))
            used = used + (inp.index(')') - inp.index('(') - 1)
            default_print = 0
            
        elif inp[i] == 'A': #나만의 기능 2
            tmp = inp[inp.index('(')+1:inp.index(')')]
            if my_BST.root == None:
                print("ERROR: Cannot Find Tree.")
            elif my_BST.isNode(int(tmp)) == 1:
                print("ERROR: Node With Such Value Already Exist.")
            else:
                if (int(tmp)<0) or (int(tmp)>99):
                    print("ERROR: Invalid Input.")
                else:
                    my_BST.replace(my_BST.root, int(tmp))
            used = used + (inp.index(')') - inp.index('(') - 1)

        elif inp[i] == 'E': #나만의 기능 3
            my_BST.preorderTraversal()
            print("")
            default_print = 0
        
        elif inp[i] == '#':
            print("%d"%(my_BST.countNode()))
            default_print = 0
         
        elif inp[i] == 'C':
            my_BST.clearTree()
            
    if default_print == 1:
        print("(", end="")
        my_BST.printTree()
        print(")")
    else:
        default_print = 1
