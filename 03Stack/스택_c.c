//자료구조 한옥영 교수님 6주차 실습과제
//스택 ADT 실습과제
//최종 작성일: 2020.06.18(목)
//2019312481 심규현

#include <stdio.h>
#include <string.h> //문자열 처리용

typedef struct stack{
    char data[21];
    int top;
}STACK;

void create(STACK* my_stack){
    for(int i=0;i<21;i++){
        my_stack->data[i] = '\0';
    }
    my_stack->top = -1;
    return;
}

int is_full(STACK* my_stack){
    if(strlen(my_stack->data)>=20) return 1; //다 차있으면 1반환
    else return 0; //아니면 0반환
}

int is_empty(STACK* my_stack){ //추가기능 1
    if(strlen(my_stack->data)==0) return 1; //비어있으면 1반환
    else return 0; //아니면 0반환
}

void push(STACK* my_stack, char data){
    if(is_full(my_stack)==1){ //스택 크기를 초과해서 저장할 수 없음
        printf("ERROR: stack is full.\n"); //오류 알림
        return;
    }
    else{
        my_stack->data[(my_stack->top)+1] = data; //가장 위에 추가
        my_stack->top++;
    }
    return;
}

char pop(STACK* my_stack){
    int tmp;
    tmp = my_stack->top;
    if(is_empty(my_stack)==1){ //원소가 배열에 없는 경우
        return 0;
    }
    else{
        tmp = my_stack->data[my_stack->top];
        my_stack->data[my_stack->top] = '\0'; //맨끝에 NULL 문자 넣어주기
        if(strlen(my_stack->data)==0){ //하나 남은 원소를 제거한 경우
            my_stack->top = -1; //top 초기화
        }
        else{
            my_stack->top--; // top 감소
        }
    }
    return tmp; //제거한 원소 반환
}

void peek(STACK* my_stack){
    printf("%c\n", my_stack->data[my_stack->top]); //top에 있는 원소 출력
    return;
}

void element_count(STACK* my_stack){
    printf("%d\n", (int)strlen(my_stack->data)); //원소의 개수 출력
    return;
}

void print_top(STACK* my_stack){
    printf("( %d, %c )\n", (int)strlen(my_stack->data), my_stack->data[my_stack->top]); //몇번째 원소가 top인지와 top의 값 출력
    return;
}

void is_member(STACK* my_stack, char target){ //멤버인지 조사
    STACK tmp_stack; //구조체 활용
    create(&tmp_stack);
    int len = (int)strlen(my_stack->data); //스택의 크기 저장
    int find = 0; //찾으면 1로 바꿀 변수
    for(int i = 0; i<len; i++){
        push(&tmp_stack, pop(my_stack)); //하나씩 pop하며 임시 스택에 저장
        if(tmp_stack.data[tmp_stack.top] == target){ //원하는 원소가 있을 경우
            find = 1; //찾았다고 표시
        }
    }
    for(int i = len-1; i>=0; i--){
        push(my_stack, pop(&tmp_stack)); //다시 원래의 스택에 값 넣어주기
    }
    if(find==1){ //찾았으면
        printf("True\n");
    }
    else if(find==0){ //없었다면
        printf("False\n");
    }
    return;
}

void replace(STACK* my_stack, char data){
    my_stack->data[my_stack->top] = data; //가장 위의 원소 값 바꾸기
    return;
}

void clear_stack(STACK* my_stack){ //스택 비우기
    int i;
    int length = (int)strlen(my_stack->data);
    for(i=0;i<length;i++){
        pop(my_stack); //pop을 원소 개수만큼 실행
    } //스택 비우기
    my_stack->top = -1; //top 초기화
    return;
}

void print(STACK* my_stack){
    STACK tmp_stack;
    create(&tmp_stack);
    int len = (int)strlen(my_stack->data);
    char tmp_data;
    if(len==0){ //비어있는 스택이면
        printf("empty stack\n");
    }
    else{
        for(int i = 0; i<len; i++){
            push(&tmp_stack, pop(my_stack)); //임시 스택에 역순으로 저장
        }
        for(int i = len-1; i>=0; i--){
            tmp_data = pop(&tmp_stack);
            printf("%c ", tmp_data); //임시 스택을 다시 역순으로 뽑아가며 출력
            push(my_stack, tmp_data); //출력 후 그 값 원 스택에 다시 저장
        }
        printf("\n");
        printf("현재 top 원소는 %d번째 원소입니다.\n", (my_stack->top)+1); //top 위치 알림. 배열식 주소 (0부터) -> 사용자가 보는 위치 (1부터) 변환
    }
    return;
}

void duplicate(STACK* my_stack){ //추가기능 2
    if(strlen(my_stack->data) == 0){ //원소 없는 배열은 복제도 불가능
        printf("ERROR: no element to duplicate.\n");
    }
    else{
        push(my_stack, my_stack->data[my_stack->top]); //현 위치의 원소를 삽입 = 복제
    }
    return;
}

void reverse(STACK* my_stack, STACK* reverse_stack){ //추가기능 3
    int len = (int)strlen(my_stack->data);
    clear_stack(reverse_stack);
    for(int i = 0; i<len; i++){
        push(reverse_stack, pop(my_stack)); //역순으로 임시 스택에 저장
    }
    my_stack->top = reverse_stack->top;
    return;
}

int main(void){ //메인 함수
    int default_print = 1;
    char inp[50]=""; //입력 받기 용 문자열 + ""로 초기화하기
    STACK my_stack;
    STACK reverse_stack;
    create(&my_stack);
    create(&reverse_stack);
    
    printf("명령문 안내\n");
    printf("+(원소의 값): 원소 추가\n");
    printf("-: (가장 끝의) 원소 제거\n");
    printf("(숫자)-: 숫자 만큼의 원소 제거\n");
    printf("P: top의 원소의 데이터 보여주기\n");
    printf("T: top의 원소의 데이터와 현재 스택의 높이(크기) 보여주기\n");
    printf("=(값): top의 원소를 입력한 값으로 대체\n");
    printf("#: 스택의 원소 개수 출력\n");
    printf("C: 스택 비우기\n");
    printf("E: 스택 비었는지 확인\n");
    printf("F: 스택 꽉 찼는지 확인\n");
    printf("?(값): 스택에 해당 값을 가지는 원소가 존재하는지 확인\n");
    printf("D: top 원소 바로 뒤에 추가\n");
    printf("R: 현재 스택의 순서 뒤바꾸기\n");
    printf("L: 스택 출력 및 커서의 위치 표시\n");
    printf("&: 프로그램 종료\n\n"); //각 기능별 설명
    
    while(1){
        printf("명령어: ");
        scanf("%[^\n]s", inp); //입력받기. [^\n]를 붙이면 엔터를 제외한 모든것을 다 받는다 (공백 입력받기 가능)
        scanf("%*c"); //*을 넣어주면 문자를 입력받아 버린다 -> 오류 수정용
        
        if(inp[0] == '&'){
            break;
        }
        
        for(int i=0;i<=strlen(inp);i++){
            if(inp[i] == '+'){ //push
                push(&my_stack, inp[i+1]); //+뒤에 문자가 오므로 바로 뒤의 문자를 배열에 추가
                i++; //이미 +의 한칸 뒤까지 다 사용했으므로 그 뒤로 이동
            }
            else if(inp[i] == '-'){ //pop
                if(is_empty(&my_stack)==1){ //비어있는 스택인 경우
                    printf("ERROR: nothing to pop.\n");
                }
                else{
                    printf("Return: %c\n", pop(&my_stack));
                }
            }
            else if(inp[i]-'0' >= 1 && inp[i]-'0' <= 9){ // 숫자로 pop 하기
                int tmp;
                if(inp[i+1]-'0' >= 1 && inp[i+1]-'0' <= 9){ //two-digit
                    if(inp[i+2]=='-'){
                        tmp = (inp[i]-'0')*10 + (inp[i+1]-'0'); //char->int
                        i=i+2;
                        printf("Return: ");
                        for(int j=1;j<=tmp;j++){ //숫자 만큼 pop 해주기
                            printf("%c ",pop(&my_stack));
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
                            printf("%c ", pop(&my_stack));
                        }
                        printf("\n");
                    }
                    else{ // - 를 못찾았다면
                        printf("잘못된 명령입니다\n");
                    }
                }
            }
            else if(inp[i] == 'P'){ //peek
                peek(&my_stack);
                default_print = 0;
            }
            else if(inp[i] == '='){ //replace
                replace(&my_stack, inp[i+1]);
                i++;
            }
            else if(inp[i] == 'C'){ //clear stack
                clear_stack(&my_stack);
            }
            else if(inp[i] == 'L'){ //print
                continue; //어차피 나가면 출력이 실행됨. 중복 출력을 피하고자 continue문 입력.
            }
            else if(inp[i] == '#'){ //element count
                element_count(&my_stack);
                default_print = 0;
            }
            else if(inp[i] == 'T'){ //print top
                print_top(&my_stack);
                default_print = 0;
            }
            else if(inp[i] == 'F'){ //is full
                if(is_full(&my_stack)==0){
                    printf("False\n");
                }
                else if(is_full(&my_stack)==1){
                    printf("True\n");
                }
                default_print = 0;
            }
            else if(inp[i] == 'E'){ //is empty
                if(is_empty(&my_stack)==0){
                    printf("False\n");
                }
                else if(is_empty(&my_stack)==1){
                    printf("True\n");
                }
                default_print = 0;
            }
            else if(inp[i] == '?'){ //is member
                is_member(&my_stack, inp[i+1]);
                i++;
                default_print = 0;
            }
            else if(inp[i] == 'D'){ //duplicate
                duplicate(&my_stack);
            }
            
            else if(inp[i] == 'R'){ //reverse
                reverse(&my_stack, &reverse_stack);
                my_stack = reverse_stack;
            }
        }
        
        if(default_print == 1){
            print(&my_stack);
        }
        else{
            default_print = 1;
        }
        
    }
    return 0;
}
