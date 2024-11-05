import streamlit as st
import kim_lau
import hoang_oc
import tam_tai

st.title('Kiểm tra tử vi tuổi của bạn')
i1, i2 = st.columns(2)
b1, b2, b3, b4, b5 = st.columns(5)

with i1:
    year_birth = st.text_input('Nhập năm sinh của bạn')
with i2:
    gender = st.selectbox('Chọn giới tính', ['Chọn', 'Nam', 'Nữ'])

with b3:
    check = st.button('Kiểm tra')

if check:
    if year_birth.isnumeric() == False:
        st.write('Năm sinh không hợp lệ')
    elif gender == 'Chọn':
        st.write('Bạn chưa chọn giới tính')
    else:
        for year in range(2024, 2101):
            kimlau_cuaban = kim_lau.phamKimLau(int(year_birth), year, gender)
            tam_tai_cuaban = tam_tai.pham_tam_tai(int(year_birth), year)
            hoangoc_cuaban = hoang_oc.pham_hoang_oc(int(year_birth), year)
            if kimlau_cuaban == '0' and tam_tai_cuaban == '0':
                st.write('Năm', str(year), 'bạn không gặp Tam tai hay Kim lâu, và Hoang ốc của bạn là', hoangoc_cuaban)
            elif kimlau_cuaban == '0' and tam_tai_cuaban == '1':
                st.write('Năm', str(year), 'bạn gặp Tam tai, không phạm Kim lâu, và Hoang ốc của bạn là', hoangoc_cuaban)
            elif kimlau_cuaban != '0' and tam_tai_cuaban == '0':
                st.write('Năm', str(year), 'bạn không gặp Tam tai,', kimlau_cuaban, 'và Hoang ốc của bạn là', hoangoc_cuaban)
            elif kimlau_cuaban != '0' and tam_tai_cuaban == '1':
                st.write('Năm', str(year), 'bạn gặp Tam tai,', kimlau_cuaban, 'và Hoang ốc của bạn là', hoangoc_cuaban)

