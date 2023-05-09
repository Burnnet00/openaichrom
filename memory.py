import langchain
import chroma

# Указываем ключ шифрования для работы с памятью Chroma
CHROMA_ENCRYPTION_KEY = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

# Указываем хранилище для памяти Chroma (в данном случае файловая система)
CHROMA_STORAGE = chroma.storages.FileStorage(
    path="chat_history.txt"
)

# Создаем функцию для создания памяти Chroma
def create_memory():
    # Создаем память Chroma с именем "chat"
    memory = chroma.Memory(
        name="chat",
        encryption_key=CHROMA_ENCRYPTION_KEY,
        storage=CHROMA_STORAGE,
        format="text"
    )
    # Возвращаем созданную память
    return memory