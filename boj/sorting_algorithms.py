
# 시간 복잡도는 O(n^2)
# 장점: 구현이 매우 간단하고, 소스코드가 직관적이다. 안정 정렬이다. 
#      추가적인 메모리 공간이 필요하지 않다. (in-place sorting)
# 단점: 시간 복잡도가, 최악, 최선, 평균일 때 모두 O(n^2)으로 매우 비효율적이다. 
#      정렬되지 않은 원소가 정렬되었을 때의 위치로 가기 위해서 교환 연산이 많이 일어나게 된다. 
def bubble_sort(elements):
    n = len(elements)
    for i in range(n):
        for j in range(1, n-i):
            if elements[j-1] > elements[j]:
                elements[j-1], elements[j] = elements[j], elements[j-1]

    return elements

# O(n^2)
# 장점: 구현이 단순하다. 버블 소트에 비해 교환 연산의 수가 적다. 
#      추가적인 메모리 공간을 필요로 하지 않는다. 
# 단점: 시간 복잡도가, 최악, 최선, 평균일 때 모두 O(n^2)으로 매우 비효율적이다.
#      불안정 정렬이다. 
def selection_sort(elements): 
    n = len(elements)
    for i in range(n-1): 
        idx_min  = i
        for j in range(i+1, n): 
            if elements[j] < elements[idx_min]: 
                idx_min = j
        elements[i], elements[idx_min] = elements[idx_min], elements[i]

    return elements


print(
    selection_sort([11, 2, 3, 6, 32, 4, 1, 5])
)
