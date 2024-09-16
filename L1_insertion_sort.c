#include <stdio.h>
#include <stdlib.h>

#define N 10

int array[N];

void print_list(int a[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%3d ", a[i]);
    }
    printf("\n");
}

void InsertionSort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i];
        int j = i - 1;

        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j -= 1;
        }
        a[j + 1] = key;
    }
}

int main(void) {

    printf("Lab 1 - insertion sort\n");
    for(int i = 0; i < N; i++){
        array[i] = rand() >> 24;
    }

    printf("List before sorting\n");
    print_list(array, N);

    InsertionSort(array, N);

    printf("List after sorting\n");
    print_list(array, N);
    return 0;
}
