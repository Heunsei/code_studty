#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>

using namespace std;

template <typename T>
struct Edge {
	unsigned src;
	unsigned dst;
	T weight;
};

template <typename T>
class Graph {
	public:
		Graph(unsigned N): V(N) {}
		// 그래프의 정점 갯수 반환
		auto vertices() const {return V;}
		auto& edges() const {return edge_list;}

		auto edges(unsigned v) const {
			vector<Edge<T>> edges_from_v;
			for(auto& e: edge_list){
				if(e.src == v){
					edges_from_v.emplace_back(e);
				}
			}
			return edges_from_v;
		}

		void add_edges(Edge<T>&& e){
			if(e.src >= 1 && e.src <=V && e.dst >=1 && e.dst <=V)
				edge_list.emplace_back(e);
			else cerr << "error";
		}
		
		template <typename U>
		friend ostream& operator<< (ostream& os, const Graph<U>& G);

	private:
		unsigned V;
		vector<Edge<T>> edge_list;
};

template <typename U>
ostream& operator<< (ostream& os, const Graph<U> G){
	for(unsigned i = 1; i<G.vertices(); i++){
		os << i << ":\t";
		
	}
}
