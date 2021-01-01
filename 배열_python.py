#자료구조 한옥영 교수님 4주차 실습과제
#배열 ADT 실습과제
#최종 작성일: 2020.06.10(수)
#2019312481 심규현

class Array:
    def __init__(self):
        self.list = []
        self.cursor = -1

    def insert(self, data): #원소 현재 위치 오른쪽에 삽입
        self.list.insert(self.cursor+1, data)
        self.cursor = self.cursor + 1

    def traverse_front(self): #현재 위치 첫번째 원소로 변경
        self.cursor = 0

    def traverse_rear(self): #현재 위치 마지막 원소로 변경
        self.cursor = len(self.list) - 1

    def go_left(self): #현재 위치 왼쪽으로 이동
        if self.cursor == 0: #첫번째 원소는 왼쪽에 원소가 없음
            print("잘못된 명령입니다.")
        else:
            self.cursor = self.cursor - 1

    def go_right(self): #현재 위치 오른쪽으로 이동
        if self.cursor == len(self.list) - 1: #마지막 원소는 오른쪽에 원소가 없음
            print("잘못된 명령입니다.")
        else:
            self.cursor = self.cursor + 1

    def delete(self): #현재 위치의 원소 삭제
        if len(self.list)==0: #원소가 배열에 없는 경우
            print("삭제할 원소가 없습니다.")
        else:
            del self.list[self.cursor] #현재 위치에 있는 원소 삭제
            if(self.cursor+1>len(self.list)):
                self.cursor = 0 #마지막 원소를 제거한 경우 제일 앞의 원소 가리킴

    def get_data(self): #현재 위치의 원소가 가지고 있는 값 보여주기
        print("Return %c"%self.list[self.cursor]) #해당 위치의 원소 출력

    def replace(self, data): #현재 위치의 원소 대체
        self.list[self.cursor] = data #해당 위치의 원소 대체

    def empty(self): #배열 비우기
        self.list = [] #배열 비우기 위해 빈 리스트를 self.list에 대입
        self.cursor = -1 #원소 없으므로 커서는 0번째 원소를 가리킴

    def data_count(self):
        return len(self.list)-1 #마지막 인덱스 번호 반환

    def move_int(self, index): #원소를 지정된 인덱스로 이동
        tmp = self.list[self.cursor]
        del self.list[self.cursor]
        self.list.insert(index, tmp) #이동하고자 하는 원소를 임시 저장후, 삭제 한뒤 원하는 위치에 재삽입
        self.cursor = index

    def move(self, data): #원소 이동
        if(data == 'P'): #원소 왼쪽으로 한칸 이동
            if self.cursor == 0:
                print("이동할 수 없습니다.") #첫번째 원소는 왼쪽으로 이동 불가능
            else:
                self.list[self.cursor],self.list[self.cursor-1] = self.list[self.cursor-1],self.list[self.cursor] #이동 가능한 경우 교환
        elif(data == 'N'): #원소 오른쪽으로 한칸 이동
            if self.cursor == (len(self.list)-1):
                print("이동할 수 없습니다.") #마지막 원소는 오른쪽으로 이동 불가능
            else:
                self.list[self.cursor],self.list[self.cursor+1] = self.list[self.cursor+1],self.list[self.cursor] #이동 가능한 경우 교환
        elif(data == 'n'): #마지막 인덱스를 찾아 그쪽으로 이동
            end = self.data_count() #마지막 인덱스 반환받기
            self.move_int(end) #마지막 인덱스로 이동
        
    def print_array(self): #배열 출력
        if len(self.list) == 0: #비어있는 배열인 경우
            print("empty self.list")
        else:
            print(self.list) #self.list 출력
            print("현재 커서 위치: %d번째 원소"%(self.cursor+1)) #현재 위치 출력, 순서로 표현하므로 +1

    def swap_array(self, data1, data2): #원소간 위치 바꾸기 #추가 기능 1
        if len(self.list) < 2: #원소가 2개 미만 -> 변경 불가능
            print("위치를 바꿀 원소의 수가 부족합니다.")
        else:
            index1 = int(data1)
            index2 = int(data2)
            self.list[index1], self.list[index2] = self.list[index2], self.list[index1] #교환

    def duplicate(self): #현재 위치의 원소 바로 뒤에 복제 #추가 기능 2
        if len(self.list) == 0: #원소 없는 배열은 복제도 불가능
            print("복제할 원소가 없습니다.")
        else:
            self.list.insert(self.cursor+1, self.list[self.cursor]) #바로 뒤에 현재 위치의 원소 추가
            self.cursor = self.cursor + 1 # 가리키는 위치 이동

    def traverse_mid(self): #현재 위치 중간 원소로 변경 #추가 기능 3
        self.cursor = int(len(self.list)/2)

print("명령문 안내")
print("+(원소의 값): 원소 추가")
print("<: 제일 왼쪽으로 현재 위치 이동")
print(">: 제일 오른쪽으로 현재 위치 이동")
print("|: 가운데로 현재 위치 이동 (만약 짝수일 경우 가운데 두 원소 중 오른쪽)")
print("-: 현재 위치의 원소 제거")
print("@: 현재 위치의 원소의 데이터 보여주기")
print("=(값): 현재 위치의 원소를 입력한 값으로 대체")
print("E: 배열 비우기")
print("M(값): 현재 커서가 위치한 원소를 이동시킴")
print("      값의 종류: P: 한칸 왼쪽, N: 한칸 오른쪽, 숫자: 해당 인덱스")
print("S(위치1)(위치2): 지정한 두 개의 원소의 위치를 서로 바꿈")
print("D: 현재 위치의 원소 바로 옆에 복제")
print("L: 배열 출력 및 커서의 위치 표시")
print("&: 프로그램 종료\n\n") #각 기능별 설명

my_array = Array()
used = 0

while True:
    inp = input("명령어: ") #문자열로 명령어 입력 받기
    
    if inp[0] == '&': #종료 명령
        break
    
    for i in range(len(inp)):
        if used > 0:
            used = used - 1
            continue
        
        elif inp[i] == '+': #insert
            my_array.insert(inp[i+1]) #+뒤에 문자가 오므로 바로 뒤의 문자를 배열에 추가
            used = used + 1 #이미 +의 한칸 뒤까지 다 사용했으므로 그 뒤로 이동
            
        elif inp[i] == '<': #traverse front
            my_array.traverse_front()

        elif inp[i] == '>': #traverse rear
            my_array.traverse_rear()

        elif inp[i] == 'P': #go previous = go left
            my_array.go_left()

        elif inp[i] == 'N': #go next = go right
            my_array.go_right()

        elif inp[i] == '-': #delete
            my_array.delete()

        elif inp[i] == '@': #get data
            my_array.get_data()

        elif inp[i] == '=': #replace
            my_array.replace(inp[i+1])
            used = used + 1

        elif inp[i] == 'E': #empty array
            my_array.empty()

        elif inp[i] == 'M': #move
            if inp[i+1] == 'P' or inp[i+1] == 'N' or inp[i+1] == 'n':
                my_array.move(inp[i+1])
            elif ord(inp[i+1]) >= ord('0') and ord(inp[i+1]) <= ord('9'): #number
                if i == len(inp)-1:  #문자열 마지막 노드인 경우
                    my_array.move_int(int(inp[i+1]))
                    used = used + 1
                elif ord(inp[i+2]) >= ord('0') and ord(inp[i+2]) <= ord('9'): #two-digit number
                    num = int(inp[i+1] + inp[i+2])
                    used = used + 2
                    my_array.move_int(num)
                else:
                    print("잘못된 입력입니다.")
        
        elif inp[i] == 'L': #print
            continue #어차피 나가면 출력이 실행됨

        elif inp[i] == 'S': #swap
            my_array.swap_array(inp[i+1],inp[i+2])

        elif inp[i] == 'D': #duplicate
            my_array.duplicate()

        elif inp[i] == '|': #traverse mid
            my_array.traverse_mid()

    my_array.print_array()
            
