//자료구조 한옥영 교수님 10주차 실습과제
//이진 탐색 트리 ADT 실습과제
//최종 작성일: 2020.06.19(금)
//2019312481 심규현

#include <stdio.h>
#include <stdlib.h>
#include <string.h> //문자열 처리용

typedef struct Node{
    int data;
    struct Node* left;
    struct Node* right;
    int height;
} NODE;

typedef struct Binary_Search_Tree{
    NODE* root;
} BST;

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

void deleteNode(BST* my_BST, NODE* node, char mode){ //mode가 L이면 좌-부트리의 Right-Most Node, R이면 우-부트리의 Left-Most Node
    int root = 0;
    if(node==NULL){
        printf("ERROR: Invalid Input.\n");
        return;
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
                free(node);
                return;
            }
            else if(parent->right == node){
                parent->right = NULL;
                free(node);
                return;
            }
        }
        else if(root == 1){ //유일한 노드
            free(node);
            my_BST->root = NULL;
            return;
        }
    }
    else if(node->left == NULL){ //right는 null이 아님 -> right가 유일한 자식
        if(root == 0){
            if(parent->left == node){
                parent->left = node->right;
                free(node);
                return;
            }
            else if(parent->right == node){
                parent->right = node->right;
                free(node);
                return;
            }
        }
        else if(root == 1){ //유일한 노드
            my_BST->root = node->right;
            free(node);
            return;
        }
    }
    else if(node->right == NULL){ //left는 null이 아님 -> left가 유일한 자식
        if(root == 0){
            if(parent->left == node){
                parent->left = node->left;
                free(node);
                return;
            }
            else if(parent->right == node){
                parent->right = node->left;
                free(node);
                return;
            }
        }
        else if(root == 1){ //유일한 노드
            my_BST->root = node->left;
            free(node);
            return;
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
            return;
        }
    }
}

void getChild(BST* my_BST, NODE* node, char mode){
    if(node == NULL){
        printf("ERROR: Node Does Not Exist.\n");
        return;
    }
    if(mode == 'L'){
        if(node->left == NULL){
            printf("NULL\n");
        }
        else{
            printf("%d\n", node->left->data);
        }
    }
    if(mode == 'R'){
        if(node->right == NULL){
            printf("NULL\n");
        }
        else{
            printf("%d\n", node->right->data);
        }
    }
    return;
}

int heightofTree(BST* my_BST, int max){
    if(my_BST->root == NULL){
        printf("ERROR: Invalid Input.\n");
        return -1;
    }
    int tmp1=0, tmp2=0;
    BST left_tree, right_tree;
    left_tree.root = my_BST->root->left;
    right_tree.root = my_BST->root->right;
    if((my_BST->root->left == NULL) && (my_BST->root->right == NULL)){
        return my_BST->root->height;
    }
    else{
        if(left_tree.root != NULL){
            tmp1 = heightofTree(&left_tree, max);
        }
        if(right_tree.root != NULL){
            tmp2 = heightofTree(&right_tree, max);
        }
    }
    if(tmp1>tmp2) return tmp1;
    else return tmp2;
}

int countNode(BST* my_BST){
    if(my_BST->root == NULL){
        return 0;
    }
    BST left_tree, right_tree;
    int lt, rt;
    left_tree.root = my_BST->root->left;
    right_tree.root = my_BST->root->right;
    lt = countNode(&left_tree);
    rt = countNode(&right_tree);
    return lt+rt+1;
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

void inorderTraversal(BST* my_BST){
    BST left_tree, right_tree;
    if(my_BST->root->left != NULL){
        left_tree.root = my_BST->root->left;
        inorderTraversal(&left_tree);
    }
    printf("%d ", my_BST->root->data);
    if(my_BST->root->right != NULL){
        right_tree.root = my_BST->root->right;
        inorderTraversal(&right_tree);
    }
    return;
}

void rightrootleftTraversal(BST* my_BST){
    BST left_tree, right_tree;
    if(my_BST->root->right != NULL){
        right_tree.root = my_BST->root->right;
        rightrootleftTraversal(&right_tree);
    }
    printf("%d ", my_BST->root->data);
    if(my_BST->root->left != NULL){
        left_tree.root = my_BST->root->left;
        rightrootleftTraversal(&left_tree);
    }
    return;
}

int get_min(BST* my_BST){
    int tmp;
    BST left_tree;
    if(my_BST->root->left != NULL){
        left_tree.root = my_BST->root->left;
        tmp = get_min(&left_tree);
    }
    else{
        return (my_BST->root->data);
    }
    return tmp;
}

int get_max(BST* my_BST){
    int tmp;
    BST right_tree;
    if(my_BST->root->right != NULL){
        right_tree.root = my_BST->root->right;
        tmp = get_max(&right_tree);
    }
    else{
        return (my_BST->root->data);
    }
    return tmp;
}

int heightofNode(BST* my_BST, NODE* node){ //나만의 기능 1
    if(my_BST->root == NULL || node == NULL){
        printf("ERROR: Invalid Input.\n");
        return -1;
    }
    int tmp;
    tmp = (node->height) - (my_BST->root->height); //부트리에서도 정확한 레벨
    return tmp;
}

void replace(BST* my_BST, NODE* node, int value){
    BST left_tree, right_tree;
    if(node->data == value){
        printf("ERROR: Cannot Replace With Same Value.\n");
    }
    else if(node->left == NULL && node->right == NULL){
        node->data = value;
    }
    else if(node->left == NULL){
        right_tree.root = my_BST->root->right;
        if(get_min(&right_tree) > value){ //우 부트리의 최솟값보다 작아야함
            node->data = value;
        }
        else{
            printf("ERROR: New Value Has To Meet Conditions of BST.\n");
        }
    }
    else if(node->right == NULL){
        left_tree.root = my_BST->root->left;
        if(get_max(&left_tree) > value){ //좌 부트리의 최대값보다 작아야함
            node->data = value;
        }
        else{
            printf("ERROR: New Value Has To Meet Conditions of BST.\n");
        }
    }
    else{
        right_tree.root = my_BST->root->right;
        left_tree.root = my_BST->root->left;
        if((get_max(&left_tree) < value) && (get_min(&right_tree) > value)){
            node->data = value;
        }
        else{
            printf("ERROR: New Value Has To Meet Conditions of BST.\n");
        }
    }
    return;
}
void preorderTraversal(BST* my_BST){ //root-left-right
    BST left_tree, right_tree;
    printf("%d ", my_BST->root->data);
    if(my_BST->root->left != NULL){
        left_tree.root = my_BST->root->left;
        preorderTraversal(&left_tree);
    }
    if(my_BST->root->right != NULL){
        right_tree.root = my_BST->root->right;
        preorderTraversal(&right_tree);
    }
    return;
}

int main(void){ //메인 함수
    BST my_BST={NULL};
    int default_print = 1;
    char heir_mode[10] = "";
    char heir = 'L';
    char inp[50] = ""; //입력 받기 용 문자열 + ""로 초기화하기
    
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
    
    printf("명령문 안내\n");
    printf("+값: 이진 트리 탐색 트리의 노드 추가\n");
    printf("-값: 해당 노드 삭제\n");
    printf("P: 트리 출력\n");
    printf("I: Left-Root-Right 방식의 순회 출력\n");
    printf("R: Right-Root-Left 방식의 순회 출력\n");
    printf("E: Root-Left-Right 방식의 순회 출력\n");
    printf("N: 최소값 출력\n");
    printf("X: 최대값 출력\n");
    printf("F값: 루트부터 해당 노드까지 가기 위한 경로 출력\n");
    printf("G(값): 해당 노드의 오른쪽 자식 출력\n");
    printf("L(값): 해당 노드의 왼쪽 자식 출력\n");
    printf("H: 트리의 높이 출력\n");
    printf("O(값): 해당 노드의 높이 출력\n");
    printf("A(값): 루트의 값 변경\n");
    printf("#: 노드 수 센 뒤 출력\n");
    printf("C: 트리 초기화\n");
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
                            if(my_BST.root ==  NULL){
                                CreateRoot(&my_BST, tmp);
                            }
                            else InsertNode(&my_BST, tmp);
                        }
                        else{
                            printf("ERROR: Only One & Two Digit Numbers Are Allowed.\n");
                        }
                    }
                    else{ //one-digit
                        if(inp[i+2]=='\0'){
                            tmp = inp[i+1]-'0'; //char->int
                            i++;
                            if(my_BST.root ==  NULL){
                                CreateRoot(&my_BST, tmp);
                            }
                            else InsertNode(&my_BST, tmp);
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
            else if(inp[i] == 'I'){
                inorderTraversal(&my_BST);
                printf("\n");
                default_print = 0;
            }
            else if(inp[i] == 'R'){
                rightrootleftTraversal(&my_BST);
                printf("\n");
                default_print = 0;
            }
            else if(inp[i] == 'N'){
                printf("%d\n",get_min(&my_BST));
                default_print = 0;
            }
            else if(inp[i] == 'X'){
                printf("%d\n",get_max(&my_BST));
                default_print = 0;
            }
            else if(inp[i] == 'F'){
                if(inp[i+1]-'0' >= 0 && inp[i+1]-'0' <= 9){ // 숫자 입력 받기
                    int tmp;
                    if(inp[i+2]-'0' >= 0 && inp[i+2]-'0' <= 9){ //two-digit
                        if(inp[i+3]=='\0'){
                            tmp = (inp[i+1]-'0')*10 + (inp[i+2]-'0'); //char->int
                            i=i+2;
                            if(isNode(&my_BST, tmp) == 0){ // 없으면
                                printf("ERROR: Node With Such Value Doesn't Exist.\n");
                            }
                            else{
                                printf("ROOT");
                                searchValue(&my_BST, tmp, 1);
                                printf("\n");
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
                            if(isNode(&my_BST, tmp) == 0){ // 없으면
                                printf("ERROR: Node With Such Value Doesn't Exist.\n");
                            }
                            else{
                                printf("ROOT");
                                searchValue(&my_BST, tmp, 1);
                                printf("\n");
                            }
                        }
                        else{
                            printf("ERROR: Invalid Input.\n");
                        }
                    }
                }
                default_print = 0;
            }
            else if(inp[i] == '-'){
                if(inp[i+1]-'0' >= 0 && inp[i+1]-'0' <= 9){ // 숫자 입력 받기
                    int tmp;
                    if(inp[i+2]-'0' >= 0 && inp[i+2]-'0' <= 9){ //two-digit
                        if(inp[i+3]=='\0'){
                            tmp = (inp[i+1]-'0')*10 + (inp[i+2]-'0'); //char->int
                            i=i+2;
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
                            printf("ERROR: Only One & Two Digit Numbers Are Allowed.\n");
                        }
                    }
                    else{ //one-digit
                        if(inp[i+2]=='\0'){
                            tmp = inp[i+1]-'0'; //char->int
                            i++;
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
                }
            }
            else if(inp[i] == 'H'){
                printf("%d\n",heightofTree(&my_BST, 0));
                default_print = 0;
            }
            else if(inp[i] == 'G' || inp[i] == 'L'){
                if(inp[i+1] == '('){
                    if(inp[i+2]-'0' >= 0 && inp[i+2]-'0' <= 9){ // 숫자 입력 받기
                        int tmp;
                        if(inp[i+3]-'0' >= 0 && inp[i+3]-'0' <= 9){ //two-digit
                            if(inp[i+4]==')'){
                                tmp = (inp[i+2]-'0')*10 + (inp[i+3]-'0'); //char->int
                                if(isNode(&my_BST, tmp) == 0){ // 없으면
                                    printf("ERROR: Node With Such Value Doesn't Exist.\n");
                                }
                                else{
                                    if(inp[i] == 'G'){
                                        getChild(&my_BST, searchValue(&my_BST, tmp, 0), 'R');
                                    }
                                    else if(inp[i] == 'L'){
                                        getChild(&my_BST, searchValue(&my_BST, tmp, 0), 'L');
                                    }
                                }
                                i=i+4;
                            }
                            else{
                                printf("ERROR: Only One & Two Digit Numbers Are Allowed.\n");
                            }
                        }
                        else{ //one-digit
                            if(inp[i+3]==')'){
                                tmp = inp[i+2]-'0'; //char->int
                                i=i+3;
                                if(isNode(&my_BST, tmp) == 0){ // 없으면
                                    printf("ERROR: Node With Such Value Doesn't Exist.\n");
                                }
                                else{
                                    if(inp[i] == 'G'){
                                        getChild(&my_BST, searchValue(&my_BST, tmp, 0), 'R');
                                    }
                                    else if(inp[i] == 'L'){
                                        getChild(&my_BST, searchValue(&my_BST, tmp, 0), 'L');
                                    }
                                }
                            }
                            else{
                                printf("ERROR: Invalid Input.\n");
                            }
                        }
                    }
                    default_print = 0;
                }
            }
            else if(inp[i] == 'O'){ //나만의 기능 1
                if(inp[i+1] == '('){
                    if(inp[i+2]-'0' >= 0 && inp[i+2]-'0' <= 9){ // 숫자 입력 받기
                        int tmp;
                        if(inp[i+3]-'0' >= 0 && inp[i+3]-'0' <= 9){ //two-digit
                            if(inp[i+4]==')'){
                                tmp = (inp[i+2]-'0')*10 + (inp[i+3]-'0'); //char->int
                                if(isNode(&my_BST, tmp) == 0){ // 없으면
                                    printf("ERROR: Node With Such Value Doesn't Exist.\n");
                                }
                                else{
                                    printf("%d\n",heightofNode(&my_BST, searchValue(&my_BST, tmp, 0)));
                                }
                                i=i+4;
                            }
                            else{
                                printf("ERROR: Only One & Two Digit Numbers Are Allowed.\n");
                            }
                        }
                        else{ //one-digit
                            if(inp[i+3]==')'){
                                tmp = inp[i+2]-'0'; //char->int
                                i=i+3;
                                if(isNode(&my_BST, tmp) == 0){ // 없으면
                                    printf("ERROR: Node With Such Value Doesn't Exist.\n");
                                }
                                else{
                                    printf("%d\n",heightofNode(&my_BST, searchValue(&my_BST, tmp, 0)));
                                }
                            }
                            else{
                                printf("ERROR: Invalid Input.\n");
                            }
                        }
                    }
                    default_print = 0;
                }
            }
            else if(inp[i] == 'A'){ //나만의 기능 2
                if(inp[i+1] == '('){
                    if(inp[i+2]-'0' >= 0 && inp[i+2]-'0' <= 9){ // 숫자 입력 받기
                        int tmp;
                        if(inp[i+3]-'0' >= 0 && inp[i+3]-'0' <= 9){ //two-digit
                            if(inp[i+4]==')'){
                                tmp = (inp[i+2]-'0')*10 + (inp[i+3]-'0'); //char->int
                                if(my_BST.root == NULL){ // 없으면
                                    printf("ERROR: Cannot Find Tree.\n");
                                }
                                else if(isNode(&my_BST, tmp) == 1){
                                    printf("ERROR: Node With Such Value Already Exist.\n");
                                }
                                else{
                                    replace(&my_BST, my_BST.root, tmp);
                                }
                                i=i+4;
                            }
                            else{
                                printf("ERROR: Only One & Two Digit Numbers Are Allowed.\n");
                            }
                        }
                        else{ //one-digit
                            if(inp[i+3]==')'){
                                tmp = inp[i+2]-'0'; //char->int
                                i=i+3;
                                if(isNode(&my_BST, tmp) == 0){ // 없으면
                                    printf("ERROR: Cannot Find Tree.\n");
                                }
                                else if(isNode(&my_BST, tmp) == 1){
                                    printf("ERROR: Node With Such Value Already Exist.\n");
                                }
                                else{
                                    replace(&my_BST, my_BST.root, tmp);
                                }
                            }
                            else{
                                printf("ERROR: Invalid Input.\n");
                            }
                        }
                    }
                }
            }
            else if(inp[i] == 'E'){ //나만의 기능 3
                preorderTraversal(&my_BST);
                printf("\n");
                default_print = 0;
            }
            else if(inp[i] == '#'){
                printf("%d\n", countNode(&my_BST));
                default_print = 0;
            }
            else if(inp[i] == 'C'){
                clearTree(&my_BST);
            }
        }
        if(default_print == 1){
            printf("(");
            printTree(&my_BST);
            printf(")\n");
        }
        else{
            default_print = 1;
        }
    }
    return 0;
}
