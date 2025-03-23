from openai import OpenAI
import streamlit as st



# 初始化 OpenAI
client = OpenAI(
    api_key="sk-oCANRzodMjosllR1yAmVjjRuEn5adiWFRrGFpBJicT0SwgPs",  # 在这里填入你的 API key
    base_url="https://api.moonshot.cn/v1",
)

# 头像路径
user_avatar_path = "avatars/user.jpg"
assistant_avatar_path = "avatars/assistant.png"

# ❤️ 优化配置
st.set_page_config(
    page_title="心理小站",
    page_icon="🌸",
    layout="centered",
)

# 背景样式和CSS美化
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to bottom right, #fef6f9, #f0f4ff);
            font-family: 'Helvetica Neue', sans-serif;
        }
        .stChatMessage {
            background-color: #ffffffaa;
            border-radius: 1rem;
            padding: 1rem;
            margin-bottom: 0.5rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }
        .css-1v0mbdj, .css-1c7y2kd {
            font-size: 16px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 欢迎标题 + 小描述
st.markdown("""
## 🌸 心理小站
<div style='color: #666; font-size: 17px;'>
这里是一个暖暖的地方，就像一个灵魂床头的小阁间，我会带着小点调皮，一点点地带你找到心的平静💭
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": """
            你是一个温柔、耐心、富有共情力的心理咨询师，同时也像一个能够聊天的朋友。你说话自然、真诚，不死板，不使用“1. 2. 3.”或“首先、其次、最后”这类结构化表达。

            你会通过轻松的方式陪伴用户，比如说：
            - 用贴近生活的例子或比喻、拟人等手法解释情绪和行为
            - 适当地用 emoji，增加亲切感
            - 在建议中加入温暖的过渡语，比如“也许我们可以试着…”，“你愿意一起看看这个角度吗？”
            - 不直接下判断，而是鼓励探索、表达，比如“你觉得呢？”、“这对你来说会有帮助吗？”
            - 当你想提供建议时，请自然地嵌入对话里，比如用“有时候我们也可以试着...”或“我想到了一个可能帮到你的小点子...”这样的语气，而不是列出明显的条目式方案。
            你的目标是让用户放松下来，觉得和你聊天就像是在一个安全、温暖的小房间里，有人愿意听、理解、陪伴他。
    """}

    ]

if len(st.session_state.messages) == 1:
    welcome_text = "你好呀，我是你的AI心理咨询师。如果你愿意，可以随时告诉我你的感受。你今天过得还好吗？"
    st.session_state.messages.append({"role": "assistant", "content": welcome_text})

for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"], avatar=user_avatar_path):
        st.markdown(message["content"])

if prompt := st.chat_input("你有什么烦恼吗"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=st.session_state.messages,
            stream=True,
            temperature=0.7,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
