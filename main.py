import streamlit as st

st.set_page_config(
    page_title="GitHub Copilot",
    page_icon="./asset/image/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

import streamlit as st

# Hiển thị hình ảnh và tiêu đề trong một div
st.write(
    """
    <style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .img-container {
        margin-bottom: 20px;
    }
      h1 {
        font-size: 80px;
    }
    </style>
    <div class="container">
        <div class="img-container">
            <img src="https://github.blog/wp-content/uploads/2021/06/GitHub-Copilot_blog-header.png?resize=1600%2C850" width="950" style="channels='RGB'">
        </div>
        <h1>GitHub Copilot</h1>
        <p>Đây là nội dung của bạn.</p>
        <!-- Thêm nội dung của bạn sau đây -->
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("Nội dung bài viết")
    source_vid = st.sidebar.write("""
    <style>
        .toc {
            background-color: #0E1117;
            border-radius: 10px;
        }
        .toc p {
            font-size: 15px;
            margin: 0;
            padding: 10px;
            cursor: pointer;
            z-index: 2;
        }
        # .toc p:nth-child(odd) {
        #     background-color: #F1F1EF; /* Màu nền cho các hàng lẻ */
        # }
        # .toc p:nth-child(even) {
        #     background-color: #262730; /* Màu nền cho các hàng chẵn */
        # }
    </style>
    <div class="toc">
        <p>1. GitHub Copilot là gì?</p>
        <p>2. Ưu & Nhược điểm.</p>
        <p>3. So sánh GitHub Copilot với một công cụ hỗ trợ lập trình khác.</p>
        <p>4. Cách cài đặt GitHub Copilot.</p>
        <p>5. GitHub Copilot hoạt động như thế nào?</p>
        <p>6. Kết luận.</p>
    </div>
    """, unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Post", "Reference"])

with tab1:
    st.header("F-Code [Techaway 2024]")
    st.markdown("#### **F-Code authors:**")
    st.write("""
        - *Phạm Nguyễn Hoàng Anh - F19*
        - *Nguyễn Huỳnh Thiên Duyên - F19*
    """)
    st.header("Lời mở đầu")
    st.write("""
        Bạn có từng khao khát sở hữu một cộng sự thông minh, tiện ích trong lĩnh vực lập
    trình? Một người bạn đồng hành có khả năng đưa ra gợi ý về đoạn mã, hàm số hay
    giải pháp phù hợp dựa trên bối cảnh của mã nguồn mà bạn đang làm việc? Một
    người có thể hướng dẫn bạn tiếp thu một kỹ năng mới hay là những phương pháp tiếp
    cận mới mẻ từ những đoạn mã mà họ đề xuất? Một người có thể biến quá trình lập
    trình của bạn trở nên nhanh chóng và hiệu quả hơn?
    
    Nếu bạn cảm thấy thích thú với bất kỳ ý tưởng nào trên đây, thì GitHub Copilot, “một
    trợ lý ảo” trong lĩnh vực lập trình có thể là thứ mà bạn đang tìm kiếm. GitHub Copilot
    không chỉ đáp ứng tất cả những yêu cầu trên mà còn nhiều hơn thế. Trong bài viết
    này, chúng mình sẽ chia sẻ về trải nghiệm khi sử dụng GitHub Copilot trong thời gian
    qua và cung cấp một số lời khuyên cũng như mẹo nhỏ để bạn có thể tận dụng tối đa
    công cụ này nhé.
    """)
    st.header("GitHub Copilot là gì?")
    st.write("""
    - GitHub Copilot là một công cụ hỗ trợ lập trình đến từ sự hợp tác giữa GitHub và
    OpenAI. Nó được xem là một trình đồng sáng tạo với sức mạnh của trí tuệ nhân
    tạo, GitHub Copilot giúp bạn đề xuất các mã code ngay trong khi bạn đang viết
    trên các môi trường phát triển tích hợp (IDE). Tính năng tự động hoàn thiện code
    dựa trên ngữ cảnh và mô tả từ người dùng của GitHub Copilot sẽ giúp việc lập
    trình của bạn trở nên hiệu quả và nhanh chóng hơn.
    """)
    st.image("https://nira.com/wp-content/uploads/2021/11/image4-1.png", width=1000, channels="RGB")
    st.write("""
    - Với lợi thế là có tập dữ liệu khổng lồ trên Github – hơn 1 tỷ dòng mã từ các dự án
    mã nguồn mở khác nhau, các tài liệu kỹ thuật về các ngôn ngữ lập trình, thư viện.
    Đồng thời sử dụng mô hình GPT- 4 để thực hiện việc huấn luyện dữ liệu thì
    GitHub Copilot hỗ trợ rất nhiều ngôn ngữ lập trình cũng như là hàng loạt các
    frameworks lập trình khác nhau. Nó gần như hoạt động tốt với hấu hết các ngôn
    ngữ như Python, JavaScript, TypeScript, Ruby, Go, C# và C++... Vì vậy, bất kể
    bạn đang làm việc với ngôn ngữ lập trình nào thì GitHub Copilot cũng đều có thể
    trở thành “một trợ lý ảo đắc lực” hỗ trợ bạn trong công việc.
    
    (trích dẫn: https://sec.vnpt.vn/2023/12/github-copilot-cong-cu-thay-doi-cuoc-
    cach-mang-lap-trinh-tu-dong-hoa/)
    """)

with tab2:
    st.header("A bird")