class Solution {
public:
    int n;
    vector<int> father;
    Solution() {
        n = 1005;
        father = vector<int>(n);

        for (int i = 0; i < n; i++) {
            father[i] = i;
        }
    }

    int find(int u) {
        if (father[u] == u) {
            return u;
        }
        father[u] = find(father[u]);

        return father[u];
    } 

    void join(int u, int v) {
        u = find(u);
        v = find(v);

        if (u == v) {
            return;
        }

        father[v] = u;
    }

    bool isSame(int u, int v) {
        if (find(u) == find(v)) {
            return true;
        }

        return false;
    } 
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
       for (vector<int> edge : edges) {
           if (isSame(edge[0], edge[1])) {
               return edge;
           } else {
               join(edge[0], edge[1]);
           }
       }

        vector<int> res;
       return res;
    }
};