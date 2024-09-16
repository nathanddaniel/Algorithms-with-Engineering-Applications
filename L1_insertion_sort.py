
def insertion_sort(A, n):
    """Sort a list or numpy array.

    Argument:
    A -- a list or numpy array
    n -- length of A
    """
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


