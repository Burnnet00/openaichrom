import langchain
import openai

# Указываем ключ API для доступа к сервису OpenAI
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Создаем токенизатор для работы с LLM
tokenizer = langchain.tokenizers.GPT3Tokenizer()

# Создаем промт для LLM, который использует историю разговоров из памяти для установки контекста
prompt = """
История разговоров:
{memory}

Пользователь: {input}
GPT-3.5-turbo: {output}
"""

# Создаем функцию для создания цепочки LangChain
def create_chain():
    # Создаем цепочку LangChain с именем "chat"
    chain = langchain.Chain("chat")
    # Добавляем шаг в цепочку, который вызывает LLM GPT-3.5-turbo через OpenAI API с заданным промтом и токенизатором
    chain.add_step(
        name="gpt3",
        action=langchain.actions.OpenAIAction(
            engine="gpt-3.5-turbo",
            api_key=OPENAI_API_KEY,
            prompt=prompt,
            tokenizer=tokenizer,
            max_tokens=100,
            temperature=0.9,
            stop="\n"
        )
    )
    # Возвращаем созданную цепочку
    return chain

