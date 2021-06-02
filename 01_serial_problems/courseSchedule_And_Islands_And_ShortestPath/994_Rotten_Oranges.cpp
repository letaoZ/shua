#include <iostream>
#include <bits/stdc++.h>

using namespace std;


class Solution{
public:
    int orangesRotting(vector <vector<int>> & grid){
        int M = grid.size();
        int N = grid[0].size();
        int cnt_orange = 0;

        vector< vector<int> > dir{
            {0,1},
            {0,-1},
            {-1,0},
            {1,0}
        };
        queue<pair<int,int>> q; // store rotten
        for(int i=0;i<M; ++i)
            for(int j=0; j<N; ++j){
                if (grid[i][j] ==2)
                    q.emplace(i,j); // equivalent to q.push_back(make_pair(i,j))
                if (grid[i][j] == 1)
                    cnt_orange += 1;
            }
        if (cnt_orange == 0)
            return 0;


        int orangen = 0;
        int minutes = -1;
        while(!q.empty()){
            int L = q.size();
            for(int i=0; i<L ; ++i){
                pair<int,int> pt = q.front();
                q.pop();
                for(auto v:dir){
                    int x= pt.first + v[0];
                    int y = pt.second + v[1];
                    if (x>=M or y>=N or x<0 or y<0 )
                        continue;
                    if (grid[x][y] != 1)
                        continue;
                    orangen += 1;
                    grid[x][y] = 2;
                    q.emplace(x,y);
                }
            }
            minutes += 1;

        }
        if (orangen <cnt_orange)
            return -1;
        return minutes;

    }

};


int main(){

    vector< vector<int>> grid{
        {2,1,1},
        {0,1,1},
        {2,0,1}
    }; 

    Solution solu;
    int res = solu.orangesRotting(grid);
    cout<<res<<endl;

    return 0;

}