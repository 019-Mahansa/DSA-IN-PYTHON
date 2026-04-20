#include <iostream>
using namespace std;

void insertion_sort(int arrays[],int n);
int main(){
    int arrays[] = {10,2,4,6,8,9,7,5,3,1};
    int n = sizeof(arrays)/sizeof(arrays[0]);

    insertion_sort(arrays,n);

    for(int i = 0; i < n; i ++){
        cout << arrays[i] << " ";
    }
}

void insertion_sort(int arrays[],int n){
    for(int i = 1; i < n; i++){
        int anchor = arrays[i];
        int j = i-1;
        while  (j >= 0 && anchor < arrays[j]){
            arrays[j+1] = arrays[j];
            j = j - 1;
        }
        arrays[j + 1] = anchor;
    }
}