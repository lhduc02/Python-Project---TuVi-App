def pham_hoang_oc(year_birth, year):
    age = year - year_birth + 1
    if age >= 70:
        age -= 60
    age = str(age)
    age1 = age[:-1]
    age2 = age[-1]
    hoangOc = ['Nhất Cát', 'Nhì Nghi', 'Tam Địa sát', 'Tứ Tấn tài', 'Ngũ Thọ tử', 'Lục Hoang ốc']
    return hoangOc[(int(age1)+int(age2))%6 - 1]

print(pham_hoang_oc(2002, 2038))
