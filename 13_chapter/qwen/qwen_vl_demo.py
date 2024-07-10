import dashscope


def simple_multimodal_conversation_call():
    """
    简单的单轮多模式会话调用。
    """
    # 设置 API key
    dashscope.api_key = "sk-05f861ceafce4f32a3590a83f55f67eb"
    # 模型类型
    model_type = "qwen-vl-plus"
    # 在线图片地址
    image_path = "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"
    # 请求体
    messages = [
        {
            "role": "user",
            "content": [
                {"image": image_path},
                {"text": "这是什么?"}
            ]
        }
    ]

    response = dashscope.MultiModalConversation.call(model=model_type,
                                                     messages=messages)
    # 打印请求结果
    if response.status_code == 200:
        print(response)
    else:
        print(response.code)
        print(response.message)


if __name__ == '__main__':
    simple_multimodal_conversation_call()
