import streamlit as st
import kimlau
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
            kimlau_cuaban = kimlau.phamKimLau(int(year_birth), year, gender)
            hoangoc_cuaban = '0'
            tam_tai_cuaban = '0'
            if kimlau_cuaban == '0' and hoangoc_cuaban == '0' and tam_tai_cuaban == '0':
                st.write('Năm', str(year), 'bạn không phạm tam tai, kim lâu hay hoàng ốc')
            else:
                st.write('Năm', str(year), 'bạn phạm', kimlau_cuaban)



