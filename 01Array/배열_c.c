//자료구조 한옥영 교수님 4주차 실습과제
//배열 ADT 실습과제
//최종 작성일: 2020.06.10(수)
//2019312481 심규현

#include <stdio.h>
#include <string.h> //문자열 처리용

void insert(char array[], int* cursor, char data){
    int push=0;
    if(strlen(array)==99){ //메인 배열의 크기를 초과해서 저장할 수 없음
        printf("99개 초과의 값을 저장할 수 없습니다.\n");
        printf("값 저장 실패.\n");
        return;
    }
    else{
        push = strlen(array) - ((*cursor)+1); //전체 원소 개수 - 이동하지 않을 원소개수 = 이동할 원소개수 -> 얘네들을 모두 cnt만큼 밀어야함
        for(int i=0; i<push; i++){
            array[strlen(array)-i]=array[strlen(array)-i-1];
        } //cursor+1뒤의 모든 원소들을 1만큼 뒤로 밀어야함
        array[(*cursor)+1] = data;
        (*cursor)++;
    }
    return;
}

void traverse_front(char array[], int* cursor){
    (*cursor) = 0;
    return;
}

void traverse_rear(char array[], int* cursor){
    (*cursor) = strlen(array) - 1;
    return;
}

void go_left(char array[], int* cursor){
    if((*cursor) == 0){ //첫번째 원소는 왼쪽에 원소가 없음
        printf("잘못된 명령입니다.\n");
    }
    else{
        (*cursor)--;
    }
    return;
}

void go_right(char array[], int* cursor){
    if((*cursor) == strlen(array) - 1){ //마지막 원소는 오른쪽에 원소가 없음
        printf("잘못된 명령입니다.\n");
    }
    else{
        (*cursor)++;
    }
    return;
}

void delete(char array[], int* cursor){
    int tmp;
    tmp = (*cursor);
    if(strlen(array)==0){ //원소가 배열에 없는 경우
        printf("삭제할 원소가 없습니다.\n");
    }
    else{
        int i;
        int pull = strlen(array) - (*cursor); //전체 원소 개수 - 이동하지 않을 원소개수 = 이동할 원소개수 -> 얘네들을 모두 한칸씩 당겨야함
        for(i=0; i<pull; i++){
            array[(*cursor)]=array[(*cursor)+1];
            (*cursor)++;
        } //당기기
        array[(*cursor)] = '\0'; //맨끝에 NULL 문자 넣어주기
        if(strlen(array)==0){ //하나 남은 원소를 제거한 경우
            (*cursor) = -1;
        }
        else{
            if(tmp+1>strlen(array)){
                (*cursor) = 0; //마지막 원소를 제거한 경우 다시 0번째 인덱스부터 채우기
            }
            else{
                (*cursor) = tmp; //그 외의 경우 원래 가르키던 곳 계속 가리킴
            }
        }
    }
    return;
}

void get_data(char array[], int* cursor){
    printf("Return %c\n", array[(*cursor)]);
    return;
}

void replace(char array[], int* cursor, char data){
    array[(*cursor)] = data;
    return;
}

void empty(char array[], int* cursor){
    int i;
    int length = strlen(array);
    for(i=0;i<length;i++){
        array[i]='\0';
    } //배열의 모든 원소 다 NULL 문자로 바꾸기 -> 배열 비우기
    (*cursor) = -1;
    return;
}

int data_count(char array[], int* cursor){
    int data;
    data = strlen(array) - 1;
    return data;
}

void move_element_int(char array[], int* cursor, int position){
    char tmp;
    int i;
    int index = position;
    int push;
    if(index == (*cursor)) printf("같은 자리로는 이동시킬 수 없습니다.\n");
    else if(index > (*cursor)){ //뒤로 이동
        tmp = array[(*cursor)]; //임시 저장
        for(i=(*cursor); i<index; i++){
            array[i]=array[i+1];
        } //하나씩 뒤에서 앞으로 당겨옴
        array[index] = tmp; //임시 저장해둔거 목표에 대입
    }
    else{ //앞으로 이동
        tmp = array[(*cursor)]; //임시저장
        push = (*cursor); //이동할 원소개수 -> 얘네들을 모두 한칸씩 밀어야함
        for(i=push-1; i>=index; i--){
            array[i+1]=array[i];
        } //하나씩 앞에서 뒤로 밀어주기
        array[index] = tmp; //임시 저장해둔거 목표에 대입
    }
    (*cursor) = index; //목표 = 희망 위치이므로 위치 재설정
    return;
}

void move_element_char(char array[], int* cursor, char position){
    char tmp;
    int count;
    int index;
    index = position - '0';
    if(position == 'P'){ //원소 왼쪽으로 한칸 이동
        if((*cursor) == 0){
            printf("이동할 수 없습니다.\n"); //첫번째 원소는 왼쪽으로 이동 불가능
        }
        else{
            tmp = array[(*cursor)];
            array[(*cursor)] = array[(*cursor)-1];
            array[(*cursor)-1] = tmp; //이동 가능한 경우 교환
        }
    }
    else if(position == 'N'){ //원소 오른쪽으로 한칸 이동
        if((*cursor) == (strlen(array)-1)){
            printf("이동할 수 없습니다.\n"); //마지막 원소는 오른쪽으로 이동 불가능
        }
        else{
            tmp = array[(*cursor)];
            array[(*cursor)] = array[(*cursor)+1];
            array[(*cursor)+1] = tmp;
        }
    }
    else if(position == 'n'){ //마지막 인덱스 찾아서 이동
        count = data_count(array, cursor);
        move_element_int(array, cursor, count); //data_count 함수에서 마지막 인덱스를 반환받아 다시 move_element 실행
    }
    else printf("잘못된 명령입니다.\n"); //유의미한 값이 존재하는 배열 범위 밖
    
    return;
}

void print(char array[], int* cursor){
    int i=0;
    if(strlen(array)>0){
        while(array[i]!='\0'){
            printf("%c ", array[i]);
            i++;
        }//NULL 문자 나올때 까지 다 출력
        printf("\n");
        printf("현재 위치는 %d번째 원소입니다.\n", (*cursor)+1); //커서 위치 알림. 배열식 주소 (0부터) -> 사용자가 보는 위치 (1부터) 변환
    }
    else{
        printf("empty array\n");
    }
    return;
}

void swap_array(char array[], int* cursor, char data1, char data2){
    int index1, index2;
    char tmp;
    if (strlen(array) < 2){ //원소가 2개 미만 -> 변경 불가능
        printf("위치를 바꿀 원소의 수가 부족합니다.\n");
    }
    else{
        index1 = data1 - '0';
        index2 = data2 - '0';
        tmp = array[index1];
        array[index1] = array[index2];
        array[index2] = tmp;//교환
    }
    return;
}

void duplicate(char array[], int* cursor){
    if(strlen(array) == 0){ //원소 없는 배열은 복제도 불가능
        printf("복제할 원소가 없습니다.\n");
    }
    else{
        insert(array, cursor, array[(*cursor)]); //현 위치의 원소를 삽입 = 복제
    }
    return;
}

void traverse_mid(char array[], int* cursor){
    (*cursor) = strlen(array)/2;
    return;
}

int main(void){ //메인 함수
    char array[101]=""; //메인 배열
    int cursor = -1; //현재 위치 나타내는 변수
    char inp[50]=""; //입력 받기 용 문자열
    
    printf("명령문 안내\n");
    printf("+(원소의 값): 원소 추가\n");
    printf("<: 제일 왼쪽으로 현재 위치 이동\n");
    printf(">: 제일 오른쪽으로 현재 위치 이동\n");
    printf("|: 가운데로 현재 위치 이동 (만약 짝수일 경우 가운데 두 원소 중 오른쪽)\n");
    printf("-: 현재 위치의 원소 제거\n");
    printf("@: 현재 위치의 원소의 데이터 보여주기\n");
    printf("=(값): 현재 위치의 원소를 입력한 값으로 대체\n");
    printf("E: 배열 비우기\n");
    printf("M(값): 현재 커서가 위치한 원소를 이동시킴\n");
    printf("      값의 종류: P: 한칸 왼쪽, N: 한칸 오른쪽, 숫자: 해당 인덱스\n");
    printf("S(위치1)(위치2): 지정한 두 개의 원소의 위치를 서로 바꿈\n");
    printf("D: 현재 위치의 원소 바로 옆에 복제\n");
    printf("L: 배열 출력 및 커서의 위치 표시\n");
    printf("&: 프로그램 종료\n\n"); //각 기능별 설명
    
    while(1){
        printf("명령어: ");
        scanf("%[^\n]s", inp); //입력받기. [^\n]를 붙이면 엔터를 제외한 모든것을 다 받는다 (공백 입력받기 가능)
        scanf("%*c"); //*을 넣어주면 문자를 입력받아 버린다 -> 오류 수정용
        
        if(inp[0] == '&'){
            break;
        }
        
        for(int i=0;i<=strlen(inp);i++){
            if(inp[i] == '+'){ //insert
                insert(array, &cursor, inp[i+1]); //+뒤에 문자가 오므로 바로 뒤의 문자를 배열에 추가
                i++; //이미 +의 한칸 뒤까지 다 사용했으므로 그 뒤로 이동
            }
            else if(inp[i] == '<'){ //traverse front
                traverse_front(array, &cursor);
            }
            else if(inp[i] == '>'){ //traverse rear
                traverse_rear(array, &cursor);
            }
            else if(inp[i] == 'P'){ //go previous = go left
                go_left(array, &cursor);
            }
            else if(inp[i] == 'N'){ //go next = go right
                go_right(array, &cursor);
            }
            else if(inp[i] == '-'){ //delete
                delete(array, &cursor);
            }
            else if(inp[i] == '@'){ //get data
                get_data(array, &cursor);
            }
            else if(inp[i] == '='){ //replace
                replace(array, &cursor, inp[i+1]);
                i++;
            }
            else if(inp[i] == 'E'){ //empty array
                empty(array, &cursor);
            }
            else if(inp[i] == 'M'){ //move
                if(inp[i+1] == 'P' || inp[i+1] == 'N' || inp[i+1] == 'n'){
                    move_element_char(array, &cursor, inp[i+1]);
                }
                else if(inp[i+1]-'0' >= 0 && inp[i+1]-'0' <= 9){ // 숫자 입력 받기
                    int tmp;
                    if(inp[i+2]-'0' >= 0 && inp[i+2]-'0' <= 9){ //two-digit
                        if(inp[i+3]=='\0'){
                            tmp = (inp[i+1]-'0')*10 + (inp[i+2]-'0'); //char->int
                            move_element_int(array, &cursor, tmp);
                            i=i+3;
                        }
                        else{
                            printf("ERROR: Only One & Two Digit Numbers Are Allowed.\n");
                        }
                    }
                    else{ //one-digit
                        if(inp[i+2]=='\0'){
                            tmp = inp[i+1]-'0'; //char->int
                            i=i+2;
                            move_element_int(array, &cursor, tmp);
                        }
                        else{
                            printf("ERROR: Invalid Input.\n");
                        }
                    }
                    //printf("tmp: %d", tmp);
                }
            }
            else if(inp[i] == 'L'){ //print
                continue; //어차피 나가면 출력이 실행됨. 중복 출력을 피하고자 continue문 입력.
            }
            else if(inp[i] == 'S'){ //swap
                swap_array(array, &cursor, inp[i+1], inp[i+2]);
            }
            else if(inp[i] == 'D'){ //duplicate
                duplicate(array, &cursor);
            }
            else if(inp[i] == '|'){ //traverse mid
                traverse_mid(array, &cursor);
            }
        }
        
        print(array, &cursor);
        
    }
    return 0;
}
