#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>

using namespace std;

class SimpleDisjoinSet {
	private:
		struct Node {
			unsigned id;
			unsigned rank;
			unsigned parent;
			Node(unsigned _id): id(_id), rank(0), parent(_id) {}
			bool operator != (const Node& n) const {
				return this->id != n.id;
			}
		};

		vector<Node> nodes;

		public:
			SimpleDisjoinSet(unsigned N){
				nodes.reserve(N);
			}

			void make_set(const unsigned& x){
				nodes.emplace_back(x);
			}

			unsigned find(unsigned x){
				auto node_it = find_if(nodes.begin(), nodes.end(),
				[x](auto n){ return n.id == x; });
				unsigned node_id = (*node_it).id;

				while(node_id != nodes[node_id].parent){
					node_id = nodes[node_id].parent;
				}

				return node_id;
			}

			void union_sets(unsigned x, unsigned y){
				auto root_x = find(x);
				auto root_y = find(y);

				if(root_x == root_y) return;

				if(nodes[root_x].rank > nodes[root_y].rank){
					swap(root_x, root_y);
				}
				nodes[root_x].parent = nodes[root_y].parent;
				nodes[root_y].rank++;
			}
};

template <typename T>
struct Edge{
	unsigned src;
	unsigned dst;
	T weight;

	// 읽기 전용 함수 구현
	inline bool operator< (const Edge<T>& a) const {
		return this->weight < a.weight;
	}

	inline bool operator> (const Edge<T>& a) const {
		return this->weight > a.weight;
	}
};

template <typename T>
class Graph {
	public:
		Graph(unsigned N): V(N) {}

		auto vertices() const {return V;}
		auto& edges() const {return edeg_list;}

		auto& edges(unsigned v) const {
			vector<Edge<T>> edges_from_v;
			for(auto& e: edge_list){
				if(e.src == v) edges_from_v.emplace_back(e);
			}
			return edges_from_v;
		}

		void add_edges(Edge<T>&& a){
			if(e.src >= 1 && e.src <= V && e.dst >=1 && e.dst <= V) edge_list.emplace_back(e);
			else cerr << "error";
		}

		template <typename T>
		friend ostream& operator<< (ostream& os, const Graph<U>& G);

		private:
			unsigned V;
			vector<Edge<T>> edge_list;
};

template <typename U>
ostream& operator<< (ostream& os, const Graph<U>& G){
	for(unsigned i = 1; i< G.vertices(); i++){
		os << i << ":\t";
		auto edges = G.edges(i);
		for(auto& e: edges){
			os << "{" << e.dst << ": " << e.weight << "}, ";
		}
		os << endl;
	}
	return os
}

template <typename T>
Graph<T> minimum_spanning_tree(const Graph<T>& G){
	priority_queue<Edge<T>,vector<Edge<T>>, greater<Edge<T>>> edge_min_heap;

	for(auto& e: G.edges){
		edge_min_heap.push(e)
	}

	auto N = G.vertices();
	SimpleDisjoinSet dset(N);
	for(unsigned i = 0; i<N; i++) dset.make_set(i);

	Graph<T> MST(N);
	while(!edge_min_heap.empty()){
		auto e = edge_min_heap.top();
		edge_min_heap.pop();
		if(dset.find(e.src) != dset.find(e.dst)){
			MST.add_edges(Edge<T>{e.src, e.dst, e.weight});
			dset.union_sets(e.src, e.dst);
		}
	}
	return MST;
}