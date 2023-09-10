class Solution {
public:

    struct Compare{
      bool operator() (const vector<int>& v1, const vector<int>& v2) {
        return (v1[0] * v1[0] + v1[1] * v1[1]) < (v2[0] * v2[0] + v2[1] * v2[1]); 
      }
    };

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>, vector<vector<int>>, Compare> pq;

        for (vector<int> point : points) {
          pq.push(point);

          if (pq.size() > k) {
            pq.pop();
          }
        }

        vector<vector<int>> res;

        while (!pq.empty()) {
          res.push_back(pq.top());
          pq.pop();
        }

        return res;
    }
};