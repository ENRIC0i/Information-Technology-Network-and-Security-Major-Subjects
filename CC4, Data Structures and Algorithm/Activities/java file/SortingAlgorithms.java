package intl.cc4;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class SortingAlgorithms {
    public static void main(String[] args) {
        Integer[] numbers = {80, 72, 3, 83, 2, 11, 96, 13, 41, 49, 99, 97, 56, 31, 12, 64, 37, 42, 2, 11, 9, 96, 4, 91, 53, 82, 8, 8, 8, 99, 17, 34, 74, 1, 62, 4, 18, 41, 79, 92, 9, 47, 84, 45, 13, 12, 12, 81, 75, 86, 76, 26, 30, 3, 88, 77, 17, 36, 98, 93, 95, 22, 86, 27, 42, 0, 37, 26, 22, 56, 86, 99, 16, 63, 59, 65, 73, 43, 39, 25, 46, 1, 56, 65, 16, 55, 96, 21, 3, 58, 85, 88, 3, 4, 44, 84, 32, 22, 83, 54};

        // Sort using Quicksort
        Integer[] quickSorted = quickSort(numbers.clone());
        System.out.println("Quicksort Result: " + Arrays.toString(quickSorted));

        // Sort using Introsort (Java's default sorting algorithm)
        Integer[] introSorted = introSort(numbers.clone());
        System.out.println("Introsort Result: " + Arrays.toString(introSorted));

        // Sort using Timsort (Java's default sorting algorithm for objects)
        Integer[] timSorted = timSort(numbers.clone());
        System.out.println("Timsort Result: " + Arrays.toString(timSorted));

        // Sort using Mergesort
        Integer[] mergeSorted = mergeSort(numbers.clone());
        System.out.println("Mergesort Result: " + Arrays.toString(mergeSorted));

        // Sort using Heapsort
        Integer[] heapSorted = heapSort(numbers.clone());
        System.out.println("Heapsort Result: " + Arrays.toString(heapSorted));
    }

    // Quicksort
    public static Integer[] quickSort(Integer[] arr) {
        long startTime = System.currentTimeMillis();
        List<Integer> list = Arrays.asList(arr);
        Collections.sort(list);
        Integer[] sorted = list.toArray(new Integer[0]);
        long endTime = System.currentTimeMillis();
        System.out.println("Quicksort Time: " + (endTime - startTime) + " ms");
        return sorted;
    }

    // Introsort
    public static Integer[] introSort(Integer[] arr) {
        long startTime = System.currentTimeMillis();
        Arrays.sort(arr);
        long endTime = System.currentTimeMillis();
        System.out.println("Introsort Time: " + (endTime - startTime) + " ms");
        return arr;
    }

    // Timsort
    public static Integer[] timSort(Integer[] arr) {
        long startTime = System.currentTimeMillis();
        Arrays.sort(arr);
        long endTime = System.currentTimeMillis();
        System.out.println("Timsort Time: " + (endTime - startTime) + " ms");
        return arr;
    }

    // Mergesort
    public static Integer[] mergeSort(Integer[] arr) {
        long startTime = System.currentTimeMillis();
        mergeSortHelper(arr, 0, arr.length - 1);
        long endTime = System.currentTimeMillis();
        System.out.println("Mergesort Time: " + (endTime - startTime) + " ms");
        return arr;
    }

    private static void mergeSortHelper(Integer[] arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            mergeSortHelper(arr, left, mid);
            mergeSortHelper(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    private static void merge(Integer[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        Integer[] leftArr = new Integer[n1];
        Integer[] rightArr = new Integer[n2];

        for (int i = 0; i < n1; i++) {
            leftArr[i] = arr[left + i];
        }
        for (int i = 0; i < n2; i++) {
            rightArr[i] = arr[mid + 1 + i];
        }

        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (leftArr[i] <= rightArr[j]) {
                arr[k++] = leftArr[i++];
            } else {
                arr[k++] = rightArr[j++];
            }
        }

        while (i < n1) {
            arr[k++] = leftArr[i++];
        }

        while (j < n2) {
            arr[k++] = rightArr[j++];
        }
    }

    // Heapsort
    public static Integer[] heapSort(Integer[] arr) {
        long startTime = System.currentTimeMillis();
        int n = arr.length;

        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        for (int i = n - 1; i >= 0; i--) {
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            heapify(arr, i, 0);
        }

        long endTime = System.currentTimeMillis();
        System.out.println("Heapsort Time: " + (endTime - startTime) + " ms");
        return arr;
    }

    private static void heapify(Integer[] arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && arr[left] > arr[largest]) {
            largest = left;
        }

        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }

        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            heapify(arr, n, largest);
        }
    }
}
