#자료구조 한옥영 교수님 6주차 실습과제
#스택 ADT 실습과제
#최종 작성일: 2020.06.19(금)
#2019312481 심규현

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.size = 0

    def create(self, n): #추가기능 1
        self.size = n #사이즈 지정

    def is_full(self): #다찼는지 확인
        if self.top+1 >= self.size: #현재 위치가 최대에 도달했다면
            return True #true
        else: #아니라면
            return False #false

    def is_empty(self): #추가기능 2 #비어있는지 확인
        if len(self.stack) == 0: #스택에 자료가 없다면
            return True #true 반환
        else: #아니라면
            return False #false 반환

    def push(self, data): #원소 끝에 삽입
        if self.is_full() == False: #배열이 아직 다 차지 않은 경우
            self.stack.append(data) #원소 추가
            self.top = self.top + 1 #top 값 조정
        else: #다 찬 경우 삽입 불가능
            print("잘못된 입력입니다")

    def pop(self): #top 원소 삭제
        if self.is_empty() == True: #원소가 스택에 없는 경우
            print("Error: nothing to pop") #pop 불가능
        else:
            tmp = self.stack.pop()
            print("return: " + tmp) #top 있는 원소 삭제와 동시에 값을 반환받아 출력
            self.top = self.top - 1 #top 값 조정
            return tmp

    def peek(self): #현재 위치의 원소가 가지고 있는 값 보여주기
        print(self.stack[self.top]) #top의 원소 출력

    def element_count(self): #현재 원소의 개수 출력
        print(self.top+1) #top은 인덱스이므로 원소의 개수 -1을 가짐. 따라서 top+1을 출력

    def print_top(self): #top관련 정보 출력
        print("( " + str(self.top+1) + ", " + self.stack[self.top] + " )") #원소의 개수와 현재 top 원소 출력

    def replace(self, data): #top 원소 대체
        self.stack[self.top] = data #top 원소 대체

    def clear_stack(self): #스택 비우기
        while (self.is_empty() == False):
            self.stack.pop() #스택식으로 초기화하기.
        self.top = -1 #top 변수 초기화

    def duplicate(self): #현재 위치의 원소 바로 뒤에 복제 #추가 기능 3
        if self.is_empty() == True: #원소 없는 스택은 복제도 불가능
            print("복제할 원소가 없습니다.")
        elif self.is_full() == True: #꽉 찬 스택은 복제 불가능
            print("복제할 공간이 없습니다.")
        else:
            self.stack.append(self.stack[self.top]) #바로 뒤에 현재 위치의 원소 추가
            self.top = self.top + 1 #top 변수 조정
        
def is_member(my_stack, tmp_stack, target): #target값을 가지는 원소 있는지 탐색
    find = 0 #찾으면 1, 못찾으면 0
    tmp_stack.clear_stack()
    for i in range(my_stack.top+1):
        if my_stack.stack[my_stack.top-i] == target: #원하던 값을 찾은경우
            find = 1 #기록
            tmp_stack.push(my_stack.pop()) #스택의 top 값을 pop해서 tmp_stack에 push
        else:
            tmp_stack.push(my_stack.pop())
            
    for i in range(my_stack.top+1):
        my_stack.push(tmp_stack.pop()) #tmp_stack의 top값을 pop해서 스택에 push -> 결국 원래대로 돌아옴
        
    if find == 1: #찾았으면
        return True #True
    elif find == 0: #못찾았으면
        return False #False
        
def reverse(my_stack, tmp_stack): #추가 기능 4
    tmp_stack.clear_stack()
    for i in range(my_stack.top+1):
        tmp_stack.push(my_stack.pop()) #스택에서 top부터 pop한 뒤 임시스택에 push -> 역순으로 저장됨
    stack = tmp_stack #그걸 그대로 스택에 대입
    
def print_stack(my_stack, tmp_stack): #스택 출력
    tmp_stack.clear_stack()
    if my_stack.is_empty() == True: #비어있는 스택인 경우
        print("empty stack")
    else: #아닌 경우
        tmp = my_stack.top+1
        print("[ ",end="") #출력 형식 맞추기용
        for i in range(tmp):
            tmp_stack.stack.append(my_stack.stack.pop()) #현재 스택의 값을 top부터 pop하며 임시 스택에 역순으로 저장
        for i in range(tmp):
            my_stack.stack.append(tmp_stack.stack.pop()) #임시 스택의 값을 top부터 pop하며 현재 스택에 다시 역순으로 (원래 순서대로) 저장
            print("%c "%(my_stack.stack[i]), end="") #동시에 값 출력 -> top 반대편부터 출력 가능
        print("]") #출력형식 맞추기 용
        print("현재 top 위치: %d번째 원소"%(my_stack.top+1)) #현재 top 위치 출력, 순서로 표현하므로 +1


print("명령문 안내")
print("+(원소의 값): 원소 추가")
print("-: (가장 끝의) 원소 제거")
print("(숫자)-: 숫자 만큼의 원소 제거")
print("P: top의 원소의 데이터 보여주기")
print("T: top의 원소의 데이터와 현재 스택의 높이(크기) 보여주기")
print("=(값): top의 원소를 입력한 값으로 대체")
print("#: 스택의 원소 개수 출력")
print("C: 스택 비우기")
print("E: 스택 비었는지 확인")
print("F: 스택 꽉 찼는지 확인")
print("?(값): 스택에 해당 값을 가지는 원소가 존재하는지 확인")
print("D: top 원소 바로 뒤에 추가")
print("R: 현재 스택의 순서 뒤바꾸기")
print("L: 스택 출력 및 커서의 위치 표시")
print("&: 프로그램 종료\n\n") #각 기능별 설명


my_stack = Stack()
tmp_stack = Stack()

n = int(input("스택의 최대 크기를 입력해주세요: ")) #배열 크기 입력받기
my_stack.create(n) #배열 크기 결정
tmp_stack.create(n)
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
        
        elif inp[i] == '+': #push
            my_stack.push(inp[i+1]) #+뒤에 문자가 오므로 바로 뒤의 문자를 스택에 추가
            used = 1 #이미 +의 한칸 뒤까지 다 사용했으므로 그 뒤로 이동

        elif inp[i] == '-': #pop
            my_stack.pop()

        elif inp[i] == 'P': #peek
            my_stack.peek()
            default_print = 0

        elif inp[i] == 'T': #top
            my_stack.print_top()
            default_print = 0

        elif inp[i] == '=': #replace
            my_stack.replace(inp[i+1])
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
                        my_stack.pop()
                else:
                    print("잘못된 입력입니다.")
                        
            else: #one-digit number
                num = int(inp[i])
                if inp[i+1] == '-':
                    used = 1
                    for i in range(num):
                        my_stack.pop()
                else:
                    print("잘못된 입력입니다.")

        elif inp[i] == '#': #element count
            my_stack.element_count()
            default_print = 0

        elif inp[i] == 'E': #is empty
            if my_stack.is_empty() == True:
                print("True")
            else:
                print("False")
            default_print = 0

        elif inp[i] == 'F': #is full
            if my_stack.is_full() == True:
                print("True")
            else:
                print("False")
            default_print = 0

        elif inp[i] == '?': #is member
            if is_member(my_stack, tmp_stack, inp[i+1]) == True:
                print("True")
            else:
                print("False")
            used = 1
            default_print = 0

        elif inp[i] == 'C': #clear
            my_stack.clear_stack()
        
        elif inp[i] == 'L': #print
            continue #어차피 나가면 출력이 실행됨

        elif inp[i] == 'D': #duplicate
            my_stack.duplicate()

        elif inp[i] == 'R': #reverse
            reverse(my_stack, tmp_stack)

    if default_print == 1:
        print_stack(my_stack, tmp_stack)
    else:
        default_print = 1
            
