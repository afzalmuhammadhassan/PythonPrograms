def subsets(num):
    temp_result = []
    subsets_utils(num, [0 for i in range(len(num))], temp_result, 0)
    main_result = []
    for lists in temp_result:
        temp = []
        for i in range(len(lists)):
            if lists[i] == 1:
                temp.append(num[i])
        main_result.append(temp)
    return main_result


def subsets_utils(num, temp, result, index):
    if index == len(num):
        result.append([i for i in temp])
        print(result)
        return
    temp[index] = 0
    subsets_utils(num, temp, result, index + 1)
    temp[index] = 1
    subsets_utils(num, temp, result, index + 1)


