import random

def quick_select(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k має бути в межах довжини масиву")
    
    def partition(left, right):
        pivot_index = random.randint(left, right)
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1
        
        arr[store_index], arr[right] = arr[right], arr[store_index]
        return store_index
    
    def select(left, right, k_smallest):
        if left == right:
            return arr[left]
        
        pivot_index = partition(left, right)
        
        if k_smallest == pivot_index:
            return arr[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)
    
    return select(0, len(arr) - 1, k - 1)

# Приклад використання
arr = [7, 10, 4, 3, 20, 15]
k = int(input("Введіть значення k: "))
print(f"{k}-й найменший елемент: {quick_select(arr, k)}")
 