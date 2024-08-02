def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    else:
        array3 = [i * i for i in array1]
    array2.sort()
    array3.sort()
    return array3 == array2
print(comp(array1=[121, 144, 19, 161, 19, 144, 19, 11], array2=[11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))
	