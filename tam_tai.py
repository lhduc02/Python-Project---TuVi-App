def pham_tam_tai(year_birth, year):
    tuoi_12_con_giap = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
    tuoi_sinh = tuoi_12_con_giap[(year_birth - 1900)%12]
    nam_hien_tai = tuoi_12_con_giap[(year - 1900)%12]
    print(tuoi_sinh, nam_hien_tai)
    if tuoi_sinh in ['Tý', 'Thìn', 'Thân'] and nam_hien_tai in ['Dần', 'Mão', 'Thìn']:
        return '1'
    elif tuoi_sinh in ['Mão', 'Mùi', 'Hợi'] and nam_hien_tai in ['Tỵ', 'Ngọ', 'Mùi']:
        return '1'
    elif tuoi_sinh in ['Ngọ', 'Dần', 'Tuất'] and nam_hien_tai in ['Thân', 'Dậu', 'Tuất']:
        return '1'
    elif tuoi_sinh in ['Sửu', 'Tỵ', 'Dần'] and nam_hien_tai in ['Tý', 'Sửu', 'Hợi']:
        return '1'
    else:
        return '0'
