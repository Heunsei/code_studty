#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

vector<int> height;
vector<int> width;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int x,y,t;
    int maxWidth, maxHeight;
    cin >> x >> y;
    cin >> t;
    for(int i{0}; i<t; i++){
        int s,e;
        cin >> s >> e;
        if(s){
            width.push_back(e);
        }else {
            height.push_back(e);
        }
    }
    width.push_back(x);
    height.push_back(y);
    sort(width.begin(), width.end());
    sort(height.begin(), height.end());

    if(height.size() == 0){
        maxHeight = y;
    }else{
        maxHeight = 0;
        for(int i{0}; i<height.size(); i++){
            if(i == 0){
                maxHeight = height[i];
            }else{
                if(maxHeight < height[i] - height[i-1]){
                    maxHeight = height[i] - height[i-1];
                }
            }
        }
    }
    if(width.size() == 0){
        maxWidth = x;
    }else{
        maxWidth = 0;
        for(int i{0}; i<width.size(); i++){
            if(i == 0){
                maxWidth = width[i];
            }else{
                if(maxWidth < width[i] - width[i-1]){
                    maxWidth = width[i] - width[i-1];
                }
            }
        }
    }
    cout << maxWidth * maxHeight;
    return 0;
}