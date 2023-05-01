import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a teacher "}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Chat Google ")

demo.launch(share=True)