//자료구조 한옥영 교수님 12주차 도전과제
//가중그래프 ADT 과제
//최종 작성일: 2020.06.07(일)
//2019312481 심규현

#include <stdio.h>
#include <stdlib.h> //동적할당용
#include <string.h> //문자열 처리용

typedef struct Vertex{ //자료형 선언
    char data; //데이터 (실질적인 값)
    struct Vertex * link; //링크
    struct Vertex * visited;
} VERTEX;

typedef struct Edge{
    VERTEX * v1;
    VERTEX * v2;
    int weight;
} EDGE;

typedef struct Graph{
    VERTEX * vertex[50]; //연결리스트 헤드
    EDGE * edge[150];
    int size;
    int n_edge;
} GRAPH;

void clear_visited(GRAPH* my_graph){
    for(int i=1; i<=my_graph->size; i++){
        my_graph->vertex[i]->visited = NULL;
    }
    return;
}

void create(GRAPH* my_graph){
    for(int i=0;i<50;i++){
        my_graph->vertex[i] = NULL;
    }
    my_graph->size = 0;
    my_graph->n_edge = 0;
    clear_visited(my_graph);
    return;
}

int position(GRAPH* my_graph, char data){
    for(int i=1; i<=my_graph->size; i++){
        if(my_graph->vertex[i]->data == data){
            return i;
        }
    }
    return -1;
}

void insert_vertex(GRAPH* my_graph, char data){
    if(position(my_graph, data) != -1){
        printf("ERROR: Vertex With Such Value Already Exists.\n");
        return;
    }
    VERTEX *new_vertex = (VERTEX*)malloc(sizeof(VERTEX));
    new_vertex->data = data;
    new_vertex->link = NULL;
    new_vertex->visited = NULL;
    my_graph->vertex[(my_graph->size)+1] = new_vertex;
    my_graph->size++;
    return;
}

int edge_position(GRAPH* my_graph, VERTEX* vertex1, VERTEX* vertex2){
    for(int i=1; i<= my_graph->n_edge; i++){
        if(my_graph->edge[i]->v1 == vertex1 && my_graph->edge[i]->v2 == vertex2){
            return i;
        }
    }
    return -1;
}

void add_struct_edge(GRAPH* my_graph, VERTEX* vertex1, VERTEX* vertex2, int w){
    if(edge_position(my_graph, vertex1, vertex2) != -1){
        printf("ERROR: Edge Already Exists.\n");
        return;
    }
    EDGE *new_edge = (EDGE*)malloc(sizeof(EDGE));
    new_edge->v1 = vertex1;
    new_edge->v2 = vertex2;
    new_edge->weight = w;
    my_graph->edge[(my_graph->n_edge)+1] = new_edge;
    my_graph->n_edge++;
    return;
}

void add_edge(GRAPH* my_graph, char data1, char data2, int w){
    int i = position(my_graph, data1), j = position(my_graph, data2);
    VERTEX *vi, *vj;
    vi = vj = NULL;
    if(i==-1 || j==-1){
        printf("ERROR: Can't Find Vertex\n");
    }
    if(i != -1){
        vi = my_graph->vertex[i];
        while(vi->link != NULL){
            vi = vi->link;
        }
    }
    if(j != -1){
        vj = my_graph->vertex[j];
        while(vj->link != NULL){
            vj = vj->link;
        }
    }
    VERTEX *new_vertex1 = (VERTEX*)malloc(sizeof(VERTEX));
    new_vertex1->data = data2;
    new_vertex1->link = NULL;
    VERTEX *new_vertex2 = (VERTEX*)malloc(sizeof(VERTEX));
    new_vertex2->data = data1;
    new_vertex2->link = NULL;
    vi->link = new_vertex1;
    vj->link = new_vertex2;
    
    //for 가중그래프
    vi = my_graph->vertex[i];
    vj = my_graph->vertex[j];
    add_struct_edge(my_graph, vi, vj, w);
}

int degree_of_vertex(GRAPH * my_graph, char data){
    VERTEX* vertex;
    int cnt=0;
    int pos = position(my_graph, data);
    if(pos == -1){
        printf("ERROR: Can't Find Vertex with Such Value.\n");
        return -1;
    }
    vertex = my_graph->vertex[pos];
    while(vertex->link != NULL){
        cnt++;
        vertex = vertex->link;
    }
    return cnt;
}

int is_empty(GRAPH * my_graph){
    if(my_graph->size == 0) return 1;
    else return 0;
}

void adjacent(GRAPH * my_graph, char data){
    int pos = position(my_graph, data);
    if(pos==-1){
        printf("ERROR: Vertex With Such Value Does Not Exist.\n");
        return;
    }
    printf("{");
    VERTEX * vertex = my_graph->vertex[pos]->link;
    while(vertex->link != NULL){
        printf("%c, ", vertex->data);
        vertex = vertex->link;
    }
    printf("%c}\n", vertex->data);
    return;
}

int path(GRAPH * my_graph, char data1, char data2){
    //printf("PATH %c %c Called\n", data1, data2);
    int pos = position(my_graph, data1);
    int tmp;
    VERTEX * temp_v, * orig;
    VERTEX * vertex = my_graph->vertex[pos];
    orig = my_graph->vertex[pos];
    if(vertex->visited != NULL){
        if(vertex->visited->data == data2){ //방문한 적이 있는 노드면 그냥 반환
            return 1;
        }
    }
    if(vertex->data == data2) return 1;
    while(vertex->link != NULL){ //직접 연결인지 확인
        temp_v = my_graph->vertex[position(my_graph, vertex->link->data)];
        //printf("1Link Data: %c\n", vertex->link->data);
        if(temp_v->visited == NULL){ //아직 방문하지 않은 노드면
            if(vertex->link->data==data2){ //연결 찾으면
                orig->visited = my_graph->vertex[position(my_graph, data2)];
                //printf("direct");
                return 1;
            }
        }
        vertex = vertex->link;
    }
    vertex = my_graph->vertex[pos];
    while(vertex->link != NULL){ //직접 연결은 아닌 상태 - 직접 연결된 노드들로 재귀탐색
        temp_v = my_graph->vertex[position(my_graph, vertex->link->data)];
        if(temp_v->visited == NULL){
            //printf("2Link Data: %c\n", vertex->link->data);
            orig->visited = my_graph->vertex[position(my_graph, vertex->link->data)]; //현재 탐색 중인 노드의 값을 visited 포인터로 가리킴.
            //printf("Calling PATH %c %c", vertex->link->data, data2);
            tmp = path(my_graph, vertex->link->data, data2);
            if(tmp == 1){
                return 1;
            }
        }
        vertex = vertex->link;
    }
    return 0;
}

int get_weight(GRAPH* my_graph, char data1, char data2){
    int i = position(my_graph, data1), j = position(my_graph, data2);
    if(i == -1 || j == -1){
        printf("ERROR: Cannot Find Vertex.\n");
        return -1;
    }
    VERTEX *v1 = my_graph->vertex[i];
    VERTEX *v2 = my_graph->vertex[j];
    int k = edge_position(my_graph, v1, v2);
    int l = edge_position(my_graph, v2, v1);
    if(k == -1 && l == -1){
        printf("ERROR: Edge Does Not Exist.\n");
        return -1;
    }
    else{
        if(k==-1){
            return my_graph->edge[l]->weight;
        }
        else if(l == -1){
            return my_graph->edge[k]->weight;
        }
    }
    return -1;
}

void printpath(GRAPH* my_graph, char data1, char data2){
    if(path(my_graph, data1, data2) == 0){ //자연스럽게 path 함수 실행해서 visited 설정해주기
        printf("No Path Between Two Vertex.\n");
    }
    else{
        int pos = position(my_graph, data1);
        int sum = 0;
        VERTEX * vertex = my_graph->vertex[pos];
        printf("PATH: ");
        while(vertex->visited != NULL){
            printf("%c -> ", vertex->data);
            sum = sum + get_weight(my_graph, vertex->data, vertex->visited->data);
            vertex = vertex->visited;
        }
        printf("%c\n", vertex->data);
        printf("WEIGHT: %d\n", sum);
    }
    return;
}

int delete_edge(GRAPH * my_graph, char data1, char data2, int mode){ //mode 1이면 출력
    int i = position(my_graph, data1), j = position(my_graph, data2);
    VERTEX *vi, *vj;
    vi = vj = NULL;
    VERTEX *edge_i, *edge_j, *before_edge_i, *before_edge_j;
    edge_i = edge_j = before_edge_i = before_edge_j = NULL;
    if(i==-1 || j==-1){
        if(mode == 1) printf("ERROR: Can't Find Vertex\n");
        return -1;
    }
    if(i==j){
        if(mode == 1) printf("ERROR: Edge Does Not Exist Between Same Vertex.\n");
        return -1;
    }
    //for 가중 그래프
    vi = my_graph->vertex[i];
    vj = my_graph->vertex[j];
    int k;
    k = edge_position(my_graph, vi, vj);
    if(k == -1){
        if(mode == 1) printf("ERROR: Edge Does Not Exist.\n");
        return -1;
    }
    EDGE* del = my_graph->edge[k];
    for(int p = k; p<my_graph->n_edge;p++){
        my_graph->edge[p] = my_graph->edge[p+1];
    }
    free(del);
    //for 가중 그래프 끝
    
    if(i != -1){
        if(my_graph->vertex[i]->link == NULL){
            if(mode == 1) printf("ERROR: Edge Does Not Exist.\n");
            return -1;
        }
        vi = my_graph->vertex[i]->link;
        if(vi->data == data2){
            edge_i = vi;
            before_edge_i = my_graph->vertex[i];
        }
        else{
            while(vi->link != NULL){
                if(vi->link->data == data2){
                    edge_i = vi->link;
                    before_edge_i = vi;
                }
                vi = vi->link;
            }
        }
    }
    if(j != -1){
        if(my_graph->vertex[j]->link == NULL){
            if(mode == 1) printf("ERROR: Edge Does Not Exist.\n");
            return -1;
        }
        vj = my_graph->vertex[j]->link;
        if(vj->data == data1){
            edge_j = vj;
            before_edge_j = my_graph->vertex[j];
        }
        else{
            while(vj->link != NULL){
                if(vj->link->data == data1){
                    edge_j = vj->link;
                    before_edge_j = vj;
                }
                vj = vj->link;
            }
        }
    }
    if(edge_i == NULL || edge_j == NULL){
        if(mode == 1) printf("ERROR: Edge Does Not Exist.\n");
        return -1;
    }
    before_edge_i->link = edge_i->link;
    free(edge_i);
    before_edge_j->link = edge_j->link;
    free(edge_j);
    return 1;
}

void delete_vertex(GRAPH * my_graph, char data, int mode){
    int pos = position(my_graph, data);
    char ans[10]="";
    if(pos == -1){
        printf("ERROR: Vertex With Such Value Does Not Exist.\n");
        return;
    }
    VERTEX * vertex = NULL;
    //삭제할 것인지 다시 확인하기
    if(mode == 1){
        printf("ARE YOU SURE YOU WANT TO DELETE VERTEX %c?", data);
        vertex = my_graph->vertex[pos];
        if(vertex->link != NULL){
            vertex = vertex->link;
            printf("\nIT HAS EDGE BETWEEN ");
            while(vertex->link != NULL){
                printf("%c, ", vertex->data);
                vertex = vertex->link;
            }
            printf("%c. (Y/N)\n", vertex->data);
            scanf("%s", ans);
        }
        else{
            printf("(Y/N)\n");
            scanf("%s", ans);
        }
    }
    else{
        ans[0] = 'Y';
    }
    if(ans[0] == 'Y'){
        //해당 vertex 연결리스트 다 free 해주기
        vertex = my_graph->vertex[pos];
        while(my_graph->vertex[pos]->link != NULL){
            vertex = my_graph->vertex[pos];
            //printf("%c ", my_graph->vertex[pos]->data);
            while(vertex->link != NULL){
                //printf("%c %c", data, vertex->link->data);
                delete_edge(my_graph, data, vertex->link->data, 0);
                //vertex = vertex->link;
            }
        }
        //vertex = my_graph->vertex[pos];
        //free(vertex);
        //배열 밀어주기
        for(int i=pos;i<my_graph->size;i++){
            //printf("%c ", my_graph->vertex[i]->data);
            my_graph->vertex[i] = my_graph->vertex[i+1];
        }
        my_graph->vertex[my_graph->size] = NULL;
        my_graph->size--;
    }
    else if(ans[0]=='N'){
        printf("DELETE CANCELLED.\n");
    }
    return;
}

int is_connected(GRAPH * my_graph){
    VERTEX * vertex1;
    vertex1 = my_graph->vertex[1];
    if(vertex1->data == '\0') return 1;
    for(int i=1; i<=my_graph->size; i++){
        if(path(my_graph, vertex1->data, my_graph->vertex[i]->data) == 0){
            return 0;
        }
        clear_visited(my_graph);
    }
    return 1;
}

int num_of_vertex(GRAPH * my_graph){
    return my_graph->size;
}

int num_of_edge(GRAPH * my_graph){
    int cnt = 0;
    for(int i=1; i<=my_graph->size; i++){
        cnt += degree_of_vertex(my_graph, my_graph->vertex[i]->data);
    }
    cnt = cnt/2;
    return cnt;
}

void rename_vertex(GRAPH * my_graph, char old, char new){
    int i = position(my_graph, old);
    int j = position(my_graph, new);
    VERTEX * vertex;
    if (i == -1){
        printf("ERROR: Vertex With Such Value Does Not Exist.\n");
        return;
    }
    if (j != -1){
        printf("ERROR: Vertex With New Value Already Exists.\n");
        return;
    }
    my_graph->vertex[i]->data = new;
    for(int k=1; k<=my_graph->size; k++){
        if(my_graph->vertex[k]->data == new) continue;
        vertex = my_graph->vertex[k];
        while(vertex->link != NULL){
            if(vertex->link->data == old){
                vertex->link->data = new;
            }
            vertex = vertex->link;
        }
    }
    return;
}

void clear_graph(GRAPH * my_graph){
    for(int i=1; i<=my_graph->size;){ //증감문이 없는 이유는 delete vertex를 하며 알아서 size가 조정되고, 배열이 당겨지기 때문.
        delete_vertex(my_graph, my_graph->vertex[i]->data, 0);
    }
    return;
}

void print_edge(VERTEX * vertex){
    if(vertex->link == NULL){
        return;
    }
    printf("(");
    while(vertex->link != NULL){
        printf("%c", vertex->link->data);
        if(vertex->link->link != NULL){
            printf(",");
        }
        vertex = vertex->link;
    }
    printf(")");
}

void print_graph(GRAPH * my_graph){
    if(my_graph->size == 0){
        printf("Empty Graph.\n");
        return;
    }
    printf("(");
    for(int i=1; i<=my_graph->size; i++){
        printf("%c", my_graph->vertex[i]->data);
        print_edge(my_graph->vertex[i]);
        if(i!=my_graph->size){
            printf(", ");
        }
    }
    printf(")\n");
}

int is_eular(GRAPH* my_graph){ //오일러 그래프여부
    int count_odd = 0;
    int tmp;
    for(int i=1; i<=my_graph->size; i++){
        tmp = degree_of_vertex(my_graph, my_graph->vertex[i]->data);
        if(tmp % 2 == 1) count_odd++;
        if(tmp == 0) return 0;
    }
    if(count_odd == 0 || count_odd == 2){
        return 1;
    }
    return 0;
}

int main(void){ //메인 함수
    GRAPH my_graph;
    
    char inp[50]={}; //입력 받기 용 문자열
    
    int default_print = 1; //출력 관리용 변수. 1이면 출력
    
    for(int i=0;i<50;i++){
        my_graph.vertex[i] = NULL;
    }
    my_graph.size = 0; //G 실행안했을 경우 대비.
    
    int tmp;
    
    printf("명령문 안내\n");
    printf("G: 그래프 생성\n");
    printf("+정점의 값: 그래프에 정점 추가\n");
    printf("-정점의 값: 그래프에서 정점 제거\n");
    printf("E(정점1,정점2): 지정한 두 개의 정점을 잇는 간선 생성\n");
    printf("W(정점1,정점2): 지정한 두 개의 정점을 잇는 간선의 가중치 값 출력\n");
    printf("V(값): 현재 정점의 간선 개수 출력\n");
    printf("C: 연결 그래프인지를 출력\n");
    printf("N: 빈 그래프인지를 출력\n");
    printf("A(정점의 값): 해당 정점의 인접 정점 출력\n");
    printf("P(정점1,정점2): 정점1부터 정점2로가는 경로의 존재 여부 출력\n");
    printf("Q(정점1,정점2): 정점1부터 정점2로가는 경로 및 가중치 값 출력\n"); //자신만의 기능
    printf("X: 그래프의 정점의 수 출력\n");
    printf("H: 그래프의 간선의 수 출력\n");
    printf("D(정점1,정점2): 지정한 두 개의 정점을 잇는 간선 삭제\n");
    printf("R(정점,새로운 값): 지정한 정점의 값을 변경\n");
    printf("L: 그래프 출력\n");
    printf("U: 오일러 그래프인지를 출력\n");
    printf("K: 그래프 비우기\n");
    printf("&: 프로그램 종료\n\n"); //각 기능별 설명
    
    while(1){
        printf("명령어: ");
        
        scanf("%s",inp);
        getchar();
        if(inp[0] == '&'){
            break;
        }
        //printf("%s\n", inp);
        
        for(int i=0;i<=strlen(inp);i++){
            if(inp[i] == 'G'){
                create(&my_graph);
            }
            else if(inp[i] == '+'){
                if(inp[i+1] == '\0' || (inp[i+1] < 'A') || (inp[i+1] > 'Z')){
                    printf("ERROR: Invalid Input.\n");
                    continue;
                }
                else{
                    insert_vertex(&my_graph, inp[i+1]);
                    i++;
                }
            }
            else if(inp[i] == '-'){
                //printf("내가 왜 두번 나오지\n");
                if(inp[i+1] == '\0' || (inp[i+1] < 'A') || (inp[i+1] > 'Z')){
                    printf("ERROR: Invalid Input.\n");
                    continue;
                }
                else{
                    delete_vertex(&my_graph, inp[i+1], 1);
                    i++;
                }
            }
            else if(inp[i] == 'E'){
                if(inp[i+1] == '(' && inp[i+5] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2] && 'A'<=inp[i+4] && 'Z'>=inp[i+4]){
                        printf("Weight: ");
                        scanf("%d", &tmp);
                        add_edge(&my_graph, inp[i+2], inp[i+4], tmp);
                        i = i+5;
                    }
                }
            }
            else if(inp[i] == 'L'){
                continue;
            }
            else if(inp[i] == 'V'){
                if(inp[i+1] == '(' && inp[i+3] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2]){
                        printf("%d\n", degree_of_vertex(&my_graph, inp[i+2]));
                    }
                }
                i = i+3;
                default_print = 0;
            }
            else if(inp[i] == 'C'){
                if(is_connected(&my_graph)==1){
                    printf("True\n");
                }
                else{
                    printf("False\n");
                }
                default_print = 0;
            }
            else if(inp[i] == 'N'){
                if(is_empty(&my_graph)==1){
                    printf("True\n");
                }
                else{
                    printf("False\n");
                }
                default_print = 0;
            }
            else if(inp[i] == 'A'){
                if(inp[i+1] == '(' && inp[i+3] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2]){
                        adjacent(&my_graph, inp[i+2]);
                    }
                }
                i = i+3;
                default_print = 0;
            }
            else if(inp[i] == 'P'){
                if(inp[i+1] == '(' && inp[i+5] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2] && 'A'<=inp[i+4] && 'Z'>=inp[i+4]){
                        if(path(&my_graph, inp[i+2], inp[i+4])==1){
                            printf("True\n");
                        }
                        else{
                            printf("False\n");
                        }
                        clear_visited(&my_graph);
                    }
                    i = i+5;
                }
                default_print = 0;
            }
            else if(inp[i] == 'Q'){
                if(inp[i+1] == '(' && inp[i+5] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2] && 'A'<=inp[i+4] && 'Z'>=inp[i+4]){
                        printpath(&my_graph,inp[i+2], inp[i+4]);
                        clear_visited(&my_graph);
                    }
                    i = i+5;
                }
                default_print = 0;
            }
            else if(inp[i] == 'X'){
                printf("%d\n", num_of_vertex(&my_graph));
                default_print = 0;
            }
            else if(inp[i] == 'H'){
                printf("%d\n", num_of_edge(&my_graph));
                default_print = 0;
            }
            else if(inp[i] == 'D'){
                if(inp[i+1] == '(' && inp[i+5] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2] && 'A'<=inp[i+4] && 'Z'>=inp[i+4]){
                        delete_edge(&my_graph, inp[i+2], inp[i+4], 1);
                    }
                }
                i = i+5;
            }
            else if(inp[i] == 'R'){
                if(inp[i+1] == '(' && inp[i+5] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2] && 'A'<=inp[i+4] && 'Z'>=inp[i+4]){
                        rename_vertex(&my_graph, inp[i+2], inp[i+4]);
                    }
                }
                i = i+5;
            }
            else if(inp[i] == 'K'){
                clear_graph(&my_graph);
            }
            else if(inp[i] == 'U'){
                if(is_eular(&my_graph)==1){
                    printf("True\n");
                }
                else{
                    printf("False\n");
                }
                default_print = 0;
            }
            else if(inp[i] == 'W'){
                if(inp[i+1] == '(' && inp[i+5] == ')'){
                    if('A'<=inp[i+2] && 'Z'>=inp[i+2] && 'A'<=inp[i+4] && 'Z'>=inp[i+4]){
                        if(get_weight(&my_graph, inp[i+2], inp[i+4]) != -1){
                            printf("Weight: %d\n", get_weight(&my_graph, inp[i+2], inp[i+4]));
                        }
                    }
                    i = i+5;
                }
                default_print = 0;
            }
        }
        if(default_print==0){
            default_print = 1;
        }
        else{
            print_graph(&my_graph);
        }
    }
    return 0;
}
