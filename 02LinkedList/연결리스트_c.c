//자료구조 한옥영 교수님 5주차 실습과제
//연결리스트 ADT 실습과제
//최종 작성일: 2020.06.17(수)
//2019312481 심규현

#include <stdio.h>
#include <stdlib.h> //동적할당용
#include <string.h> //문자열 처리용

typedef struct Node{ //자료형 NODE 선언
    char data; //데이터 (실질적인 값)
    struct Node *link; //링크
} NODE;

typedef struct LinkedList{
    NODE* head;
    NODE* position; //현재 위치를 가리키는 변수
    int cursor;
    int listlen;
} LL;

void create(LL* my_list){
    NODE *new_node = malloc(sizeof(NODE)); //헤드노드 선언
    my_list->cursor = 0;
    my_list->listlen = 0;
    my_list->head = new_node;
    my_list->head->data = '\0';
    my_list->head->link = NULL; //헤드노드 초기화
    my_list->position = my_list->head; //처음에는 헤드노드 가리킴
}

void add(LL* my_list, char data){
    NODE* new_node = malloc(sizeof(NODE)); //새로운 노드 생성
    NODE* target = my_list->position;
    if(target->link == NULL){ //마지막 노드인 경우
        new_node->data = data; //새로운 노드에 값 주기
        new_node->link = NULL; //마지막 노드이므로 NULL가리킴
        target->link = new_node; //그 전 노드는 새로운 노드를 가리킴
    }
    else{//마지막 노드가 아닌 경우
        new_node->data = data; //값주기
        new_node->link = target->link; //기존 노드가 가리키던 노드 가리킴
        target->link = new_node; //기존 노드는 새로운 노드 가리킴
    }
    my_list->cursor++; //출력용 변수 업데이트
    my_list->listlen++; //리스트의 길이 +1
    my_list->position = my_list->position->link;
    return;
}

void get_data(LL* my_list){
    printf("%c\n", my_list->position->data); //현재 위치의 데이터 출력
    return;
}

void traverse_front(LL* my_list){
    if(my_list->head->link == NULL){ //빈 연결리스트인 경우
        printf("잘못된 명령입니다\n");
    }
    else{
        my_list->position = my_list->head->link; //맨앞으로 가기
        my_list->cursor = 1; //출력용 변수 업데이트
    }
    return;
}

void traverse_rear(LL* my_list){
    int i;
    if(my_list->head->link == NULL){ //빈 연결리스트인 경우
        printf("잘못된 명령입니다\n");
    }
    else{
        traverse_front(my_list); //현재 위치 앞으로 보낸 뒤
        for(i=0;i<my_list->listlen-1;i++){ // 연결리스트의 길이만큼 link를타고 이동 = 제일 마지막 노드
            my_list->position = my_list->position->link;
        }
        my_list->cursor = my_list->listlen; //출력용 변수 업데이트
    }
    return;
}

void print(LL* my_list){
    NODE *current = NULL;
    current = my_list->head->link; //첫번째 노드부터
    if(my_list->listlen == 0){ //빈 연결리스트라면
        printf("\n"); //빈 상태를 출력
    }
    else{
        while (current != NULL) // 마지막 노드까지
        {
            printf("%c ", current->data);    // 현재 노드의 데이터 출력
            current = current->link;             // 포인터에 다음 노드의 주소 저장
        }
        printf("\n");
    }
    printf("현재 커서의 위치는 %d번째 노드입니다.\n", my_list->cursor); //현재 위치를 나타내는 출력용 변수 출력
    return;
}

void go_right(LL* my_list){
    if(my_list->position->link == NULL){ //마지막 원소인 경우
        printf("잘못된 명령입니다.\n"); //이동 불가능
    }
    else{
        my_list->position = my_list->position->link; //오른쪽으로 링크타고 이동
        my_list->cursor++; //출력용 변수 업데이트
    }
    return;
}

void delete(LL* my_list){
    int i;
    NODE *before = NULL;
    NODE* target = my_list->position;
    before = my_list->head;
    if(my_list->listlen==0){ //빈 연결리스트인 경우
        printf("잘못된 입력입니다.\n"); //삭제 불가능
        return;
    }
    for(i=0;i<my_list->listlen;i++){ //전 노드 찾기
        if(before->link == target){ //현재 노드를 가리키는 노드를 찾으면 전 노드로 저장
            break;
        }
        before = before->link; //못찾으면 찾을때까지 계속 탐색
    }
    if(target->link==NULL){ //제일 끝 노드인 경우
        before->link = NULL;
        if(my_list->listlen-1==0){ //하나남은 노드일 경우
            my_list->position = my_list->head; //현재 위치 연결리스트 제일 앞 (헤드노드)으로 이동
            my_list->cursor = 0; //출력용 변수 업데이트
        }
        else{ //하나남은 노드가 아닌 경우
            my_list->position = my_list->head->link; //제일 앞의 노드 (헤드노드 바로 다음의 노드)로 이동
            my_list->cursor = 1; //출력용 변수 업데이트
        }
        free(target); //공간 free
    }
    else{ //제일 끝 노드가 아닌 경우
        before->link = target->link; //바로 전 노드가 현재 노드가 가리키는 노드 가리키게 함
        my_list->position = target->link; //현재 노드를 바로 다음 노드로 바꿈
        free(target); //공간 free
    }
    my_list->listlen--; //삭제 시 연결리스트의 길이 -1
    return;
}

void replace(LL* my_list, char data){
    my_list->position->data = data; //현재 위치의 값 바꾸기
    return;
}

void data_count(LL* my_list){
    printf("%d\n", my_list->listlen); //연결리스트의 길이 출력
    return;
}

void is_member(LL* my_list, char find){
    int i;
    int found = 0; //찾으면 1로 바꿀 변수
    NODE *current = my_list->head->link;
    for(i=1;i<=my_list->listlen;i++){ // 쭉 돌면서 찾기
        if(current->data == find){ //찾으면
            my_list->position = current; //
            my_list->cursor = i; //현재 위치 저장
            found = 1; //찾았음을 알림
            break;
        }
        current = current->link; //아니면 계속 돌기
    }
    if(found==0){ //못찾았으면
        printf("노드 %c는 연결리스트 안에 존재하지 않습니다.\n", find);
    }
    else{
        printf("%d: ", my_list->cursor); //찾은 위치 출력
    }
    return;
}

void traverse_n(LL* my_list, int num){
    int i;
    NODE *current = NULL;
    current = my_list->head; //임시 변수 헤드로 설정해두기
    if(num>my_list->listlen){ //접근 불가능한 숫자에 가려고하면
        printf("잘못된 입력입니다.\n"); //안됨
    }
    else{
        for(i=0;i<num;i++){ //받은 숫자만큼 다음 노드로 이동
            current = current->link;
        }
        my_list->position = current; //현재 위치 변경
        my_list->cursor = num; //출력용 변수 업데이트
    }
    return;
}

void clear_the_list(LL* my_list){
    NODE *current = NULL;
    NODE *next = NULL;
    current = my_list->head->link; //첫 번째 노드부터
    while (current != NULL) // 마지막 노드까지 차례대로
    {
        next = current->link;// 다음 노드 주소 저장
        current = next; //다음 노드로 넘어가기
    }
    my_list->head->link = NULL; //헤드 링크 끊어버리기
    my_list->position = my_list->head; //현재 위치 헤드 노드로 이동
    my_list->cursor = 0; //출력용 변수 초기화
    my_list->listlen = 0; //연결리스트 길이 0
    free(current); //임시 노드 free
    return;
}

void is_empty(LL* my_list){
    if(my_list->listlen==0){ //비어있으면
        printf("True\n");
    }
    else{ //안비어있으면
        printf("False\n");
    }
    return;
}

void traverse_mid(LL* my_list){
    int i, mid;
    my_list->position = my_list->head;
    mid = (my_list->listlen)/2 + 1; //중간은 몇번째 노드인지 구하기
    for(i=0;i<mid;i++){ //그만큼 헤드부터 이동
        my_list->position = my_list->position->link;
    }
    my_list->cursor = mid; //출력용 변수 이동
    return;
}

void duplicate(LL* my_list){
    char data;
    if(my_list->listlen==0){ //빈 연결리스트인 경우
        printf("잘못된 명령입니다\n");
    }
    else{
        data = my_list->position->data; //현재 위치의 데이터 저장
        add(my_list, data); //현재 위치에 현재 위치의 데이터 추가
    }
    return;
}

void swap(LL* my_list, char target1, char target2){
    int i;
    int value1, value2;
    char tmp;
    NODE *point1 = NULL;
    NODE *point2 = NULL; //사용되는 변수들 사용
    point1 = my_list->head;
    point2 = my_list->head; //각각의 포인터가 헤드노드 가리키게 함
    value1 = target1 - '0';
    value2 = target2 - '0'; //char -> int 바꿔주기
    if(value1>my_list->listlen || value2>my_list->listlen){ //둘 중에 범위가 연결리스트 밖이 있으면 안됨
        printf("잘못된 입력입니다.\n");
    }
    else if(my_list->listlen<2){ //원소가 두개 미만이어도 안됨
        printf("잘못된 입력입니다.\n");
    }
    else{
        for(i=0;i<value1;i++){
            point1 = point1->link; //n번째 노드 찾기
        }
        for(i=0;i<value2;i++){
            point2 = point2->link; //m번째 노드 찾기
        }
        tmp = point1->data;
        point1->data = point2->data;
        point2->data = tmp; //데이터 값 바꾸기
    }
}

int main(void){ //메인 함수
    LL my_list = {NULL};
    create(&my_list);
    
    char inp[50]=""; //입력 받기 용 문자열
    
    int default_print = 1; //출력 관리용 변수. 1이면 출력
    
    int tmp; //임시값 저장용 변수
    
    printf("명령문 안내\n");
    printf("+(노드의 값): 현재 위치의 바로 뒤에 값 추가\n");
    printf("*(노드의 값): 연결 리스트의 맨 앞에 값 추가\n"); //자신만의 기능
    printf("<: 연결 리스트의 가장 앞 노드로 현재 위치 이동\n");
    printf("   이동을 위한 명령문: N: 다음 노드\n");
    printf(">: 연결 리스트의 맨 뒤 노드로 현재 위치 이동\n");
    printf("(숫자): 해당 숫자 번재의 노드로 현재 위치 이동\n");
    printf("|: 가운데로 현재 위치 이동 (만약 짝수일 경우 가운데 두 노드 중 오른쪽)\n"); //자신만의 기능
    printf("-: 현재 위치의 노드 제거\n");
    printf("G: 현재 위치의 노드의 데이터 보여주기\n");
    printf("=(값): 현재 위치의 노드를 입력한 값으로 대체\n");
    printf("E: 연결리스트가 비어있는지 확인\n");
    printf("#: 현재 노드의 개수를 출력\n");
    printf("?(값): 입력한 값을 가지는 노드가 몇번째 노드인지 출력\n");
    printf("C: 연결리스트 초기화 (비우기)\n");
    printf("S(위치1)(위치2): 지정한 두 개의 노드의 위치를 서로 바꿈\n"); //자신만의 기능
    printf("D: 현재 위치의 노드 바로 옆에 복제\n"); //자신만의 기능
    printf("L: 연결리스트 출력 및 커서의 위치 표시\n");
    printf("&: 프로그램 종료\n\n"); //각 기능별 설명
    
    while(1){
        printf("명령어: ");
        scanf("%[^\n]s", inp); //입력받기. [^\n]를 붙이면 엔터를 제외한 모든것을 다 받는다 (공백 입력받기 가능)
        scanf("%*c"); //*을 넣어주면 문자를 입력받아 버린다 -> 오류 수정용
        
        if(inp[0] == '&'){
            break;
        }
        
        for(int i=0;i<=strlen(inp);i++){
            if(inp[i] == '+'){ //add
                add(&my_list, inp[i+1]);
                i++;
            }
            else if(inp[i] == '<'){ //traverse front
                traverse_front(&my_list);
            }
            else if(inp[i] == '>'){ //traverse rear
                traverse_rear(&my_list);
            }
            else if(inp[i] == 'N'){ // go right
                go_right(&my_list);
            }
            else if(inp[i] == 'G'){ //get data
                get_data(&my_list);
                default_print = 0;
            }
            else if(inp[i] == '-'){ //delete
                delete(&my_list);
            }
            else if(inp[i] == '='){ //replace
                replace(&my_list, inp[i+1]);
                i++;
            }
            else if(inp[i] == '#'){ //data count
                data_count(&my_list);
                default_print = 0;
            }
            else if(inp[i] == '?'){ //is member
                is_member(&my_list, inp[i+1]);
                i++;
            }
            else if(inp[i]-'0' >= 1 && inp[i]-'0' <= 9){ //traverse by number
                if(inp[i+1]-'0' >= 1 && inp[i+1]-'0' <= 9){ //two-digit
                    tmp = (inp[i]-'0')*10 + (inp[i+1]-'0'); //char->int
                    i++;
                }
                else{ //one-digit
                    tmp = inp[i]-'0'; //char->int
                }
                traverse_n(&my_list, tmp);
            }
            else if(inp[i] == 'C'){ //clear the list
                clear_the_list(&my_list);
            }
            else if(inp[i] == 'E'){ //is empty
                is_empty(&my_list);
                default_print = 0;
            }
            else if(inp[i] == '*'){ //add front
                my_list.position = my_list.head;
                add(&my_list, inp[i+1]);
                my_list.position = my_list.position->link;
                i++;
                my_list.cursor = 1;
            }
            else if(inp[i] == 'L'){ //print
                continue; //기본적으로 반복문마다 출력됨
            }
            else if(inp[i] == 'S'){ //swap
                swap(&my_list, inp[i+1], inp[i+2]);
                i=i+2;
            }
            else if(inp[i] == 'D'){ //duplicate
                duplicate(&my_list);
            }
            else if(inp[i] == '|'){ //traverse mid
                traverse_mid(&my_list);
            }
        }
        if(default_print==0){
            default_print = 1;
        }
        else{
            print(&my_list);
        }
    }
    return 0;
}
