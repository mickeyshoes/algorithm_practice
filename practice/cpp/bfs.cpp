#include <iostream>
#include <vector>
#include <queue>

using namespace std;

bool is_range(int x, int y, int N){
    return (0<=x && x<N && 0<=y && y<N);
}


int BFS(int depth, vector<vector<int> > ary, int N){
    int result = 0;
    bool visited[N][N];
    int dx[] = {1,0,0,-1};
    int dy[] = {0,1,-1,0};
    queue< pair<int,int> > q;


    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            visited[i][j]=false;
        }
    }

    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            if(ary[i][j] > depth && !visited[i][j]){
                visited[i][j] = true;
                result +=1;
                q.push(make_pair(i,j));

                while (!q.empty()){
                    pair<int,int> coord = q.front();
                    q.pop();

                    for (int k=0; k<4; k++){
                        int tx = coord.first + dx[k];
                        int ty = coord.second + dy[k];

                        if(is_range(tx,ty,N) && !visited[tx][ty] && ary[tx][ty]>depth){
                            visited[tx][ty] = true;
                            q.push(make_pair(tx,ty));
                        }
                    }

                }

            }
        }
    }
    return result;
}

int main(int argc, char** argv)
{
    int N;
    cin>>N;
    vector< vector<int> > ary(N,vector<int>(N,0));

    int max_value = 0;
    int answer = 1;
    //define array
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            cin >> ary[i][j];
            max_value = max(max_value, ary[i][j]);
        }
    }
    
    for (int i=1; i<max_value; i++){
        answer = max(answer, BFS(i, ary, N));
    }

	return 0;
}