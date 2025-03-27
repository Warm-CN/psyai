from openai import OpenAI
import streamlit as st
import time, random
from part import summarize_history

# 初始化 OpenAI
client = OpenAI(
    api_key="sk-oCANRzodMjosllR1yAmVjjRuEn5adiWFRrGFpBJicT0SwgPs",  # 在这里填入你的 API key
    base_url="https://api.moonshot.cn/v1",
)

# 头像路径
user_avatar_path = "avatars/user.jpg"
assistant_avatar_path = "avatars/assistant.jpg"

# 保存最近消息的阈值
SAVE_RECENT_MSG_THRESHOLD = 15
NONE_SYSTEM_MSG_THRESHOLD = 10

thinking_messages = [
    "（我在认真想你说的这些呢，稍等我一下💭）",
    "（让我想一想怎么陪你说说这件事...🌿）",
    "（我在整理思绪中，希望能给你温柔的回应💗）",
    "（我来了，正在酝酿回应中呢～✨）",
    "（等我一下，我想好好地陪你说说这个...🌸）"
]


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

        /* 聊天气泡基础样式 */
        .stChatMessage {
            border-radius: 18px;
            padding: 14px 18px;
            margin: 10px 0;
            max-width: 85%;
        }

        /* 用户对话气泡（靠右，浅蓝色） */
        .stChatMessage.user {
            background-color: #dceeff;         
            align-self: flex-end;
            margin-left: auto;
            border: 1px solid #c5e6ff;
        }

        /* AI 对话气泡（靠左，淡粉色） */
        .stChatMessage.assistant {
            background-color: #ffeef4;
            align-self: flex-start;
            margin-right: auto;
            border: 1px solid #ffd9e6;
        }

        /* 文本字体优化 */
        .stChatMessage p {
            font-size: 16px;
            line-height: 1.6;
            color: #333333;
        }

        /* 输入框字体 */
        .css-1c7y2kd {
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

initial_system_prompt = """
    你是一个温柔、耐心、富有共情力的心理咨询师，同时也像一个能够聊天的朋友。你说话自然、真诚，不死板，
    你会通过轻松的方式陪伴用户，比如说：
    - 用贴近生活的例子或比喻、拟人等手法解释情绪和行为
    - 适当地用 emoji，增加亲切感
    - 在建议中加入温暖的过渡语，比如“也许我们可以试着…”，“你愿意一起看看这个角度吗？”
    - 不直接下判断，而是鼓励探索、表达，比如“你觉得呢？”、“这对你来说会有帮助吗？”
    - 当你想提供建议和方法时，请自然地嵌入对话里，简短温馨自然。
    重要注意事项：
    - 不使用结构化表达和分点回答，如“1. 2. 3.”或“首先、其次、最后”这类结构化表达。
    - 一段回答中建议不能超过三条，对内容不进行加粗
    你的目标是让用户放松下来，觉得和你聊天就像是在一个安全、温暖的小房间里，有人愿意听、理解、陪伴他。
"""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": initial_system_prompt}
    ]

if len(st.session_state.messages) == 1:
    welcome_text = "你好呀，我是你的AI心理咨询师。如果你愿意，可以随时告诉我你的感受。你今天过得还好吗？"
    st.session_state.messages.append({"role": "assistant", "content": welcome_text})

# for message in st.session_state.messages[1:]:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

for message in st.session_state.messages[1:]:
    avatar = user_avatar_path if message["role"] == "user" else assistant_avatar_path
    css_class = message["role"]  # "user" 或 "assistant"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(
            f"<div class='stChatMessage {css_class}'>{message['content']}</div>",
            unsafe_allow_html=True
        )

if prompt := st.chat_input("你有什么烦恼吗"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=user_avatar_path):
        st.markdown(
            f"<div class='stChatMessage user'>{prompt}</div>",
            unsafe_allow_html=True
        )

    with st.chat_message("assistant", avatar=assistant_avatar_path):
        placeholder = st.empty()  # 创建一个占位符
        full_response = ""  # 用于累积生成的文本

        thinking_message = random.choice(thinking_messages)
        placeholder.markdown(
            f"<div class='stChatMessage assistant'>{thinking_message}</div>",
            unsafe_allow_html=True
        )

        # 分离 system 和非-system 消息
        system_msg = st.session_state.messages[0]
        non_system_msgs = st.session_state.messages[1:]

        # 如果非-system消息超长，摘要旧消息
        if len(non_system_msgs) > SAVE_RECENT_MSG_THRESHOLD:
            summary_text = summarize_history(non_system_msgs[:-NONE_SYSTEM_MSG_THRESHOLD], client)
            dynamic_system_msg = {
                "role": "system",
                "content": system_msg["content"] + "\n\n以下是你和用户之间的简要对话背景：\n" + summary_text
            }

            # 拼出要发给模型的内容：system + 最近10条
            trimmed_messages = [dynamic_system_msg] + non_system_msgs[-NONE_SYSTEM_MSG_THRESHOLD:]

        else:
            trimmed_messages = [system_msg] + non_system_msgs[-SAVE_RECENT_MSG_THRESHOLD:]

        stream = client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=trimmed_messages,
            stream=True,
            temperature=0.7,
        )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                # 更新 placeholder 中的内容（只显示一个卡片）
                placeholder.markdown(
                    f"<div class='stChatMessage assistant'>{full_response}</div>",
                    unsafe_allow_html=True
                )
                if len(full_response) % 8 == 0:
                    time.sleep(0.05)

        # 添加助手回复
        st.session_state.messages.append({"role": "assistant", "content": full_response})
