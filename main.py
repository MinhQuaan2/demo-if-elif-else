toan = van = anh = 0
HSG = HSK = HSTB = con_lai = 0
while True:
    a = input('Nhập tên học sinh: ')
    toan = float(input('Nhập điểm toán: '))
    van = float(input('Nhập điểm văn: '))
    anh = float(input('Nhập điểm anh: '))

    trung_binh_cong = (toan*2 + van*2 + anh)/5
    print('Điểm trung bình của học sinh', a, 'là: ', trung_binh_cong)

    if trung_binh_cong > 8:
        HSG += 1
        print('Học sinh', a, 'là học sinh giỏi')
    elif trung_binh_cong > 6:
        HSK += 1
        print('Học sinh', a, 'là học sinh khá')
    elif trung_binh_cong > 5:
        HSTB += 1
        print('Học sinh', a, 'là học sinh trung bình')
    else:
        con_lai += 1
        print('Học sinh', a, 'chưa đạt')
    yn = input('Bạn còn muốn tiếp tục nhập không? (Y/N):').strip().upper()
    if yn != "Y":
        break

print('Số học sinh giỏi:', HSG)
print('Số học sinh khá:', HSK)
print('Số học sinh trung bình:', HSTB)
print('Số học sinh còn lại:', con_lai)

