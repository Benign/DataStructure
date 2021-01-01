#자료구조 한옥영 교수님 7주차 도전과제
#이중 연결리스트를 활용한 덱 ADT
#최종 작성일: 2020.05.05(화)
#2019312481 심규현

class Node:
    def __init__(self, value): #생성자
        self.data = value #data
        self.llink = '\0' #llink
        self.rlink = '\0' #rlink
    
class Deque:
    def __init__(self): #생성자
        head = Node("trash") #헤드포인터 역할을 해줄 노드 생성
        self.head = head #self.head: 덱의 head 포인터. 첫번째 노드를 가리킴.
        self.tail = head #self.tail: 덱의 가장 마지막 노드
        self.size = 0 #덱의 크기(노드의 개수)를 나타내는 변수

    def is_empty(self):
        if self.head.rlink == '\0':
            return True
        else:
            return False

    def enqueue_front(self, data):
        new_node = Node(data)  # 새로운 노드 생성
        new_node.rlink = self.head.rlink  # 기존의 첫번재 노드를 우링크로 연결
        if(self.is_empty() == False):
            self.head.rlink.llink = new_node #기존의 첫번째 노드의 좌링크를 newnode로 연결
        new_node.llink = self.head
        if(new_node.rlink == '\0'):
            self.tail = new_node
        self.head.rlink = new_node  # 첫번째 노드를 새로운 노드로 변경
        self.size = self.size + 1  # count해주기

    def enqueue_rear(self, data):
        new_node = Node(data) #새로운 노드 생성
        new_node.llink = self.tail #기존의 마지막 노드를 좌링크로 연결
        new_node.rlink = self.tail.rlink
        self.tail.rlink = new_node #현재 위치 바로 다음을 새로운 노드로 설정
        self.tail = new_node #새로운 노드를 마지막 노드로 변경
        self.size = self.size + 1 #count해주기

    def dequeue_front(self):
        if self.is_empty() == True:
            print("ERROR: deque is empty")
            return 0
        else:
            tmp = self.head.rlink.data #첫번째 원소의 값 저장
            self.head.rlink = self.head.rlink.rlink #두 번째 원소를 첫번째 원소로 변경
            self.head.rlink.llink = self.head #새로운 첫번째 원소의 좌링크를 헤드포인터로 변경
            self.size = self.size - 1 #size 변수 관리
            return tmp

    def dequeue_rear(self):
        if self.is_empty() == True:
            print("ERROR: deque is empty")
            return 0
        else:
            tmp = self.tail.data #마지막 원소의 값 저장
            self.tail = self.tail.llink #마지막에서 두번째 원소를 마지막 원소로 저장
            print(self.tail.data)
            self.tail.rlink = '\0' #새로운 마지막 원소의 우링크 NULL로 다시 바꾸기
            self.size = self.size - 1 #size 변수 관리
            return tmp
        
    def print_deque(self): #덱 출력
        current = self.head.rlink
        if self.is_empty() == True:
            print("empty deque")
        else:
            print("[ ",end="") #출력 형식 맞추기용
            for i in range(self.size): #차례대로 덱의 노드 값 출력
                print(current.data, end=' ')
                current = current.rlink
            print("]") #출력형식 맞추기 용

    def get_head(self): #첫번째 노드가 가지고 있는 값 출력
        if self.is_empty() == True:
            print("ERROR: deque is empty")
        else:
            print(self.head.rlink.data)

    def get_tail(self): #마지막 노드가 가지고 있는 값 출력
        if self.is_empty() == True:
            print("ERROR: deque is empty")
        print(self.tail.data)

    def data_count(self):
        print(self.size) #그 동안 세온 size 변수 출력

    def is_member(self, target):
        found = 0 #찾으면 1로 바꿀 변수
        position = 0
        move = self.head
        for i in range(self.size): #쭉 돌면서 찾기
            move = move.rlink
            if target == move.data: #찾으면
                found = 1
                position = i+1
                break

        if found == 0: #못찾으면
            print("Does not exist.")
            return -1
        elif found == 1: #찾으면
            print("Position: %d"%position)
            return position

    def replace_front(self, new_data):
        if self.is_empty() == True:
            print("ERROR: deque is empty")
        else:
            self.head.rlink.data = new_data
            
    def replace_rear(self, new_data):
        if self.is_empty() == True:
            print("ERROR: deque is empty")
        else:
            self.tail.data = new_data

    def clear(self): #비우기
        tmp = self.size
        for i in range(tmp-1): #앞에서부터 싹 제거
            self.dequeue_front()
        self.head.rlink = '\0' #헤드 링크 끊어버리기
        self.tail = self.head
        self.size = 0 #관련 변수 모두 초기화

    def delete_by_value(self, target): #값으로 삭제
        tmp = self.size
        count = 0 #제거한 횟수
        for i in range(tmp):
            if self.head.rlink.data == target: #만약 현재 제일 앞의 원소가 찾는 원소와 같다면
                self.dequeue_front() #제일 앞의 원소 제거
                count = count + 1 #count 증가
            else: #다르다면
                self.enqueue_rear(self.dequeue_front()) #큐의 제일 앞의 값을 dequeue해서 뒤에 enqueue
        print("%d data has been deleted."%count)
            
    def move_back(self): #가장 앞의 원소 가장 뒤로 이동
        self.enqueue_rear(self.dequeue_front())

    def move_front(self): #가장 뒤의 원소 가장 앞으로 이동
        self.enqueue_front(self.dequeue_rear())
    
            

print("명령문 안내")
print("E: 덱이 비어있는지 확인")
print("#: 현재 노드의 개수를 출력")
print("?(값): 입력한 값을 가지는 노드가 몇번째 노드인지 출력")
print("!(값): 지정한 값을 가지는 노드 전부 삭제")
print("MB: 가장 앞의 원소 가장 뒤로 이동")
print("MF: 가장 뒤의 원소 가장 앞으로 이동")
print("C: 덱 초기화 (비우기)")
print("L: 덱 출력")
print("&: 프로그램 종료")
print("H(아래 명령문): 앞에서 명령 수행")
print("T(아래 명령문): 뒤에서 명령 수행")
print("   +(노드의 값): 새로운 노드 추가")
print("   -: 노드 제거")
print("   G: 노드의 데이터 보여주기")
print("   =(값): 노드의 데이터를 입력한 값으로 대체")
print("   (숫자)-: 해당 숫자만큼의 노드 제거")


deque = Deque()


while True:
    default_print = 1
    used = 0 #한 명령에서 한 개 이상의 문자를 사용할 경우 중복 입력 방지용 변수
    
    inp = input("명령어: ") #문자열로 명령어 입력 받기
    
    if inp[0] == '&': #종료 명령
        break
    
    for i in range(len(inp)):
        if used > 0:
            used = used - 1

        elif inp[i] == 'H': #앞에서 명령 수행
            if inp[i+1] == '+': #enqueue
                deque.enqueue_front(inp[i+2]) #+뒤에 문자가 오므로 바로 뒤의 문자를 덱에 추가
                used = 2 #이미 +의 두칸 뒤까지 다 사용했으므로 그 뒤로 이동

            elif inp[i+1] == '-': #dequeue
                temp = deque.dequeue_front()
                if temp != 0:
                    print("Return: %c"%temp)
                used = 1

            elif inp[i+1] == 'G': #get data
                deque.get_head()
                default_print = 0
                used = 1

            elif inp[i+1] == '=': #replace
                deque.replace_front(inp[i+2])
                used = 2
                
            elif inp[i+1] == '0' or inp[i+1] == '1' or inp[i+1] == '2' or\
             inp[i+1] == '3' or inp[i+1] == '4' or inp[i+1] == '5' or\
             inp[i+1] == '6' or inp[i+1] == '7' or inp[i+1] == '8' or\
             inp[i+1] == '9': #dequeue by number
                if i+1 == len(inp)-1:  #문자열 마지막 노드인 경우
                    print("Invalid Request.")
                elif inp[i+2] == '0' or inp[i+2] == '1' or inp[i+2] == '2' or\
                     inp[i+2] == '3' or inp[i+2] == '4' or inp[i+2] == '5' or\
                     inp[i+2] == '6' or inp[i+2] == '7' or inp[i+2] == '8' or\
                     inp[i+2] == '9': #two-digit number
                    num = int(inp[i+1] + inp[i+2])
                    if inp[i+3] == '-':
                        used = 4
                        print("Return: ", end='')
                        for i in range(num):
                            temp = deque.dequeue_front()
                            if temp != 0:
                                print("%c "%temp, end='')
                        print("\n")
                    else:
                        print("Invalid Request")
                        
                else: #one-digit number
                    num = int(inp[i+1])
                    if inp[i+2] == '-':
                        used = 3
                        print("Return: ", end='')
                        for i in range(num):
                            temp = deque.dequeue_front()
                            if temp != 0:
                                print("%c "%temp, end='')
                        print("\n")
                    else:
                        print("Invalid Request")
            
        elif inp[i] == 'T': #뒤에서 명령 수행
            if inp[i+1] == '+': #enqueue
                deque.enqueue_rear(inp[i+2]) #+뒤에 문자가 오므로 바로 뒤의 문자를 덱에 추가
                used = 2 #이미 +의 두칸 뒤까지 다 사용했으므로 그 뒤로 이동

            elif inp[i+1] == '-': #dequeue
                temp = deque.dequeue_rear()
                if temp != 0:
                    print("Return: %c"%temp)
                used = 1

            elif inp[i+1] == 'G': #get data
                deque.get_tail()
                default_print = 0
                used = 1

            elif inp[i+1] == '=': #replace
                deque.replace_rear(inp[i+2])
                used = 2
                
            elif inp[i+1] == '0' or inp[i+1] == '1' or inp[i+1] == '2' or\
             inp[i+1] == '3' or inp[i+1] == '4' or inp[i+1] == '5' or\
             inp[i+1] == '6' or inp[i+1] == '7' or inp[i+1] == '8' or\
             inp[i+1] == '9': #dequeue by number
                if i+1 == len(inp)-1:  #문자열 마지막 노드인 경우
                    print("Invalid Request.")
                elif inp[i+2] == '0' or inp[i+2] == '1' or inp[i+2] == '2' or\
                     inp[i+2] == '3' or inp[i+2] == '4' or inp[i+2] == '5' or\
                     inp[i+2] == '6' or inp[i+2] == '7' or inp[i+2] == '8' or\
                     inp[i+2] == '9': #two-digit number
                    num = int(inp[i+1] + inp[i+2])
                    if inp[i+3] == '-':
                        used = 4
                        print("Return: ", end='')
                        for i in range(num):
                            temp = deque.dequeue_rear()
                            if temp != 0:
                                print("%c "%temp, end='')
                        print("\n")
                    else:
                        print("Invalid Request")
                        
                else: #one-digit number
                    num = int(inp[i+1])
                    if inp[i+2] == '-':
                        used = 3
                        print("Return: ", end='')
                        for i in range(num):
                            temp = deque.dequeue_rear()
                            if temp != 0:
                                print("%c "%temp, end='')
                        print("\n")
                    else:
                        print("Invalid Request")
        

        elif inp[i] == 'C': #clear deque
            deque.clear()

        elif inp[i] == '#': #data count
            deque.data_count()
            default_print = 0

        elif inp[i] == '?': #is member
            deque.is_member(inp[i+1])
            used = 1

        elif inp[i] == '!': #delete by value
            deque.delete_by_value(inp[i+1])
            used = 1

        elif inp[i] == 'E': #is empty
            if deque.is_empty() == True:
                print("True")
            else:
                print("False")
            default_print = 0 
         
        elif inp[i] == 'L': #print
            deque.print_deque()
            default_print = 0

        elif inp[i] == 'M': #move
            if inp[i+1] == 'F':
                deque.move_front()
                used = 1
            elif inp[i+1] == 'B':
                deque.move_back()
                used = 1
            else:
                print("Invalid Request")
            

    if default_print == 1:
        deque.print_deque()
    else:
        default_print = 1
