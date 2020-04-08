#자료구조 한옥영 교수님 4주차 실습과제
#배열 ADT 실습과제
#최종 작성일: 2020.04.06(월)
#2019312481 심규현

array = [] #initailize
cursor = -1 #배열식 카운트
#전역 변수를 사용하여 사용자 설정 함수에서 바꾼 값이 본래의 배열에 영향을 미치도록 함

#저는 array와 count 같은 값을 함수들간 주고받는 것이 복제되는 것과 안되는 것이 헷갈려서
#아예 혼돈을 배제하고자 array를 전역으로 선언하고, 현재 위치의 이동을 관리하기 위한 변수 cursor 역시 전역으로 선언하여
#혼돈을 피하는 것이 더 편하다고 판단하였습니다. 명령어와 실행 결과에는 어떤 차이도 없습니다!

def insert(data): #원소 현재 위치 오른쪽에 삽입
    global array
    global cursor
    array.insert(cursor+1, data)
    cursor = cursor + 1

def traverse_front(): #현재 위치 첫번째 원소로 변경
    global cursor
    cursor = 0

def traverse_rear(): #현재 위치 마지막 원소로 변경
    global cursor
    cursor = len(array) - 1

def go_left(): #현재 위치 왼쪽으로 이동
    global cursor
    if cursor == 0: #첫번째 원소는 왼쪽에 원소가 없음
        print("잘못된 명령입니다.")
    else:
        cursor = cursor - 1

def go_right(): #현재 위치 오른쪽으로 이동
    global cursor
    if cursor == len(array) - 1: #마지막 원소는 오른쪽에 원소가 없음
        print("잘못된 명령입니다.")
    else:
        cursor = cursor + 1

def delete(): #현재 위치의 원소 삭제
    global array
    global cursor
    if len(array)==0: #원소가 배열에 없는 경우
        print("삭제할 원소가 없습니다.")
    else:
        del array[cursor] #현재 위치에 있는 원소 삭제
        if(cursor+1>len(array)):
            cursor = 0 #마지막 원소를 제거한 경우 제일 앞의 원소 가리킴

def get_data(): #현재 위치의 원소가 가지고 있는 값 보여주기
    global array
    global cursor
    print("Return %c"%array[cursor]) #해당 위치의 원소 출력

def replace(data): #현재 위치의 원소 대체
    global array
    global cursor
    array[cursor] = data #해당 위치의 원소 대체

def empty(): #배열 비우기
    global array
    global cursor
    array = [] #배열 비우기 위해 빈 리스트를 array에 대입
    cursor = -1 #원소 없으므로 커서는 0번째 원소를 가리킴

def data_count():
    global array
    return len(array)-1 #마지막 인덱스 번호 반환

def move(data): #원소 이동
    global array
    global cursor
    if(data == 'P'): #원소 왼쪽으로 한칸 이동
        if cursor == 0:
            print("이동할 수 없습니다.") #첫번째 원소는 왼쪽으로 이동 불가능
        else:
            array[cursor],array[cursor-1] = array[cursor-1],array[cursor] #이동 가능한 경우 교환
    elif(data == 'N'): #원소 오른쪽으로 한칸 이동
        if cursor == (len(array)-1):
            print("이동할 수 없습니다.") #마지막 원소는 오른쪽으로 이동 불가능
        else:
            array[cursor],array[cursor+1] = array[cursor+1],array[cursor] #이동 가능한 경우 교환
    elif(data == 'n'): #마지막 인덱스를 찾아 그쪽으로 이동
        end = data_count() #마지막 인덱스 반환받기
        move(end) #마지막 인덱스로 이동
    else: #원소를 지정된 인덱스로 이동
        index = int(data) #문자로 입력받은 숫자를 정수형 변수로 변환
        tmp = array[cursor]
        del array[cursor]
        array.insert(index, tmp) #이동하고자 하는 원소를 임시 저장후, 삭제 한뒤 원하는 위치에 재삽입
        cursor = index
    
def print_array(): #배열 출력
    global array
    global cursor
    if len(array) == 0: #비어있는 배열인 경우
        print("empty array")
    else:
        print(array) #array 출력
        print("현재 커서 위치: %d번째 원소"%(cursor+1)) #현재 위치 출력, 순서로 표현하므로 +1

def swap_array(data1, data2): #원소간 위치 바꾸기 #추가 기능 1
    global array
    if len(array) < 2: #원소가 2개 미만 -> 변경 불가능
        print("위치를 바꿀 원소의 수가 부족합니다.")
    else:
        index1 = int(data1)
        index2 = int(data2)
        array[index1], array[index2] = array[index2], array[index1] #교환

def duplicate(): #현재 위치의 원소 바로 뒤에 복제 #추가 기능 2
    global array
    global cursor
    if len(array) == 0: #원소 없는 배열은 복제도 불가능
        print("복제할 원소가 없습니다.")
    else:
        array.insert(cursor+1, array[cursor]) #바로 뒤에 현재 위치의 원소 추가
        cursor = cursor + 1 # 가리키는 위치 이동

def traverse_mid(): #현재 위치 중간 원소로 변경 #추가 기능 3
    global cursor
    cursor = int(len(array)/2)

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


while True:
    inp = input("명령어: ") #문자열로 명령어 입력 받기
    
    if inp[0] == '&': #종료 명령
        break
    
    for i in range(len(inp)):
        if inp[i] == '+': #insert
            insert(inp[i+1]) #+뒤에 문자가 오므로 바로 뒤의 문자를 배열에 추가
            i = i+1 #이미 +의 한칸 뒤까지 다 사용했으므로 그 뒤로 이동
            
        elif inp[i] == '<': #traverse front
            traverse_front()

        elif inp[i] == '>': #traverse rear
            traverse_rear()

        elif inp[i] == 'P': #go previous = go left
            go_left()

        elif inp[i] == 'N': #go next = go right
            go_right()

        elif inp[i] == '-': #delete
            delete()

        elif inp[i] == '@': #get data
            get_data()

        elif inp[i] == '=': #replace
            replace(inp[i+1])
            i = i+1

        elif inp[i] == 'E': #empty array
            empty()

        elif inp[i] == 'M': #move
            move(inp[i+1])
        
        elif inp[i] == 'L': #print
            continue #어차피 나가면 출력이 실행됨

        elif inp[i] == 'S': #swap
            swap_array(inp[i+1],inp[i+2])

        elif inp[i] == 'D': #duplicate
            duplicate()

        elif inp[i] == '|': #traverse mid
            traverse_mid()

    print_array()
            
