import winsound 
import time

def merge_sort(arr, level=0):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, level + 1)
        merge_sort(R, level + 1)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            print(f"Level {level}: {arr}")
            winsound.Beep(1000, 100)  # Sound effect for each comparison

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            print(f"Level {level}: {arr}")
            winsound.Beep(1000, 100)

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            print(f"Level {level}: {arr}")
            winsound.Beep(1000, 100)

if __name__ == "__main__":
    arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
    print("Original array:", arr)
    merge_sort(arr)
    print("Sorted array:", arr)