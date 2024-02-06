def phamKimLau(year_birth, year, gender):
    age = year - year_birth + 1
    if gender == 'Nam':
        kl = age%9
        if kl == 1:
            return 'Kim lâu thân'
        elif kl == 3:
            return 'Kim lâu thê'
        elif kl == 6:
            return 'Kim lâu tử'
        elif kl == 8:
            return 'Kim lâu súc'
        else:
            return '0'
    else:
        kl = int(str(age)[-1])
        if kl in [1, 3, 6, 8]:
            return 'Kim lâu'
        else:
            return '0'
