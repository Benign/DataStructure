//자료구조 한옥영 교수님 10주차 도전과제 & 도전의 도전과제
//이진 탐색 트리 ADT 도전과제
//최종 작성일: 2020.05.20(수)
//2019312481 심규현

//단순히 MAX HEAP -> BST가 아니라, 설명 영상에서 언급하셨던 대로 BST-> MAX or MIN HEAP 역시 구현해보았습니다.
//추가로, MIN HEAP -> BST도 구현되어 있습니다.
//입력과 삭제는 MAX HEAP, MIN HEAP, BST 세 자료구조 모두 가능합니다.

#include <stdio.h>
#include <stdlib.h>
#include <string.h> //문자열 처리용

typedef struct Heap{
    int heap[100];
    int size;
} HEAP;

typedef struct Node{
    int data;
    struct Node* left;
    struct Node* right;
    int height;
} NODE;

typedef struct Binary_Search_Tree{
    NODE* root;
} BST;

void addMaxHeap(HEAP* my_HEAP, int data){
    int i;
    my_HEAP->size++;
    i = my_HEAP->size;
    while((i!=1) && (data > my_HEAP->heap[i/2])){ //루트가 아니고 들어온 값이 부모노드의 값보다 큰 동안
        my_HEAP->heap[i] = my_HEAP->heap[i/2]; //부모노드의 값을 현재 위치에 저장 (입력받은 값은 나중에 한번에 목표 위치에 대입)
        i = i/2;
    }
    my_HEAP->heap[i] = data; //while문이 끝나면 heap의 조건을 만족하는 위치 -> 대입
    return;
}

int deleteMaxHeap(HEAP* my_HEAP){
    int parent = 1;
    int child = 2;
    int data = my_HEAP->heap[1]; //현재 루트노드의 값 저장
    int temp = my_HEAP->heap[my_HEAP->size]; //마지막 노드의 값 저장
    my_HEAP->size--;
    while(child <= my_HEAP->size){ //마지막 노드의 값을 Heap의 조건을 만족하도록 재배열 (루트부터 시작)
        if((child < my_HEAP->size) && (my_HEAP->heap[child] < my_HEAP->heap[child+1])){ //우측 자식이 좌측 자식보다 크다면
            child = child+1; //우측자식 선택
        }
        if(temp >= my_HEAP->heap[child]){ //temp의 값이 현재 자식노드의 값보다 크다면 Heap의 조건 만족
            break;
        }
        else{ //Heap의 조건 만족이 안된경우
            my_HEAP->heap[parent] = my_HEAP->heap[child]; //부모노드의 값에 자식들 중 더 큰 값 대입
            parent = child;
            child = child*2; //Level 1 내려가기
        }
    }
    my_HEAP->heap[parent] = temp;
    return data;
}

void addMinHeap(HEAP* my_HEAP, int data){
    int i;
    my_HEAP->size++;
    i = my_HEAP->size;
    while((i!=1) && (data < my_HEAP->heap[i/2])){ //루트가 아니고 들어온 값이 부모노드의 값보다 작은 동안
        my_HEAP->heap[i] = my_HEAP->heap[i/2]; //부모노드의 값을 현재 위치에 저장 (입력받은 값은 나중에 한번에 목표 위치에 대입)
        i = i/2;
    }
    my_HEAP->heap[i] = data; //while문이 끝나면 heap의 조건을 만족하는 위치 -> 대입
    return;
}

int deleteMinHeap(HEAP* my_HEAP){
    int parent = 1;
    int child = 2;
    int data = my_HEAP->heap[1]; //현재 루트노드의 값 저장
    int temp = my_HEAP->heap[my_HEAP->size]; //마지막 노드의 값 저장
    my_HEAP->size--;
    while(child <= my_HEAP->size){ //마지막 노드의 값을 Heap의 조건을 만족하도록 재배열 (루트부터 시작)
        if((child < my_HEAP->size) && (my_HEAP->heap[child] > my_HEAP->heap[child+1])){ //우측 자식이 좌측 자식보다 작다면
            child = child+1; //우측자식 선택
        }
        if(temp <= my_HEAP->heap[child]){ //temp의 값이 현재 자식노드의 값보다 작다면 Heap의 조건 만족
            break;
        }
        else{ //Heap의 조건 만족이 안된경우
            my_HEAP->heap[parent] = my_HEAP->heap[child]; //부모노드의 값에 자식들 중 더 작은 값 대입
            parent = child;
            child = child*2; //Level 1 내려가기
        }
    }
    my_HEAP->heap[parent] = temp;
    return data;
}

void printHeap(HEAP* my_HEAP, int i){
    if(my_HEAP->size == 0){
        printf("Heap is Empty.");
        return;
    }
    printf("%d", my_HEAP->heap[i]);
    if((i*2 > my_HEAP->size) && ((i*2)+1 > my_HEAP->size)){
        return;
    }
    printf("(");
    if(i*2 <= my_HEAP->size){
        printHeap(my_HEAP, (i*2));
    }
    printf(",");
    if((i*2)+1 <= my_HEAP->size){
        printHeap(my_HEAP, ((i*2)+1));
    }
    printf(")");
    return;
}

void CreateRoot(BST* my_BST, int data){
    if(my_BST->root != NULL){
        printf("ERROR: Root Already Exists.\n");
    }
    else{
        NODE* rootNode = (NODE*)malloc(sizeof(NODE));
        rootNode->data = data;
        rootNode->left = NULL;
        rootNode->right = NULL;
        rootNode->height = 0;
        my_BST->root = rootNode;
    }
    return;
}

NODE* searchValue(BST* my_BST, int target, int print){
    NODE* position;
    BST sub_tree;
    position = my_BST->root;
    if(position->data == target){
        return position;
    }
    else if(position->data > target){ //목표보다 크면 왼쪽으로 이동
        if(my_BST->root->left == NULL){ //비어있다면
            return NULL;
        }
        sub_tree.root = my_BST->root->left;
        if(print == 1){
            printf(" > Left");
        }
        position = searchValue(&sub_tree, target, print);
    }
    else if(position->data < target){ //목표보다 작으면 오른쪽으로 이동
        if(my_BST->root->right == NULL){ //비어있다면
            return NULL;
        }
        sub_tree.root = my_BST->root->right;
        if(print == 1){
            printf(" > Right");
        }
        position = searchValue(&sub_tree, target, print);
    }
    return position;
}

int isNode(BST* my_BST, int target){
    NODE* tmp;
    tmp = searchValue(my_BST, target, 0);
    if(tmp == NULL){
        return 0;
    }
    else{
        return 1;
    }
}

void InsertNode(BST* my_BST, int data){
    int done = 0;
    int count = 0;
    if(my_BST->root == NULL){
        printf("ERROR: Tree Not Found.\n");
        return;
    }
    if(isNode(my_BST, data) == 1){ //해당 값을 가진 노드가 이미 존재
        printf("ERROR: Binary Search Tree Cannot Have 2 Nodes With Same Value.\n");
        return;
    }
    NODE * current;
    current = my_BST->root;
    while(done == 0){
        if(current->data > data){
            if(current->left == NULL){ //current->left에 노드 생성
                done = 1; //left
            }
            else{
                current = current->left;
            }
        }
        else if(current->data < data){
            if(current->right == NULL){ //current->right에 노드 생성
                done = 2; //right
            }
            else{
                current = current->right;
            }
        }
        count++;
    }
    NODE * newNode = (NODE*)malloc(sizeof(NODE));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    newNode->height = count;
    if(done == 1){ // left
        current->left = newNode;
    }
    else if(done == 2){ //right
        current->right = newNode;
    }
    return;
}

void printTree(BST* my_BST){
    if(my_BST->root == NULL){
        printf("Tree is Empty.");
        return;
    }
    BST left_tree, right_tree;
    left_tree.root = my_BST->root->left;
    right_tree.root = my_BST->root->right;
    printf("%d", my_BST->root->data);
    if(left_tree.root == NULL && right_tree.root == NULL){
        return;
    }
    printf("(");
    if(left_tree.root != NULL){
        printTree(&left_tree);
    }
    printf(",");
    if(right_tree.root != NULL){
        printTree(&right_tree);
    }
    printf(")");
    return;
}

NODE* findParent(BST* my_BST, int target){
    if((my_BST->root->data) == target){
        return NULL;
    }
    BST left_tree, right_tree;
    NODE* position;
    NODE* tmp;
    left_tree.root = my_BST->root->left;
    right_tree.root = my_BST->root->right;
    position = my_BST->root;
    if((position->left == NULL) && (position->right == NULL)){
        return NULL;
    }
    if((position->left != NULL) && (position->left->data) == target){ //왼쪽에 자식
        return position;
    }
    else if((position->right != NULL) && (position->right->data) == target){ //오른쪽에 자식
        return position;
    }
    else{
        if(position->right == NULL){
            tmp = findParent(&left_tree, target);
            return tmp;
        }
        else if(position->left == NULL){
            tmp = findParent(&right_tree, target);
            return tmp;
        }
        else{
            tmp = findParent(&left_tree, target);
            if(tmp==NULL){
                tmp = findParent(&right_tree, target);
            }
            return tmp;
        }
    }
}

int deleteNode(BST* my_BST, NODE* node, char mode){ //mode가 L이면 좌-부트리의 Right-Most Node, R이면 우-부트리의 Left-Most Node
    int root = 0;
    int tmp;
    if(node==NULL){
        printf("ERROR: Invalid Input.\n");
        return 0;
    }
    if(node->data==my_BST->root->data){
        root = 1;
    }
    NODE* parent;
    parent = NULL;
    if(root == 0){
        parent = findParent(my_BST, node->data);
    }
    if(node->left == NULL && node->right == NULL){ //leaf node
        if(root == 0){
            if(parent->left == node){
                parent->left = NULL;
                tmp = node->data;
                free(node);
                return tmp;
            }
            else if(parent->right == node){
                parent->right = NULL;
                tmp = node->data;
                free(node);
                return tmp;
            }
        }
        else if(root == 1){ //유일한 노드
            tmp = node->data;
            free(node);
            my_BST->root = NULL;
            return tmp;
        }
    }
    else if(node->left == NULL){ //right는 null이 아님 -> right가 유일한 자식
        if(root == 0){
            if(parent->left == node){
                tmp = node->data;
                parent->left = node->right;
                free(node);
                return tmp;
            }
            else if(parent->right == node){
                tmp = node->data;
                parent->right = node->right;
                free(node);
                return tmp;
            }
        }
        else if(root == 1){ //유일한 노드
            tmp = node->data;
            my_BST->root = node->right;
            free(node);
            return tmp;
        }
    }
    else if(node->right == NULL){ //left는 null이 아님 -> left가 유일한 자식
        if(root == 0){
            if(parent->left == node){
                tmp = node->data;
                parent->left = node->left;
                free(node);
                return tmp;
            }
            else if(parent->right == node){
                tmp = node->data;
                parent->right = node->left;
                free(node);
                return tmp;
            }
        }
        else if(root == 1){ //유일한 노드
            tmp = node->data;
            my_BST->root = node->left;
            free(node);
            return tmp;
        }
    }
    else{ //자식노드 두개 다 존재
        int temp;
        NODE* heir; //후계자
        if(mode == 'L'){ //좌부트리에서 선택
            heir = node->left;
            while(heir->right != NULL){ //Most right Node를 찾아서
                heir = heir->right;
            }
            temp = node->data;
            node->data = heir->data; //data 가져온뒤
            heir->data = temp;
            deleteNode(my_BST, heir, 'L'); //후계자 위치의 노드 삭제
        }
        else if(mode == 'R'){ //우부트리에서 선택
            heir = node->right;
            while(heir->left != NULL){ //Most left Node를 찾아서
                heir = heir->left;
            }
            temp = node->data;
            node->data = heir->data; //data 가져온뒤
            heir->data = temp;
            deleteNode(my_BST, heir, 'R');
        }
        else{
            printf("ERROR: Cannot Choose Heir.\n");
            return 0;
        }
    }
    return 0;
}

void clearTree(BST* my_BST){
    NODE* left_node = my_BST->root;
    while(my_BST->root != NULL){
        left_node = my_BST->root;
        while(left_node->left!=NULL){
            left_node = left_node->left;
        }
        deleteNode(my_BST, left_node, 'L');
    }
    return;
}

void HeapToBST(HEAP* my_heap, BST* my_BST){ //max heap 출력 결과 편향트리의 형태로 나타남.
                                            //사실 생각해보면 MAX HEAP에서 나온다는 것은
                                            //가장 큰 원소이므로 항상 왼쪽 자식노드에 들어가게 되므로 당연하다고 볼 수도 있다...
    int i;
    int size;
    size = my_heap->size;
    clearTree(my_BST);
    for(i=1;i<=size;i++){
        if(i==1){
            CreateRoot(my_BST, deleteMaxHeap(my_heap));
        }
        else{
            InsertNode(my_BST, deleteMaxHeap(my_heap));
        }
    }
    return;
}

void BSTToMaxHeap(BST* my_BST, HEAP* my_heap){
    NODE* left_node = my_BST->root;
    while(my_BST->root != NULL){
        left_node = my_BST->root;
        while(left_node->left!=NULL){
            left_node = left_node->left;
        }
        addMaxHeap(my_heap, deleteNode(my_BST, left_node, 'L'));
    }
    return;
}

void BSTToMinHeap(BST* my_BST, HEAP* my_heap){
    NODE* left_node = my_BST->root;
    while(my_BST->root != NULL){
        left_node = my_BST->root;
        while(left_node->left!=NULL){
            left_node = left_node->left;
        }
        addMinHeap(my_heap, deleteNode(my_BST, left_node, 'L'));
    }
    return;
}


int main(void){ //메인 함수
    BST my_BST={NULL};
    HEAP max_heap = {};
    HEAP min_heap = {};
    max_heap.size = min_heap.size = 0; //초기화
    int default_print = 1;
    char input_mode[10] = "";
    char inpmode = 'M';
    char heir_mode[10] = "";
    char heir = 'L';
    char inp[50] = ""; //입력 받기 용 문자열 + ""로 초기화하기
    
    printf("입력할 자료구조를 선택하세요.\n");
    printf("MAX_HEAP 선택: M\n");
    printf("MIN_HEAP 선택: N\n");
    printf("BST 선택: B\n");
    printf("기본설정: MAX_HEAP\n");
    scanf("%s", input_mode);
    
    if(input_mode[0] == 'M'){
        inpmode = 'M';
    }
    else if(input_mode[0] == 'B'){
        inpmode = 'B';
    }
    else if(input_mode[0] == 'N'){
        inpmode = 'N';
    }
    else{
        printf("기본설정을 따릅니다.\n");
    }
    
    if(inpmode=='B'){
        printf("좌-부트리에서 후계자 선택: L\n");
        printf("우-부트리에서 후계자 선택: R\n");
        printf("기본설정: 좌-부트리\n");
        scanf("%s", heir_mode);
        
        if(heir_mode[0] == 'L'){
            heir = 'L';
        }
        else if(heir_mode[0] == 'R'){
            heir = 'R';
        }
        else{
            printf("기본설정을 따릅니다.\n");
        }
    }
    printf("HEAP 명령문 안내\n");
    printf("   +값: 힙의 값 추가\n");
    printf("   -: 힙의 루트 삭제 삭제\n");
    printf("   P: 힙 출력\n");
    printf("   B: BST로 변환\n\n\n");
    
    printf("BST 명령문 안내\n");
    printf("   +값: 이진 트리 탐색 트리의 노드 추가\n");
    printf("   -값: 해당 노드 삭제\n");
    printf("   P: 트리 출력\n");
    printf("   M: MAX_HEAP으로 변환\n");
    printf("   N: MIN_HEAP으로 변환\n");
    printf("   C: 트리 초기화\n\n");
    printf("&: 프로그램 종료\n\n"); //각 기능별 설명
    
    scanf("%*c");

    while(1){
        printf("명령어: ");
        scanf("%[^\n]s", inp); //입력받기. [^\n]를 붙이면 엔터를 제외한 모든것을 다 받는다 (공백 입력받기 가능)
        scanf("%*c"); //*을 넣어주면 문자를 입력받아 버린다 -> 오류 수정용
        
        if(inp[0] == '&'){
            break;
        }
        
        for(int i=0;i<=strlen(inp);i++){
            if(inp[i] == '+'){
                if(inp[i+1]-'0' >= 0 && inp[i+1]-'0' <= 9){ // 숫자 입력 받기
                    int tmp;
                    if(inp[i+2]-'0' >= 0 && inp[i+2]-'0' <= 9){ //two-digit
                        if(inp[i+3]=='\0'){
                            tmp = (inp[i+1]-'0')*10 + (inp[i+2]-'0'); //char->int
                            i=i+2;
                            if(inpmode=='M'){
                                addMaxHeap(&max_heap, tmp);
                            }
                            if(inpmode=='N'){
                                addMinHeap(&min_heap, tmp);
                            }
                            if(inpmode=='B'){
                                if(my_BST.root ==  NULL){
                                    CreateRoot(&my_BST, tmp);
                                }
                                else InsertNode(&my_BST, tmp);
                            }
                        }
                        else{
                            printf("ERROR: Only One & Two Digit Numbers Are Allowed.\n");
                        }
                    }
                    else{ //one-digit
                        if(inp[i+2]=='\0'){
                            tmp = inp[i+1]-'0'; //char->int
                            i++;
                            if(inpmode=='M'){
                                addMaxHeap(&max_heap, tmp);
                            }
                            if(inpmode=='N'){
                                addMinHeap(&min_heap, tmp);
                            }
                            if(inpmode=='B'){
                                if(my_BST.root ==  NULL){
                                    CreateRoot(&my_BST, tmp);
                                }
                                else InsertNode(&my_BST, tmp);
                            }
                        }
                        else{
                            printf("ERROR: Invalid Input.\n");
                        }
                    }
                }
            }
            else if(inp[i] == 'P'){
                continue; //어차피 나가면 출력이 실행됨. 중복 출력을 피하고자 continue문 입력.
            }
            else if(inp[i] == 'B'){ //BST로 변환
                if(inpmode == 'B'){
                    printf("ERROR: Heap Not Found.\n");
                }
                else{
                    if(inpmode == 'M'){
                        HeapToBST(&max_heap, &my_BST);
                    }
                    else if(inpmode == 'N'){
                        HeapToBST(&min_heap, &my_BST);
                    }
                    inpmode = 'B';
                }
            }
            else if(inp[i] == 'M'){ //Max heap으로 변환
                if(inpmode == 'M' || inpmode == 'N'){
                    printf("ERROR: Binary Search Tree Not Found.\n");
                }
                else{
                    BSTToMaxHeap(&my_BST, &max_heap);
                    inpmode = 'M';
                }
            }
            else if(inp[i] == 'N'){ //Min heap으로 변환
                if(inpmode == 'M' || inpmode == 'N'){
                    printf("ERROR: Binary Search Tree Not Found.\n");
                }
                else{
                    BSTToMinHeap(&my_BST, &min_heap);
                    inpmode = 'N';
                }
            }
            else if(inp[i] == '-'){
                if(inp[i+1] == '\0'){
                    if(inpmode == 'M'){
                        deleteMaxHeap(&max_heap);
                    }
                    else if(inpmode == 'M'){
                        deleteMinHeap(&min_heap);
                    }
                    else{
                        printf("ERROR: Invalid Input.\n");
                    }
                }
                else if(inp[i+1]-'0' >= 0 && inp[i+1]-'0' <= 9){ // 숫자 입력 받기
                    int tmp;
                    if(inp[i+2]-'0' >= 0 && inp[i+2]-'0' <= 9){ //two-digit
                        if(inp[i+3]=='\0'){
                            tmp = (inp[i+1]-'0')*10 + (inp[i+2]-'0'); //char->int
                            i=i+2;
                            if(inpmode == 'B'){
                                if(my_BST.root ==  NULL){
                                    printf("ERROR: Tree Is Empty.\n");
                                }
                                else if(isNode(&my_BST, tmp) == 0){
                                    printf("ERROR: Node With Such Value Doesn't Exist.\n");
                                }
                                else{
                                    deleteNode(&my_BST, searchValue(&my_BST, tmp, 0), heir);
                                }
                            }
                            else{
                                printf("ERROR: Invalid Input.\n");
                            }
                        }
                        else{
                            if(inpmode=='B'){
                                printf("ERROR: Only One & Two Digit Numbers Are Allowed.\n");
                            }
                            else{
                                printf("ERROR: Invalid Input.\n");
                            }
                        }
                    }
                    else{ //one-digit
                        if(inp[i+2]=='\0'){
                            tmp = inp[i+1]-'0'; //char->int
                            i++;
                            if(inpmode == 'B'){
                                if(my_BST.root ==  NULL){
                                    printf("ERROR: Tree Is Empty.\n");
                                }
                                else if(isNode(&my_BST, tmp) == 0){
                                    printf("ERROR: Node With Such Value Doesn't Exist.\n");
                                }
                                else{
                                    deleteNode(&my_BST, searchValue(&my_BST, tmp, 0), heir);
                                }
                            }
                            else{
                                printf("ERROR: Invalid Input.\n");
                            }
                        }
                        else{
                            printf("ERROR: Invalid Input.\n");
                        }
                    }
                }
            }
            else if(inp[i] == 'C'){
                if(inpmode=='M'){
                    printf("ERROR: Invalid Input.\n");
                }
                if(inpmode=='N'){
                    printf("ERROR: Invalid Input.\n");
                }
                if(inpmode=='B'){
                    clearTree(&my_BST);
                }
            }
        }
        if(default_print == 1){
            if(inpmode=='M'){
                printf("(");
                printHeap(&max_heap, 1);
                printf(")\n");
            }
            if(inpmode=='N'){
                printf("(");
                printHeap(&min_heap, 1);
                printf(")\n");
            }
            if(inpmode=='B'){
                printf("(");
                printTree(&my_BST);
                printf(")\n");
            }
        }
        else{
            default_print = 1;
        }
    }
    return 0;
}
