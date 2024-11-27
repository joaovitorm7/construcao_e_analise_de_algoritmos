#include <stdio.h>

void bubbleSort(int arr[], int n) {
    int i, j, temp;
    int trocou;

    for (i = 0; i < n - 1; i++) {
        trocou = 0;
        for (j = 0; j < n - i; j++){
            if(arr[j] > arr[j + 1]){
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                trocou = 1;
            }
        }
        if (!trocou) break;
    }
}