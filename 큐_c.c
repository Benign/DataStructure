//자료구조 한옥영 교수님 7주차 실습과제
//큐 ADT 실습과제
//최종 작성일: 2020.06.19(금)
//2019312481 심규현

#include <stdio.h>
#include <string.h> //문자열 처리용

typedef struct queue{
    char data[21];
    int head;
    int tail;
}QUEUE;

void create(QUEUE* my_queue){
    for(int i=0;i<21;i++){
        my_queue->data[i] = '\0';
    }
    my_queue->head = -1;
    my_queue->tail = -1;
    return;
}

int is_full(QUEUE* my_queue){
    if(my_queue->tail+1==20) return 1; //배열의 마지막 칸에 원소가 있다면 1반환
    else return 0; //아니면 0반환
}

int is_empty(QUEUE* my_queue){
    if(my_queue->tail-my_queue->head == 0) return 1; //비어있으면 1반환
    else return 0; //아니면 0반환
}

void enqueue(QUEUE* my_queue, char data){
    int push=0; //얼마나 밀것인지 나타내는 변수
    if(is_full(my_queue)==1){ //큐의 마지막 공간이 이미 차있는 경우
        if(my_queue->data[0] == '\0'){ //앞에 공간이 있다면 == 모든 칸이 차있는 큐가 아니라면
            push = my_queue->head+1;
            for(int i=my_queue->head+1;i<=my_queue->tail;i++){ //head를 -1로 만들기 위해 head+1씩 모든 칸을 앞으로 당긴다.
                my_queue->data[i-push] = my_queue->data[i];
            }
            my_queue->head = -1; //head -1로 초기화
            my_queue->tail = my_queue->tail - push; //tail은 head를 민 만큼 같이 밀기
        }
        else{ //밀 공간도 없는 경우 = 진짜 다찬경우
            printf("ERROR: No space to Enqueue\n"); //enqueue 불가능
            return;
        }
    }
    my_queue->data[my_queue->tail+1] = data; //tail의 뒤에 추가
    my_queue->tail++; //tail 증가
    return;
}

char dequeue(QUEUE* my_queue){
    int tmp;
    tmp = my_queue->head;
    if(is_empty(my_queue)==1){ //원소가 배열에 없는 경우
        return 0;
    }
    else{
        tmp = my_queue->data[my_queue->head+1]; //제거하기 전 임시 저장
        my_queue->data[my_queue->head+1] = '\0'; //NULL 문자 넣어주기
        my_queue->head++;
    }
    return tmp; //제거한 원소 반환
}

void peek(QUEUE* my_queue){
    printf("%c\n", my_queue->data[my_queue->head+1]); //head+1에 있는 원소 출력
    return;
}

int data_count(QUEUE* my_queue){
    return (my_queue->tail - my_queue->head);
}

void print_head(QUEUE* my_queue){
    printf("%d\n", my_queue->head+2); //head 인덱스에는 원소 없음 --> +2
    return;
}

void print_tail(QUEUE* my_queue){
    printf("%d\n", my_queue->tail+1); //tail 인덱스에는 원소 있음 --> +1
    return;
}

int is_member(QUEUE* my_queue, char target){ //멤버인지 조사 //멤버 위치 출력할때 사용자의 편의를 우선적으로 고려하여 head+2의 값이 아닌 실제로 몇번째 원소인지를 출력하였습니다.
    char tmp_queue[20] = "";
    int tmp_head = my_queue->head; //head의 값 임시 저장 : enqueue, dequeue 중에 변할 수 있기 때문.
    int tmp_tail = my_queue->tail; //tail의 값 임시 저장
    int len = my_queue->tail - my_queue->head; //큐의 길이 저장
    int find = -1; //찾은 값의 위치를 저장할 변수
    for(int i = 0; i<len; i++){ //큐의 길이 동안
        tmp_queue[i] = dequeue(my_queue); //하나씩 dequeue하며 임시 큐에 저장
        if(tmp_queue[i] == target){ //원하는 원소가 있을 경우
            find = i+1; //find에 찾은 값의 위치 저장
        }
    }
    my_queue->head = -1;
    my_queue->tail = -1;
    for(int i = 0; i<=tmp_head; i++){ //기존의 head 위치까지 도달할동안
        enqueue(my_queue, '\0'); //null을 enqueue -> head와 tail이 바뀌지 않도록.
    }
    for(int i = 0; i<len; i++){
        enqueue(my_queue, tmp_queue[i]); //임시 큐에 저장된 값들을 다시 원래 큐에 enqueue
    }
    my_queue->head = tmp_head;
    my_queue->tail = tmp_tail;
    return find; //찾은 원소의 위치 반환. 못찾았으면 초기화 한 수인 -1 반환.
}

void replace(QUEUE* my_queue, char data){
    if(my_queue->tail-my_queue->head == 0){ //원소 없는 배열은 대체 불가능
        printf("ERROR: no element to replace.\n");
    }
    else{
        my_queue->data[my_queue->tail] = data; //가장 위의 원소 값 바꾸기
    }
    return;
}

void clear_queue(QUEUE* my_queue){ //큐 비우기
    int i;
    int length = my_queue->tail - my_queue->head;
    for(i=0;i<length;i++){
        dequeue(my_queue); //dequeue을 원소 개수만큼 실행
    } //큐 비우기
    my_queue->head = -1; //head 초기화
    my_queue->tail = -1; //tail 초기화
    return;
}

void print(QUEUE* my_queue){
    char tmp_queue[20]="";
    int tmp_head = my_queue->head; //head의 값 임시 저장 : enqueue, dequeue 중에 변할 수 있기 때문.
    int tmp_tail = my_queue->tail; //tail의 값 임시 저장
    int len = my_queue->tail - my_queue->head; //큐의 길이 저장
    if(is_empty(my_queue)==1){ //비어있는 큐이면
        printf("empty queue\n");
    }
    else{
        for(int i = 0; i<len; i++){
            tmp_queue[i] = dequeue(my_queue); //임시 큐에 저장하며 출력
            printf("%c ", tmp_queue[i]);
        }
        my_queue->head = -1;
        my_queue->tail = -1;
        for(int i = 0; i<=tmp_head; i++){ //기존의 head 위치까지 도달할동안
            enqueue(my_queue, '\0'); //null을 enqueue -> head와 tail이 바뀌지 않도록.
        }
        for(int i = 0; i<len; i++){
            enqueue(my_queue, tmp_queue[i]); //임시 큐에 저장된 값들을 다시 원래 큐에 enqueue
        }
        printf("\n");
    }
    my_queue->head = tmp_head;
    my_queue->tail = tmp_tail;
    return;
}

void duplicate(QUEUE* my_queue){ //추가기능 1
    if(my_queue->tail-my_queue->head == 0){ //원소 없는 배열은 복제도 불가능
        printf("ERROR: no element to duplicate.\n");
    }
    else{
        enqueue(my_queue, my_queue->data[my_queue->tail]); //tail 위치의 원소를 삽입 = 복제
    }
    return;
}

void move_back(QUEUE* my_queue){ //추가기능 2
    char tmp;
    tmp = dequeue(my_queue); //앞의 원소를 dequeue를 통해 임시 변수에 저장한 다음
    enqueue(my_queue, tmp); //뒤에 다시 enqueue
    return;
}

void delete(QUEUE* my_queue, QUEUE* tmp_queue, char target){
    char tmp;
    int count=0;
    int tmp_head = my_queue->head;
    int tmp_tail = my_queue->tail;
    int len = my_queue->tail - my_queue->head;
    if(is_empty(my_queue)==1){ //비어있는 큐이면
        printf("ERROR: no element to delete\n");
    }
    else{
        for(int i = 0, j = 0; i<len; i++){
            tmp = dequeue(my_queue); //임시로 tmp에 저장 (검사해보기 위해서)
            if(tmp == target){ //제거 대상이면
                count++; //count만 증가하고 저장 안함
            }
            else{ // 제거 대상이 아니면
                enqueue(tmp_queue, tmp); //임시 큐에 저장
                j++; //저장용 인덱스 증가
            }
        }
        my_queue->head = -1;
        my_queue->tail = -1;
        for(int i = 0; i<=tmp_head; i++){
            enqueue(my_queue, '\0');
        }
        for(int i = 0; i<len-count; i++){
            enqueue(my_queue, dequeue(tmp_queue)); //임시 큐에 저장된 값들을 다시 원래 큐에 enqueue
        }
    }
    my_queue->head = tmp_head;
    my_queue->tail = tmp_tail-count;
    clear_queue(tmp_queue);
    return;
}


int main(void){ //메인 함수
    QUEUE my_queue;
    QUEUE tmp_queue;
    int default_print = 1;
    char inp[50]=""; //입력 받기 용 문자열 + ""로 초기화하기
    
    printf("명령문 안내\n");
    printf("+(원소의 값): 뒤에 원소 추가\n");
    printf("-: 가장 앞의 원소 제거\n");
    printf("(숫자)-: 숫자 만큼의 원소 앞에서 제거\n");
    printf("P: tail의 원소의 데이터 보여주기\n");
    printf("H: head가 큐의 몇번째 칸에 들어있는지 보여주기\n");
    printf("T: tail이 큐의 몇번째 칸에 들어있는지 보여주기\n");
    printf("=(값): tail의 원소를 입력한 값으로 대체\n");
    printf("#: 큐의 원소 개수 출력\n");
    printf("C: 큐 비우기\n");
    printf("E: 큐 비었는지 확인\n");
    printf("F: 큐의 마지막 칸이 차있는지 확인\n");
    printf("?(값): 큐에 해당 값을 가지는 원소가 존재하는지 확인\n");
    printf("!(값): 큐 안의 해당 값을 가지는 원소를 모두 제거\n");
    printf("D: tail 원소 바로 뒤에 추가\n");
    printf("B: 현재 큐의 맨 앞 원소를 맨 뒤로 이동\n");
    printf("L: 큐 출력 및 커서의 위치 표시\n");
    printf("&: 프로그램 종료\n\n"); //각 기능별 설명
    
    create(&my_queue);
    create(&tmp_queue);
    
    while(1){
        printf("명령어: ");
        scanf("%[^\n]s", inp); //입력받기. [^\n]를 붙이면 엔터를 제외한 모든것을 다 받는다 (공백 입력받기 가능)
        scanf("%*c"); //*을 넣어주면 문자를 입력받아 버린다 -> 오류 수정용
        
        if(inp[0] == '&'){
            break;
        }
        
        for(int i=0;i<=strlen(inp);i++){
            if(inp[i] == '+'){ //enqueue
                enqueue(&my_queue, inp[i+1]); //+뒤에 문자가 오므로 바로 뒤의 문자를 배열에 추가
                i++; //이미 +의 한칸 뒤까지 다 사용했으므로 그 뒤로 이동
            }
            else if(inp[i] == '-'){ //dequeue
                if(is_empty(&my_queue)==1){ //비어있는 큐인 경우
                    printf("ERROR: nothing to dequeue.\n");
                }
                else{
                    printf("Return: %c\n", dequeue(&my_queue));
                }
            }
            else if(inp[i]-'0' >= 1 && inp[i]-'0' <= 9){ // 숫자로 dequeue 하기
                int tmp;
                if(inp[i+1]-'0' >= 1 && inp[i+1]-'0' <= 9){ //two-digit
                    if(inp[i+2]=='-'){
                        tmp = (inp[i]-'0')*10 + (inp[i+1]-'0'); //char->int
                        i=i+2;
                        printf("Return: ");
                        for(int j=1;j<=tmp;j++){ //숫자 만큼 dequeue 해주기
                            printf("%c ",dequeue(&my_queue));
                        }
                        printf("\n");
                    }
                    else{ // - 를 못찾았다면
                        printf("잘못된 명령입니다\n");
                    }
                }
                else{ //one-digit
                    if(inp[i+1]=='-'){
                        tmp = inp[i]-'0'; //char->int
                        i++;
                        printf("Return: ");
                        for(int j=1;j<=tmp;j++){
                            printf("%c ",dequeue(&my_queue));
                        }
                        printf("\n");
                    }
                    else{ // - 를 못찾았다면
                        printf("잘못된 명령입니다\n");
                    }
                }
            }
            else if(inp[i] == 'P'){ //peek
                peek(&my_queue);
                default_print = 0;
            }
            else if(inp[i] == '='){ //replace
                replace(&my_queue, inp[i+1]);
                i++;
            }
            else if(inp[i] == 'C'){ //clear queue
                clear_queue(&my_queue);
            }
            else if(inp[i] == 'L'){ //print
                continue; //어차피 나가면 출력이 실행됨. 중복 출력을 피하고자 continue문 입력.
            }
            else if(inp[i] == '#'){ //element count
                printf("%d\n",data_count(&my_queue));
                default_print = 0;
            }
            else if(inp[i] == 'H'){ //print head
                print_head(&my_queue);
                default_print = 0;
            }
            else if(inp[i] == 'T'){ //print tail
                print_tail(&my_queue);
                default_print = 0;
            }
            else if(inp[i] == 'F'){ //is full
                if(is_full(&my_queue)==0){
                    printf("False\n");
                }
                else if(is_full(&my_queue)==1){
                    printf("True\n");
                }
                default_print = 0;
            }
            else if(inp[i] == 'E'){ //is empty
                if(is_empty(&my_queue)==0){
                    printf("False\n");
                }
                else if(is_empty(&my_queue)==1){
                    printf("True\n");
                }
                default_print = 0;
            }
            else if(inp[i] == '?'){ //is member
                printf("%d\n", is_member(&my_queue, inp[i+1]));
                i++;
                default_print = 0;
            }
            else if(inp[i] == 'D'){ //duplicate
                duplicate(&my_queue);
            }
            else if(inp[i] == 'B'){ //move_back
                move_back(&my_queue);
            }
            else if(inp[i] == '!'){ //delete
                delete(&my_queue, &tmp_queue, inp[i+1]);
                i++;
            }
        }
        
        if(default_print == 1){
            print(&my_queue);
        }
        else{
            default_print = 1;
        }
        
    }
    return 0;
}
