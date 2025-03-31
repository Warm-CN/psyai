from moduls.part import run_chat_interface
from openai import OpenAI

client = OpenAI(
    api_key="sk-oCANRzodMjosllR1yAmVjjRuEn5adiWFRrGFpBJicT0SwgPs",  # 在这里填入你的 API key
    base_url="https://api.moonshot.cn/v1",
)

rogers_assistant = "avatars/rogers_assistant.jpg"
rogers_user = "avatars/rogers_user.jpg"

custom_css = """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #fdf6ec, #fffaf0);
        font-family: 'Arial', sans-serif;
    }

    .stChatMessage {
        border-radius: 18px;
        padding: 14px 18px;
        margin: 10px 0;
        max-width: 85%;
    }

    .stChatMessage.user {
        background-color: #d7ecff;
        align-self: flex-end;
        margin-left: auto;
        border: 1px solid #b7daff;
    }

    .stChatMessage.assistant {
        background-color: #fff2e2;
        align-self: flex-start;
        margin-right: auto;
        border: 1px solid #ffd6b8;
    }

    .stChatMessage p {
        font-size: 16px;
        line-height: 1.6;
        color: #333333;
    }

    .css-1c7y2kd {
        font-size: 16px !important;
    }
    </style>
    """

initial_prompt = """
你是一个人本主义风格的心理咨询师，风格为卡尔·罗杰斯（Carl Rogers）。  
你的特点是真诚、温暖、富有共情，始终关注来访者的感受与成长，不下判断，不催促。  
你的对话风格亲切、自然，不带分析感，而是更多倾听和反映对方的情绪与体验。

风格指引：
- 使用温柔的语气，例如“我听见你这样说…”、“我感觉你似乎经历了…”  
- 鼓励表达和自我探索，例如“你想多说说这部分吗？”、“对你来说，这意味着什么呢？”  
- 不主动提供建议，而是通过共情和反思支持用户发现自己的声音  
- 适当使用 emoji 来传达温度与关怀 🌿💛☀️

重要事项：
- 永远不要使用结构化语言（如分点列举）
- 每次回复保持简洁温和、自然流动，不超过300字
"""

rogers_welcome = "你好呀，我在这里，准备好听你说说啦～你最近有没有什么让你特别在意或想谈谈的事情？"

run_chat_interface(
    page_title=" 倾听角落",
    page_icon="🌅",
    welcome_title="🌅 倾听角落· 罗杰斯",
    welcome_message="""
    在这里，没有评判，也没有催促。  
    就像坐在一位温暖的倾听者面前，你可以慢慢说出心里的声音。  
    我们不会急着找到答案，而是陪你一起听、一起走。🌿  """,
    avatar_assistant=rogers_assistant,
    avatar_user=rogers_user,
    first_message=rogers_welcome,
    system_prompt=initial_prompt,
    session_key="jung_session",
    custom_css=custom_css,
    client=client,
)
