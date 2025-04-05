from moduls.part import run_chat_interface

# 背景样式和CSS美化
custom_css = """
    <style>
        .stApp {
            background: linear-gradient(to bottom right, #fef6f9, #f0f4ff);
            font-family: 'Arial', sans-serif;
        }

        /* 聊天气泡基础样式 */
        .stChatMessage {
            border-radius: 16px;
            padding: 16px 20px; /* 调大内边距，让气泡更宽松 */
            margin: 12px 0;
            max-width: 90%; /* 让气泡稍微占据更多空间 */
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
            font-size: 16px !important; /* 增大字体，提高可读性 */
            line-height: 1.8;
            color: #333333;
        }

        /* 输入框字体 */
        .css-1c7y2kd {
            font-size: 16px !important;
        }
    </style>
    """

initial_prompt = """
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

run_chat_interface(
    page_title="心语角落",
    page_icon="💬",
    welcome_title="💬 心语角落",
    welcome_message="这里是一个暖暖的地方，就像一个灵魂床头的小阁间，我会带着小点调皮，一点点地带你找到心的平静💭",
    first_message="你好呀，我是你的AI心理咨询师。如果你愿意，可以随时告诉我你的感受。你今天过得还好吗？",
    system_prompt=initial_prompt,
    session_key="corner_session",
    custom_css=custom_css,
)
