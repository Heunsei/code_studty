// 베스트앨범
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

void musicCntSort(const map<string, int> & music_cnt);
void musicListSort(const map<string, vector<pair<int, int>>>& music_list);

bool cmp(const pair<string, int>& a,const pair<string, int> &b);
bool musicCmp(const pair<int, int>& a, const pair<int, int> &b);
map<string, vector<pair<int, int>>> top_2_music;
vector<int> answer;

vector<int> solution(vector<string> genres, vector<int> plays) {
    map<string, int> play_cnt;
    map<string, vector<pair<int, int>>> music_list;
    
    for(int i{0}; i< genres.size(); i++){
        if(play_cnt.find(genres[i]) == play_cnt.end()){
            play_cnt.insert({genres[i], plays[i]});
            vector<pair<int, int>> tmp;
            tmp.push_back(make_pair(plays[i], i));
            music_list.insert({genres[i], tmp});
        } else {
            play_cnt[genres[i]] += plays[i];
            music_list[genres[i]].push_back(make_pair(plays[i], i));
        }
    }
    musicListSort(music_list);
    musicCntSort(play_cnt);
    return answer;
}

bool cmp(const pair<string, int>& a,const pair<string, int> &b){
    return a.second > b.second;
}

bool musicCmp(const pair<int, int>& a, const pair<int, int> &b){
    if(a.first == b.first){
        return a.second < b.second;
    }else {
        return a.first > b.first;
    }
}

void musicCntSort(const map<string, int>& music_cnt){
    vector<pair<string, int>> vec;
    for(auto& m : music_cnt){
        vec.push_back(m);
    }
    sort(vec.begin(), vec.end(), cmp);
    for(auto& i : vec){
        cout << i.first << " " << i.second << '\n';
        for(auto& j : top_2_music[i.first]){
            answer.push_back(j.second);
            cout << typeid(j.second).name() << '\n';
        }
    }
}

void musicListSort(const map<string, vector<pair<int, int>>>& music_list){
    using namespace std;
    vector<pair<string, vector<pair<int, int>>>> vec;
    for(auto& m : music_list){
        vec.push_back(m);
    }
    
    for(auto& i : vec){
        sort(i.second.begin(), i.second.end(), musicCmp);
        int cnt = 0;
        for(auto& j : i.second){
            if(cnt >= 2) break;
            if(top_2_music.find(i.first) == top_2_music.end()){
                vector<pair<int, int>> tmp;
                tmp.push_back(make_pair(j.first, j.second));
                top_2_music.insert({i.first, tmp});
            } else {
                top_2_music[i.first].push_back(make_pair(j.first, j.second));
            }
            cout << j.first << ' ' << j.second << '\n';
            cnt++;
        }
    }
}