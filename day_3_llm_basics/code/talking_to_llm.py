from ollama import chat
from ollama import ChatResponse


def parse_response(responce):
    s = responce.strip().split(':')
    return int(s[-1])
        
def generate_prompt():
    s = input()
    return s

if __name__ == '__main__':

    prompt = generate_prompt()
    response: ChatResponse = chat(
        model='gemma3:1b',
        messages=[{'role': 'user', 'content': prompt}]
    )
    print(response.message.content)
