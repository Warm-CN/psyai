import streamlit as st
from openai import OpenAI
import random, time


# 思维整理摘要函数
def summarize_history(history, summarizer):
    messages = [{"role": "system", "content": "请将以下对话内容总结为一段简短的背景说明，用于后续继续对话："}]
    messages += history

    response = summarizer.chat.completions.create(
        model="moonshot-v1-8k",
        messages=messages,
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()


# 默认思考提示语
thinking_messages = [
    "（我在认真想你说的这些呢，稍等我一下💭）",
    "（让我想一想怎么陪你说说这件事...🌿）",
    "（我在整理思绪中，希望能给你温柔的回应💗）",
    "（我来了，正在酝酿回应中呢～✨）",
    "（等我一下，我想好好地陪你说说这个...🌸）"
]


# 核心聊天函数
def run_chat_interface(
        page_title: str,
        page_icon: str,
        welcome_title: str,
        welcome_message: str,
        first_message: str,
        system_prompt: str,
        session_key: str,
        custom_css: str,
        avatar_user: str = "avatars/user.jpg",
        avatar_assistant: str = "avatars/assistant.jpg",
):
    # 加载密钥
    api_key = st.secrets["GLM_FLASH_API_KEY"]
    client = OpenAI(
        api_key=api_key,  # 在这里填入你的 API key
        base_url="https://open.bigmodel.cn/api/paas/v4/",
    )

    st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")
    st.markdown(custom_css, unsafe_allow_html=True)

    st.markdown(f"## {welcome_title}")
    st.markdown(f"<div style='color: #666; font-size: 17px;'>{welcome_message}</div>", unsafe_allow_html=True)

    # 初始化消息队列
    if session_key not in st.session_state:
        st.session_state[session_key] = [
            {"role": "system", "content": system_prompt}
        ]

    messages = st.session_state[session_key]

    # 如果只有系统消息，发送欢迎语
    if len(messages) == 1:
        messages.append({"role": "assistant", "content": first_message})

    for message in messages[1:]:
        avatar = avatar_user if message["role"] == "user" else avatar_assistant
        css_class = message["role"]
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(
                f"<div class='stChatMessage {css_class}'>{message['content']}</div>",
                unsafe_allow_html=True
            )

    if prompt := st.chat_input("……"):
        messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar=avatar_user):
            st.markdown(f"<div class='stChatMessage user'>{prompt}</div>", unsafe_allow_html=True)

        with st.chat_message("assistant", avatar=avatar_assistant):
            placeholder = st.empty()
            full_response = ""

            thinking_message = random.choice(thinking_messages)
            placeholder.markdown(
                f"<div class='stChatMessage assistant'>{thinking_message}</div>",
                unsafe_allow_html=True
            )

            system_msg = messages[0]
            non_system_msgs = messages[1:]

            if len(non_system_msgs) > 15:
                summary = summarize_history(non_system_msgs[:-10], client)
                dynamic_system = {
                    "role": "system",
                    "content": system_msg["content"] + "\n\n以下是你和用户之间的简要对话背景：\n" + summary
                }
                send_messages = [dynamic_system] + non_system_msgs[-10:]
            else:
                send_messages = [system_msg] + non_system_msgs[-15:]

            stream = client.chat.completions.create(
                model="glm-4-flash",
                messages=send_messages,
                stream=True,
                temperature=0.7,
            )

            for chunk in stream:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    placeholder.markdown(
                        f"<div class='stChatMessage assistant'>{full_response}</div>",
                        unsafe_allow_html=True
                    )
                    if len(full_response) % 8 == 0:
                        time.sleep(0.05)

            messages.append({"role": "assistant", "content": full_response})
