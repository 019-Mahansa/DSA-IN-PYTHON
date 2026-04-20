#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
void bucket_sort(vector<int>& data);
int main(){
    vector<int> list = {65,2,3,5,10};
    // int length = sizeof(list)/sizeof(list[0]);

    bucket_sort(list);
    for(int num : list){
        cout << num << " ";
    }

}

void bucket_sort(vector<int>& data){
    int n = data.size();
    if (n<= 1) return;

    int min_val = *min_element(data.begin(), data.end());
    int max_val = *max_element(data.begin(), data.end());

    int num_buckets = 10;
    vector<vector<int>> buckets(num_buckets);

    for (int num : data) {
        int bucket_index = (num - min_val) * num_buckets / (max_val - min_val + 1);
        if (bucket_index >= num_buckets) bucket_index = num_buckets - 1;  
        buckets[bucket_index].push_back(num);  
    }
    
    for (auto& bucket : buckets) {
        sort(bucket.begin(), bucket.end());
    }
    
    int index = 0;
    for (const auto& bucket : buckets) {
        for (int num : bucket) {
            data[index++] = num;
        }
    }

}
