
array1 = [00, 00, 00, 11, 12, 13, 00, 00, 00, 00, 00, 00]
array2 = [00, 00, 00, 14, 15, 16, 00, 00, 00, 00, 00, 00]
array3 = [00, 00, 00, 17, 18, 19, 00, 00, 00, 00, 00, 00]
array4 = [41, 42, 43, 21, 22, 23, 51, 52, 53, 61, 62, 63]
array5 = [44, 45, 46, 24, 25, 26, 54, 55, 56, 64, 65, 66]
array6 = [47, 48, 49, 27, 28, 29, 57, 58, 59, 67, 68, 69]
array7 = [00, 00, 00, 31, 32, 33, 00, 00, 00, 00, 00, 00]
array8 = [00, 00, 00, 34, 35, 36, 00, 00, 00, 00, 00, 00]
array9 = [00, 00, 00, 37, 38, 39, 00, 00, 00, 00, 00, 00]



array_mosse = [00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00]
array_soluzioni = []
movimento_completo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#funzioni temporanee
def print_arrays():
    print(array1)
    print(array2)
    print(array3)
    print(array4)
    print(array5)
    print(array6)
    print(array7)
    print(array8)
    print(array9)
    return

print_arrays()
##dichiarazioni funzioni
#funzioni standard
def front():
    global array3
    global array4
    global array5
    global array6
    global array7
    global array_mosse
    global array_soluzioni

    i = 0

    while(i <= 20):

        if (i <= 2):
            counter_array = i + 3
            array_mosse[i] = array3[counter_array]
        elif (i > 2 and i <= 7):
            counter_array = i - 1
            array_mosse[i] = array4[counter_array]
        elif (i > 7 and i <= 12):
            counter_array = i - 6
            array_mosse[i] = array5[counter_array]
        elif (i > 12 and i <= 17):
            counter_array = i - 11
            array_mosse[i] = array6[counter_array]
        else:
            counter_array = i - 15
            array_mosse[i] = array7[counter_array]
        i = i + 1

    array4[6] = array_mosse[0]
    array5[6] = array_mosse[1]
    array6[6] = array_mosse[2]
    array3[5] = array_mosse[3]
    array4[5] = array_mosse[4]
    array5[5] = array_mosse[5]
    array6[5] = array_mosse[6]
    array7[5] = array_mosse[7]
    array3[4] = array_mosse[8]
    array4[4] = array_mosse[9]
    array6[4] = array_mosse[11]
    array7[4] = array_mosse[12]
    array3[3] = array_mosse[13]
    array4[3] = array_mosse[14]
    array5[3] = array_mosse[15]
    array6[3] = array_mosse[16]
    array7[3] = array_mosse[17]
    array4[2] = array_mosse[18]
    array5[2] = array_mosse[19]
    array6[2] = array_mosse[20]
    array_soluzioni.append("F")
    return

def front_inv():
    global array3
    global array4
    global array5
    global array6
    global array7
    global array_mosse
    global array_soluzioni

    i = 0

    while (i <= 20):

        if (i <= 2):
            counter_array = i + 3
            array_mosse[i] = array3[counter_array]
        elif (i > 2 and i <= 7):
            counter_array = i - 1
            array_mosse[i] = array4[counter_array]
        elif (i > 7 and i <= 12):
            counter_array = i - 6
            array_mosse[i] = array5[counter_array]
        elif (i > 12 and i <= 17):
            counter_array = i - 11
            array_mosse[i] = array6[counter_array]
        else:
            counter_array = i - 15
            array_mosse[i] = array7[counter_array]
        i = i + 1

    array6[2] = array_mosse[0]
    array5[2] = array_mosse[1]
    array4[2] = array_mosse[2]
    array7[3] = array_mosse[3]
    array6[3] = array_mosse[4]
    array5[3] = array_mosse[5]
    array4[3] = array_mosse[6]
    array3[3] = array_mosse[7]
    array7[4] = array_mosse[8]
    array6[4] = array_mosse[9]
    array4[4] = array_mosse[11]
    array3[4] = array_mosse[12]
    array7[5] = array_mosse[13]
    array6[5] = array_mosse[14]
    array5[5] = array_mosse[15]
    array4[5] = array_mosse[16]
    array3[5] = array_mosse[17]
    array6[6] = array_mosse[18]
    array5[6] = array_mosse[19]
    array4[6] = array_mosse[20]
    array_soluzioni.append("Fi")
    return

def right():
    global array1
    global array2
    global array3
    global array4
    global array5
    global array6
    global array7
    global array8
    global array9
    global array_mosse
    global array_soluzioni


    i = 0

    while (i <= 20):

        if (i == 0):
            counter_array = i + 5
            array_mosse[i] = array1[counter_array]
        elif (i == 1):
            counter_array = i + 4
            array_mosse[i] = array2[counter_array]
        elif (i == 2):
            counter_array = i + 3
            array_mosse[i] = array3[counter_array]
        elif (i > 2 and i <= 7):
            counter_array = i + 2
            array_mosse[i] = array4[counter_array]
        elif (i > 7 and i <= 12):
            counter_array = i - 3
            array_mosse[i] = array5[counter_array]
        elif (i > 12 and i <= 17):
            counter_array = i - 8
            array_mosse[i] = array6[counter_array]
        elif (i == 18):
            counter_array = i - 13
            array_mosse[i] = array7[counter_array]
        elif (i == 19):
            counter_array = i - 14
            array_mosse[i] = array8[counter_array]
        else:
            counter_array = i - 15
            array_mosse[i] = array9[counter_array]
        i = i + 1

    array6[9] = array_mosse[0]
    array5[9] = array_mosse[1]
    array4[9] = array_mosse[2]
    array1[5] = array_mosse[3]
    array4[8] = array_mosse[4]
    array5[8] = array_mosse[5]
    array6[8] = array_mosse[6]
    array9[5] = array_mosse[7]
    array2[5] = array_mosse[8]
    array4[7] = array_mosse[9]
    array6[7] = array_mosse[11]
    array8[5] = array_mosse[12]
    array3[5] = array_mosse[13]
    array4[6] = array_mosse[14]
    array5[6] = array_mosse[15]
    array6[6] = array_mosse[16]
    array7[5] = array_mosse[17]
    array4[5] = array_mosse[18]
    array5[5] = array_mosse[19]
    array6[5] = array_mosse[20]
    array_soluzioni.append("R")
    return

def right_inv():
    global array1
    global array2
    global array3
    global array4
    global array5
    global array6
    global array7
    global array8
    global array9
    global array_mosse
    global array_soluzioni

    i = 0

    while (i <= 20):

        if (i == 0):
            counter_array = i + 5
            array_mosse[i] = array1[counter_array]
        elif (i == 1):
            counter_array = i + 4
            array_mosse[i] = array2[counter_array]
        elif (i == 2):
            counter_array = i + 3
            array_mosse[i] = array3[counter_array]
        elif (i > 2 and i <= 7):
            counter_array = i + 2
            array_mosse[i] = array4[counter_array]
        elif (i > 7 and i <= 12):
            counter_array = i - 3
            array_mosse[i] = array5[counter_array]
        elif (i > 12 and i <= 17):
            counter_array = i - 8
            array_mosse[i] = array6[counter_array]
        elif (i == 18):
            counter_array = i - 13
            array_mosse[i] = array7[counter_array]
        elif (i == 19):
            counter_array = i - 14
            array_mosse[i] = array8[counter_array]
        else:
            counter_array = i - 15
            array_mosse[i] = array9[counter_array]
        i = i + 1

    array4[5] = array_mosse[0]
    array5[5] = array_mosse[1]
    array6[5] = array_mosse[2]
    array7[5] = array_mosse[3]
    array6[6] = array_mosse[4]
    array5[6] = array_mosse[5]
    array4[6] = array_mosse[6]
    array3[5] = array_mosse[7]
    array8[5] = array_mosse[8]
    array6[7] = array_mosse[9]
    array4[7] = array_mosse[11]
    array2[5] = array_mosse[12]
    array9[5] = array_mosse[13]
    array6[8] = array_mosse[14]
    array5[8] = array_mosse[15]
    array4[8] = array_mosse[16]
    array1[5] = array_mosse[17]
    array6[9] = array_mosse[18]
    array5[9] = array_mosse[19]
    array4[9] = array_mosse[20]
    array_soluzioni.append("Ri")
    return

def left():
    global array1
    global array2
    global array3
    global array4
    global array5
    global array6
    global array7
    global array8
    global array9
    global array_mosse
    global array_soluzioni

    i=0

    while (i <= 20):

        if (i == 0):
            counter_array = i + 3
            array_mosse[i] = array1[counter_array]
        elif (i == 1):
            counter_array = i + 2
            array_mosse[i] = array2[counter_array]
        elif (i == 2):
            counter_array = i + 1
            array_mosse[i] = array3[counter_array]
        elif (i > 2 and i < 7):
            counter_array = i - 3
            array_mosse[i] = array4[counter_array]
        elif (i == 7):
            counter_array = i + 4
            array_mosse[i] = array4[counter_array]
        elif (i > 7 and i < 12):
            counter_array = i - 8
            array_mosse[i] = array5[counter_array]
        elif (i == 12):
            counter_array = i - 1
            array_mosse[i] = array5[counter_array]
        elif (i > 12 and i < 17):
            counter_array = i - 13
            array_mosse[i] = array6[counter_array]
        elif ( i == 17):
            counter_array = i - 6
            array_mosse[i] = array6[counter_array]
        elif (i == 18):
            counter_array = i - 15
            array_mosse[i] = array7[counter_array]
        elif (i == 19):
            counter_array = i - 16
            array_mosse[i] = array8[counter_array]
        else:
            counter_array = i - 17
            array_mosse[i] = array9[counter_array]
        i = i + 1

    array4[3] = array_mosse[0]
    array5[3] = array_mosse[1]
    array6[3] = array_mosse[2]
    array4[2] = array_mosse[3]
    array5[2] = array_mosse[4]
    array6[2] = array_mosse[5]
    array7[3] = array_mosse[6]
    array3[3] = array_mosse[7]
    array4[1] = array_mosse[8]
    array6[1] = array_mosse[10]
    array8[3] = array_mosse[11]
    array2[3] = array_mosse[12]
    array4[0] = array_mosse[13]
    array5[0] = array_mosse[14]
    array6[0] = array_mosse[15]
    array9[3] = array_mosse[16]
    array1[3] = array_mosse[17]
    array6[11] = array_mosse[18]
    array5[11] = array_mosse[19]
    array4[11] = array_mosse[20]
    array_soluzioni.append("L")
    return

def left_inv():
    global array1
    global array2
    global array3
    global array4
    global array5
    global array6
    global array7
    global array8
    global array9
    global array_mosse
    global array_soluzioni

    i=0

    while (i <= 20):

        if (i == 0):
            counter_array = i + 3
            array_mosse[i] = array1[counter_array]
        elif (i == 1):
            counter_array = i + 2
            array_mosse[i] = array2[counter_array]
        elif (i == 2):
            counter_array = i + 1
            array_mosse[i] = array3[counter_array]
        elif (i > 2 and i < 7):
            counter_array = i - 3
            array_mosse[i] = array4[counter_array]
        elif (i == 7):
            counter_array = i + 4
            array_mosse[i] = array4[counter_array]
        elif (i > 7 and i < 12):
            counter_array = i - 8
            array_mosse[i] = array5[counter_array]
        elif (i == 12):
            counter_array = i - 1
            array_mosse[i] = array5[counter_array]
        elif (i > 12 and i < 17):
            counter_array = i - 13
            array_mosse[i] = array6[counter_array]
        elif ( i == 17):
            counter_array = i - 6
            array_mosse[i] = array6[counter_array]
        elif (i == 18):
            counter_array = i - 15
            array_mosse[i] = array7[counter_array]
        elif (i == 19):
            counter_array = i - 16
            array_mosse[i] = array8[counter_array]
        else:
            counter_array = i - 17
            array_mosse[i] = array9[counter_array]
        i = i + 1

    array6[11] = array_mosse[0]
    array5[11] = array_mosse[1]
    array4[11] = array_mosse[2]
    array6[0] = array_mosse[3]
    array5[0] = array_mosse[4]
    array4[0] = array_mosse[5]
    array1[3] = array_mosse[6]
    array9[3] = array_mosse[7]
    array6[1] = array_mosse[8]
    array4[1] = array_mosse[10]
    array2[3] = array_mosse[11]
    array8[3] = array_mosse[12]
    array6[2] = array_mosse[13]
    array5[2] = array_mosse[14]
    array4[2] = array_mosse[15]
    array3[3] = array_mosse[16]
    array7[3] = array_mosse[17]
    array4[3] = array_mosse[18]
    array5[3] = array_mosse[19]
    array6[3] = array_mosse[20]
    array_soluzioni.append("Li")
    return

def back():
    global array1
    global array4
    global array5
    global array6
    global array9
    global array_mosse
    global array_soluzioni

    i = 0

    while (i <= 20):

        if (i <= 2):
            counter_array = i + 3
            array_mosse[i] = array1[counter_array]
        elif (i == 3):
            counter_array = i - 3
            array_mosse[i] = array4[counter_array]
        elif (i > 3 and i <= 7):
            counter_array = i + 4
            array_mosse[i] = array4[counter_array]
        elif (i == 8):
            counter_array = i - 8
            array_mosse[i] = array5[counter_array]
        elif (i > 8 and i <= 12):
            counter_array = i - 1
            array_mosse[i] = array5[counter_array]
        elif (i == 13):
            counter_array = i - 13
            array_mosse[i] = array6[counter_array]
        elif (i > 13 and i <= 17):
            counter_array = i - 6
            array_mosse[i] = array6[counter_array]
        else:
            counter_array = i - 15
            array_mosse[i] = array9[counter_array]
        i = i + 1

    array6[0] = array_mosse[0]
    array5[0] = array_mosse[1]
    array4[0] = array_mosse[2]
    array9[3] = array_mosse[3]
    array1[3] = array_mosse[4]
    array4[11] = array_mosse[5]
    array5[11] = array_mosse[6]
    array6[11] = array_mosse[7]
    array9[4] = array_mosse[8]
    array1[4] = array_mosse[9]
    array4[10] = array_mosse[10]
    array6[10] = array_mosse[12]
    array9[5] = array_mosse[13]
    array1[5] = array_mosse[14]
    array4[9] = array_mosse[15]
    array5[9] = array_mosse[16]
    array6[9] = array_mosse[17]
    array6[8] = array_mosse[18]
    array5[8] = array_mosse[19]
    array4[8] = array_mosse[20]
    array_soluzioni.append("B")
    return

def back_inv():
    global array1
    global array4
    global array5
    global array6
    global array9
    global array_mosse
    global array_soluzioni

    i = 0

    while (i <= 20):

        if (i <= 2):
            counter_array = i + 3
            array_mosse[i] = array1[counter_array]
        elif (i == 3):
            counter_array = i - 3
            array_mosse[i] = array4[counter_array]
        elif (i > 3 and i <= 7):
            counter_array = i + 4
            array_mosse[i] = array4[counter_array]
        elif (i == 8):
            counter_array = i - 8
            array_mosse[i] = array5[counter_array]
        elif (i > 8 and i <= 12):
            counter_array = i - 1
            array_mosse[i] = array5[counter_array]
        elif (i == 13):
            counter_array = i - 13
            array_mosse[i] = array6[counter_array]
        elif (i > 13 and i <= 17):
            counter_array = i - 6
            array_mosse[i] = array6[counter_array]
        else:
            counter_array = i - 15
            array_mosse[i] = array9[counter_array]
        i = i + 1

    array4[8] = array_mosse[0]
    array5[8] = array_mosse[1]
    array6[8] = array_mosse[2]
    array1[5] = array_mosse[3]
    array9[5] = array_mosse[4]
    array6[9] = array_mosse[5]
    array5[9] = array_mosse[6]
    array4[9] = array_mosse[7]
    array1[4] = array_mosse[8]
    array9[4] = array_mosse[9]
    array6[10] = array_mosse[10]
    array4[10] = array_mosse[12]
    array1[3] = array_mosse[13]
    array9[3] = array_mosse[14]
    array6[11] = array_mosse[15]
    array5[11] = array_mosse[16]
    array4[11] = array_mosse[17]
    array4[0] = array_mosse[18]
    array5[0] = array_mosse[19]
    array6[0] = array_mosse[20]
    array_soluzioni.append("Bi")
    return

def up():
    global array1
    global array2
    global array3
    global array4
    global array_mosse
    global array_soluzioni

    i = 0

    while (i <= 20):

        if (i <= 2):
            counter_array = i + 3
            array_mosse[i] = array1[counter_array]
        elif (i > 2 and i <= 5):
            counter_array = i
            array_mosse[i] = array2[counter_array]
        elif (i > 5 and i <= 8):
            counter_array = i - 3
            array_mosse[i] = array3[counter_array]
        else:
            counter_array = i - 9
            array_mosse[i] = array4[counter_array]

        i = i + 1

    array1[5] = array_mosse[0]
    array2[5] = array_mosse[1]
    array3[5] = array_mosse[2]
    array1[4] = array_mosse[3]
    array3[4] = array_mosse[5]
    array1[3] = array_mosse[6]
    array2[3] = array_mosse[7]
    array3[3] = array_mosse[8]
    array4[9] = array_mosse[9]
    array4[10] = array_mosse[10]
    array4[11] = array_mosse[11]
    array4[0] = array_mosse[12]
    array4[1] = array_mosse[13]
    array4[2] = array_mosse[14]
    array4[3] = array_mosse[15]
    array4[4] = array_mosse[16]
    array4[5] = array_mosse[17]
    array4[6] = array_mosse[18]
    array4[7] = array_mosse[19]
    array4[8] = array_mosse[20]
    array_soluzioni.append("U")
    return

def up_inv():
    global array1
    global array2
    global array3
    global array4
    global array_mosse
    global array_soluzioni

    i = 0

    while (i <= 20):

        if (i <= 2):
            counter_array = i + 3
            array_mosse[i] = array1[counter_array]
        elif (i > 2 and i <= 5):
            counter_array = i
            array_mosse[i] = array2[counter_array]
        elif (i > 5 and i <= 8):
            counter_array = i - 3
            array_mosse[i] = array3[counter_array]
        else:
            counter_array = i - 9
            array_mosse[i] = array4[counter_array]

        i = i + 1

    array3[3] = array_mosse[0]
    array2[3] = array_mosse[1]
    array1[3] = array_mosse[2]
    array3[4] = array_mosse[3]
    array1[4] = array_mosse[5]
    array3[5] = array_mosse[6]
    array2[5] = array_mosse[7]
    array1[5] = array_mosse[8]
    array4[3] = array_mosse[9]
    array4[4] = array_mosse[10]
    array4[5] = array_mosse[11]
    array4[6] = array_mosse[12]
    array4[7] = array_mosse[13]
    array4[8] = array_mosse[14]
    array4[9] = array_mosse[15]
    array4[10] = array_mosse[16]
    array4[11] = array_mosse[17]
    array4[0] = array_mosse[18]
    array4[1] = array_mosse[19]
    array4[2] = array_mosse[20]
    array_soluzioni.append("Ui")
    return

def down():
    global array6
    global array7
    global array8
    global array9
    global array_mosse
    global array_soluzioni

    i = 0

    while (i <= 20):

        if (i <= 11):
            counter_array = i
            array_mosse[i] = array6[counter_array]
        elif (i > 11 and i <= 14):
            counter_array = i - 9
            array_mosse[i] = array7[counter_array]
        elif (i > 14 and i <= 17):
            counter_array = i - 12
            array_mosse[i] = array8[counter_array]
        else:
            counter_array = i - 15
            array_mosse[i] = array9[counter_array]

        i = i + 1

    array6[3] = array_mosse[0]
    array6[4] = array_mosse[1]
    array6[5] = array_mosse[2]
    array6[6] = array_mosse[3]
    array6[7] = array_mosse[4]
    array6[8] = array_mosse[5]
    array6[9] = array_mosse[6]
    array6[10] = array_mosse[7]
    array6[11] = array_mosse[8]
    array6[0] = array_mosse[9]
    array6[1] = array_mosse[10]
    array6[2] = array_mosse[11]
    array7[5] = array_mosse[12]
    array8[5] = array_mosse[13]
    array9[5] = array_mosse[14]
    array7[4] = array_mosse[15]
    array9[4] = array_mosse[17]
    array7[3] = array_mosse[18]
    array8[3] = array_mosse[19]
    array9[3] = array_mosse[20]
    array_soluzioni.append("D")
    return

def down_inv():
    global array6
    global array7
    global array8
    global array9
    global array_mosse
    global array_soluzioni

    i = 0

    while (i <= 20):

        if (i <= 11):
            counter_array = i
            array_mosse[i] = array6[counter_array]
        elif (i > 11 and i <= 14):
            counter_array = i - 9
            array_mosse[i] = array7[counter_array]
        elif (i > 14 and i <= 17):
            counter_array = i - 12
            array_mosse[i] = array8[counter_array]
        else:
            counter_array = i - 15
            array_mosse[i] = array9[counter_array]

        i = i + 1

    array6[9] = array_mosse[0]
    array6[10] = array_mosse[1]
    array6[11] = array_mosse[2]
    array6[0] = array_mosse[3]
    array6[1] = array_mosse[4]
    array6[2] = array_mosse[5]
    array6[3] = array_mosse[6]
    array6[4] = array_mosse[7]
    array6[5] = array_mosse[8]
    array6[6] = array_mosse[9]
    array6[7] = array_mosse[10]
    array6[8] = array_mosse[11]
    array9[3] = array_mosse[12]
    array8[3] = array_mosse[13]
    array7[3] = array_mosse[14]
    array9[4] = array_mosse[15]
    array7[4] = array_mosse[17]
    array9[5] = array_mosse[18]
    array8[5] = array_mosse[19]
    array7[5] = array_mosse[20]
    array_soluzioni.append("Di")
    return

#movimenti totali del cubo
def x(): #tutto da fixare
    global array1
    global array2
    global array3
    global array4
    global array5
    global array6
    global array7
    global array8
    global array9
    global movimento_completo
    global array_soluzioni

    i = 0

    while (i <= 53):

        if (i <= 2):
            counter_array = i + 3
            movimento_completo[i] = array1[counter_array]
        elif (i > 2 and i <= 5):
            counter_array = i
            movimento_completo[i] = array2[counter_array]
        elif (i > 5 and i <= 8):
            counter_array = i - 3
            movimento_completo[i] = array3[counter_array]
        elif (i > 8 and i <= 20):
            counter_array = i - 9
            movimento_completo[i] = array4[counter_array]
        elif (i > 20 and i <= 32):
            counter_array = i - 21
            movimento_completo[i] = array5[counter_array]
        elif (i > 32 and i <= 44):
            counter_array = i - 33
            movimento_completo[i] = array6[counter_array]
        elif (i > 44 and i <= 47):
            counter_array = i - 42
            movimento_completo[i] = array7[counter_array]
        elif (i > 47 and i <= 50):
            counter_array = i - 45
            movimento_completo[i] = array8[counter_array]
        else:
            counter_array = i - 48
            movimento_completo[i] = array9[counter_array]
        i = i + 1

    array6[11] = movimento_completo[0]
    array6[10] = movimento_completo[1]
    array6[9] = movimento_completo[2]
    array5[11] = movimento_completo[3]
    array5[10] = movimento_completo[4]
    array5[9] = movimento_completo[5]
    array4[11] = movimento_completo[6]
    array4[10] = movimento_completo[7]
    array4[9] = movimento_completo[8]
    array6[0] = movimento_completo[9]
    array5[0] = movimento_completo[10]
    array4[0] = movimento_completo[11]
    array1[3] = movimento_completo[12]
    array1[4] = movimento_completo[13]
    array1[5] = movimento_completo[14]
    array4[8] = movimento_completo[15]
    array5[8] = movimento_completo[16]
    array6[8] = movimento_completo[17]
    array9[5] = movimento_completo[18]
    array9[4] = movimento_completo[19]
    array9[3] = movimento_completo[20]
    array6[1] = movimento_completo[21]
    array4[1] = movimento_completo[23]
    array2[3] = movimento_completo[24]
    array2[4] = movimento_completo[25]
    array2[5] = movimento_completo[26]
    array4[7] = movimento_completo[27]
    array6[7] = movimento_completo[29]
    array8[5] = movimento_completo[30]
    array8[4] = movimento_completo[31]
    array8[3] = movimento_completo[32]
    array6[2] = movimento_completo[33]
    array5[2] = movimento_completo[34]
    array4[2] = movimento_completo[35]
    array3[3] = movimento_completo[36]
    array3[4] = movimento_completo[37]
    array3[5] = movimento_completo[38]
    array4[6] = movimento_completo[39]
    array5[6] = movimento_completo[40]
    array6[6] = movimento_completo[41]
    array7[5] = movimento_completo[42]
    array7[4] = movimento_completo[43]
    array7[3] = movimento_completo[44]
    array4[3] = movimento_completo[45]
    array4[4] = movimento_completo[46]
    array4[5] = movimento_completo[47]
    array5[3] = movimento_completo[48]
    array5[4] = movimento_completo[49]
    array5[5] = movimento_completo[50]
    array6[3] = movimento_completo[51]
    array6[4] = movimento_completo[52]
    array6[5] = movimento_completo[53]
    array_soluzioni.append("X")
    return

def x_inv():
    global array1
    global array2
    global array3
    global array4
    global array5
    global array6
    global array7
    global array8
    global array9
    global movimento_completo
    global array_soluzioni

    i = 0

    while (i <= 53):

        if (i <= 2):
            counter_array = i + 3
            movimento_completo[i] = array1[counter_array]
        elif (i > 2 and i <= 5):
            counter_array = i
            movimento_completo[i] = array2[counter_array]
        elif (i > 5 and i <= 8):
            counter_array = i - 3
            movimento_completo[i] = array3[counter_array]
        elif (i > 8 and i <= 20):
            counter_array = i - 9
            movimento_completo[i] = array4[counter_array]
        elif (i > 20 and i <= 32):
            counter_array = i - 21
            movimento_completo[i] = array5[counter_array]
        elif (i > 32 and i <= 44):
            counter_array = i - 33
            movimento_completo[i] = array6[counter_array]
        elif (i > 44 and i <= 47):
            counter_array = i - 42
            movimento_completo[i] = array7[counter_array]
        elif (i > 47 and i <= 50):
            counter_array = i - 45
            movimento_completo[i] = array8[counter_array]
        else:
            counter_array = i - 48
            movimento_completo[i] = array9[counter_array]
        i = i + 1

    array4[3] = movimento_completo[0]
    array4[4] = movimento_completo[1]
    array4[5] = movimento_completo[2]
    array5[3] = movimento_completo[3]
    array5[4] = movimento_completo[4]
    array5[5] = movimento_completo[5]
    array6[3] = movimento_completo[6]
    array6[4] = movimento_completo[7]
    array6[5] = movimento_completo[8]
    array4[2] = movimento_completo[9]
    array5[2] = movimento_completo[10]
    array6[2] = movimento_completo[11]
    array7[3] = movimento_completo[12]
    array7[4] = movimento_completo[13]
    array7[5] = movimento_completo[14]
    array6[6] = movimento_completo[15]
    array5[6] = movimento_completo[16]
    array4[6] = movimento_completo[17]
    array3[5] = movimento_completo[18]
    array3[4] = movimento_completo[19]
    array3[3] = movimento_completo[20]
    array4[1] = movimento_completo[21]
    array5[1] = movimento_completo[22]
    array6[1] = movimento_completo[23]
    array8[3] = movimento_completo[24]
    array8[4] = movimento_completo[25]
    array8[5] = movimento_completo[26]
    array6[7] = movimento_completo[27]
    array5[7] = movimento_completo[28]
    array4[7] = movimento_completo[29]
    array2[5] = movimento_completo[30]
    array2[4] = movimento_completo[31]
    array2[3] = movimento_completo[32]
    array4[0] = movimento_completo[33]
    array5[0] = movimento_completo[34]
    array6[0] = movimento_completo[35]
    array9[3] = movimento_completo[36]
    array9[4] = movimento_completo[37]
    array9[5] = movimento_completo[38]
    array6[8] = movimento_completo[39]
    array5[8] = movimento_completo[40]
    array4[8] = movimento_completo[41]
    array1[5] = movimento_completo[42]
    array1[4] = movimento_completo[43]
    array1[3] = movimento_completo[44]
    array6[11] = movimento_completo[45]
    array6[10] = movimento_completo[46]
    array6[9] = movimento_completo[47]
    array5[11] = movimento_completo[48]
    array5[10] = movimento_completo[49]
    array5[9] = movimento_completo[50]
    array4[11] = movimento_completo[51]
    array4[10] = movimento_completo[52]
    array4[9] = movimento_completo[53]
    array_soluzioni.append("Xi")
    return

def y():
    global array1
    global array2
    global array3
    global array4
    global array5
    global array6
    global array7
    global array8
    global array9
    global movimento_completo
    global array_soluzioni

    i = 0

    while (i <= 53):

        if (i <= 2):
            counter_array = i + 3
            movimento_completo[i] = array1[counter_array]
        elif (i > 2 and i <= 5):
            counter_array = i
            movimento_completo[i] = array2[counter_array]
        elif (i > 5 and i <= 8):
            counter_array = i - 3
            movimento_completo[i] = array3[counter_array]
        elif (i > 8 and i <= 20):
            counter_array = i - 9
            movimento_completo[i] = array4[counter_array]
        elif (i > 20 and i <= 32):
            counter_array = i - 21
            movimento_completo[i] = array5[counter_array]
        elif (i > 32 and i <= 44):
            counter_array = i - 33
            movimento_completo[i] = array6[counter_array]
        elif (i > 44 and i <= 47):
            counter_array = i - 42
            movimento_completo[i] = array7[counter_array]
        elif (i > 47 and i <= 50):
            counter_array = i - 45
            movimento_completo[i] = array8[counter_array]
        else:
            counter_array = i - 48
            movimento_completo[i] = array9[counter_array]
        i = i + 1

    array1[5] = movimento_completo[0]
    array2[5] = movimento_completo[1]
    array3[5] = movimento_completo[2]
    array1[4] = movimento_completo[3]
    array2[4] = movimento_completo[4]
    array3[4] = movimento_completo[5]
    array1[3] = movimento_completo[6]
    array2[3] = movimento_completo[7]
    array3[3] = movimento_completo[8]
    array4[9] = movimento_completo[9]
    array4[10] = movimento_completo[10]
    array4[11] = movimento_completo[11]
    array4[0] = movimento_completo[12]
    array4[1] = movimento_completo[13]
    array4[2] = movimento_completo[14]
    array4[3] = movimento_completo[15]
    array4[4] = movimento_completo[16]
    array4[5] = movimento_completo[17]
    array4[6] = movimento_completo[18]
    array4[7] = movimento_completo[19]
    array4[8] = movimento_completo[20]
    array5[9] = movimento_completo[21]
    array5[10] = movimento_completo[22]
    array5[11] = movimento_completo[23]
    array5[0] = movimento_completo[24]
    array5[1] = movimento_completo[25]
    array5[2] = movimento_completo[26]
    array5[3] = movimento_completo[27]
    array5[4] = movimento_completo[28]
    array5[5] = movimento_completo[29]
    array5[6] = movimento_completo[30]
    array5[7] = movimento_completo[31]
    array5[8] = movimento_completo[32]
    array6[9] = movimento_completo[33]
    array6[10] = movimento_completo[34]
    array6[11] = movimento_completo[35]
    array6[0] = movimento_completo[36]
    array6[1] = movimento_completo[37]
    array6[2] = movimento_completo[38]
    array6[3] = movimento_completo[39]
    array6[4] = movimento_completo[40]
    array6[5] = movimento_completo[41]
    array6[6] = movimento_completo[42]
    array6[7] = movimento_completo[43]
    array6[8] = movimento_completo[44]
    array9[3] = movimento_completo[45]
    array8[3] = movimento_completo[46]
    array7[3] = movimento_completo[47]
    array9[4] = movimento_completo[48]
    array8[4] = movimento_completo[49]
    array7[4] = movimento_completo[50]
    array9[5] = movimento_completo[51]
    array8[5] = movimento_completo[52]
    array7[5] = movimento_completo[53]
    array_soluzioni.append("Y")
    return

while_example = 0
mossa = "F"



#CROCE GIALLA
#giallo-blu
if array1[4] == 32:
  up()
  up()
  front()
  front()
elif array2[5] == 32:
  up()
  front()
  front()
elif array3[4] == 32:
  front()
  front()
elif array2[3] == 32:
  up_inv()
  front()
  front()
elif array4[4] == 32:
  up_inv()
  right_inv()
  front()
elif array5[5] == 32:
  right_inv()
  down_inv()
elif array6[4] == 32:
  front_inv()
  right_inv()
  down_inv()
elif array5[3] == 32:
  left()
  down()
elif array4[7] == 32:
  right_inv()
  front()
elif array5[8] == 32:
  right()
  right()
  front()
elif array6[7] == 32:
  right()
  front()
elif array5[6] == 32:
  front()
elif array4[10] == 32:
  up()
  right_inv()
  front()
elif array5[11] == 32:
  left_inv()
  down()
elif array6[10] == 32:
  back_inv()
  left_inv()
  down()
elif array5[9] == 32:
  right()
  down_inv()
elif array4[1] == 32:
  left()
  front_inv()
elif array5[2] == 32:
  front_inv()
elif array6[1] == 32:
  left_inv()
  front_inv()
elif array5[0] == 32:
  left()
  left()
  front_inv()
elif array8[5] == 32:
  down_inv()
elif array9[4] == 32:
  down()
  down()
elif array8[3] == 32:
  down()
#giallo-arancio
if array1[4] == 36:
  up()
  right()
  right()
elif array2[5] == 36:
    right()
    right()
elif array3[4] == 36:
    up_inv()
    right()
    right()
elif array2[3] == 36:
  up()
  up()
  right()
  right()
elif array4[4] == 36:
  front()
  right_inv()
  front_inv()
elif array5[5] == 36:
  right_inv()
elif array5[3] == 36:
  down()
  down()
  left()
  down()
  down()
elif array4[7] == 36:
  down_inv()
  right_inv()
  front()
  down()
elif array5[8] == 36:
  down()
  back_inv()
  down_inv()
elif array6[7] == 36:
  right()
  down_inv()
  front()
  down()
elif array5[6] == 36:
  down_inv()
  front()
  down()
elif array4[10] == 36:
  back_inv()
  right()
elif array5[11] == 36:
    back()
    back()
    right()
elif array6[10] == 36:
    back()
    right()
elif array5[9] == 36:
  right()
elif array4[1] == 36:
  up()
  back_inv()
  right()
elif array5[2] == 36:
  down_inv()
  front_inv()
  down()
elif array6[1] == 36:
  left_inv()
  down_inv()
  front_inv()
  down()
elif array5[0] == 36:
  down()
  back()
  down_inv()
elif array9[4] == 36:
  back()
  down()
  back_inv()
  down_inv()
elif array8[3] == 36:
  left()
  back()
  back()
  right()
#giallo-verde
if array1[4] == 38:
  back()
  back()
elif array2[5] == 38:
    up_inv()
    back()
    back()
elif array3[4] == 38:
    up()
    up()
    back()
    back()
elif array2[3] == 38:
  up()
  back()
  back()
elif array4[4] == 38:
  up()
  left_inv()
  back()
elif array5[5] == 38:
  down_inv()
  right_inv()
  down()
elif array5[3] == 38:
  down()
  left()
  down_inv()
elif array4[7] == 38:
  right()
  back_inv()
  right_inv()
elif array5[8] == 38:
  back_inv()
elif array5[6] == 38:
  down()
  down()
  front()
  down()
  down()
elif array4[10] == 38:
  up_inv()
  left_inv()
  back()
elif array5[11] == 38:
    down()
    left_inv()
    down_inv()
elif array6[10] == 38:
    back_inv()
    down()
    left_inv()
    down_inv()
elif array5[9] == 38:
    down_inv()
    right()
    down()
elif array4[1] == 38:
  left_inv()
  back()
elif array5[2] == 38:
  left()
  left()
  back()
elif array6[1] == 38:
  left()
  back()
elif array5[0] == 38:
  back()
elif array8[3] == 38:
  left_inv()
  down()
  left()
  down_inv()
#giallo-rosso
if array1[4] == 34:
  up_inv()
  left()
  left()
  print("asdfsd")
elif array2[5] == 34:
    up()
    up()
    left()
    left()
elif array3[4] == 34:
    up()
    left()
    left()
elif array2[3] == 34:
    left()
    left()
elif array4[4] == 34:
  front_inv()
  left()
  front()
elif array5[5] == 34:
  down()
  down()
  right_inv()
  down()
  down()
elif array5[3] == 34:
  left()
elif array4[7] == 34:
  up()
  front_inv()
  left()
  front()
elif array5[8] == 34:
  down_inv()
  back_inv()
  down()
elif array5[6] == 34:
  down()
  front()
  down_inv()
elif array4[10] == 34:
  back()
  left_inv()
  back_inv()
elif array5[11] == 34:
    left_inv()
elif array5[9] == 34:
    down()
    down()
    right()
    down()
    down()
elif array4[1] == 34:
  left()
  down()
  front_inv()
  down_inv()
elif array5[2] == 34:
  down()
  front_inv()
  down_inv()
elif array6[1] == 34:
  left_inv()
  down()
  front_inv()
  down_inv()
elif array5[0] == 34:
  down_inv()
  back()
  down()
#F2L
#sistemare lo spigolo blu-arancio
if array1[4] == 26 or array1[4] == 54:
    up()
elif array3[4] == 26 or array3[4] == 54:
    up_inv()
elif array2[3] == 26 or array2[3] == 54:
    up()
    up()
elif array5[5] == 26 or array5[5] == 54:
    front_inv()
    up_inv()
    front()
elif array5[3] == 26 or array5[3] == 54:
    front()
    up_inv()
    front_inv()
elif array5[8] == 26 or array5[8] == 54:
    back()
    up()
    back_inv()
elif array5[11] == 26 or array5[11] == 54:
    back_inv()
    up()
    back()
#inserire la coppia blu-arancio
#spigolo orientato
if array2[5] == 26:
    if array1[3] == 33:
        right()
        up()
        right()
        right()
        front()
        right()
        front_inv()
    elif array1[5] == 33:
        up()
        up()
        right()
        up_inv()
        right_inv()
        up_inv()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up_inv()
        right_inv()
    elif array3[5] == 33:
        right()
        up()
        up()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
    elif array3[3] == 33:
        right()
        up()
        up()
        right()
        right()
        front()
        right()
        front_inv()
    elif array4[3] == 33:
        up_inv()
        right()
        up()
        right_inv()
    elif array4[5] == 33:
        up()
        right()
        up_inv()
        right_inv()
    elif array6[5] == 33:
        right()
        up_inv()
        right()
        right()
        front()
        right()
        front_inv()
    elif array6[3] == 33:
        up_inv()
        left_inv()
        up()
        left()
        up_inv()
        right()
        up()
        right_inv()
    elif array4[6] == 33:
        up_inv()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up()
        right_inv()
    elif array4[8] == 33:
        up()
        right()
        up()
        right_inv()
        up()
        up()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up_inv()
        right_inv()
    elif array6[8] == 33:
        up_inv()
        right_inv()
        up_inv()
        right()
        right()
        up()
        up()
        right_inv()
    elif array6[6] == 33:
        right()
        up()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
    elif array4[9] == 33:
        up()
        right_inv()
        up()
        up()
        right()
        right()
        up()
        right()
        right()
        up()
        right()
    elif array4[11] == 33:
        up()
        right()
        up()
        up()
        right_inv()
        up()
        up()
        right()
        up_inv()
        right_inv()
    elif array6[11] == 33:
        up()
        up()
        left()
        up_inv()
        left_inv()
        right()
        up()
        up()
        right_inv()
    elif array6[9] == 33:
        up()
        right_inv()
        up()
        right()
        up()
        right()
        up()
        right_inv()
    elif array4[0] == 33:
        right()
        up_inv()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
    elif array4[2] == 33:
        up()
        up()
        right()
        up()
        right_inv()
        up()
        up()
        right()
        up_inv()
        right_inv()
    elif array6[2] == 33:
        up()
        left_inv()
        right()
        up_inv()
        right_inv()
        left()
    elif array6[0] == 33:
        up()
        up()
        left()
        up()
        left_inv()
        up()
        right()
        up()
        right_inv()
    elif array7[3] == 33:
        left_inv()
        up()
        left()
        right()
        up_inv()
        right_inv()
    elif array7[5] == 33:
        up_inv()
        right_inv()
        front()
        right()
        front_inv()
        right()
        up()
        right_inv()
    elif array9[5] == 33:
        up()
        up()
        right_inv()
        up()
        right()
        up()
        up()
        right()
        up_inv()
        right_inv()
    elif array9[3] == 33:
        up()
        back_inv()
        up()
        up()
        right()
        up()
        right_inv()
        back()
#spigolo non orientato
else:
    if array1[3] == 33:
        up()
        front_inv()
        up()
        up()
        front()
        front()
        right_inv()
        front_inv()
        right()
    elif array1[5] == 33:
        up()
        front_inv()
        up()
        up()
        front()
        up()
        front_inv()
        up_inv()
        front()
    elif array3[5] == 33:
        up_inv()
        right_inv()
        front()
        right()
        front_inv()
        up_inv()
        front_inv()
        up_inv()
        front()
    elif array3[3] == 33:
        up()
        front_inv()
        up_inv()
        front()
        front()
        right_inv()
        front_inv()
        right()
    elif array4[3] == 33:
        front_inv()
        up()
        up()
        front()
        up()
        up()
        front_inv()
        up()
        front()
    elif array4[5] == 33:
        up_inv()
        right()
        up()
        up()
        right_inv()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[5] == 33:
        up_inv()
        right()
        up_inv()
        right_inv()
        front_inv()
        up_inv()
        front()
    elif array6[3] == 33:
        up()
        front_inv()
        left()
        front()
        left()
        left()
        right()
        up()
        up()
        right_inv()
        left()
    elif array4[6] == 33:
        right()
        up_inv()
        right_inv()
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array4[8] == 33:
        up()
        up()
        front_inv()
        up()
        front()
        up_inv()
        front_inv()
        up_inv()
        front()
    elif array6[8] == 33:
        right_inv()
        up_inv()
        right()
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[6] == 33:
        up()
        right()
        up()
        right_inv()
        up()
        up()
        front_inv()
        up()
        front()
    elif array4[9] == 33:
        front_inv()
        up()
        front()
    elif array4[11] == 33:
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[11] == 33:
        up()
        left()
        up_inv()
        left_inv()
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[9] == 33:
        right_inv()
        up()
        right()
        front_inv()
        up()
        front()
    elif array4[0] == 33:
        up_inv()
        front_inv()
        up_inv()
        front()
        up()
        up()
        front_inv()
        up()
        front()
    elif array4[2] == 33:
        right()
        up()
        right_inv()
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[2] == 33:
        up()
        up()
        left_inv()
        up_inv()
        left()
        front_inv()
        up_inv()
        front()
    elif array6[0] == 33:
        up_inv()
        left()
        front_inv()
        up()
        up()
        front()
        left_inv()
    elif array7[3] == 33:
        up_inv()
        left()
        front_inv()
        left_inv()
        front()
        up_inv()
        front_inv()
        up_inv()
        front()
    elif array7[5] == 33:
        up()
        up()
        right()
        up_inv()
        right_inv()
        up_inv()
        front_inv()
        up()
        front()
    elif array9[5] == 33:
        up()
        back()
        up()
        front_inv()
        up_inv()
        front()
        back_inv()
    elif array9[3] == 33:
        left()
        up_inv()
        left_inv()
        front_inv()
        up()
        up()
        front()
y()
#sistemare lo spigolo arancio-verde
if array1[4] == 56 or array1[4] == 64:
    up()
elif array3[4] == 56 or array3[4] == 64:
    up_inv()
elif array2[3] == 56 or array2[3] == 64:
    up()
    up()
elif array5[5] == 56 or array5[5] == 64:
    front_inv()
    up_inv()
    front()
elif array5[3] == 56 or array5[3] == 64:
    front()
    up()
    front_inv()
elif array5[8] == 56 or array5[8] == 64:
    back()
    up()
    back_inv()
elif array5[11] == 56 or array5[11] == 64:
    back_inv()
    up()
    back()
#inserire la coppia arancio-verde
#spigolo orientato
if array2[5] == 56:
    if array1[3] == 39:
        right()
        up()
        right()
        right()
        front()
        right()
        front_inv()
    elif array1[5] == 39:
        up()
        up()
        right()
        up_inv()
        right_inv()
        up_inv()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up_inv()
        right_inv()
    elif array3[5] == 39:
        right()
        up()
        up()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
    elif array3[3] == 39:
        right()
        up()
        up()
        right()
        right()
        front()
        right()
        front_inv()
    elif array4[3] == 39:
        up_inv()
        right()
        up()
        right_inv()
    elif array4[5] == 39:
        up()
        right()
        up_inv()
        right_inv()
    elif array6[5] == 39:
        right()
        up_inv()
        right()
        right()
        front()
        right()
        front_inv()
    elif array4[6] == 39:
        up_inv()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up()
        right_inv()
    elif array4[8] == 39:
        up()
        right()
        up()
        right_inv()
        up()
        up()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up_inv()
        right_inv()
    elif array6[8] == 39:
        up_inv()
        right_inv()
        up_inv()
        right()
        right()
        up()
        up()
        right_inv()
    elif array6[6] == 39:
        right()
        up()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
    elif array4[9] == 39:
        up()
        right_inv()
        up()
        up()
        right()
        right()
        up()
        right()
        right()
        up()
        right()
    elif array4[11] == 39:
        up()
        right()
        up()
        up()
        right_inv()
        up()
        up()
        right()
        up_inv()
        right_inv()
    elif array6[11] == 39:
        up()
        up()
        left()
        up_inv()
        left_inv()
        right()
        up()
        up()
        right_inv()
    elif array6[9] == 39:
        up()
        right_inv()
        up()
        right()
        up()
        right()
        up()
        right_inv()
    elif array4[0] == 39:
        right()
        up_inv()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
    elif array4[2] == 39:
        up()
        up()
        right()
        up()
        right_inv()
        up()
        up()
        right()
        up_inv()
        right_inv()
    elif array6[0] == 39:
        up()
        up()
        left()
        up()
        left_inv()
        up()
        right()
        up()
        right_inv()
    elif array7[5] == 39:
        up_inv()
        right_inv()
        front()
        right()
        front_inv()
        right()
        up()
        right_inv()
    elif array9[5] == 39:
        up()
        up()
        right_inv()
        up()
        right()
        up()
        up()
        right()
        up_inv()
        right_inv()
    elif array9[3] == 39:
        up()
        back_inv()
        up()
        up()
        right()
        up()
        right_inv()
        back()
#spigolo non orientato
else:
    if array1[3] == 39:
        up()
        front_inv()
        up()
        up()
        front()
        front()
        right_inv()
        front_inv()
        right()
    elif array1[5] == 39:
        up()
        front_inv()
        up()
        up()
        front()
        up()
        front_inv()
        up_inv()
        front()
    elif array3[5] == 39:
        up_inv()
        right_inv()
        front()
        right()
        front_inv()
        up_inv()
        front_inv()
        up_inv()
        front()
    elif array3[3] == 39:
        up()
        front_inv()
        up_inv()
        front()
        front()
        right_inv()
        front_inv()
        right()
    elif array4[3] == 39:
        front_inv()
        up()
        up()
        front()
        up()
        up()
        front_inv()
        up()
        front()
    elif array4[5] == 39:
        up_inv()
        right()
        up()
        up()
        right_inv()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[5] == 39:
        up_inv()
        right()
        up_inv()
        right_inv()
        front_inv()
        up_inv()
        front()
    elif array4[6] == 39:
        right()
        up_inv()
        right_inv()
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array4[8] == 39:
        up()
        up()
        front_inv()
        up()
        front()
        up_inv()
        front_inv()
        up_inv()
        front()
    elif array6[8] == 39:
        right_inv()
        up_inv()
        right()
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[6] == 39:
        up()
        right()
        up()
        right_inv()
        up()
        up()
        front_inv()
        up()
        front()
    elif array4[9] == 39:
        front_inv()
        up()
        front()
    elif array4[11] == 39:
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[11] == 39:
        up()
        left()
        up_inv()
        left_inv()
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[9] == 39:
        right_inv()
        up()
        right()
        front_inv()
        up()
        front()
    elif array4[0] == 39:
        up_inv()
        front_inv()
        up_inv()
        front()
        up()
        up()
        front_inv()
        up()
        front()
    elif array4[2] == 39:
        right()
        up()
        right_inv()
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[0] == 39:
        up_inv()
        left()
        front_inv()
        up()
        up()
        front()
        left_inv()
    elif array7[5] == 39:
        up()
        up()
        right()
        up_inv()
        right_inv()
        up_inv()
        front_inv()
        up()
        front()
    elif array9[5] == 39:
        up()
        back()
        up()
        front_inv()
        up_inv()
        front()
        back_inv()
    elif array9[3] == 39:
        left()
        up_inv()
        left_inv()
        front_inv()
        up()
        up()
        front()
y()
#sistemare lo spigolo verde-rosso
if array1[4] == 66 or array1[4] == 44:
    up()
elif array3[4] == 66 or array3[4] == 44:
    up_inv()
elif array2[3] == 66 or array2[3] == 44:
    up()
    up()
elif array5[5] == 66 or array5[5] == 44:
    front_inv()
    up_inv()
    front()
elif array5[3] == 66 or array5[3] == 44:
    front()
    up()
    front_inv()
elif array5[8] == 66 or array5[8] == 44:
    back()
    up()
    back_inv()
elif array5[11] == 66 or array5[11] == 44:
    back_inv()
    up()
    back()
#inserire la coppia verde-rosso
#spigolo orientato
if array2[5] == 66:
    if array1[3] == 37:
        right()
        up()
        right()
        right()
        front()
        right()
        front_inv()
    elif array1[5] == 37:
        up()
        up()
        right()
        up_inv()
        right_inv()
        up_inv()
        right()
        up_inv()
        right()
        right()
        front()
        right()
        front_inv()
    elif array3[5] == 37:
        right()
        up()
        up()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
    elif array3[3] == 37:
        right()
        up()
        up()
        right()
        right()
        front()
        right()
        front_inv()
    elif array4[3] == 37:
        up_inv()
        right()
        up()
        right_inv()
    elif array4[5] == 37:
        up()
        right()
        up_inv()
        right_inv()
    elif array6[5] == 37:
        right()
        up_inv()
        right()
        right()
        front()
        right()
        front_inv()
    elif array4[6] == 37:
        up_inv()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up()
        right_inv()
    elif array4[8] == 37:
        up()
        right()
        up()
        right_inv()
        up()
        up()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up_inv()
        right_inv()
    elif array6[8] == 37:
        up_inv()
        right_inv()
        up_inv()
        right()
        right()
        up()
        up()
        right_inv()
    elif array6[6] == 37:
        right()
        up()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
    elif array4[9] == 37:
        up()
        right_inv()
        up()
        up()
        right()
        right()
        up()
        right()
        right()
        up()
        right()
    elif array4[11] == 37:
        up()
        right()
        up()
        up()
        right_inv()
        up()
        up()
        right()
        up_inv()
        right_inv()
    elif array6[9] == 37:
        up()
        right_inv()
        up()
        right()
        up()
        right()
        up()
        right_inv()
    elif array4[0] == 37:
        right()
        up_inv()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
    elif array4[2] == 37:
        up()
        up()
        right()
        up()
        right_inv()
        up()
        up()
        right()
        up_inv()
        right_inv()
    elif array7[5] == 37:
        up_inv()
        right_inv()
        front()
        right()
        front_inv()
        right()
        up()
        right_inv()
    elif array9[5] == 37:
        up()
        up()
        right_inv()
        up()
        right()
        up()
        up()
        right()
        up_inv()
        right_inv()
#spigolo non orientato
else:
    if array1[3] == 37:
        up()
        front_inv()
        up()
        up()
        front()
        front()
        right_inv()
        front_inv()
        right()
    elif array1[5] == 37:
        up()
        front_inv()
        up()
        up()
        front()
        up()
        front_inv()
        up_inv()
        front()
    elif array3[5] == 37:
        up_inv()
        right_inv()
        front()
        right()
        front_inv()
        up_inv()
        front_inv()
        up_inv()
        front()
    elif array3[3] == 37:
        up()
        front_inv()
        up_inv()
        front()
        front()
        right_inv()
        front_inv()
        right()
    elif array4[3] == 37:
        front_inv()
        up()
        up()
        front()
        up()
        up()
        front_inv()
        up()
        front()
    elif array4[5] == 37:
        up_inv()
        right()
        up()
        up()
        right_inv()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[5] == 37:
        up_inv()
        right()
        up_inv()
        right_inv()
        front_inv()
        up_inv()
        front()
    elif array4[6] == 37:
        right()
        up_inv()
        right_inv()
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array4[8] == 37:
        up()
        up()
        front_inv()
        up()
        front()
        up_inv()
        front_inv()
        up_inv()
        front()
    elif array6[8] == 37:
        right_inv()
        up_inv()
        right()
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[6] == 37:
        up()
        right()
        up()
        right_inv()
        up()
        up()
        front_inv()
        up()
        front()
    elif array4[9] == 37:
        front_inv()
        up()
        front()
    elif array4[11] == 37:
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[9] == 37:
        right_inv()
        up()
        right()
        front_inv()
        up()
        front()
    elif array4[0] == 37:
        up_inv()
        front_inv()
        up_inv()
        front()
        up()
        up()
        front_inv()
        up()
        front()
    elif array4[2] == 37:
        right()
        up()
        right_inv()
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array7[5] == 37:
        up()
        up()
        right()
        up_inv()
        right_inv()
        up_inv()
        front_inv()
        up()
        front()
    elif array9[5] == 37:
        up()
        back()
        up()
        front_inv()
        up_inv()
        front()
        back_inv()
y()
#sistemare lo spigolo rosso-blu
if array1[4] == 46 or array1[4] == 24:
    up()
elif array3[4] == 46 or array3[4] == 24:
    up_inv()
elif array2[3] == 46 or array2[3] == 24:
    up()
    up()
elif array5[5] == 46 or array5[5] == 24:
    front_inv()
    up_inv()
    front()
#inserire la coppia rosso-blu
#spigolo orientato
if array2[5] == 46:
    if array1[3] == 31:
        right()
        up()
        right()
        right()
        front()
        right()
        front_inv()
    elif array1[5] == 31:
        up()
        up()
        right()
        up_inv()
        right_inv()
        up_inv()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up_inv()
        right_inv()
    elif array3[5] == 31:
        right()
        up()
        up()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
    elif array3[3] == 31:
        right()
        up()
        up()
        right()
        right()
        front()
        right()
        front_inv()
    elif array4[3] == 31:
        up_inv()
        right()
        up()
        right_inv()
    elif array4[5] == 31:
        up()
        right()
        up_inv()
        right_inv()
    elif array6[5] == 31:
        right()
        up_inv()
        right()
        right()
        front()
        right()
        front_inv()
    elif array4[6] == 31:
        up_inv()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up()
        right_inv()
    elif array4[8] == 31:
        up()
        right()
        up()
        right_inv()
        up()
        up()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up_inv()
        right_inv()
    elif array6[6] == 31:
        right()
        up()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
    elif array4[9] == 31:
        up()
        right_inv()
        up()
        up()
        right()
        right()
        up()
        right()
        right()
        up()
        right()
    elif array4[11] == 31:
        up()
        right()
        up()
        up()
        right_inv()
        up()
        up()
        right()
        up_inv()
        right_inv()
    elif array4[0] == 31:
        right()
        up_inv()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
    elif array4[2] == 31:
        up()
        up()
        right()
        up()
        right_inv()
        up()
        up()
        right()
        up_inv()
        right_inv()
    elif array7[5] == 31:
        up_inv()
        right_inv()
        front()
        right()
        front_inv()
        right()
        up()
        right_inv()
#spigolo non orientato
else:
    if array1[3] == 31:
        up()
        front_inv()
        up()
        up()
        front()
        front()
        right_inv()
        front_inv()
        right()
    elif array1[5] == 31:
        up()
        front_inv()
        up()
        up()
        front()
        up()
        front_inv()
        up_inv()
        front()
    elif array3[5] == 31:
        up_inv()
        right_inv()
        front()
        right()
        front_inv()
        up_inv()
        front_inv()
        up_inv()
        front()
    elif array3[3] == 31:
        up()
        front_inv()
        up_inv()
        front()
        front()
        right_inv()
        front_inv()
        right()
    elif array4[3] == 31:
        front_inv()
        up()
        up()
        front()
        up()
        up()
        front_inv()
        up()
        front()
    elif array4[5] == 31:
        up_inv()
        right()
        up()
        up()
        right_inv()
        up()
        front_inv()
        up_inv()
        front()
    elif array6[5] == 31:
        up_inv()
        right()
        up_inv()
        right_inv()
        front_inv()
        up_inv()
        front()
    elif array4[6] == 31:
        right()
        up_inv()
        right_inv()
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array4[8] == 31:
        up()
        up()
        front_inv()
        up()
        front()
        up_inv()
        front_inv()
        up_inv()
        front()
    elif array6[6] == 31:
        up()
        right()
        up()
        right_inv()
        up()
        up()
        front_inv()
        up()
        front()
    elif array4[9] == 31:
        front_inv()
        up()
        front()
    elif array4[11] == 31:
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array4[0] == 31:
        up_inv()
        front_inv()
        up_inv()
        front()
        up()
        up()
        front_inv()
        up()
        front()
    elif array4[2] == 31:
        right()
        up()
        right_inv()
        up()
        up()
        front_inv()
        up_inv()
        front()
    elif array7[5] == 31:
        up()
        up()
        right()
        up_inv()
        right_inv()
        up_inv()
        front_inv()
        up()
        front()
y()
#controllo spigoli oll
if array1[4] <= 19: #if A==bianco (un bianco qualsiasi)
    if array2[5] <= 19:
        if array3[4] <= 19:
            eo=1
        else:
            up_inv()
            eo=2
    else:
        if array3[4] <= 19:
            up()
            eo=3
        else:
            eo=2
else:
    if array2[5] <=19:
        if array3[4] <= 19:
            up()
            up()
            eo=2
        else:
            eo=3
    else:
        if array3[4] <= 19:
            up()
            eo=2
        else:
            eo=0
#controllo angoli oll
if array1[3] <= 19:
    if array1[5] <= 19:
        if array3[5] <= 19:
            caso=111
        elif array4[5] <= 19:
            caso=112
        elif array4[6] <= 19:
            caso=113
    elif array4[8] <= 19:
        if array3[5] <= 19:
            caso=121
        elif array4[5] <= 19:
            caso=122
        elif array4[6] <= 19:
            caso=123
    elif array4[9] <= 19:
        if array3[5] <= 19:
            caso=131
        elif array4[5] <= 19:
            caso=132
        elif array4[6] <= 19:
            caso=133
elif array4[11] <= 19:
    if array1[5] <= 19:
        if array3[5] <= 19:
            caso=211
        elif array4[5] <= 19:
            caso=212
        elif array4[6] <= 19:
            caso=213
    elif array4[8] <= 19:
        if array3[5] <= 19:
            caso=221
        elif array4[5] <= 19:
            caso=222
        elif array4[6] <= 19:
            caso=223
    elif array4[9] <= 19:
        if array3[5] <= 19:
            caso=231
        elif array4[5] <= 19:
            caso=232
        elif array4[6] <= 19:
            caso=233
elif array4[0] <= 19:
    if array1[5] <= 19:
        if array3[5] <= 19:
            caso=311
        elif array4[5] <= 19:
            caso=312
        elif array4[6] <= 19:
            caso=313
    elif array4[8] <= 19:
        if array3[5] <= 19:
            caso=321
        elif array4[5] <= 19:
            caso=322
        elif array4[6] <= 19:
            caso=323
    elif array4[9] <= 19:
        if array3[5] <= 19:
            caso=331
        elif array4[5] <= 19:
            caso=332
        elif array4[6] <= 19:
            caso=333
#oll vero e proprio
print(array_soluzioni)
#L oll
if eo == 2:
    if caso == 111:
        left()
        front()
        right_inv()
        front_inv()
        left_inv()
        right()
        up()
        right()
        up_inv()
        right_inv()
    elif caso == 112:
        up()
        front_inv()
        up_inv()
        left_inv()
        up()
        left()
        front()
    elif caso == 113:
        up()
        right_inv()
        up_inv()
        front()
        up()
        right()
        up_inv()
        right_inv()
        front_inv()
        right()
    elif caso == 121:
        front()
        right_inv()
        front_inv()
        right()
        up()
        right()
        up_inv()
        right_inv()
    elif caso == 122:
        right_inv()
        front()
        front()
        left()
        front()
        left_inv()
        front()
        right()
    elif caso == 123:
        front()
        up()
        right()
        up_inv()
        right_inv()
        front_inv()
    elif caso == 131:
        up()
        up()
        right()
        up()
        up()
        right()
        right()
        front()
        right()
        front_inv()
        right()
        up()
        up()
        right_inv()
    elif caso == 132:
        left()
        up()
        front_inv()
        up_inv()
        left_inv()
        up()
        left()
        front()
        left_inv()
    elif caso == 133:
        up()
        left()
        front()
        front()
        right_inv()
        front_inv()
        right()
        front_inv()
        left_inv()
    elif caso == 211:
        right()
        up()
        right_inv()
        up_inv()
        right()
        up_inv()
        right_inv()
        front_inv()
        up_inv()
        front()
        right()
        up()
        right_inv()
    elif caso == 212:
        left()
        front()
        right_inv()
        front()
        right_inv()
        down()
        right()
        down_inv()
        right()
        front()
        front()
        left_inv()
    elif caso == 213:
        right()
        up()
        right_inv()
        up()
        right()
        up_inv()
        right_inv()
        up_inv()
        right_inv()
        front()
        right()
        front_inv()
    elif caso == 221:
        up_inv()
        right()
        up()
        right_inv()
        up()
        right_inv()
        front()
        right()
        front_inv()
        right()
        up()
        up()
        right_inv()
    elif caso == 222:
        left()
        front()
        right_inv()
        front()
        right()
        front()
        front()
        left_inv()
    elif caso == 223:
        up()
        up()
        front_inv()
        up_inv()
        left_inv()
        up()
        left()
        front()
        back()
        up()
        left()
        up_inv()
        left_inv()
        back_inv()
    elif caso == 231:
        right()
        up()
        right_inv()
        up()
        right()
        up()
        up()
        right_inv()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
    elif caso == 232:
        front()
        right()
        up()
        right_inv()
        up_inv()
        front()
        front()
        up_inv()
        left_inv()
        up()
        left()
        up_inv()
        left_inv()
        up()
        left()
        front()
    elif caso == 233:
        up()
        front_inv()
        left_inv()
        up_inv()
        left()
        up()
        left_inv()
        up_inv()
        left()
        up()
        front()
    elif caso == 311:
        up_inv()
        right_inv()
        up_inv()
        right()
        up_inv()
        right_inv()
        up()
        up()
        right()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
    elif caso == 312:
        up()
        left_inv()
        up_inv()
        left()
        up_inv()
        left_inv()
        up()
        left()
        up()
        left()
        front_inv()
        left_inv()
        front()
    elif caso == 313:
        up()
        right_inv()
        front_inv()
        left()
        front_inv()
        left_inv()
        front()
        front()
        right()
    elif caso == 321:
        front()
        right_inv()
        front()
        right()
        right()
        up_inv()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
        front()
        front()
    elif caso == 322:
        up()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front()
        front()
        up_inv()
        left_inv()
        up()
        left()
        front()
    elif caso == 323:
        up()
        front_inv()
        left_inv()
        up_inv()
        left()
        up()
        front()
        front()
        up()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up_inv()
        right_inv()
        front_inv()
    elif caso == 331:
        right()
        up()
        right_inv()
        up_inv()
        right_inv()
        front()
        right()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
    elif caso == 332:
        front()
        right()
        up()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
    elif caso == 333:
        up()
        left()
        right()
        right()
        front_inv()
        right()
        front_inv()
        right_inv()
        front()
        front()
        right()
        front_inv()
        left_inv()
        right()
#I oll
elif eo == 3:
    if caso == 111: #oll 57
        right()
        up()
        right_inv()
        up_inv()
        right_inv()
        left()
        front()
        right()
        front_inv()
        left_inv()
    elif caso == 112: #oll 46
        up_inv()
        right_inv()
        up_inv()
        right_inv()
        front()
        right()
        front_inv()
        up()
        right()
    elif caso == 113: #oll 34
        up()
        up()
        right()
        up()
        right()
        right()
        up_inv()
        right_inv()
        front()
        right()
        up()
        right()
        up_inv()
        front_inv()
    elif caso == 121: #oll 40
        up()
        up()
        right_inv()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
        up()
        right()
    elif caso == 122: #oll 15
        front()
        up()
        right()
        up_inv()
        right_inv()
        front_inv()
        right_inv()
        up_inv()
        front_inv()
        up()
        front()
        right()
    elif caso == 123:
        front_inv()
        left_inv()
        up_inv()
        left()
        up()
        front()
    elif caso == 131: #oll 40
        right_inv()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
        up()
        right()
    elif caso == 132:
        left_inv()
        up_inv()
        left()
        up()
        left()
        front_inv()
        left_inv()
        front()
    elif caso == 133: #oll 14
        up()
        up()
        right_inv()
        front()
        right()
        up()
        right_inv()
        front_inv()
        right()
        front()
        up_inv()
        front_inv()
    elif caso == 211: #oll 33
        right()
        up()
        right_inv()
        up_inv()
        right_inv()
        front()
        right()
        front_inv()
    elif caso == 212: #oll 13
        up()
        up()
        front()
        up()
        right()
        up_inv()
        right()
        right()
        front_inv()
        right()
        up()
        right()
        up_inv()
        right_inv()
    elif caso == 213: #oll 39
        left()
        front_inv()
        left_inv()
        up_inv()
        left()
        up()
        front()
        up_inv()
        left_inv()
    elif caso == 221: #oll 15
        up()
        up()
        front()
        up()
        right()
        up_inv()
        right_inv()
        front_inv()
        right_inv()
        up_inv()
        front_inv()
        up()
        front()
        right()
    elif caso == 222: #oll 13
        front()
        up()
        right()
        up_inv()
        right()
        right()
        front_inv()
        right()
        up()
        right()
        up_inv()
        right_inv()
    elif caso == 223: #oll 51
        front()
        up()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up_inv()
        right_inv()
        front_inv()
    elif caso == 231: #oll 46
        up()
        right_inv()
        up_inv()
        right_inv()
        front()
        right()
        front_inv()
        up()
        right()
    elif caso == 232: #oll 55
        right_inv()
        front()
        right()
        up()
        right()
        up_inv()
        right()
        right()
        front_inv()
        right()
        right()
        up_inv()
        right_inv()
        up()
        right()
        up()
        right_inv()
    elif caso == 233: #oll 52
        up()
        right()
        up()
        right_inv()
        up()
        right()
        up_inv()
        back()
        up_inv()
        back_inv()
        right_inv()
    elif caso == 311: #oll 45
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
    elif caso == 312: #oll 39
        up()
        up()
        left()
        front_inv()
        left_inv()
        up_inv()
        left()
        up()
        front()
        up_inv()
        left_inv()
    elif caso == 313: #oll 16
        front_inv()
        up_inv()
        left_inv()
        up()
        left()
        front()
        left()
        up()
        front()
        up_inv()
        front_inv()
        left_inv()
    elif caso == 321: #oll 34
        right()
        up()
        right()
        right()
        up_inv()
        right_inv()
        front()
        right()
        up()
        right()
        up_inv()
        front_inv()
    elif caso == 322: #oll 52
        up_inv()
        right()
        up()
        right_inv()
        up()
        right()
        up_inv()
        back()
        up_inv()
        back_inv()
        right_inv()
    elif caso == 323: #oll 56
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
        up()
        right()
        up()
        right()
        down()
        right_inv()
        up_inv()
        right()
        down_inv()
        right()
        right()
    elif caso == 331: #oll 14
        right_inv()
        front()
        right()
        up()
        right_inv()
        front_inv()
        right()
        front()
        up_inv()
        front_inv()
    elif caso == 332:
        front_inv()
        up_inv()
        left_inv()
        up()
        left()
        up_inv()
        left_inv()
        up()
        left()
        front()
    elif caso == 333: #oll 16
        up()
        up()
        front_inv()
        up_inv()
        left_inv()
        up()
        left()
        front()
        left()
        up()
        front()
        up_inv()
        front_inv()
        left_inv()
#cross oll
elif eo == 1:
    if caso == 112: #oll 23
        right()
        right()
        down()
        right_inv()
        up()
        up()
        right()
        down_inv()
        right_inv()
        up()
        up()
        right_inv()
    elif caso == 113: #oll 24
        up()
        left()
        front()
        right_inv()
        front_inv()
        left_inv()
        front()
        right()
        front_inv()
    elif caso == 121: #oll 25
        front()
        right_inv()
        front_inv()
        left()
        front()
        right()
        front_inv()
        left_inv()
    elif caso == 122:
        front()
        up()
        front_inv()
        up()
        front()
        up()
        up()
        front_inv()
    elif caso == 123: #oll 23
        up()
        right()
        right()
        down()
        right_inv()
        up()
        up()
        right()
        down_inv()
        right_inv()
        up()
        up()
        right_inv()
    elif caso == 131: #oll 25
        up()
        up()
        front()
        right_inv()
        front_inv()
        left()
        front()
        right()
        front_inv()
        left_inv()
    elif caso == 132: #oll 24
        up()
        up()
        left()
        front()
        right_inv()
        front_inv()
        left_inv()
        front()
        right()
        front_inv()
    elif caso == 133:
        right_inv()
        up_inv()
        right()
        up_inv()
        right_inv()
        up()
        up()
        right()
    elif caso == 211: #oll 24
        left()
        front()
        right_inv()
        front_inv()
        left_inv()
        front()
        right()
        front_inv()
    elif caso == 212:
        left()
        up()
        left_inv()
        up()
        left()
        up()
        up()
        left_inv()
    elif caso == 213: #oll 25
        up()
        front()
        right_inv()
        front_inv()
        left()
        front()
        right()
        front_inv()
        left_inv()
    elif caso == 221:
        back()
        up()
        back_inv()
        up()
        back()
        up()
        up()
        back_inv()
    elif caso == 222: #oll 27
        right()
        up()
        right_inv()
        up()
        right()
        up()
        up()
        right_inv()
    elif caso == 223: #oll 22
        up()
        up()
        right()
        up()
        up()
        right()
        right()
        up_inv()
        right()
        right()
        up_inv()
        right()
        right()
        up()
        up()
        right()
    elif caso == 231:
        right()
        right()
        down_inv()
        right()
        up()
        up()
        right_inv()
        down()
        right()
        up()
        up()
        right_inv()
    elif caso == 232: #oll 21
        right()
        up()
        up()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
        up_inv()
        right()
        up_inv()
        right_inv()
    elif caso == 233: #oll 22
        up_inv()
        right()
        up()
        up()
        right()
        right()
        up_inv()
        right()
        right()
        up_inv()
        right()
        right()
        up()
        up()
        right()
    elif caso == 311: #oll 23
        up_inv()
        right()
        right()
        down()
        right_inv()
        up()
        up()
        right()
        down_inv()
        right_inv()
        up()
        up()
        right_inv()
    elif caso == 312: #oll 25
        up_inv()
        front()
        right_inv()
        front_inv()
        left()
        front()
        right()
        front_inv()
        left_inv()
    elif caso == 313: #oll 26
        right()
        up()
        up()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
    elif caso == 321: #oll 24
        up_inv()
        left()
        front()
        right_inv()
        front_inv()
        left_inv()
        front()
        right()
        front_inv()
    elif caso == 322: #oll 22
        up()
        right()
        up()
        up()
        right()
        right()
        up_inv()
        right()
        right()
        up_inv()
        right()
        right()
        up()
        up()
        right()
    elif caso == 323: #oll 21
        up()
        right()
        up()
        up()
        right_inv()
        up_inv()
        right()
        up()
        right_inv()
        up_inv()
        right()
        up_inv()
        right_inv()
    elif caso == 331:
        left_inv()
        up_inv()
        left()
        up_inv()
        left_inv()
        up()
        up()
        left()
    elif caso == 332: #oll 22
        right()
        up()
        up()
        right()
        right()
        up_inv()
        right()
        right()
        up_inv()
        right()
        right()
        up()
        up()
        right()
    elif caso == 333:
        back_inv()
        up_inv()
        back()
        up_inv()
        back_inv()
        up()
        up()
        back()
#dot oll
elif eo == 0:
    if caso == 111: #oll 20
        front_inv()
        up_inv()
        left_inv()
        up()
        left()
        front()
        right_inv()
        up_inv()
        right_inv()
        front()
        right()
        front_inv()
        up()
        right()
    elif caso == 112: #oll 18
        left()
        front()
        right_inv()
        front()
        right()
        front()
        front()
        left()
        left()
        back_inv()
        right()
        back_inv()
        right_inv()
        back()
        back()
        left()
    elif caso == 113: #oll 19
        right()
        left_inv()
        back()
        right()
        back()
        right_inv()
        back_inv()
        left()
        right()
        right()
        front()
        right()
        front_inv()
    elif caso == 121: #oll 17
        front()
        right_inv()
        front_inv()
        right()
        right()
        left_inv()
        back()
        right()
        back_inv()
        right_inv()
        back_inv()
        left()
        right_inv()
    elif caso == 122: #oll 3
        up()
        up()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
        up_inv()
        front_inv()
        up_inv()
        left_inv()
        up()
        left()
        front()
    elif caso == 123: #oll 18
        up()
        left()
        front()
        right_inv()
        front()
        right()
        front()
        front()
        left()
        left()
        back_inv()
        right()
        back_inv()
        right_inv()
        back()
        back()
        left()
    elif caso == 131: #oll 17
        up()
        up()
        front()
        right_inv()
        front_inv()
        right()
        right()
        left_inv()
        back()
        right()
        back_inv()
        right_inv()
        back_inv()
        left()
        right_inv()
    elif caso == 132: #oll 19
        up()
        right()
        left_inv()
        back()
        right()
        back()
        right_inv()
        back_inv()
        left()
        right()
        right()
        front()
        right()
        front_inv()
    elif caso == 133: #oll 4
        up_inv()
        front()
        up()
        right()
        up_inv()
        right_inv()
        front_inv()
        up_inv()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
    elif caso == 211: #oll 19
        up_inv()
        right()
        left_inv()
        back()
        right()
        back()
        right_inv()
        back_inv()
        left()
        right()
        right()
        front()
        right()
        front_inv()
    elif caso == 212: #oll 3
        up()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
        up_inv()
        front_inv()
        up_inv()
        left_inv()
        up()
        left()
        front()
    elif caso == 213: #oll 17
        up()
        front()
        right_inv()
        front_inv()
        right()
        right()
        left_inv()
        back()
        right()
        back_inv()
        right_inv()
        back_inv()
        left()
        right_inv()
    elif caso == 221: #oll 3
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
        up_inv()
        front_inv()
        up_inv()
        left_inv()
        up()
        left()
        front()
    elif caso == 222: #oll 3
        up_inv()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
        up_inv()
        front_inv()
        up_inv()
        left_inv()
        up()
        left()
        front()
    elif caso == 223: #oll 2
        up()
        up()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
        back()
        up()
        left()
        up_inv()
        left_inv()
        back_inv()
    elif caso == 231: #oll 18
        up()
        up()
        left()
        front()
        right_inv()
        front()
        right()
        front()
        front()
        left()
        left()
        back_inv()
        right()
        back_inv()
        right_inv()
        back()
        back()
        left()
    elif caso == 232: #oll 1
        up()
        right()
        up()
        up()
        right()
        right()
        front()
        right()
        front_inv()
        up()
        up()
        right_inv()
        front()
        right()
        front_inv()
    elif caso == 233: #oll 2
        up_inv()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
        back()
        up()
        left()
        up_inv()
        left_inv()
        back_inv()
    elif caso == 311: #oll 18
        up_inv()
        left()
        front()
        right_inv()
        front()
        right()
        front()
        front()
        left()
        left()
        back_inv()
        right()
        back_inv()
        right_inv()
        back()
        back()
        left()
    elif caso == 312: #oll 17
        up_inv()
        front()
        right_inv()
        front_inv()
        right()
        right()
        left_inv()
        back()
        right()
        back_inv()
        right_inv()
        back_inv()
        left()
        right_inv()
    elif caso == 313: #oll 4
        up()
        up()
        front()
        up()
        right()
        up_inv()
        right_inv()
        front_inv()
        up_inv()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
    elif caso == 321: #oll 19
        up()
        up()
        right()
        left_inv()
        back()
        right()
        back()
        right_inv()
        back_inv()
        left()
        right()
        right()
        front()
        right()
        front_inv()
    elif caso == 322: #oll 2
        up()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
        back()
        up()
        left()
        up_inv()
        left_inv()
        back_inv()
    elif caso == 323: #oll 1
        right()
        up()
        up()
        right()
        right()
        front()
        right()
        front_inv()
        up()
        up()
        right_inv()
        front()
        right()
        front_inv()
    elif caso == 331: #oll 4
        up()
        front()
        up()
        right()
        up_inv()
        right_inv()
        front_inv()
        up_inv()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
    elif caso == 332: #oll 2
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
        back()
        up()
        left()
        up_inv()
        left_inv()
        back_inv()
    elif caso == 333: #oll 4
        front()
        up()
        right()
        up_inv()
        right_inv()
        front_inv()
        up_inv()
        front()
        right()
        up()
        right_inv()
        up_inv()
        front_inv()
#controllo headlights nel pll
if int(array4[9] / 10) == int(array4[11] / 10):
    if int(array4[8] / 10) == int(array4[6] / 10):
        headlights=0
    else:
        headlights=1
        up_inv()
else:
    if int(array4[8] / 10) == int(array4[6] / 10):
        headlights=1
        up()
        up()
    else:
        if int(array4[5] / 10) == int(array4[3] / 10):
            headlights=1
            up()
        else:
            if int(array4[2] / 10) == int(array4[0] / 10):
                headlights=1
            else:
                headlights=2
#controllo supplementare per U perm
if headlights == 0:
    if int(array4[10] / 10) == int(array4[9] / 10):
        caso=0
    elif int(array4[7] / 10) == int(array4[6] / 10):
        caso=0
        up_inv()
    elif int(array4[4] / 10) == int(array4[3] / 10):
        caso=0
        up()
        up()
    elif int(array4[1] / 10) == int(array4[0] / 10):
        caso=0
        up()
#pll vero e proprio
#pll adj
if headlights == 1:
    j = int(array4[1] / 10)
    k = int(array4[0] / 10)
    if j == k:
        j = int(array4[10] / 10)
        k = int(array4[11] / 10)
        if j == k: #pll Jb
            right()
            up()
            right_inv()
            front_inv()
            right()
            up()
            right_inv()
            up_inv()
            right_inv()
            front()
            right()
            right()
            up_inv()
            right_inv()
        elif 3*(j*j+k*k)+abs(j-k) == 124: #pll F
            right_inv()
            up_inv()
            front_inv()
            right()
            up()
            right_inv()
            up_inv()
            right_inv()
            front()
            right()
            right()
            up_inv()
            right_inv()
            up_inv()
            right()
            up()
            right_inv()
            up()
            right()
        elif 3*(j*j+k*k)+abs(j-k) != 124 and j != k: #pll Ja
            x()
            right()
            right()
            front()
            right()
            front_inv()
            right()
            up()
            up()
            left_inv()
            back()
            left()
            up()
            up()
            x_inv()
    elif 3*(j*j+k*k)+abs(j-k) == 124:
        j = int(array4[10] / 10)
        k = int(array4[11] / 10)
        if j == k: #pll T
            right()
            up()
            right_inv()
            up_inv()
            right_inv()
            front()
            right()
            right()
            up_inv()
            right_inv()
            up_inv()
            right()
            up()
            right_inv()
            front_inv()
        elif 3*(j*j+k*k)+abs(j-k) == 124: #pll Gd
            right()
            up()
            right_inv()
            up_inv()
            down()
            right()
            right()
            up_inv()
            right()
            up_inv()
            right_inv()
            up()
            right_inv()
            up()
            right()
            right()
            down_inv()
        elif 3*(j*j+k*k)+abs(j-k) != 124 and j != k: #pll Gb
            right_inv()
            up_inv()
            right()
            up()
            down_inv()
            right()
            right()
            up()
            right_inv()
            up()
            right()
            up_inv()
            right()
            up_inv()
            right()
            right()
            down()
    elif 3*(j*j+k*k)+abs(j-k) != 124 and j != k:
        j = int(array4[10] / 10)
        k = int(array4[11] / 10)
        if j == k: #pll Rb
            right()
            right()
            front()
            right()
            up()
            right()
            up_inv()
            right_inv()
            front_inv()
            right()
            up()
            up()
            right_inv()
            up()
            up()
            right()
        elif 3*(j*j+k*k)+abs(j-k) == 124: #pll Ga
            right()
            right()
            up()
            right_inv()
            up()
            right_inv()
            up_inv()
            right()
            up_inv()
            right()
            right()
            up_inv()
            down()
            right_inv()
            up()
            right()
            down_inv()
        elif 3*(j*j+k*k)+abs(j-k) != 124 and j != k:
            j = int(array4[7] / 10)
            k = int(array4[8] / 10)
            if j == k: #pll Ab
                x_inv()
                left()
                left()
                down()
                down()
                left()
                up()
                left_inv()
                down()
                down()
                left()
                up_inv()
                left()
                x()
            elif 3*(j*j+k*k)+abs(j-k) == 124: #pll Aa
                x()
                left()
                left()
                down()
                down()
                left_inv()
                up_inv()
                left()
                down()
                down()
                left_inv()
                up()
                left_inv()
                x_inv()
            elif 3*(j*j+k*k)+abs(j-k) != 124 and j != k:
                if int(array4[10] / 10) == int(array4[9] / 10): #pll Gc
                    right()
                    right()
                    up_inv()
                    right()
                    up_inv()
                    right()
                    up()
                    right_inv()
                    up()
                    right()
                    right()
                    up()
                    down_inv()
                    right()
                    up_inv()
                    right_inv()
                    down()
                else: #pll Ra
                    right()
                    up_inv()
                    right_inv()
                    up_inv()
                    right()
                    up()
                    right()
                    down()
                    right_inv()
                    up_inv()
                    right()
                    down_inv()
                    right_inv()
                    up()
                    up()
                    right_inv()
#pll edges
elif headlights == 0:
    if caso == 0:
        j = int(array4[7] / 10)
        k = int(array4[6] / 10)
        if 3*(j*j+k*k)+abs(j-k) == 124: #pll Ua
            right()
            up_inv()
            right()
            up()
            right()
            up()
            right()
            up_inv()
            right_inv()
            up_inv()
            right()
            right()
        elif 3*(j*j+k*k)+abs(j-k) != 124 and j != k: #pll Ub
            right()
            right()
            up()
            right()
            up()
            right_inv()
            up_inv()
            right_inv()
            up_inv()
            right_inv()
            up()
            right_inv()
    else:
        j = int(array4[10] / 10)
        k = int(array4[9] / 10)
        if 3*(j*j+k*k)+abs(j-k) == 124: #pll H
            right()
            right()
            up()
            up()
            right()
            up()
            up()
            right()
            right()
            up()
            up()
            right()
            right()
            up()
            up()
            right()
            up()
            up()
            right()
            right()
        else:
            if j == int(array4[8] / 10): #pll Z
                right_inv()
                up_inv()
                right()
                up_inv()
                right()
                up()
                right()
                up_inv()
                right_inv()
                up()
                right()
                up()
                right()
                right()
                up_inv()
                right_inv()
            else: #pll Z
                up()
                right_inv()
                up_inv()
                right()
                up_inv()
                right()
                up()
                right()
                up_inv()
                right_inv()
                up()
                right()
                up()
                right()
                right()
                up_inv()
                right_inv()
#pll diag
elif headlights == 2:
    j = int(array4[10] / 10)
    k = int(array4[11] / 10)
    if j == k:
        j = int(array4[1] / 10)
        k = int(array4[0] / 10)
        if j == k: #pll V
            up_inv()
            right_inv()
            up()
            right_inv()
            up_inv()
            right()
            down_inv()
            right_inv()
            down()
            right_inv()
            up()
            down_inv()
            right()
            right()
            up_inv()
            right()
            right()
            down()
            right()
            right()
        elif 3*(j*j+k*k)+abs(j-k) == 124: #pll Na
            right()
            up()
            right_inv()
            up()
            right()
            up()
            right_inv()
            front_inv()
            right()
            up()
            right_inv()
            up_inv()
            right_inv()
            front()
            right()
            right()
            up_inv()
            right_inv()
            up()
            up()
            right()
            up_inv()
            right_inv()
        elif 3*(j*j+k*k)+abs(j-k) != 124 and j != k: #pll Y
            up()
            front()
            right()
            up_inv()
            right_inv()
            up_inv()
            right()
            up()
            right_inv()
            front_inv()
            right()
            up()
            right_inv()
            up_inv()
            right_inv()
            front()
            right()
            front_inv()
    elif 3*(j*j+k*k)+abs(j-k) == 124:
        j = int(array4[7] / 10)
        k = int(array4[8] / 10)
        if j == k: #pll V
            up()
            up()
            right_inv()
            up()
            right_inv()
            up_inv()
            right()
            down_inv()
            right_inv()
            down()
            right_inv()
            up()
            down_inv()
            right()
            right()
            up_inv()
            right()
            right()
            down()
            right()
            right()
        elif 3*(j*j+k*k)+abs(j-k) == 124: #pll Nb
            right_inv()
            up()
            right()
            up_inv()
            right_inv()
            front_inv()
            up_inv()
            front()
            right()
            up()
            right_inv()
            front()
            right_inv()
            front_inv()
            right()
            up_inv()
            right()
        elif 3*(j*j+k*k)+abs(j-k) != 124 and j != k: #pll Y
            up()
            up()
            front()
            right()
            up_inv()
            right_inv()
            up_inv()
            right()
            up()
            right_inv()
            front_inv()
            right()
            up()
            right_inv()
            up_inv()
            right_inv()
            front()
            right()
            front_inv()
    elif 3*(j*j+k*k)+abs(j-k) != 124 and j != k:
        j = int(array4[1] / 10)
        k = int(array4[0] / 10)
        if j == k: #pll Y
            up_inv()
            front()
            right()
            up_inv()
            right_inv()
            up_inv()
            right()
            up()
            right_inv()
            front_inv()
            right()
            up()
            right_inv()
            up_inv()
            right_inv()
            front()
            right()
            front_inv()
        elif 3*(j*j+k*k)+abs(j-k) == 124: #pll V
            right_inv()
            up()
            right_inv()
            up_inv()
            right()
            down_inv()
            right_inv()
            down()
            right_inv()
            up()
            down_inv()
            right()
            right()
            up_inv()
            right()
            right()
            down()
            right()
            right()
        elif 3*(j*j+k*k)+abs(j-k) != 124 and j != k:
            j = int(array4[4] / 10)
            k = int(array4[5] / 10)
            if j == k: #pll V
                up()
                right_inv()
                up()
                right_inv()
                up_inv()
                right()
                down_inv()
                right_inv()
                down()
                right_inv()
                up()
                down_inv()
                right()
                right()
                up_inv()
                right()
                right()
                down()
                right()
                right()
            elif 3*(j*j+k*k)+abs(j-k) == 124: #pll Y
                front()
                right()
                up_inv()
                right_inv()
                up_inv()
                right()
                up()
                right_inv()
                front_inv()
                right()
                up()
                right_inv()
                up_inv()
                right_inv()
                front()
                right()
                front_inv()
            elif 3*(j*j+k*k)+abs(j-k) != 124 and j != k:
                if j == int(array4[6] / 10): #pll E
                    up()
                    x_inv()
                    right()
                    up_inv()
                    right_inv()
                    down()
                    right()
                    up()
                    right_inv()
                    down_inv()
                    right()
                    up()
                    right_inv()
                    down()
                    right()
                    up_inv()
                    right_inv()
                    down_inv()
                    x()
                else: #pll E
                    x_inv()
                    right()
                    up_inv()
                    right_inv()
                    down()
                    right()
                    up()
                    right_inv()
                    down_inv()
                    right()
                    up()
                    right_inv()
                    down()
                    right()
                    up_inv()
                    right_inv()
                    down_inv()
                    x()
#AUF
if array4[4] == 52:
    up_inv()
elif array4[4] == 62:
    up()
    up()
elif array4[4] == 42:
    up()

print_arrays()
print(array_soluzioni)

rp = len(array_soluzioni) - 10
scambi = 1
while scambi != 0:
    ss = 0
    scambi = 0
    while ss < rp:
        if array_soluzioni[ss] == array_soluzioni[ss+1] and array_soluzioni[ss] == array_soluzioni[ss+2]:
            if array_soluzioni[ss] == 'F':
                del array_soluzioni[ss]
                del array_soluzioni[ss + 1]
                array_soluzioni[ss] = 'Fi'
                rp = rp - 2
                scambi = scambi + 1
            elif array_soluzioni[ss] == 'Fi':
                del array_soluzioni[ss]
                del array_soluzioni[ss + 1]
                array_soluzioni[ss] = 'F'
                rp = rp - 2
                scambi = scambi + 1
            elif array_soluzioni[ss] == 'U':
                del array_soluzioni[ss]
                del array_soluzioni[ss + 1]
                array_soluzioni[ss] = 'Ui'
                rp = rp - 2
                scambi = scambi + 1
            elif array_soluzioni[ss] == 'Ui':
                array_soluzioni[ss] = 'U'
                del array_soluzioni[ss]
                del array_soluzioni[ss + 1]
                rp = rp -2
                scambi = scambi + 1
            elif array_soluzioni[ss] == 'D':
                array_soluzioni[ss] = 'Di'
                del array_soluzioni[ss]
                del array_soluzioni[ss + 1]
                rp = rp - 2
                scambi = scambi + 1
            elif array_soluzioni[ss] == 'Di':
                array_soluzioni[ss] = 'D'
                del array_soluzioni[ss]
                del array_soluzioni[ss + 1]
                rp = rp - 2
                scambi = scambi + 1
            elif array_soluzioni[ss] == 'B':
                array_soluzioni[ss] = 'Bi'
                del array_soluzioni[ss]
                del array_soluzioni[ss + 1]
                rp = rp - 2
                scambi = scambi + 1
            elif array_soluzioni[ss] == 'Bi':
                array_soluzioni[ss] = 'B'
                del array_soluzioni[ss]
                del array_soluzioni[ss + 1]
                rp = rp - 2
                scambi = scambi + 1
            elif array_soluzioni[ss] == 'L':
                array_soluzioni[ss] = 'Li'
                del array_soluzioni[ss]
                del array_soluzioni[ss + 1]
                rp = rp - 2
                scambi = scambi + 1
            elif array_soluzioni[ss] == 'Li':
                array_soluzioni[ss] = 'L'
                del array_soluzioni[ss]
                del array_soluzioni[ss + 1]
                rp = rp - 2
                scambi = scambi + 1
            elif array_soluzioni[ss] == 'R':
                array_soluzioni[ss] = 'Ri'
                del array_soluzioni[ss]
                del array_soluzioni[ss + 1]
                rp = rp - 2
                scambi = scambi + 1
            elif array_soluzioni[ss] == 'Ri':
                array_soluzioni[ss] = 'R'
                del array_soluzioni[ss]
                del array_soluzioni[ss + 1]
                rp = rp - 2
                scambi = scambi + 1
        if (array_soluzioni[ss] == 'F' and array_soluzioni[ss + 1] == 'Fi') or (
                array_soluzioni[ss] == 'Fi' and array_soluzioni[ss + 1] == 'F'):
            del array_soluzioni[ss]
            del array_soluzioni[ss]
            rp = rp - 2
            scambi = scambi + 1
        elif (array_soluzioni[ss] == 'R' and array_soluzioni[ss + 1] == 'Ri') or (
                array_soluzioni[ss] == 'Ri' and array_soluzioni[ss + 1] == 'R'):
            del array_soluzioni[ss]
            del array_soluzioni[ss]
            scambi = scambi + 1
            rp = rp - 2
        elif (array_soluzioni[ss] == 'L' and array_soluzioni[ss + 1] == 'Li') or (
                array_soluzioni[ss] == 'Li' and array_soluzioni[ss + 1] == 'L'):
            del array_soluzioni[ss]
            del array_soluzioni[ss]
            scambi = scambi + 1
        elif (array_soluzioni[ss] == 'B' and array_soluzioni[ss + 1] == 'Bi') or (
                array_soluzioni[ss] == 'Bi' and array_soluzioni[ss + 1] == 'B'):
            del array_soluzioni[ss]
            del array_soluzioni[ss]
            rp = rp - 2
            scambi = scambi + 1
        elif (array_soluzioni[ss] == 'U' and array_soluzioni[ss + 1] == 'Ui') or (
                array_soluzioni[ss] == 'Ui' and array_soluzioni[ss + 1] == 'U'):
            del array_soluzioni[ss]
            del array_soluzioni[ss]
            rp = rp - 2
            scambi = scambi + 1
            print(ss)
        elif (array_soluzioni[ss] == 'D' and array_soluzioni[ss + 1] == 'Di') or (
                array_soluzioni[ss] == 'Di' and array_soluzioni[ss + 1] == 'D'):
            del array_soluzioni[ss]
            del array_soluzioni[ss]
            rp = rp - 2
            scambi = scambi + 1
        ss = ss + 1
print(array_soluzioni)
