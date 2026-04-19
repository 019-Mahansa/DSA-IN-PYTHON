#include <iostream>
using namespace std;

void Bubble_sort(int arrays[],int n);

int main(){
    int arrays[] = {10,2,4,6,8,9,7,5,3,1};
    int n = sizeof(arrays)/sizeof(arrays[0]);

    Bubble_sort(arrays,n);

    for(int i = 0; i < n; i++){
        cout << arrays[i] << " " ; //return tidak menggunakan array lagi karena ketika kita panggil arrays nya langsung maka output yang keluar adalah memory addess nya
    }
}
void Bubble_sort(int arrays[],int n){
    for(int i = 0; i < n-1; i++){
        for(int j = 0; j < n - i - 1; j++){
            if (arrays[j] > arrays[j+1]){
                int temp = arrays[j];
                arrays[j] = arrays[j+1];
                arrays[j+1] = temp;
            }else{
                continue;
            }
        }
    }
}