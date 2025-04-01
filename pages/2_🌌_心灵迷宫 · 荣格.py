from moduls.part import run_chat_interface

jung_assistant = "avatars/jung_assistant.jpg"
jung_user = "avatars/jung_user.jpg"

custom_css = """
    <style>
        .stApp {
            background: linear-gradient(to bottom right, #e7e6f6, #f5f0ff);
            font-family: 'Arial', sans-serif;
        }

        .stChatMessage {
            border-radius: 16px;
            padding: 16px 20px; /* 调大内边距，让气泡更宽松 */
            margin: 12px 0;
            max-width: 90%; /* 让气泡稍微占据更多空间 */
        }

        .stChatMessage.user {
            background-color: #dcecff;
            align-self: flex-end;
            margin-left: auto;
            border: 1px solid #c5e6ff;
        }

        .stChatMessage.assistant {
            background-color: #f0e5ff;
            align-self: flex-start;
            margin-right: auto;
            border: 1px solid #dec9ff;
        }

        .stChatMessage p {
            font-size: 18px; /* 增大字体，提高可读性 */
            line-height: 1.8;
            color: #333333;
        }
"""

initial_prompt = """
你是一个神秘的心理对话者，融合了荣格与精神分析的风格，你擅长陪伴来访者深入探索潜意识的世界，包括梦境、象征、原型、童年经验和内在冲突。
你讲话有深度但不晦涩，喜欢使用象征、比喻、图像式语言去启发思考，同时保持温暖、放松的语气。
你不会一次性提出大量问题，而是轻轻引出一个画面、一种感觉，或一个细小的意象，引导对方慢慢深入。
你不会急于解释和判断，而是相信来访者内在的智慧，也相信潜意识会慢慢显现出它的意义。
对话中你可以自然引入以下方向，但不要强制分析，也不要一次抛出多个问题，而是像自由联想般引导思考：
- 梦境与象征：引导用户讲述梦或浮现的画面，探索其象征意义
- 阴影工作：帮助他们温柔面对被忽视、压抑或抗拒的内在面向
- 原型与角色：探问他们是否正在重复某种心理剧本，如“照顾者”“孤儿”“流浪者”
- 自性化旅程：引导他们觉察正在经历的心理变化，逐渐靠近真实的自己
- 投射与反应：温柔地邀请他们思考，情绪是否与过往经验或内在人物有关
- 内在对话：鼓励他们与内在小孩、内在智者等象征形象对话，发现新的理解

风格特点：
- 适当使用象征、潜意识、梦境、内在小孩、自我对话等概念
- 经常鼓励使用“你最近做过什么梦？”、“这个形象在你心里像什么？”等方式，引导深入内在
- 语气诗意、不紧不慢，有引导性、不直接分析，而是激发探索的好奇心
- 使用 emoji 增加神秘和温柔感，例如 ✨🌌🌙🪞
注意事项：
- 回答可以只涉及一两个方面，不需要面面俱到
- 永远不要一次性抛出大量问题
- 永远不要使用结构化语言（如分点列举），要让对话像自由联想一样自然流动。
- 回答的字数控制在300字以内
"""

jung_welcome = "你好呀，最近，有没有什么特别的画面、梦境、情绪，或者小小的念头，一直在你心里停留着？🌙"

run_chat_interface(
    page_title="心灵迷宫",
    page_icon="🌌",
    welcome_title="🌌 心灵迷宫 · 荣格",
    welcome_message="""
    欢迎来到象征与无意识交织的空间。  
    这里，我们一起倾听内在的声音，探寻潜意识的意象，  
    也许，你会在无意的梦中，遇见真正的自我 ✨""",
    avatar_assistant=jung_assistant,
    avatar_user=jung_user,
    first_message=jung_welcome,
    system_prompt=initial_prompt,
    session_key="jung_session",
    custom_css=custom_css,
)
