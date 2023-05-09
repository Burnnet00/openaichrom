import langchain
import chain
import memory

# Создаем цепочку LangChain из файла chain.py
chat_chain = chain.create_chain()

# Создаем память Chroma из файла memory.py
chat_memory = memory.create_memory()

# Создаем интерфейс пользователя (в данном случае консольный)
print("Добро пожаловать в приложение для разговора с GPT-3.5-turbo!")
print("Для выхода из приложения введите 'quit'.")
user_input = input("Введите ваше сообщение: ")

# Запускаем цикл разговора
while user_input.lower() != "quit":
    # Вызываем цепочку LangChain с вводом пользователя и памятью Chroma
    chat_output, chat_memory = chat_chain(user_input, chat_memory)
    # Выводим ответ LLM на экран
    print("GPT-3.5-turbo:", chat_output)
    # Получаем новый ввод пользователя
    user_input = input("Введите ваше сообщение: ")

# Завершаем приложение
print("Спасибо за разговор! До свидания!")

