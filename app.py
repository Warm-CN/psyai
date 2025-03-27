import streamlit as st

st.set_page_config(
    page_title="心理小站 - 首页",
    page_icon="🌸",
    layout="centered",
)

# 自定义样式：加宽按钮、圆角、间距
st.markdown("""
    <style>
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        padding: 0.6em 1em;
        margin-bottom: 10px;
        font-size: 16px;
    }
    .stCaption {
        font-size: 15px !important;
        color: #666 !important;
        margin-top: -10px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 欢迎语
st.markdown("""
# 🌸 欢迎来到心理小站

<div style='font-size:17px; line-height:1.7; color:#555'>
这里是一个温柔的精神角落，无论你是想放松片刻，还是倾诉心事，  
我们都为你准备了几个独特的小空间，  
每一个空间都通向一位心理学家的世界，也许你会在那里，遇见更了解自己的方式 🕊️  
</div>
""", unsafe_allow_html=True)

# 分隔线
st.markdown("---")
st.markdown("## 🧭 请选择一个让你安心的小站：")

# 场景按钮列表（横向布局）
col1, col2 = st.columns(2)

with col1:
    if st.button("💬 心理小站"):
        st.switch_page("pages/corner.py")
    st.caption("和温柔又理解你的 AI 心理师聊聊心情 🌱")

    if st.button("🌌 梦境小屋 · 荣格"):
        st.switch_page("pages/jung.py")
    st.caption("探索潜意识的符号世界，让梦与回忆为你指引方向 ✨")

with col2:
    if st.button("🌅 倾听角落 · 罗杰斯"):
        st.switch_page("pages/rogers.py")
    st.caption("在被理解的空间里，让真实的自己慢慢展开 💛")

    if st.button("📘 思维工坊 · 贝克"):
        st.switch_page("pages/cbt.py")
    st.caption("轻轻整理那些影响情绪的思维模式，一点点找回清晰和平静 🛠️")
