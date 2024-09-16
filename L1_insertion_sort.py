import random
from array import array

N = 10
list = array('i', [0] * N)

def insertion_sort(A, n):
    # Traverse the list or array from index 1 to n-1.
    for i in range(1, n):
        key = A[i]

        # Insert A[i] into the sorted subarray A[0:i].
        # Compare stored key with the already sorted values to its left.
        # Move each item one position to the right until we find the
        # position for the key or fall off the left end of the list or array.
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1

        # Insert key at the correct position in the list or array.
        A[j + 1] = key

def print_list(A, n):
    for i in range (0, n):
        print(" %3d" % (A[i]), end="")
    print()

def main():
    print("LAB 1 - INSERTION SORT")

    for i in range(0, N):
        list[i] = random.randint(0, 99)

    print("LIST BEFORE SORT")
    print_list(list, N)

    print("LIST AFTER SORT")
    insertion_sort(list, N)
    print_list(list, N)


if __name__ == "__main__":
	main()