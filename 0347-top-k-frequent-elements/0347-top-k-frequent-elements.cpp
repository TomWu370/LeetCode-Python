class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> freq;
        priority_queue<pair<int, int>> queue(freq.begin(), freq.end());
        vector<int> ans;
        for (int i: nums){
            freq[i] ++;
        }

        while (!freq.empty()){
            queue.push({freq.begin()->second, freq.begin()->first});
            freq.erase(freq.begin());
        }
        for (int i=0; i < k; i++){
            ans.push_back(queue.top().second);
            queue.pop();
        }
        return ans;
    }
};

// use a frequency map, see python version for details
// use freq[i] ++; to tally up frequency, if not defined then the map will define the key itself
// the syntax of the push operation essentially pushes an initialised valid pair of (key, value) tuple onto the queue
// the {} initialises such tuple pair
// and begin() accesses the first key value pair of the iterator pointer
// and -> first/second simply selects the first/second element of such pair/triplet
// in this case first means the key and second means the value
// in conclusion, sinc a priority queue will automatically sort by highest priority or in this case value
// by pushing the value/frequency of a pair into the queue, will let it auto sort
// then we erase this pair and repeat the pushing process until all elements are pushed
// we then use queue.top() to access the highest priority element, then use .second() to get the stored key