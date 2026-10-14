import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="QUẢN LÝ ĐIỂM SINH VIÊN", page_icon="🎓", layout="centered"
)

st.markdown(
    "<h1 style='text-align: center; color: #1f77b4;'>QUẢN LÝ ĐIỂM SINH VIÊN</h1>",
    unsafe_allow_html=True,
)
st.write("---")

data = {
    "Họ và tên": [
        "Nguyễn Văn An",
        "Trần Thị Bình",
        "Lê Hoàng Cường",
        "Phạm Thị Dung",
        "Hoàng Văn Em",
        "Vũ Thị Phương",
        "Đỗ Minh Giang",
        "Bùi Thị Hoa",
        "Ngô Văn Hùng",
        "Dương Thị Kim",
    ],
    "Điểm chuyên cần": [10, 9, 8, 10, 7, 9, 8, 10, 6, 9],
    "Điểm giữa kỳ": [8, 7.5, 6, 9, 5.5, 8, 7, 8.5, 5, 9],
    "Điểm cuối kỳ": [7.5, 8, 7, 8.5, 6, 9, 7.5, 9.5, 5.5, 8],
    "Tong_ket": [8.15, 8.05, 6.9, 8.95, 6.05, 8.7, 7.45, 9.3, 5.45, 8.5],
    "Xep_loai": [
        "Khá",
        "Khá",
        "Trung bình",
        "Giỏi",
        "Trung bình",
        "Giỏi",
        "Khá",
        "Giỏi",
        "Trung bình",
        "Giỏi",
    ],
}
df = pd.DataFrame(data)

st.subheader("📋 Bảng điểm của 10 sinh viên")
st.dataframe(df, use_container_width=True)

st.write("---")
st.subheader("📊 Thống kê chung của lớp")
diem_tb_lop = df["Tong_ket"].mean()
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = len(df[df["Tong_ket"] >= 5.0])

col1, col2 = st.columns(2)
with col1:
    st.metric(
        label="Điểm trung bình của lớp", value=f"{diem_tb_lop:.2f} / 10"
    )
    st.metric(label="Số sinh viên đạt (>= 5.0)", value=f"{so_sv_dat} / 10")
with col2:
    st.info(
        f"🏆 **Cao nhất:** {sv_max['Họ và tên']} ({sv_max['Tong_ket']} điểm)"
    )
    st.warning(
        f"⚠️ **Thấp nhất:** {sv_min['Họ và tên']} ({sv_min['Tong_ket']} điểm)"
    )

st.write("---")
st.subheader("🔍 Tra cứu chi tiết điểm sinh viên")
ten_sinh_vien = st.selectbox("Chọn một sinh viên:", df["Họ và tên"].tolist())
sv_chon = df[df["Họ và tên"] == ten_sinh_vien].iloc[0]

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Chuyên cần", sv_chon["Điểm chuyên cần"])
c2.metric("Giữa kỳ", sv_chon["Điểm giữa kỳ"])
c3.metric("Cuối kỳ", sv_chon["Điểm cuối kỳ"])
c4.metric("Tổng kết", sv_chon["Tong_ket"])
c5.metric("Xếp loại", sv_chon["Xep_loai"])

st.write("---")
st.subheader("📈 Biểu đồ điểm tổng kết của 10 sinh viên")
chart_data = df.set_index("Họ và tên")[["Tong_ket"]]
st.bar_chart(chart_data)
