# testing purpose
def objective(arr) :
    # nilai minimum objektif = -(1 + 1x13 + 25 + 25 + 25 + 15 + 4) = -108
    # nilai maksimum objektif = 0
    # lag : ke 5 angka memenuhi angka magic
    # lead : angka pinggir = 189

    count = 0
    # pusat
    if arr[62] != 63 :
        count+=1000

    # 3 angka tengah (13*1)

    # baris plane 3
    if arr[61] + 63 + arr[63] != 189 :
        count+=100

    # kolom plane 3
    if arr[57] + 63 + arr[67] != 189 :
        count+=100

    # diagonal bidang 1 sb y plane 3
    if arr[56] + 63 + arr[68] != 189 :
        count+=100

    # diagonal bidang 2 sb y plane 3
    if arr[58] + 63 + arr[66] != 189 :
        count+=100

    # tiang
    if arr[37] + 63 + arr[87] != 189 :
        count+=100

    #tes
    # diagonal bidang 1 sb x
    if arr[42] + 63 + arr[82] != 189 :
        count+=100

    # diagonal bidang 2 sb x
    if arr[32] + 63 + arr[92] != 189 :
        count+=100

    # diagonal bidang 1 sb z
    if arr[36] + 63 + arr[88] != 189 :
        count+=100

    # diagonal bidang 2 sb z
    if arr[38] + 63 + arr[86] != 189 :
        count+=100

    # diagonal ruang 1
    if arr[31] + 63 + arr[93] != 189 :
        count+=100

    # diagonal ruang 2
    if arr[33] + 63 + arr[91] != 189 :
        count+=100

    # diagonal ruang 3
    if arr[41] + 63 + arr[83] != 189 :
        count+=100

    # diagonal ruang 4
    if arr[43] + 63 + arr[81] != 189 :
        count+=100

    # Baris (25*1)
    for i in range(0,121,5) :
        if arr[i] + 189 + arr[i+4] !=315 :
            count+=10

    #Kolom (25*1)
    for j in range(0,5) :
        for i in range(j*25,(j*25)+5) :
            if arr[i] + 189 + arr[i+20]!=315 :
                count+=10

    # Tiang (25*1)
    for i in range(0,25) :
        if arr[i] + 189 + arr[i+100]!=315 :
            count+=10

    # Diagonal Bidang (5*2*3*1)
    #  diagonal sumbu tiang
    for i in range(0,125,25) :
        if (arr[i] + arr[i+6] + arr[i+18] + arr[i+24])-(arr[i+4] + arr[i+8] + arr[i+16] + arr[i+20])!=0:
            count+=25

    #  diagonal sb baris
    for i in range(0,21,5) :
        if (arr[i] + arr[i+26] + arr[i+78] + arr[i+104])-(arr[i+4] + arr[i+28] + arr[i+76] + arr[i+100])!=0 :
            count+=25

    #  diagonal sb kolom
    for i in range(0,5) :
        if (arr[i] + arr[i+30] + arr[i+60] + arr[i+90] + arr[i+120])-(arr[i+20] + arr[i+40] + arr[i+60] + arr[i+80] + arr[i+100])!=0 :
            count+=25

    # Diagonal Ruang (4*1)
    if arr[0] + 189 + arr[124] !=315 :
        count+=50
    if arr[4] + 189 + arr[120] !=315 :
        count+=50
    if arr[20] + 189 + arr[104] !=315 :
        count+=50
    if arr[24] + 189 + arr[100] !=315 :
        count+=50
        
    return (-count)

def diagnostic(arr):
    # nilai minimum objektif = -(1 + 1x13 + 25 + 25 + 25 + 15 + 4) = -108
    # nilai maksimum objektif = 0
    # lag : ke 5 angka memenuhi angka magic
    # lead : angka pinggir = 189
    center = True
    count = 0
    # pusat
    if arr[62] != 63 :
        count+=1000

    # 3 angka tengah (13*1)

    # baris plane 3
    if arr[61] + 63 + arr[63] != 189 :
        count+=100
        center=False

    # kolom plane 3
    if arr[57] + 63 + arr[67] != 189 :
        count+=100
        center=False

    # diagonal bidang 1 sb y plane 3
    if arr[56] + 63 + arr[68] != 189 :
        count+=100
        center=False

    # diagonal bidang 2 sb y plane 3
    if arr[58] + 63 + arr[66] != 189 :
        count+=100
        center=False

    # tiang
    if arr[37] + 63 + arr[87] != 189 :
        count+=100
        center=False

    #tes
    # diagonal bidang 1 sb x
    if arr[42] + 63 + arr[82] != 189 :
        count+=100
        center=False

    # diagonal bidang 2 sb x
    if arr[32] + 63 + arr[92] != 189 :
        count+=100
        center=False

    # diagonal bidang 1 sb z
    if arr[36] + 63 + arr[88] != 189 :
        count+=100
        center=False

    # diagonal bidang 2 sb z
    if arr[38] + 63 + arr[86] != 189 :
        count+=100
        center=False

    # diagonal ruang 1
    if arr[31] + 63 + arr[93] != 189 :
        count+=100
        center=False

    # diagonal ruang 2
    if arr[33] + 63 + arr[91] != 189 :
        count+=100
        center=False

    # diagonal ruang 3
    if arr[41] + 63 + arr[83] != 189 :
        count+=100
        center=False

    # diagonal ruang 4
    if arr[43] + 63 + arr[81] != 189 :
        count+=100
        center=False

    if(center): print("center cube is solved")

    # Baris (25*1)
    baris=True
    for i in range(0,121,5) :
        if arr[i] + 189 + arr[i+4] !=315 :
            count+=1
            baris=False
    if(baris): print("baris is sovled")

    #Kolom (25*1)
    kolom = True
    for j in range(0,5) :
        for i in range(j*25,(j*25)+5) :
            if arr[i] + 189 + arr[i+20]!=315 :
                count+=1
                kolom = False
    if(kolom): print("kolom is solved")

    # Tiang (25*1)
    tiang = True
    for i in range(0,25) :
        if arr[i] + 189 + arr[i+100]!=315 :
            count+=1
            tiang = False
    if(tiang): print("tiang is solved")


    # Diagonal Bidang (5*2*3*1)
    #  diagonal sumbu tiang
    dgtiang = True
    for i in range(0,125,25) :
        if (arr[i] + arr[i+6] + arr[i+18] + arr[i+24])-(arr[i+4] + arr[i+8] + arr[i+16] + arr[i+20])!=0:
            count+=1
            dgtiang = False
    if(dgtiang): print("dgtiang is solved")

    #  diagonal sb baris
    dgbaris = True
    for i in range(0,21,5) :
        if (arr[i] + arr[i+26] + arr[i+78] + arr[i+104])-(arr[i+4] + arr[i+28] + arr[i+76] + arr[i+100])!=0 :
            count+=1
            dgbaris = False
    if (dgbaris): print("dgbaris is solved")


    #  diagonal sb kolom
    dgkolom = True
    for i in range(0,5) :
        if (arr[i] + arr[i+30] + arr[i+60] + arr[i+90] + arr[i+120])-(arr[i+20] + arr[i+40] + arr[i+60] + arr[i+80] + arr[i+100])!=0 :
            count+=1
            dgkolom = False
    if (dgkolom): print("dgkolom is solved")

    # Diagonal Ruang (4*1)
    dr = True
    if arr[0] + 189 + arr[124] !=315 :
        count+=10
        dr = False
    if arr[4] + 189 + arr[120] !=315 :
        count+=10
        dr = False
    if arr[20] + 189 + arr[104] !=315 :
        count+=10
        dr = False
    if arr[24] + 189 + arr[100] !=315 :
        count+=10
        dr = False
    if(dr): print("diagonal ruang is solved")
        
    return