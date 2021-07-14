import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
tree = {}
for _ in range(N):
    root, left, right = input().rstrip('\n').split()
    tree[root] = [left,right]

def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if tree[node][0] != '.':
        inorder(tree[node][0])
    print(node, end='')
    if tree[node][1] != '.':
        inorder(tree[node][1])

def postorder(node):
    if tree[node][0] != '.':
        postorder(tree[node][0])
    if tree[node][1] != '.':
        postorder(tree[node][1])
    print(node, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')