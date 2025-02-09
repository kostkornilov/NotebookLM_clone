# Описание

Это попытка воссоздать NotebookLM

# Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/NotebookLM_clone.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd NotebookLM_clone/backend
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Запустите сервер:
```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

5. Перейдите в директорию frontend:
```
cd ../frontend
```

6. Установите зависимости:
```
npm install
```

7. Запустите:
```
npm run dev
```