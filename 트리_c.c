//자료구조 한옥영 교수님 9주차 실습과제
//트리 ADT 실습과제
//최종 작성일: 2020.05.13(수)
//2019312481 심규현

#include <stdio.h>
#include <stdlib.h>
#include <string.h> //문자열 처리용

int BT = 0; //이진트리 모드 활성화하면 1 아니면 0

typedef struct Node{
    char data;
    struct Node* left;
    struct Node* right;
    int level;
    int degree;
} NODE;

typedef struct Tree{
    NODE* root;
} TREE;

void CreateRoot(TREE* my_tree, char data){
    if(my_tree->root != NULL){
        printf("ERROR: Root Already Exists.\n");
    }
    else{
        NODE* rootNode = (NODE*)malloc(sizeof(NODE));
        rootNode->data = data;
        rootNode->left = NULL;
        rootNode->right = NULL;
        rootNode->level = 0;
        rootNode->degree = 0;
        my_tree->root = rootNode;
    }
    return;
}

NODE* searchValue(TREE* my_tree, char target){
    NODE* position;
    TREE left_tree, right_tree;
    position = my_tree->root;
    left_tree.root = my_tree->root->left;
    right_tree.root = my_tree->root->right;
    while(1){
        if(position->data == target){
            return position;
        }
        else if(position->left == NULL && position->right == NULL){
            return NULL;
        }
        else{
            if(position->right == NULL) position = searchValue(&left_tree, target);
            else if(position->left == NULL) position = searchValue(&right_tree, target);
            else{ //둘다 있는 경우
                position = searchValue(&left_tree, target);
                if(position == NULL) position = searchValue(&right_tree, target);
            }
            return position;
        }
    }
}

int isNode(TREE* my_tree, char target){
    NODE* tmp;
    tmp = searchValue(my_tree, target);
    if(tmp == NULL){
        return 0;
    }
    else{
        return 1;
    }
}

void InsertNode(TREE* my_tree, NODE* pNode, char data[]){
    if(pNode==NULL){
        printf("ERROR: Parent Node Not Found.\n");
        return;
    }
    int n = strlen(data);
    if(BT==1 && n>2){
        printf("ERROR: Binary Tree Can't Have More Than 2 Child.\n");
        return;
    }
    else if(BT==1 && (pNode->degree)+n>2){
        printf("ERROR: Binary Tree Can't Have More Than 2 Child.\n");
        return;
    }
    NODE * current;
    current = pNode;
    if(pNode->left == NULL){
        current = pNode;
    }
    else{ //이미 자식이 있으면
        current = pNode->left;
        for(int i=0;i<((pNode->degree)-1);i++){
            current = current->right;
        }
    }
    for(int i=0;i<n;i++){
        NODE * newNode = (NODE*)malloc(sizeof(NODE));
        newNode->data = data[i];
        newNode->left = NULL;
        newNode->right = NULL;
        newNode->level = (pNode->level) + 1;
        newNode->degree = 0;
        if(pNode->degree==0){
            current->left = newNode;
        }
        else{
            current->right = newNode;
        }
        pNode->degree = (pNode->degree) + 1;
        current = newNode;
    }
}

void printTree(TREE* my_tree){
    if(my_tree->root == NULL){
        printf("Tree is Empty.");
        return;
    }
    TREE left_tree, right_tree;
    left_tree.root = my_tree->root->left;
    right_tree.root = my_tree->root->right;
    printf("%c", my_tree->root->data);
    if(left_tree.root != NULL){
        printf("(");
        printTree(&left_tree);
        printf(")");
    }
    if(right_tree.root != NULL){
        printf(",");
        printTree(&right_tree);
    }
    return;
}

NODE* findParent(TREE* my_tree, char target, NODE* parent){
    if((my_tree->root->data) == target){
        return NULL;
    }
    TREE left_tree, right_tree;
    NODE* position;
    NODE* tmp;
    left_tree.root = my_tree->root->left;
    right_tree.root = my_tree->root->right;
    position = my_tree->root;
    if((position->left == NULL) && (position->right == NULL)){
        return NULL;
    }
    if((position->left != NULL) && (position->left->data) == target){
        return position;
    }
    else if((position->right != NULL) && (position->right->data) == target){
        return parent;
    }
    else{
        if(position->right == NULL){
            tmp = findParent(&left_tree, target, position);
            return tmp;
        }
        else if(position->left == NULL){
            tmp = findParent(&right_tree, target, parent);
            return tmp;
        }
        else{
            tmp = findParent(&left_tree, target, position);
            if(tmp==NULL){
                tmp = findParent(&right_tree, target, parent);
            }
            return tmp;
        }
    }
}

void getSibling(TREE* my_tree, NODE* node){
    if(node==NULL){
        printf("ERROR: Invalid Input.\n");
        return;
    }
    char value = node->data;
    int count;
    if(node == my_tree->root){
        printf("ERROR: ROOT DOES NOT HAVE A SIBLING.\n");
        return;
    }
    NODE* parent;
    NODE* position;
    parent = findParent(my_tree, value, my_tree->root);
    position = parent->left;
    count = (parent->degree)-1;
    if(count == 0){
        printf("This Node Does Not Have A Sibling.\n");
        return;
    }
    printf("{");
    for(int i=0;i<(parent->degree);i++){
        if(position->data != value && count != 0){
            printf("%c,", position->data);
        }
        else if(position->data != value){
            printf("%c", position->data);
        }
        position = position->right;
        count--;
    }
    printf("}\n");
    return;
}

void getChild(TREE* my_tree, NODE* node){
    if(node==NULL){
        printf("ERROR: Invalid Input.\n");
        return;
    }
    if(node->degree == 0){
        printf("This Node Does Not Have A Child.\n");
        return;
    }
    NODE* position;
    position = node->left;
    printf("{");
    for(int i=0;i<(node->degree);i++){
        if(i != (node->degree)-1){
            printf("%c,", position->data);
        }
        else{
            printf("%c", position->data);
        }
        position = position->right;
    }
    printf("}\n");
    return;
}

int levelofNode(TREE* my_tree, NODE* node){
    if(my_tree->root == NULL || node == NULL){
        printf("ERROR: Invalid Input.\n");
        return -1;
    }
    int tmp;
    tmp = (node->level) - (my_tree->root->level); //부트리에서도 정확한 레벨
    return tmp;
}

int levelofTree(TREE* my_tree, int max){
    if(my_tree->root == NULL){
        printf("ERROR: Invalid Input.\n");
        return -1;
    }
    int tmp1=0, tmp2=0;
    TREE left_tree, right_tree;
    left_tree.root = my_tree->root->left;
    right_tree.root = my_tree->root->right;
    if((my_tree->root->left == NULL) && (my_tree->root->right == NULL)){
        return my_tree->root->level;
    }
    else{
        if(left_tree.root != NULL){
            tmp1 = levelofTree(&left_tree, max);
        }
        if(right_tree.root != NULL){
            tmp2 = levelofTree(&right_tree, max);
        }
    }
    if(tmp1>tmp2) return tmp1;
    else return tmp2;
}

void deleteNode(TREE* my_tree, NODE* node){
    if(node==NULL){
        printf("ERROR: Invalid Input.\n");
        return;
    }
    if(node->left != NULL){//부모 노드
        printf("ERROR: Can Not Delete Parent Node.\n");
        return;
    }
    else if(node == my_tree->root){
        free(node);
        my_tree->root = NULL;
        return;
    }
    NODE* parent;
    NODE* before;
    NODE* after;
    parent = findParent(my_tree, node->data, my_tree->root);
    after = node->right;
    if(parent->left == node){//첫 자식 (직접 연결인 경우)
        before = parent;
        if(after==NULL){ //유일한 자식
            parent->left = NULL;
            (parent->degree) = (parent->degree)-1;
            free(node);
        }
        else{
            parent->left = after;
            (parent->degree) = (parent->degree)-1;
            free(node);
        }
    }
    else{
        before = parent->left;
        while(before->right != node){
            before = before->right;
        }
        (parent->degree) = (parent->degree)-1;
        before->right = node->right;
        free(node);
    }
    return;
}

void get_ancestors(TREE* my_tree, NODE* node){
    NODE* position;
    position = findParent(my_tree, node->data, my_tree->root);
    while(position != NULL){
        printf("%c ", position->data);
        position = findParent(my_tree, position->data, my_tree->root);
    }
    printf("\n");
    return;
}

void printDescendants(TREE* my_tree){
    TREE left_tree, right_tree;
    left_tree.root = my_tree->root->left;
    right_tree.root = my_tree->root->right;
    printf("%c", my_tree->root->data);
    if(left_tree.root != NULL){
        printf("(");
        printDescendants(&left_tree);
        printf(")");
    }
    if(right_tree.root != NULL){
        printf(" ");
        printDescendants(&right_tree);
    }
    return;
}

void get_descendants(TREE* my_tree, NODE* node){
    TREE left_tree;
    left_tree.root = node->left;
    if(left_tree.root != NULL){
        printDescendants(&left_tree);
    }
    printf("\n");
    return;
}

int degreeofNode(TREE* my_tree, NODE* node){
    int tmp;
    tmp = node->degree;
    return tmp;
}

int degreeofTree(TREE* my_tree){
    if(my_tree->root == NULL){
        return 0;
    }
    TREE left_tree, right_tree;
    int lt, rt, self;
    int max;
    left_tree.root = my_tree->root->left;
    right_tree.root = my_tree->root->right;
    lt = degreeofTree(&left_tree);
    rt = degreeofTree(&right_tree);
    self = my_tree->root->degree;
    max = lt>rt ? lt:rt;
    max = max>self ? max:self;
    return max;
}

int countNode(TREE* my_tree){
    if(my_tree->root == NULL){
        return 0;
    }
    TREE left_tree, right_tree;
    int lt, rt;
    left_tree.root = my_tree->root->left;
    right_tree.root = my_tree->root->right;
    lt = countNode(&left_tree);
    rt = countNode(&right_tree);
    return lt+rt+1;
}

void insertSibling(TREE* my_tree, NODE* node, char data[]){
    if(node==NULL || node == my_tree->root){
        printf("ERROR: Invalid Input.\n");
    }
    InsertNode(my_tree, findParent(my_tree, node->data, my_tree->root), data);
    return;
}

void increaseLevel(TREE* my_tree){
    if(my_tree->root == NULL){
        return;
    }
    (my_tree->root->level) = (my_tree->root->level) + 1;
    TREE left_tree, right_tree;
    left_tree.root = my_tree->root->left;
    right_tree.root = my_tree->root->right;
    increaseLevel(&left_tree);
    increaseLevel(&right_tree);
    return;
}

TREE* joinTrees(char data, TREE* tree1, TREE* tree2){
    TREE* join_tree = (TREE*)malloc(sizeof(TREE));
    join_tree->root = NULL;
    CreateRoot(join_tree, data);
    join_tree->root->left = tree1->root;
    join_tree->root->left->right = tree2->root;
    join_tree->root->level = -1;
    join_tree->root->degree = 2;
    increaseLevel(join_tree);
    return join_tree;
}

void clearTree(TREE* my_tree){
    NODE* left_node = my_tree->root;
    while(my_tree->root != NULL){
        left_node = my_tree->root;
        while(left_node->left!=NULL){
            left_node = left_node->left;
        }
        deleteNode(my_tree, left_node);
    }
    return;
}

int main(void){ //메인 함수
    TREE my_tree={NULL};
    TREE tmp_tree={NULL};
    TREE* current_tree = &my_tree;
    int default_print = 1;
    int using_tmp_node = 0;
    char binary[10] = "";
    char inp[50] = ""; //입력 받기 용 문자열 + ""로 초기화하기
    
    printf("이진트리 모드: B\n");
    printf("일반트리 모드: N\n입력: ");
    scanf("%s", binary);
    
    if(binary[0] == 'B'){
        BT = 1;
    }
    else if(binary[0] == 'N'){
        BT = 0;
    }
    
    printf("명령문 안내\n");
    printf("+^(값): 트리의 루트 노드 추가\n");
    printf("+(부모노드)[(값1),(값2)...]: 부모노드 아래에 노드 추가\n");
    printf("S(값): 해당 노드의 형제 노드 보여주기\n");
    printf("T: 트리 출력\n");
    printf("P(자식노드): 부모노드의 값 출력\n");
    printf("C(부모노드): 자식노드의 값 출력\n");
    printf("L: 트리의 레벨 출력\n");
    printf("L(값): 노드의 레벨 출력\n");
    printf("G: 트리의 degree 출력\n");
    printf("G(값): 노드의 degree 출력\n");
    printf("-(값): 해당 노드 삭제\n");
    printf("A(값): 해당 노드의 조상 노드 출력\n");
    printf("D(값): 해당 노드의 후손 노드 전부 출력\n");
    printf("#: 노드 수 센 뒤 출력\n");
    printf("=+(부모노드)[(값1),(값2)...]: 큐에 해당 값을 가지는 원소가 존재하는지 확인\n");
    printf("J: 트리 합병 모드 활성화/비활성화\n");
    printf("K: 트리 초기화\n");
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
                if(inp[i+1] == '^'){
                    CreateRoot(current_tree, inp[i+2]);
                    i = i+2;
                }
                else{
                    char pNode = inp[i+1];
                    char data[50] = "";
                    if(inp[i+2] == '('){
                        int j = i+3;
                        int count = 0;
                        while(inp[j] != ')'){
                            if('A'<=inp[j] && 'Z'>=inp[j]){
                                data[count] = inp[j];
                                count++;
                            }
                            j++;
                        }
                        InsertNode(current_tree, searchValue(current_tree, pNode), data);
                        i = j;
                    }
                }
            }
            else if(inp[i] == 'S'){
                if(inp[i+1] == '(' && inp[i+3] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2]){
                        getSibling(current_tree, searchValue(current_tree, inp[i+2]));
                        i = i+3;
                    }
                    default_print = 0;
                }
            }
            else if(inp[i] == 'T'){
                continue; //어차피 나가면 출력이 실행됨. 중복 출력을 피하고자 continue문 입력.
            }
            else if(inp[i] == 'P'){
                if(inp[i+1] == '(' && inp[i+3] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2]){
                        if(isNode(current_tree, inp[i+2])==1){
                            if(findParent(current_tree, inp[i+2], current_tree->root)){
                                printf("%c\n", (findParent(current_tree, inp[i+2], current_tree->root)->data));
                                i = i+3;
                            }
                        }
                        else{
                            printf("ERROR: Can't Find NODE %c.\n", inp[i+2]);
                        }
                    }
                }
                default_print = 0;
            }
            else if(inp[i] == 'C'){
                if(inp[i+1] == '(' && inp[i+3] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2]){
                        getChild(current_tree, searchValue(current_tree, inp[i+2]));
                        i = i+3;
                    }
                }
                default_print = 0;
            }
            else if(inp[i] == 'L'){
                if(inp[i+1] == '\0'){
                    printf("%d\n", levelofTree(current_tree, 0));
                    i++;
                }
                else if(inp[i+1] == '(' && inp[i+3] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2]){
                        printf("%d\n", levelofNode(current_tree, searchValue(current_tree, inp[i+2])));
                        i = i+3;
                    }
                }
                default_print = 0;
            }
            else if(inp[i] == '-'){
                if('A'<=inp[i+1] && 'Z'>=inp[i+1]){
                    deleteNode(current_tree, searchValue(current_tree, inp[i+1]));
                    i++;
                }
            }
            else if(inp[i] == 'A'){
                if(inp[i+1] == '(' && inp[i+3] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2]){
                        get_ancestors(current_tree, searchValue(current_tree, inp[i+2]));
                        i = i+3;
                    }
                }
                default_print = 0;
            }
            else if(inp[i] == 'D'){
                if(inp[i+1] == '(' && inp[i+3] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2]){
                        get_descendants(current_tree, searchValue(current_tree, inp[i+2]));
                        i = i+3;
                    }
                }
                default_print = 0;
            }
            else if(inp[i] == 'G'){
                if(inp[i+1] == '\0'){
                    printf("%d\n", degreeofTree(current_tree));
                    i++;
                }
                else if(inp[i+1] == '(' && inp[i+3] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2]){
                        printf("%d\n", degreeofNode(current_tree, searchValue(current_tree, inp[i+2])));
                        i = i+3;
                    }
                }
                default_print = 0;
            }
            else if(inp[i] == '#'){
                printf("%d\n", countNode(current_tree));
                default_print = 0;
            }
            else if(inp[i] == '='){
                if(inp[i+1] == '+'){
                    char sNode = inp[i+2];
                    char data[50] = "";
                    if(inp[i+3] == '('){
                        int j = i+4;
                        int count = 0;
                        while(inp[j] != ')'){
                            if('A'<=inp[j] && 'Z'>=inp[j]){
                                data[count] = inp[j];
                                count++;
                            }
                            j++;
                        }
                        insertSibling(current_tree, searchValue(current_tree, sNode), data);
                        i = j;
                    }
                }
            }
            else if(inp[i] == 'J'){
                if(inp[i+1] == '\0'){
                    if(using_tmp_node == 0){
                        printf("Creating New Temporary Tree...\n");
                        printf("Created!\n");
                        printf("Now Please Start By Creating A Root.\n");
                        printf("After Managing, Press \"J\" Again to Merge it With Original Tree.\n");
                        /* ADT의 재해석: J를 입력하면 사용자가 기존의 명령어를 이용하여 같은 방식으로 임시 트리를 생성할 수 있게 하고,
                           트리의 생성 및 수정이 끝났다면 다시 J를 입력하여 기존의 트리와 합병한 트리를 생성할 수 있게 하였다. */
                        using_tmp_node = 1;
                        tmp_tree.root = NULL;
                        current_tree = &tmp_tree;
                    }
                    else if(using_tmp_node == 1){
                        current_tree = &my_tree;
                        char value[10]="";
                        printf("Value for New Root of Joined Tree: ");
                        scanf("%s", value);
                        scanf("%*c");
                        TREE* result = joinTrees(value[0], &my_tree, &tmp_tree);
                        my_tree = *result;
                        free(result);
                        using_tmp_node = 0;
                    }
                }
            }
            else if(inp[i] == 'K'){
                clearTree(current_tree);
            }
        }
        
        if(default_print == 1){
            printf("(");
            printTree(current_tree);
            printf(")\n");
        }
        else{
            default_print = 1;
        }
        
    }
    return 0;
}
