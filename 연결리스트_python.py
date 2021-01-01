#자료구조 한옥영 교수님 5주차 실습과제
#연결리스트 ADT 실습과제
#최종 작성일: 2020.04.14(화)
#2019312481 심규현

class Node:
    def __init__(self, value): #생성자
        self.data = value #data
        self.link = '\0' #link
    
class LinkedList:
    def __init__(self): #생성자
        head = Node("trash") #헤드포인터 역할을 해줄 노드 생성
        self.head = head #self.head: 연결리스트의 가장 첫 번째 노드
        self.tail = head #self.tail: 연결리스트의 가장 마지막 노드

        self.cursor = head #self.cursor: 현재 위치를 나타내는 노드
        self.size = 0 #연결리스트의 크기(노드의 개수)를 나타내는 변수
        self.position = 0 #현재 위치를 사용자 관점에서 나타내는 변수

    def add(self, data):
        new_node = Node(data) #새로운 노드 생성
        if self.cursor == self.tail: #현재 노드가 마지막 노드인 경우
            self.tail = new_node #새로운 노드를 마지막 노드로 변경
        new_node.link = self.cursor.link
        self.cursor.link = new_node #현재 위치 바로 다음을 새로운 노드로 설정
        self.cursor = new_node #현재 위치 조정
        self.size = self.size + 1 #count해주기
        self.position = self.position + 1 #현재 위치 이동했으므로 position 변수 역시 같이 변경
        
    def print_linkedlist(self): #연결리스트 출력
        current = self.head.link
        for i in range(self.size): #차례대로 연결리스트의 노드 값 출력
            print(current.data, end=' ')
            current = current.link
        print("\n현재 커서의 위치는 %d번째 노드입니다"%self.position) #커서 위치 출력

    def get_data(self):
        print(self.cursor.data) #현재 위치의 노드가 가지고 있는 값 출력

    def traverse_front(self):
        self.cursor = self.head.link #현재 위치 가장 앞으로 이동
        self.position = 1 #print용 변수 position 역시 1로 바꿔줌

    def traverse_rear(self):
        self.cursor = self.tail #현재 위치 가장 뒤로 이동
        self.position = self.size #print용 변수 최대로 바꿔줌

    def go_next(self):
        self.cursor = self.cursor.link #링크타고 다음 노드로 이동
        self.position = self.position + 1 #print용 변수 증가

    def delete(self):
        before = self.head
        for i in range(self.size): #전 노드를 찾기 위해 탐색
            if before.link == self.cursor:
                break
            before = before.link
            
        if self.cursor == self.tail: #마지막 노드일 경우
            before.link = self.cursor.link
            self.cursor.link = '\0'
            self.tail = before #마지막 노드 바꿔주기
            if before == self.head: #삭제한 노드가 유일한 노드였을 경우
                self.cursor = self.head #연결 리스트 맨 앞(헤드)으로 가기
                self.position = 0
            else:
                self.cursor = self.head.link #연결 리스트의 맨 앞 노드로 가기
                self.position = 1

        else: #마지막 노드가 아닌 경우
            before.link = self.cursor.link
            self.cursor = self.cursor.link
            self.position = self.position #삭제된 노드는 당겨지므로 순서 변화 없음
            
        self.size = self.size - 1 #size 변수 관리
            
    def replace(self, new_data):
        self.cursor.data = new_data #노드의 값 바꾸기
        if self.cursor == self.tail: #마지막 노드를 대체하는 경우
            self.tail.data = new_data #마지막 노드를 저장하는 변수 역시 변경

    def traverse_n(self, num):
        move = self.head #헤드로 이동
        for i in range(num): #받은 숫자만큼 다음 노드로 이동
            move = move.link
        self.cursor = move
        self.position = num #관련 변수들 바꿔주기

    def data_count(self):
        print(self.size) #그 동안 세온 size 변수 출력

    def is_member(self, target):
        found = 0 #찾으면 1로 바꿀 변수
        move = self.head
        for i in range(self.size): #쭉 돌면서 찾기
            move = move.link
            if target == move.data: #찾으면
                found = 1
                self.cursor = move #현재 위치 저장
                self.position = i+1
                break

        if found == 0: #못찾으면
            print("해당 값은 연결 리스트안에 없습니다.")
        elif found == 1: #찾으면
            print("%d: "%self.position, end='')

    def clear(self): #비우기
        self.head.link = '\0' #헤드 링크 끊어버리기
        self.tail = self.head
        self.cursor = self.head
        self.size = 0
        self.position = 0 #관련 변수 모두 초기화

    def is_empty(self):
        if self.head.link == '\0': #비어있으면
            print("True")
        else: #안비어있으면
            print("False")

    def traverse_mid(self): #가운데로 이동
        num = int(self.size/2) + 1 #가운데 찾기
        linkedlist.traverse_n(num) #가운데로 이동

    def duplicate(self): #복제
        tmp = self.cursor.data #현재 위치의 값 저장 후
        linkedlist.add(tmp) #현재 위치 뒤에 현재 위치의 값 그대로 추가

    def delete_by_value(self, target): #값으로 삭제
        move = self.head
        for i in range(self.size): #전체 연결리스트를 돌면서 탐색
            move = move.link
            if target == move.data: #target 찾으면
                self.cursor = move
                linkedlist.delete() #삭제
        if self.size == 0: #삭제하다가 모든 값을 다 없앤 경우
            self.cursor = self.head
            self.position = 0 #관련 변수 초기화
        else: #아닌 경우
            self.cursor = self.head.link
            self.position = 1 #가장 앞의 원소로 위치 바꾸기
            
    def add_front(self, data): #가장 앞에 추가
        self.cursor = self.head
        self.position = 0 #가장 앞으로 이동
        linkedlist.add(data) #변수 값 추가

print("명령문 안내")
print("+(노드의 값): 현재 위치의 바로 뒤에 값 추가")
print("*(노드의 값): 연결 리스트의 맨 앞에 값 추가")
print("<: 연결 리스트의 가장 앞 노드로 현재 위치 이동")
print("   이동을 위한 명령문: N: 다음 노드")
print(">: 연결 리스트의 맨 뒤 노드로 현재 위치 이동")
print("(숫자): 해당 숫자 번재의 노드로 현재 위치 이동")
print("|: 가운데로 현재 위치 이동 (만약 짝수일 경우 가운데 두 노드 중 오른쪽)") #자신만의 기능
print("-: 현재 위치의 노드 제거")
print("G: 현재 위치의 노드의 데이터 보여주기")
print("=(값): 현재 위치의 노드를 입력한 값으로 대체")
print("E: 연결리스트가 비어있는지 확인")
print("#: 현재 노드의 개수를 출력")
print("?(값): 입력한 값을 가지는 노드가 몇번째 노드인지 출력")
print("C: 연결리스트 초기화 (비우기)")
print("!(값): 지정한 값을 가지는 노드 전부 삭제") #자신만의 기능
print("D: 현재 위치의 노드 바로 옆에 복제") #자신만의 기능
print("L: 연결리스트 출력 및 커서의 위치 표시")
print("&: 프로그램 종료\n\n") #각 기능별 설명

linkedlist = LinkedList()

while True:
    default_print = 1
    used = 0 #한 명령에서 한 개 이상의 문자를 사용할 경우 중복 입력 방지용 변수
    
    inp = input("명령어: ") #문자열로 명령어 입력 받기
    
    if inp[0] == '&': #종료 명령
        break
    
    for i in range(len(inp)):
        if used == 1:
            used = 0
            
        elif inp[i] == '+': #add
            linkedlist.add(inp[i+1]) #+뒤에 문자가 오므로 바로 뒤의 문자를 연결리스트에 추가
            used = 1 #이미 +의 한칸 뒤까지 다 사용했으므로 그 뒤로 이동

        elif inp[i] == 'G': #get data
            linkedlist.get_data()
            default_print = 0
            
        elif inp[i] == '<': #traverse front
            linkedlist.traverse_front()

        elif inp[i] == '>': #traverse rear
            linkedlist.traverse_rear()

        elif inp[i] == 'N': #go next
            linkedlist.go_next()

        elif inp[i] == '-': #delete
            linkedlist.delete()

        elif inp[i] == '=': #replace
            linkedlist.replace(inp[i+1])
            used = 1

        elif inp[i] == 'C': #clear linked list
            linkedlist.clear()

        elif inp[i] == '#': #data count
            linkedlist.data_count()
            default_print = 0

        elif inp[i] == '?': #is member
            linkedlist.is_member(inp[i+1])
            used = 1

        elif inp[i] == 'E': #is empty
            linkedlist.is_empty()
            default_print = 0

        elif inp[i] == '0' or inp[i] == '1' or inp[i] == '2' or\
             inp[i] == '3' or inp[i] == '4' or inp[i] == '5' or\
             inp[i] == '6' or inp[i] == '7' or inp[i] == '8' or\
             inp[i] == '9': #traverse with number
            if i == len(inp)-1:  #문자열 마지막 노드인 경우
                num = int(inp[i])
                linkedlist.traverse_n(num) 
            elif inp[i+1] == '0' or inp[i+1] == '1' or inp[i+1] == '2' or\
               inp[i+1] == '3' or inp[i+1] == '4' or inp[i+1] == '5' or\
               inp[i+1] == '6' or inp[i+1] == '7' or inp[i+1] == '8' or\
               inp[i+1] == '9': #two-digit number
                num = int(inp[i] + inp[i+1])
                used = 1
                linkedlist.traverse_n(num)
            else: #one-digit number
                num = int(inp[i])
                linkedlist.traverse_n(num)  
         
        elif inp[i] == 'L': #print
            linkedlist.print_linkedlist()
            default_print = 0

        elif inp[i] == '|': #traverse mid
            linkedlist.traverse_mid()

        elif inp[i] == 'D': #duplicate
            linkedlist.duplicate()
            
        elif inp[i] == '!': #delete by value
            linkedlist.delete_by_value(inp[i+1])
            used = 1
            
        elif inp[i] == '*': #add front
            linkedlist.add_front(inp[i+1])
            used = 1

    if default_print == 1:
        linkedlist.print_linkedlist()
    else:
        default_print = 1
