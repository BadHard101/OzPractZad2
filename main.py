#Задание №2
#Нахождение суммы чисел между отрицательными числами первого и последнего вхождения в массиве

#нахождение индекса отрицательного числа в массиве
def FindNeg(mas):
    for i in range(len(mas)):
        if (mas[i]<0):
            return i
    return -1

#нахождение суммы элементов массива между заданными индексами
def SumBetwNeg(mas,N1,N2):
    Sum=0
    for i in range(N1+1,N2):
        Sum+=mas[i]
    return Sum


if __name__ == '__main__':
    n = int(input("Введите кол-во элементов массива (n): "))
    my_array = [0]*n
    for i in range(n):
        print(i,"й элемент:",sep='', end=" ")
        my_array[i] = int(input())

    #два индекса отрицательных чисел (Neg1-сначала, Neg2-с конца)
    Neg1 = FindNeg(my_array)
    Neg2 = len(my_array)-1-FindNeg(my_array[::-1])

    if (Neg1==-1 or Neg2==-1):
        print("Нет отрицательных значений в массиве")
    else:
        print(SumBetwNeg(my_array,Neg1,Neg2))
