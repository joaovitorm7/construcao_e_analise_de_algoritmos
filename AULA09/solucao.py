def MaxCrossingSum(arr, left, middle, right):
    leftSum = float('-inf')
    total = 0
    for i in range(middle, left - 1, -1):
        total = total + arr[i]
        if (total > leftSum):
            left = total
    
    rightSum = float('-inf')
    total = 0
    for i in range(middle + 1, right + 1):
        total = total + arr[i]
        if(total > rightSum):
            rightSum = total

    return leftSum + rightSum


def MaxSubarraySum(arr, left, right):
    if left == right:
        return arr[left] # Caso base: subvetor com um único elemento
    
    middle = (left + right) // 2

    # 1. Subvetor inteiramente à esquerda do meio
    leftMax = MaxSubarraySum(arr, left, middle)

    # 2. Subvetor inteiramente à direita do meio
    rightMax = MaxSubarraySum(arr, middle + 1, right)

    # 3. Subvetor que cruza o meio
    crossingMax = MaxCrossingSum(arr, left, middle, right)

    # Retorna o maior valor entre os três casos
    return max(leftMax, rightMax, crossingMax)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
resultado = MaxSubarraySum(arr, 0, len(arr) - 1)
print("Soma máxima do subarray:", resultado)

    