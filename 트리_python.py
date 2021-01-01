#자료구조 한옥영 교수님 9주차 실습과제
#트리 ADT 실습 과제
#최종 작성일: 2020.05.13(수)
#2019312481 심규현

BT = 0

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
        global BT
        if pNode is None:
            print("ERROR: Parent Node Not Found.")
            return
        n = len(data)
        if (BT==1 and n>2):
            print("ERROR: Binary Tree Can't Have More Than 2 Child.")
            return
        elif (BT==1 and (pNode.degree)+n > 2):
            print("ERROR: Binary Tree Can't Have More Than 2 Child.")
            return
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
        print("%c"%(self.root.data),end="")
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

    def getSibling(self, node):
        if node is None:
            print("ERROR: Invalid Input.")
            return
        value = node.data
        count = 0
        if node is self.root:
            print("ERROR: ROOT DOES NOT HAVE A SIBLING")
            return
        parent = Node(None)
        position = Node(None)
        parent = self.findParent(value, self.root)
        position = parent.left
        count = (parent.degree)-1
        if count == 0:
            print("This Node Does Not Have A Sibling.")
            return
        print("{",end="")
        for i in range(parent.degree):
            if (position.data != value) and (count != 0):
                print("%c,"%(position.data), end="")
            elif position.data != value:
                print("%c"%(position.data), end="")
            position = position.right
            count = count - 1
        print("}")
        return

    def getChild(self, node):
        if node == None:
            print("ERROR: Invalid Input.")
            return
        if node.degree == 0:
            print("This Node Does Not Have A Child.")
            return
        position = Node(None)
        position = node.left
        print("{",end="")
        for i in range(node.degree):
            if i != (node.degree)-1:
                print("%c,"%position.data, end="")
            else:
                print("%c"%position.data, end="")
            position = position.right
        print("}")
        return

    def levelofNode(self, node):
        if (self.root is None) or (node is None):
            print("ERROR: Invalid Input.")
            return -1
        tmp = 0
        tmp = (node.level) - (self.root.level)
        return tmp

    def levelofTree(self, max):
        if self.root is None:
            print("ERROR: Invalid Input.")
            return -1;
        tmp1 = 0
        tmp2 = 0
        left_tree = Tree()
        right_tree = Tree()
        left_tree.root = self.root.left
        right_tree.root = self.root.right
        if (self.root.left is None) and (self.root.right is None):
            return self.root.level
        else:
            if left_tree.root != None:
                tmp1 = left_tree.levelofTree(max)
            if right_tree.root != None:
                tmp2 = right_tree.levelofTree(max)
        if tmp1>tmp2:
            return tmp1
        else:
            return tmp2

    def deleteNode(self, node):
        if node is None:
            print("ERROR: Invalid Input.")
            return
        if node.left != None:
            print("ERROR: Can Not Delete Parent Node.")
            return
        elif (node is self.root):
            self.root = None
            return
        parent = Node(None)
        before = Node(None)
        after = Node(None)
        parent = self.findParent(node.data, self.root)
        after = node.right
        if parent.left is node:
            before = parent
            if after is None:
                parent.left = None
                parent.degree = (parent.degree) - 1
            else:
                parent.left = after
                parent.degree = (parent.degree) - 1
        else:
            before = parent.left
            while(before.right != node):
                before = before.right
            parent.degree = (parent.degree) - 1
            before.right = node.right
        return

    def get_ancestors(self, node):
        position = Node(None)
        position = self.findParent(node.data, self.root)
        while(position != None):
            print("%c "%position.data, end="")
            position = self.findParent(position.data, self.root)
        print("")
        return

    def printDescendants(self):
        if(self.root is None):
            print("Tree is Empty.", end="")
            return
        left_tree = Tree()
        right_tree = Tree()
        left_tree.root = self.root.left
        right_tree.root = self.root.right
        print("%c"%(self.root.data),end="")
        if left_tree.root != None:
            print("(",end="")
            left_tree.printDescendants()
            print(")",end="")
        if right_tree.root != None:
            print(" ", end="")
            right_tree.printDescendants()
        return

    def get_descendants(self, node):
        left_tree = Tree()
        left_tree.root = node.left
        if left_tree.root != None:
            left_tree.printDescendants()
        print("\n")
        return

    def degreeofNode(self, node):
        tmp = 0
        tmp = node.degree
        return tmp

    def degreeofTree(self):
        if self.root is None:
            return 0
        left_tree = Tree()
        right_tree = Tree()
        left_tree.root = self.root.left
        right_tree.root = self.root.right
        lt = left_tree.degreeofTree()
        rt = right_tree.degreeofTree()
        own = self.root.degree
        max = 0
        if lt>rt:
            max = lt
        else:
            max = rt
        if max>own:
            max = max
        else:
            max = own
        return max

    def countNode(self):
        if self.root is None:
            return 0
        left_tree = Tree()
        right_tree = Tree()
        left_tree.root = self.root.left
        right_tree.root = self.root.right
        lt = left_tree.countNode()
        rt = right_tree.countNode()
        return (lt+rt+1)

    def insertSibling(self, node, data):
        if (node is None) or (node is self.root):
            print("ERROR: Invalid Input.")
        self.InsertNode(self.findParent(node.data, self.root), data)
        return

    def increaseLevel(self):
        if(self.root is None):
            return
        self.root.level = (self.root.level) + 1
        left_tree = Tree()
        right_tree = Tree()
        left_tree.root = self.root.left
        right_tree.root = self.root.right
        left_tree.increaseLevel()
        right_tree.increaseLevel()
        return

    def clearTree(self):
        left_node = Node(None)
        left_node = self.root
        while(self.root != None):
            left_node = my_tree.root
            while(left_node.left != None):
                left_node = left_node.left
            self.deleteNode(left_node)
        return

def joinTrees(data, tree1, tree2):
    join_tree = Tree()
    join_tree.root = None
    join_tree.createRoot(data)
    join_tree.root.left = tree1.root
    join_tree.root.left.right = tree2.root
    join_tree.root.level = -1
    join_tree.root.degree = 2
    join_tree.increaseLevel()
    return join_tree
            

print("명령문 안내")
print("+^(값): 트리의 루트 노드 추가")
print("+(부모노드)[(값1),(값2)...]: 부모노드 아래에 노드 추가")
print("S(값): 해당 노드의 형제 노드 보여주기")
print("T: 트리 출력")
print("P(자식노드): 부모노드의 값 출력")
print("C(부모노드): 자식노드의 값 출력")
print("L: 트리의 레벨 출력")
print("L(값): 노드의 레벨 출력")
print("G: 트리의 degree 출력")
print("G(값): 노드의 degree 출력")
print("-(값): 해당 노드 삭제")
print("A(값): 해당 노드의 조상 노드 출력")
print("D(값): 해당 노드의 후손 노드 전부 출력")
print("#: 노드 수 센 뒤 출력")
print("=+(부모노드)[(값1),(값2)...]: 큐에 해당 값을 가지는 원소가 존재하는지 확인")
print("J: 트리 합병 모드 활성화/비활성화")
print("K: 트리 초기화")
print("&: 프로그램 종료\n") #각 기능별 설명


my_tree = Tree()
tmp_tree = Tree()
current_tree = my_tree
using_tmp_node = 0
print("이진트리 모드: B")
print("일반트리 모드: N")
binary = input("입력: ")
if binary[0] == 'B':
    BT = 1
elif binary[0] == 'N':
    BT = 0

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
            if inp[i+1] == '^':
                current_tree.createRoot(inp[i+2])
                used = 2 #이미 +의 두칸 뒤까지 다 사용했으므로 그 뒤로 이동

            else:
                pNode = inp[i+1]
                data = [];
                if inp[i+2] == '(':
                    j = i+3
                    while(inp[j] != ')'):
                        if (ord(inp[j])-ord('A') >=0) and (ord('Z')-ord(inp[j]) >=0):
                            data.append(inp[j])
                        j = j+1
                    current_tree.InsertNode(current_tree.searchValue(pNode), data)
                    used = j
                    
        elif inp[i] == 'S':
            if (inp[i+1] == '(') and (inp[i+3] == ')'):
                if (ord(inp[i+2])-ord('A') >= 0) and (ord('Z')-ord(inp[i+2]) >= 0):
                    current_tree.getSibling(current_tree.searchValue(inp[i+2]))
                    used = 3
                default_print = 0

        elif inp[i] == 'T':
            print("(", end="")
            current_tree.printTree()
            print(")")
            default_print = 0

        elif inp[i] == 'P':
            if (inp[i+1] == '(') and (inp[i+3] == ')'):
                if (ord(inp[i+2])-ord('A') >= 0) and (ord('Z')-ord(inp[i+2]) >= 0):
                    if current_tree.isNode(inp[i+2]) == 1:
                        if current_tree.findParent(inp[i+2], current_tree.root):
                            print("%c"%((current_tree.findParent(inp[i+2], current_tree.root)).data))
                            used = 3
                    else:
                        print("ERROR: Can't Find NODE %c"%inp[i+2])
                default_print = 0

        elif inp[i] == 'C':
            if (inp[i+1] == '(') and (inp[i+3] == ')'):
                if (ord(inp[i+2])-ord('A') >= 0) and (ord('Z')-ord(inp[i+2]) >= 0):
                    current_tree.getChild(current_tree.searchValue(inp[i+2]))
                    used = 3
            default_print = 0

        elif inp[i] == 'L':
            if i==len(inp)-1:
                print("%d"%(current_tree.levelofTree(0)))
                used = 1
            elif (inp[i+1] == '(') and (inp[i+3] == ')'):
                if (ord(inp[i+2])-ord('A') >= 0) and (ord('Z')-ord(inp[i+2]) >= 0):
                    print("%d"%(current_tree.levelofNode(current_tree.searchValue(inp[i+2]))))
                    used = 3
            else:
                print("%d"%(current_tree.levelofTree(0)))
                used = 1
            default_print = 0

        elif inp[i] == '-':
            if (ord(inp[i+1])-ord('A') >= 0) and (ord('Z') - ord(inp[i+1]) >= 0):
                current_tree.deleteNode(current_tree.searchValue(inp[i+1]))
                used = 1
        
        elif inp[i] == 'A': 
            if (inp[i+1] == '(') and (inp[i+3] == ')'):
                if (ord(inp[i+2])-ord('A') >= 0) and (ord('Z')-ord(inp[i+2]) >= 0):
                    current_tree.get_ancestors(current_tree.searchValue(inp[i+2]))
                    used = 3
            default_print = 0

        elif inp[i] == 'D':
            if (inp[i+1] == '(') and (inp[i+3] == ')'):
                if (ord(inp[i+2])-ord('A') >= 0) and (ord('Z')-ord(inp[i+2]) >= 0):
                    current_tree.get_descendants(current_tree.searchValue(inp[i+2]))
                    used = 3
            default_print = 0

        elif inp[i] == 'G':
            if i == len(inp)-1:
                print("%d"%(current_tree.degreeofTree()))
                used = 1
            elif (inp[i+1] == '(') and (inp[i+3] == ')'):
                if (ord(inp[i+2])-ord('A') >= 0) and (ord('Z')-ord(inp[i+2]) >= 0):
                    print("%d"%(current_tree.degreeofNode(current_tree.searchValue(inp[i+2]))))
                    used = 3
            else:
                print("%d"%(current_tree.degreeofTree()))
                used = 1
            default_print = 0

        elif inp[i] == '#':
            print("%d"%(current_tree.countNode()))
            default_print = 0

        elif inp[i] == '=':
            if inp[i+1] == '+':
                sNode = inp[i+2]
                data = []
                if inp[i+3] == '(':
                    j = i+4
                    while(inp[j] != ')'):
                        if(ord(inp[j])-ord('A') >= 0) and (ord('Z') - ord(inp[j]) >= 0):
                            data.append(inp[j])
                        j = j+1
                    current_tree.insertSibling(current_tree.searchValue(sNode), data)
                    i=j
                    used = 4

        elif inp[i] == 'J':
            if i == len(inp)-1 or inp[i+1] == '\0':
                if using_tmp_node == 0:
                    print("Creating New Temporary Tree...");
                    print("Created!");
                    print("Now Please Start By Creating A Root.");
                    print("After Managing, Press \"J\" Again to Merge it With Original Tree.");
                    #ADT의 재해석: J를 입력하면 사용자가 기존의 명령어를 이용하여 같은 방식으로 임시 트리를 생성할 수 있게 하고,
                    #트리의 생성 및 수정이 끝났다면 다시 J를 입력하여 기존의 트리와 합병한 트리를 생성할 수 있게 하였다.
                    using_tmp_node = 1;
                    tmp_tree.root = None
                    current_tree = tmp_tree
                elif using_tmp_node == 1:
                    value = input("Value for New Root of Joined Tree: ")
                    result = Tree()
                    result = joinTrees(value[0], my_tree, tmp_tree)
                    my_tree = result
                    current_tree = my_tree
                    using_tmp_node = 0
         
        elif inp[i] == 'K':
            current_tree.clearTree()
            
    if default_print == 1:
        print("(", end="")
        current_tree.printTree()
        print(")")
    else:
        default_print = 1
