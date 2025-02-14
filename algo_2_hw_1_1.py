def find_min_max(arr):
    def divide_and_conquer(arr, left, right):
        # Базовий випадок: один елемент
        if left == right:
            return (arr[left], arr[left])
        
        # Базовий випадок: два елементи
        if right - left == 1:
            if arr[left] < arr[right]:
                return (arr[left], arr[right])
            else:
                return (arr[right], arr[left])
        
        # Ділимо масив на дві частини
        mid = (left + right) // 2
        min1, max1 = divide_and_conquer(arr, left, mid)
        min2, max2 = divide_and_conquer(arr, mid + 1, right)
        
        # Об'єднуємо результати
        return (min(min1, min2), max(max1, max2))
    
    if not arr:
        raise ValueError("Масив не може бути порожнім")
    
    return divide_and_conquer(arr, 0, len(arr) - 1)

# Приклад використання
arr = [3, 5, 1, 9, 2, 8, 7, 4]
print(find_min_max(arr)) 