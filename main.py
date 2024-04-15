import streamlit as st
import pandas as pd

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

tab1, tab2, tab3 = st.tabs(["Post", "Demo", "Reference"])

with tab1:
    st.markdown("<h2 style='color: #FFC81B;'>F-Code [Techaway 2024]</h2>",unsafe_allow_html=True)
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

    st.markdown("<h2 style='color: #51C95D;'>1. GitHub Copilot là gì?</h2>", unsafe_allow_html=True)
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

    st.markdown("<h2 style='color: #51C95D;'>2. Ưu & Nhược điểm</h2>", unsafe_allow_html=True)
    st.write("""
    - #### *Ưu điểm:*
    """)

    df_1 = pd.DataFrame(
        [
            {"command": "1. Tăng tốc độ lập trình",
             "main": "GitHub Copilot cung cấp các gợi ý mẫu mã nguồn tự động, giúp nhà phát triển viết code nhanh và hiệu quả hơn."},
            {"command": "2. Tiết kiệm thời gian",
             "main": "Có các đoạn code sẵn giúp giảm thời gian phát triển và hạn chế nguy cơ phạm sai lầm."},
            {"command": "3. Hỗ trợ đa ngôn ngữ và nền tảng",
             "main": "Hỗ trợ nhiều ngôn ngữ lập trình + nền tảng khác nhau, Python, JavaScript, C++, Java,...."},
            {"command": "4. Dễ sử dụng",
             "main": "Công cụ tích hợp trực tiếp vào môi trường lập trình thông qua plugin, giúp người dùng dễ dàng truy cập và sử dụng."},
        ]
    )

    edited_df_1 = st.data_editor(
        df_1,
        width=1200,  # Adjust width here
        column_config={
            "command": st.column_config.Column(
                "",
                width="small",
            ),
            "main": st.column_config.Column(
                "",
                width="large",
            )
        },
        hide_index=True,
        disabled=["command", "main"],
    )

    st.write("""
    - #### *Nhược điểm:*
    """)

    df_2 = pd.DataFrame(
        [
            {"command": "1. Khả năng đề xuất mã không hoàn hảo.",
             "main": "Mặc dù có thể cung cấp những gợi ý hữu ích, nhưng GitHub Copilot vẫn có thể đề xuất mã không hoàn hảo hoặc không phù hợp với ngữ cảnh cụ thể của dự án."},
            {"command": "2. Nguy cơ vi phạm bản quyền.",
             "main": "Sử dụng một lượng lớn mã nguồn mở từ GitHub để đào tạo mô hình của mình, có thể gây vấn đề bản quyền trong một số trường hợp."},
            {"command": "3. Cần hiểu biết chuyên sâu.",
             "main": "Đối với người mới bắt đầu, có thể khó hiểu được lời gợi ý và mẫu mà GitHub Copilot đề xuất."},
            {"command": "4. Phụ thuộc vào kết nối internet.",
             "main": "GitHub Copilot yêu cầu internet để hoạt động."},
        ]
    )

    edited_df_2 = st.data_editor(
        df_2,
        key="unique_key_for_df_2",  # Unique key for this data editor widget
        width=1200,
        column_config={
            "command": st.column_config.Column(
                "",
                width="small",
            ),
            "main": st.column_config.Column(
                "",
                width="large",
            )
        },
        hide_index=True,
        disabled=["command", "main"],
    )

    st.markdown("<h2 style='color: #51C95D;'>3. So sánh GitHub Copilot với một công cụ hỗ trợ lập trình khác</h2>", unsafe_allow_html=True)

    st.write("""
    - ##### Trong phần này chúng mình sẽ đưa ra sự so sánh giữa GitHub Copilot với [Tabnin AI](https://www.tabnine.com/) để các bạn hình dung ra rõ hơn nhé!
    """)

    df_3 = pd.DataFrame(
        [
            {"command": "1. Nền tảng sử dụng.",
             "main_cpl": "Tích hợp trực tiếp vào trình soạn thảo mã của GitHub và hỗ trợ một số lượng lớn ngôn ngữ lập trình.",
             "main_tab": "Cung cấp plugin cho nhiều trình soạn thảo mã khác nhau nhưng không phải là một nền tảng cụ thể."},
            {"command": "2. Phong cách hỗ trợ.",
             "main_cpl": "Tạo ra các đoạn mã hoàn chỉnh dựa trên yêu cầu hoặc mô tả.",
             "main_tab": "Dự đoán mã dựa trên ngữ cảnh hiện tại và hoàn thành các dòng mã."},
            {"command": "3. Dữ liệu đào tạo.",
             "main_cpl": "Sử dụng dữ liệu từ GitHub, bao gồm hàng triệu dòng mã nguồn mở trên GitHub để đào tạo mô hình.",
             "main_tab": "Sử dụng một lượng lớn dữ liệu mã nguồn mở từ trên web, bao gồm cả GitHub, nhưng không phải chủ yếu là dữ liệu từ GitHub."},
            {"command": "4. Hiệu suất và chất lượng",
             "main_cpl": "Thường cung cấp các gợi ý mã chính xác và phù hợp với dự án hiện tại với sự tích hợp sâu vào môi trường phát triển.",
             "main_tab": "Cung cấp gợi ý mã nhanh chóng và phù hợp trong nhiều trường hợp, nhưng có thể không chính xác như GitHub Copilot trừ một số trường hợp do phương pháp dự đoán khác nhau."},
        ]
    )

    edited_df_3 = st.data_editor(
        df_3,
        key="unique_key_for_df_3",  # Unique key for this data editor widget
        width=1200,
        column_config={
            "command": st.column_config.Column(
                "",
                width="small",
            ),
            "main_cpl": st.column_config.Column(
                "GitHub Copilot",
                width="large",
            ),
            "main_tab": st.column_config.Column(
                "Tabnine AI",
                width="large",
            )
        },
        hide_index=True,
        disabled=["command", "main_cpl"],
    )

    st.markdown("<h2 style='color: #51C95D;'>4. Cách cài đặt GitHub Copilot</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.write("""
        #### a) Cài Đặt IDE Hỗ Trợ: 
        """)
        st.write("""
        - Sử dụng một IDE (Integrated Development Environment - Môi trường phát triển tích hợp) có hỗ trợ  **GitHub Copilot**. 
        - Trong bài viết này, chúng mình sẽ giới thiệu cách cài đặt **Github Copilot** trên **Visual Studio Code**.
        """)

        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 12, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.write("")

        st.write("""
        b) Mở **Visual Studio Code** và đi tới phần Extensions bằng cách nhấp vào biểu tượng  trên thanh bên trái hoặc nhấn `Ctrl+Shift+X` trên **Window** hay `Cmd+Shift+X` trên **macOS**.
        """)

        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 12, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.write("")

        st.write("""
        c) Trong trang Extensions, tìm kiếm **"GitHub Copilot"** trong ô tìm kiếm. Nhấp vào tiện ích mang tên **"GitHub Copilot"** của GitHub sau đó nhấp vào nút **Install** để cài đặt tiện ích.
        """)

        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 12, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)


        st.write("d) Sau khi quá trình cài đặt hoàn tất, bạn sẽ thấy nhận được thông báo phải đăng nhập tài khoản GitHub của bạn. Nếu bạn chưa có tài khoản GitHub, bạn sẽ phải tạo một tài khoản.")

        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 12, unsafe_allow_html=True)
        st.write("")


        st.write("e) Sau khi đăng nhập tài khoản GitHub đã có đăng ký GitHub Copilot, thì ở phía dưới cùng bên phải màn hình, bạn sẽ thấy GitHub Copilot đã được kích hoạt.")

        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 12, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.write("")

        st.write("""
        - Với số lợi ích đáng kể mà GitHub Copilot đem lại thì giá trị của các gói tiện ích ấy cũng không hề rẻ. Bên đây là các gói mà bạn có thể tham khảo mua.
        
        - GitHub Copilot hiện đang miễn phí cho sinh viên và giáo viên. Nhưng nếu bạn không phải là sinh viên hay giáo viên thì bạn cũng có thể thử sử dụng miễn phí phiên dùng thử trong vòng 30 ngày. Sau khi phiên dùng thử miễn phí kết thúc, bạn sẽ cần đăng ký trả phí để tiếp tục sử dụng. Truy cập [vào đây](https://github.com/features/copilot) để biết thêm thông tin nhé.
        """)


    with col2:
        st.image('https://near-question-fad.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fdd0e0693-d59f-4b82-a4b1-ac0a25ed824e%2F3ca94ee7-0b00-4db4-837c-21b44036b9dc%2FIDE.png?table=block&id=7224fd15-bfdc-4492-b58a-df26b135a34f&spaceId=dd0e0693-d59f-4b82-a4b1-ac0a25ed824e&width=1670&userId=&cache=v2',
                 width=350, channels="RGB", caption="IDE for GitHub Copilot")
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.image("https://near-question-fad.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fdd0e0693-d59f-4b82-a4b1-ac0a25ed824e%2F8eb4cc86-0425-4b6a-9e89-9e89b6a394e5%2Fextension_(1).png?table=block&id=cb071e30-8cb5-4b75-b23a-e9c3100f0d5d&spaceId=dd0e0693-d59f-4b82-a4b1-ac0a25ed824e&width=2000&userId=&cache=v2",
                 width=350, channels="RGB", caption="Open VSCode Extensions")
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.image("https://near-question-fad.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fdd0e0693-d59f-4b82-a4b1-ac0a25ed824e%2F7df195a5-389f-4296-ba95-d2fc0c6e8783%2Finstall.png?table=block&id=643861e9-d94f-4b88-b0d8-8639fd7a2a07&spaceId=dd0e0693-d59f-4b82-a4b1-ac0a25ed824e&width=2000&userId=&cache=v2",
                 width=350, channels="RGB", caption="Github Copilot search on VSCode Extensions")
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.image("https://near-question-fad.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fdd0e0693-d59f-4b82-a4b1-ac0a25ed824e%2Fbd09eebe-45da-435e-9669-37ceed10e72b%2Flogin.png?table=block&id=d6ca1ec8-fa98-4e3d-8cac-fb533f8f2e6f&spaceId=dd0e0693-d59f-4b82-a4b1-ac0a25ed824e&width=1930&userId=&cache=v2",
                width=350, channels="RGB", caption="Notification for login")
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.image("https://near-question-fad.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fdd0e0693-d59f-4b82-a4b1-ac0a25ed824e%2F8e1addd7-e8ac-407f-9290-5163fcc25720%2Fkichs_hoatj.png?table=block&id=1289e7ae-d56e-45f0-98ae-e097ec908d43&spaceId=dd0e0693-d59f-4b82-a4b1-ac0a25ed824e&width=1110&userId=&cache=v2",
                width=350, channels="RGB", caption="GitHub Copilot Activation")
        st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
        st.image("https://near-question-fad.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fdd0e0693-d59f-4b82-a4b1-ac0a25ed824e%2F5e2706f9-f6f5-4373-8ef9-19d4bf29baca%2Fpricing.png?table=block&id=32b50e62-9f29-4620-9a3d-3169d0058265&spaceId=dd0e0693-d59f-4b82-a4b1-ac0a25ed824e&width=2000&userId=&cache=v2",
                width=350, channels="RGB", caption="GitHub Copilot Pricing")

    st.markdown("<h2 style='color: #51C95D;'>5. GitHub Copilot hoạt động như thế nào?</h2>", unsafe_allow_html=True)
    st.write("Sau khi thành công trong việc cài đặt và kích hoạt GitHub Copilot trên Visual Studio Code, hãy cùng nhau khám phá xem GitHub Copilot có thể hỗ trợ chúng ta như thế nào trong quá trình lập trình nhé!")
    st.markdown("<h4 style='color: #FFC81B;'>Inline suggestions - Gợi ý hoàn thành mã trực tiếp</h4>",unsafe_allow_html=True)

    st.write("""
    - Khi bạn bắt đầu viết code hoặc các bình luận thì GitHub Copilot sẽ phân tích các mã code hiện tại của bạn và tự động đề xuất các đoạn mã code có thể điền vào tiếp theo ngay trong dòng bạn đang gõ. Việc này sẽ giúp việc lập trình của bạn trở nên hiệu quả hơn cũng như là sẽ giảm thiểu thời gian và công sức bạn phải bỏ ra để viết code.
    
    - Khi bạn nhận được một gợi ý từ GitHub Copilot, bạn có thể nhận phím **`Tab`** để chấp nhận gợi ý đó.
    """)
    st.image("https://near-question-fad.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fdd0e0693-d59f-4b82-a4b1-ac0a25ed824e%2F48cd9997-33bf-4438-99ec-9ad92e760441%2Finline.png?table=block&id=69d1a7c0-83f8-4db2-bbd5-5a71286312a3&spaceId=dd0e0693-d59f-4b82-a4b1-ac0a25ed824e&width=2000&userId=&cache=v2")

    st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)

    st.write("""
    - Hoặc là thay vì để GitHub Copilot tự động cung cấp các gợi ý khi bạn đang gõ, bạn cũng có thể sử dụng các bình luận trong code để đưa ra hướng dẫn. Bạn có thể làm cho những gợi ý mà bạn tìm kiếm trở nên cụ thể hơn. Ví dụ, bạn có thể chỉ định một loại thuật toán cần sử dụng, hoặc các phương thức và thuộc tính nào nên được thêm vào.
    """)
    st.image("https://near-question-fad.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fdd0e0693-d59f-4b82-a4b1-ac0a25ed824e%2Ff4fa7008-adb8-4244-b8a4-124e40f565df%2Fcomment.png?table=block&id=ebd2ec9d-6793-45c5-897f-b429dc55defe&spaceId=dd0e0693-d59f-4b82-a4b1-ac0a25ed824e&width=2000&userId=&cache=v2")

    st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)

    st.write("""
    - Dưới đây là một số phím tắt để bạn có thể sử dụng GitHub Copilot một cách dễ dàng hơn:
    """)

    import pandas as pd
    import streamlit as st

    df_4 = pd.DataFrame(
        [
            {"command": "Chấp nhận gợi ý",
             "main": "Tab"},
            {"command": "Bỏ qua gợi ý",
             "main": "Esc"},
            {"command": "Xem gợi ý tiếp theo",
             "main": "Alt + ] hoặc Option (⌥) + ] trên macOS"},
            {"command": "Xem lại gợi ý trước đó",
             "main": "Alt + [ hoặc Option (⌥) + [ trên macOS"},
        ]
    )

    edited_df_4 = st.data_editor(
        df_4,
        key="unique_key_for_df_4",
        width=1200,
        column_config={
            "command": st.column_config.Column(
                "Mục Đích",
                width="small",
            ),
            "main": st.column_config.Column(
                "Phím Tắt",
                width="large",
            )
        },
        hide_index=True,
        disabled=["command", "main"],
    )

    st.write("""
    **Keyboard Shortcuts:**

    - **`Tab`**: Chấp nhận gợi ý
    - **`Esc`**: Bỏ qua gợi ý
    - **`Alt + ]`** hoặc **`Option (⌥) + ]`** trên macOS: Xem gợi ý tiếp theo
    - **`Alt + [`** hoặc **`Option (⌥) + [`** trên macOS: Xem lại gợi ý trước đó
    """)

    st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)
    st.markdown("<h4 style='color: #FFC81B;'>Chat features - Các tính năng trò chuyện</h4>",unsafe_allow_html=True)
    st.write("""
    - Chat view: 
        - GitHub Copilot đã mang lại một trải nghiệm “Trò chuyện tương tác” nơi bạn có thể đặt những câu hỏi, từ những vấn đề đơn giản cho đến phức tạp và bạn sẽ nhận về được những giải đáp cũng như những gợi ý thông minh, được cá nhân hóa dựa trên dự án cũng như là bối cảnh làm việc của bạn. Công cụ này không chỉ giúp giải quyết các khó khăn về lập trình bạn gặp phải mà nó còn góp phần vào việc nâng cao kiến thức cũng như là hiểu biết của bạn qua từng câu hỏi, từ đó việc học hỏi sẽ trở nên linh hoạt và thú vị hơn. 
        
        - Để có thể truy cập “Chat view” bạn có thể bấm vào biểu tượng trên thanh Công cụ phía bên trái màn hình.
    """)
    st.image("https://near-question-fad.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fdd0e0693-d59f-4b82-a4b1-ac0a25ed824e%2F1ab2f8aa-c298-4f92-b53c-c30a84ff9cf6%2Fchat_view.png?table=block&id=e36ea3c1-90df-4c91-aeaa-b78c18ee2256&spaceId=dd0e0693-d59f-4b82-a4b1-ac0a25ed824e&width=2000&userId=&cache=v2")

    st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)

    st.write("""
    - Inline chat:  
        Một tính năng khá đặc biệt của GitHub Copilot là trả lời trực tiếp các câu hỏi khi bạn đang viết mã. Trong bất kỳ tệp nào, bạn có thể nhấn cmd + I ở macOs ( hoặc ctrl + I ở Window) để hiển thị “Inline chat” của GitHub Copilot. Bạn có thể đặt các câu hỏi xuất hiện khi bạn đang viết code, chẳng hạn như "Giải thích đoạn code này" hoặc "Làm cách nào để thêm chức năng A để thực hiện hành động C?".
        
        - Để có thể truy cập “Chat view” bạn có thể bấm vào biểu tượng trên thanh Công cụ phía bên trái màn hình.
    """)
    st.video("https://www.youtube.com/watch?v=q502Jj-bJgI")

    st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)

    st.write("Tùy thuộc vào câu hỏi của bạn, Copilot cũng có thể đề xuất sửa đổi mã cũng của bạn.")
    st.video("https://www.youtube.com/watch?v=Aw4mLTZ4Dcg")
    st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)

    st.write("""
    - Các tính năng khác:
        - Ngoài các tính năng chat hay inline suggestions thì GitHub Copilot còn có thể trợ giúp bạn thực hiện các nhiệm vụ cũng như là các quy trình khác. Ví dụ như là:
            + Tạo “Git commit messages”: Copilot có thể giúp bạn viết “Git commit messages”. Trong mục Source Control, hãy chọn nút “✨” ở bên phải và GitHub Copilot sẽ tạo ra một commit messages dựa trên các thay đổi đang chờ.
    """)
    st.image("https://near-question-fad.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fdd0e0693-d59f-4b82-a4b1-ac0a25ed824e%2Fee393459-cbdd-418c-abbc-0e67a4132308%2FCleanShot_2024-03-10_at_15.12.11.png?table=block&id=19f480f2-6b92-4094-8440-0846c4c05bb2&spaceId=dd0e0693-d59f-4b82-a4b1-ac0a25ed824e&width=2000&userId=&cache=v2")

    st.markdown("&nbsp;\n" * 24, unsafe_allow_html=True)

    st.write("Giải thích lỗi đang mà bạn gặp phải: Khi lệnh không chạy được trong Terminal, GitHub Copilot sẽ hiển thị một “ ✨”, nếu bạn bấm vào thì nó sẽ đưa ra giải thích điều gì đã xảy ra cũng như là sẽ đưa ra biện pháp để bạn khắc phục.")
    st.video("https://www.youtube.com/watch?v=rbzvpjgTOYY")

    st.markdown("<h2 style='color: #FFC81B;'>6. Kết luận</h2>", unsafe_allow_html=True)
    st.write("**Cuối cùng, GitHub Copilot không chỉ là một công cụ trợ lý lập trình AI, mà còn là một đối tác lý tưởng trong quá trình phát triển phần mềm của bạn. Nó không chỉ giúp cải thiện và tối ưu hóa mã nguồn, mà còn mở rộng kiến thức và tầm nhìn của bạn trong lập trình. Dù bạn là một lập trình viên chuyên nghiệp hay mới bắt đầu thì GitHub Copilot đều có thể mang lại những giá trị không ngờ. Tuy nhiên, cũng cần lưu ý rằng GitHub Copilot có thể tạo ra mã nguồn không hoàn thiện, không tối ưu, hoặc đưa ra đề xuất không chính xác thậm chí là không an toàn. Vì vậy, hãy xem GitHub Copilot như một người hỗ trợ bạn trong lập trình, không nên quá phụ thuộc vào nó. Hy vọng rằng qua bài viết này, bạn đã nắm bắt được nhiều hơn về GitHub Copilot và biết cách tận dụng tối đa công cụ này. Hãy tiếp tục khám phá và trải nghiệm để tạo ra những sản phẩm tuyệt vời với sự hỗ trợ của GitHub Copilot. Chúc bạn thành công trên con đường lập trình của mình!**")

with tab2:
    st.markdown("<h2 style='color: #FFC81B;'>Demo</h2>",unsafe_allow_html=True)
    st.write("""
    - Khi sử dụng GitHub Copilot có thể giúp bạn viết mã nguồn một cách nhanh chóng, chính xác và hiệu quả hơn, đặc biệt là khi làm việc trên các dự án lớn và phức tạp. 
    
    - Sau đây là một demo nho nhỏ mà chúng mình sẽ sử dụng các tính năng điển hình của GitHub Copilot. Yêu cầu là tạo một chương trình bằng ngôn ngữ C để quản lí các thông tin về thành viên của câu lạc bộ F-Code:
        - Thêm tên, ID và thông tin liên lạc của thành viên ( email và số điện thoại)
        - Xoá thành viên.
        - Cập nhật thông tin thành viên.
        - Hiển thị thông tin của các thành viên.
        - Tìm kiếm thông tin thành viên qua ID.
    - Nếu không có sự hỗ trợ của “trợ lí ảo” GitHub Copilot thì với các yêu cầu trên chúng ta sẽ phải tạo chương trình trong vòng ít nhất 1 đến 2 tiếng nhưng với ví dụ trên khi có sự hỗ trợ của GitHub Copilot thì chương trình được xây dựng chưa đầy 5 phút.
    """)
    st.video("https://www.youtube.com/watch?v=SvrOL1wUI_Q")

with tab3:
    # Create two columns with a ratio of 1:2
    col1, col2 = st.columns([1, 2])

    # In the first column, display the image
    with col1:
        pass

    # In the second column, display the heading
    with col2:
        st.image("./asset/image/F-Code_logo.png", width=280)
        st.markdown("<h2 style='color: #FFC81B;'>Nguồn Tham Khảo</h2>", unsafe_allow_html=True)
    st.write("")
    st.write("""
            - https://code.visualstudio.com/docs/copilot/overview
    
            - https://en.wikipedia.org/wiki/GitHub_Copilot
    
            - https://github.com/features/copilot
    
            - https://serokell.io/blog/github-copilot-overview
    
            - https://inspeerity.com/blog/github-copilot-part1/
    
            - https://dagshub.com/blog/github-copilot-not-code/
    
            - https://www.toponseek.com/blogs/copilot-github-la-gi/
    
            - https://thinhdanggroup.github.io/ai-pair-programing-vn-copy/
    
            - https://sec.vnpt.vn/2023/12/github-copilot-cong-cu-thay-doi-cuoc-cach-mang-lap-trinh-tu-dong-hoa/
    
            - https://www.youtube.com/watch?v=wTMSDbAli0s&t=373s
    
            - https://www.youtube.com/watch?v=h8SpwivM4po
    
            - https://www.youtube.com/watch?v=SZVCJRUADc4
    
            - https://www.youtube.com/watch?v=2q0BoioYSxQ
    
            """)
