#자료구조 한옥영 교수님 7주차 추가과제
#큐 ADT 실습과제
#최종 작성일: 2020.05.05(화)
#2019312481 심규현

class Queue:
    def __init__(self):
        self.queue = []
        self.head = -1
        self.tail = -1
        self.size = 0 #큐의 최대 크기를 나타내는 변수.

    def create(self, n): #추가기능 1
        self.size = n #사이즈 지정

    def is_full(self): #다 찼는지 확인
        if self.tail+1 >= self.size: #현재 위치가 최대에 도달했다면
            return True #true
        else: #아니라면
            return False #false

    def is_empty(self): #비어있는지 확인
        if (self.tail-self.head) == 0: #큐에 자료가 없다면
            return True #true 반환
        else: #아니라면
            return False #false 반환

    def enqueue(self, data): #원소 끝에 삽입
        if self.is_full() == False: #배열이 아직 다 차지 않은 경우
            self.queue.append(data) #원소 추가
            self.tail = self.tail + 1 #tail 값 조정
        else: #다 찬 경우 삽입 불가능
            print("잘못된 입력입니다")

    def dequeue(self): #제일 앞의 원소 삭제
        if self.is_empty() == True: #원소가 큐에 없는 경우
            print("Error: nothing to dequeue") #dequeue 불가능
        else:
            print("return: " + self.queue.pop(0)) #제알 앞에 있는 원소 삭제와 동시에 값을 반환받아 출력
            self.tail = self.tail - 1 #tail 값 조정

    def peek(self): #제일 앞의 원소가 가지고 있는 값 보여주기
        print(self.queue[self.head+1]) #제일 앞의 원소 출력

    def data_count(self): #현재 원소의 개수 출력
        print(self.tail-self.head)

    def print_head(self): #head관련 정보 출력
        print(self.head+2) #head+2 출력. 현재 head가 배열 상 몇번째 칸에 있는지를 표시 -> 파이썬은 동적할당이라 항상 1

    def print_tail(self): #tail관련 정보 출력
        print(self.tail+1) #tail+1 출력. 현재 tail이 배열 상 몇번째 칸에 있는지를 표시

    def is_member(self, target): #target값을 가지는 원소 있는지 탐색
        find = -1 #찾으면 1, 못찾으면 -1
        for i in range(self.tail+1):
            if (self.queue[0] == target) and (find == -1): #원하던 값을 처음 찾은경우
                find = i+1
            self.queue.append(self.queue.pop(0)) #큐의 제일 앞의 값을 dequeue해서 뒤에 enqueue
        return find
                

    def replace(self, data): #tail 원소 대체
        if (self.tail-self.head) == 0:
            print("ERROR: no element to replace.")
        else:
            self.queue[self.tail] = data #tail 원소 대체

    def clear_queue(self): #큐 비우기
        for i in range(self.tail+1):
            self.queue.pop(0) #쭉 돌면서 하나씩 앞에서부터 삭제하기
        self.tail = -1 #tail 초기화
        
    def print_queue(self): #큐 출력
        if self.is_empty() == True: #비어있는 큐인 경우
            print("empty queue")
        else: #아닌 경우
            print("[ ",end="") #출력 형식 맞추기용
            print("%c "%(self.queue[0]), end="") #queue의 가장 앞 원소 출력
            for i in range(self.tail):
                self.queue.append(self.queue.pop(0)) #큐의 제일 앞의 값을 dequeue해서 뒤에 enqueue
                print("%c "%(self.queue[0]), end="") #queue의 가장 앞 원소 출력
            self.queue.append(self.queue.pop(0))
            print("]") #출력형식 맞추기 용

    def duplicate(self): #현재 위치의 원소 바로 뒤에 복제 #추가 기능 2
        if self.is_empty() == True: #원소 없는 큐는 복제도 불가능
            print("복제할 원소가 없습니다.")
        elif self.is_full() == True: #꽉 찬 큐는 복제 불가능
            print("복제할 공간이 없습니다.")
        else:
            self.queue.append(self.queue[self.tail]) #바로 뒤에 현재 위치의 원소 추가
            self.tail = self.tail + 1 #tail 변수 조정

    def move_back(self): #추가 기능 3
        self.queue.append(self.queue.pop(0)) #큐의 제일 앞의 값을 dequeue해서 뒤에 enqueue

    def delete(self, target): #추가 기능 4
        count = 0 #제거한 횟수
        for i in range(self.tail+1):
            if self.queue[0] == target: #만약 현재 제일 앞의 원소가 찾는 원소와 같다면
                self.queue.pop(0) #제일 앞의 원소 제거
                count = count + 1 #count 증가
            else: #다르다면
                self.queue.append(self.queue.pop(0)) #큐의 제일 앞의 값을 dequeue해서 뒤에 enqueue
        self.tail = self.tail - count #제거한 횟수만큼 tail 감소
    

print("명령문 안내")
print("+(원소의 값): 뒤에 원소 추가")
print("-: 가장 앞의 원소 제거")
print("(숫자)-: 숫자 만큼의 원소 앞에서 제거")
print("P: tail의 원소의 데이터 보여주기")
print("H: head가 큐의 몇번째 칸에 들어있는지 보여주기")
print("T: tail이 큐의 몇번째 칸에 들어있는지 보여주기")
print("=(값): tail의 원소를 입력한 값으로 대체")
print("#: 큐의 원소 개수 출력")
print("C: 큐 비우기")
print("E: 큐 비었는지 확인")
print("F: 큐의 마지막 칸이 차있는지 확인")
print("?(값): 큐에 해당 값을 가지는 원소가 존재하는지 확인")
print("!(값): 큐 안의 해당 값을 가지는 원소를 모두 제거")
print("D: tail 원소 바로 뒤에 추가")
print("B: 현재 큐의 맨 앞 원소를 맨 뒤로 이동")
print("L: 큐 출력 및 커서의 위치 표시")
print("&: 프로그램 종료\n\n") #각 기능별 설명

my_queue = Queue()

n = int(input("큐의 최대 크기를 입력해주세요: ")) #배열 크기 입력받기
my_queue.create(n) #배열 크기 결정
used = 0 #하나의 명령이 복수의 글자를 사용하는 경우 식별용
default_print = 1 #특정 명령은 기본 형태의 출력을 요구하지 않음. 그 명령 판별용

while True:
    inp = input("명령어: ") #문자열로 명령어 입력 받기
    
    if inp[0] == '&': #종료 명령
        break
    
    for i in range(len(inp)):
        if used > 0:
            used = used - 1
            continue
        
        elif inp[i] == '+': #enqueue
            my_queue.enqueue(inp[i+1]) #+뒤에 문자가 오므로 바로 뒤의 문자를 큐에 추가
            used = 1 #이미 +의 한칸 뒤까지 다 사용했으므로 그 뒤로 이동

        elif inp[i] == '-': #dequeue
            my_queue.dequeue()

        elif inp[i] == 'P': #peek
            my_queue.peek()
            default_print = 0

        elif inp[i] == 'H': #head
            my_queue.print_head()
            default_print = 0

        elif inp[i] == 'T': #tail
            my_queue.print_tail()
            default_print = 0

        elif inp[i] == '=': #replace
            my_queue.replace(inp[i+1])
            i = i+1

        elif inp[i] == '0' or inp[i] == '1' or inp[i] == '2' or\
             inp[i] == '3' or inp[i] == '4' or inp[i] == '5' or\
             inp[i] == '6' or inp[i] == '7' or inp[i] == '8' or\
             inp[i] == '9': #number
            if i == len(inp)-1:  #문자열 마지막 노드인 경우
                print("잘못된 입력입니다.")
            elif inp[i+1] == '0' or inp[i+1] == '1' or inp[i+1] == '2' or\
                 inp[i+1] == '3' or inp[i+1] == '4' or inp[i+1] == '5' or\
                 inp[i+1] == '6' or inp[i+1] == '7' or inp[i+1] == '8' or\
                 inp[i+1] == '9': #two-digit number
                num = int(inp[i] + inp[i+1])
                if inp[i+2] == '-':
                    used = 2
                    for i in range(num):
                        my_queue.dequeue()
                else:
                    print("잘못된 입력입니다.")
                        
            else: #one-digit number
                num = int(inp[i])
                if inp[i+1] == '-':
                    used = 1
                    for i in range(num):
                        my_queue.dequeue()
                else:
                    print("잘못된 입력입니다.")

        elif inp[i] == '#': #element count
            my_queue.data_count()
            default_print = 0

        elif inp[i] == 'E': #is empty
            if my_queue.is_empty() == True:
                print("True")
            else:
                print("False")
            default_print = 0

        elif inp[i] == 'F': #is full
            if my_queue.is_full() == True:
                print("True")
            else:
                print("False")
            default_print = 0

        elif inp[i] == '?': #is member
            print("%d"%(my_queue.is_member(inp[i+1])))
            used = 1
            default_print = 0

        elif inp[i] == '!': #delete
            my_queue.delete(inp[i+1])
            used = 1

        elif inp[i] == 'C': #clear
            my_queue.clear_queue()
        
        elif inp[i] == 'L': #print
            continue #어차피 나가면 출력이 실행됨

        elif inp[i] == 'D': #duplicate
            my_queue.duplicate()

        elif inp[i] == 'B': #move_back
            my_queue.move_back()

    if default_print == 1:
        my_queue.print_queue()
    else:
        default_print = 1
            
