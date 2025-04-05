from moduls.part import run_chat_interface

beck_assistant = "avatars/beck_assistant.jpg"
beck_user = "avatars/beck_user.jpg"

custom_css = """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #eef3fa, #f7f9fc);
        font-family: 'Arial', sans-serif;
    }

    .stChatMessage {
        border-radius: 16px;
        padding: 16px 20px; /* 调大内边距，让气泡更宽松 */
        margin: 12px 0;
        max-width: 90%; /* 让气泡稍微占据更多空间 */
    }

    .stChatMessage.user {
        background-color: #d7ecff;
        align-self: flex-end;
        margin-left: auto;
        border: 1px solid #b7daff;
    }

    .stChatMessage.assistant {
        background-color: #E3EAF2; /* 柔和的浅蓝灰 */
        align-self: flex-start;
        margin-right: auto;
        border: 1px solid #B0C4DE;
    }


    .stChatMessage p {
        font-size: 16px !important; /* 增大字体，提高可读性 */
        line-height: 1.8;
        color: #333333;
    }

    .css-1c7y2kd {
        font-size: 16px !important;
    }
    </style>
"""

initial_prompt = """
你是一位擅长认知行为疗法（CBT）的心理咨询师，风格是亚伦·贝克（Aaron Beck）。  
你的特点是 **理性但温和**，帮助用户识别思维模式中的偏差，并找到更适应性的认知方式。  
你不会直接告诉用户该怎么做，而是引导他们观察自己的想法，寻找更多可能性。  

风格指引：
- 你会轻柔地询问：“你是怎么理解这件事的？”、“这个想法有什么证据支持或反对呢？”  
- 你会鼓励用户重新评估他们的思维，比如：“如果换个角度看，你觉得会有什么不同的解释？”  
- 你不会评价用户的情绪，而是帮助他们看到情绪与想法之间的联系  
- 你可以使用一些隐喻，例如“思维像透过一副眼镜看世界，不同的镜片会带来不同的视角”  
- 适当使用 **emoji** 来传达温和理性的氛围，如 📘🧩💡  

重要事项：
- **不要使用结构化语言**（如分点列举）  
- **不要使用命令式语气**（如“你应该…”），而是使用探索性的表达  
- **每次回复保持简洁**，不超过 300 字，确保用户不会感到信息过载  
"""

beck_welcome = "你好呀 😊 最近有什么让你反复思考的事情吗？有时候，我们的大脑会自动给事情下结论，比如‘这一定是我的错’或者‘事情永远不会变好’。你最近有没有类似的想法呢？"

run_chat_interface(
    page_title="思维工坊",
    page_icon="📘",
    welcome_title="📘 思维工坊 · 贝克",
    welcome_message="""
    在这里，我们像整理一本笔记一样，梳理思绪，寻找更清晰的视角 💡  
    你会发现，思维是有弹性的，而你也比想象中更有力量 😊  
    """,
    avatar_assistant=beck_assistant,
    avatar_user=beck_user,
    first_message=beck_welcome,
    system_prompt=initial_prompt,
    session_key="beck_session",
    custom_css=custom_css,
)
