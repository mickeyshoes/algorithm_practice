#include <iostream>
#define MAX_NODE 10000

struct Node {
	int data;
	Node* next;
};

Node node[MAX_NODE];
int nodeCnt;
Node* head;

Node* getNode(int data) {
	node[nodeCnt].data = data;
	node[nodeCnt].next = nullptr;
	return &node[nodeCnt++];
}

void addNode2Head(int data) 
{
    Node* newNode = getNode(data);
    if(head->next != nullptr){
        newNode->next = head->next;
    }
    head->next = newNode;

    printf("start head\n");
    Node* n= head->next;
    for(int i=0; i<nodeCnt; i++){
        printf("%d\n", n->data);
        n = n->next;
    }

    //node 배열이 빈 경우
    //head는 새로운 노드를 가르키게 한다.

    // 아닌 경우
    //head가 가르키는 헤드를 새로운 노드가 가르키게 하고
    //head는 새로운 노드를 가르키게 한다
}

void addNode2Tail(int data) 
{
    Node* newNode = getNode(data);
    if (head->next==nullptr){
        head->next = newNode;
    }
    else{
        Node* n = head->next;
        while(n->next != nullptr){
          n = n->next;
        }
        n->next = newNode;
        newNode->next = nullptr;
    }

    printf("start tail\n");
    Node* n= head->next;
    for(int i=0; i<nodeCnt; i++){
        printf("%d\n", n->data);
        n = n->next;
    }
    //node 배열이 빈 경우
    //head 는 새로운 노드를 가르키게 한다.

    //아닌경우
    // nodeCnt번 반복을 돌아서 꼬리를 알아낸 후에
    // 꼬리를 변경해준다.

}

void addNode2Num(int data, int num) 
{
    //node 배열이 비어있음 
    //num이 1이 아닌 경우와 1인 경우
    if (nodeCnt == 0){
        if (num == 1)
            addNode2Head(data);
    }
    else{
        int cnt = 1;
        if(num<=nodeCnt){
            Node* n = head->next;
            while(cnt != num-1){
                n = n->next;
                cnt+=1;
            }
            Node* newNode = getNode(data);
            newNode->next = n->next;
            n->next = newNode;

        }
    }

    printf("start num\n");
    Node* n= head->next;
    for(int i=0; i<nodeCnt; i++){
        printf("%d\n", n->data);
        n = n->next;
    }

    //node 배열이 차있음
    //num 의 값이 nodeCnt 보다 작은 경우와 큰 경우
        // 삽입 위치의 이전 노드는 새로운 노드를 가르키고
        // 새로운 노드는 이전 노드가 가진 주소를 가르킨다.

}

void removeNode(int data) 
{

    //값이 없다면 안한다.
    //값이 없는 경우 = 데이터가 같지 않거나 끝까지 탐색한 경우
    //삭제하는 노드가 가지고 있는 주소값을 삭제 이전 노드가 가리켜야 해서 필요하다.

    Node* n = head->next;
    while(n->data != data && n->next != nullptr){
        if(n->next->data == data)
            break;
        n = n->next;
    }

    if(n->next != nullptr){
        //삭제할 노드가 다음 값을 가르키는 경우
        if(n->next->next != nullptr)
            n->next = n->next->next;
        //삭제할 노드가 가르키고 있는 다음 값이 없는 경우
        else
            n->next = nullptr;

        // 삭제할 노드가 속한 노드 배열의 인덱스 탐색
        int idx = nodeCnt;
        for(int i=0; i<nodeCnt; i++){
            if (node[i].data == data){
                idx = i;
            }
        }
        // 삭제할 노드 인덱스가 중간에 있을경우 끝값을 중간으로 이동
        if (idx != nodeCnt-1){
            node[idx] = node[nodeCnt-1];
        }
        nodeCnt-=1;

        printf("del node\n");
        Node* n= head->next;
        for(int i=0; i<nodeCnt; i++){
            printf("%d\n", n->data);
            n = n->next;
        }

    }
    
}

int main(void)
{
    head = new Node();
    head->next = nullptr;
    nodeCnt = 0;
    
    addNode2Head(1);
    addNode2Head(2);
    addNode2Head(4);
    //addNode2Tail(1);
    //addNode2Tail(2);
    //addNode2Tail(4);
    addNode2Num(3,3);
    removeNode(3);
    printf("test\n");
    removeNode(9);
    //addNode2Tail(4);

    return 0;
}