def summarize_history(history, summarizer):
    """
    将旧对话压缩为一段摘要文本，作为新的 system message 返回
    history: 对话列表 [{"role": "user"/"assistant", "content": "..."}, ...]
    summarizer: OpenAI 客户端，用于生成摘要
    """
    messages = [{"role": "system", "content": "请将以下对话内容总结为一段简短的背景说明，用于后续继续对话："}]
    messages += history

    response = summarizer.chat.completions.create(
        model="moonshot-v1-8k",
        messages=messages,
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()
