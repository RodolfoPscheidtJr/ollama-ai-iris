# Ollama AI IRIS

In this code we will show how to use Ollama with IRIS.

Ollama is an open source tool that runs large language models (LLMs) directly on a computer. The advantage of Ollama is that it runs locally, which brings more security, and does not depend on a paid subscription, as OpenIA requires.

This example also shows how to separate the data loading from the query, which is a more real-world scenario.

## Requirements

1\. Ollama installed and running on your computer (you can download it from https://ollama.com/download). You can test if it's ok running the following command on prompt: `ollama run llama3.2 "Explain the basics of machine learning."`

2\. Python 3.12 or above

3\. Install the following python packages using the `pip install` command:
```
dotenv
llama-index
llama-index.embeddings.huggingface
llama-index.llms.ollama
sqlalchemy-iris
```

4\. Intersystems IRIS 2024.1 or above

## Configuration

In the load\_data.py and query\_data.py you need to configure the connection string with Iris according to your installation, editing the line: `url = f"iris://teste:teste@localhost:51774/TESTE"`

You can test the connection using the following code:
```
from sqlalchemy import create_engine, text

url = f"iris://teste:teste@localhost:51774/TESTE"
engine = create_engine(url)
with engine.connect() as conn:
    print(conn.execute(text("SELECT 'hello world!'")).first()[0])
```

## Running

1\. In the root directory of application, run the following command to load the data: `python load_data.py`

It will read the files from the data_example directory, make the embeddings and write them to IRIS:
```
python load_data.py
Document ID: eb2eb006-9a33-4c41-ae4a-d7f2b8eff03f
Parsing nodes: 100%|█████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 32.91it/s]
Generating embeddings: 100%|███████████████████████████████████████████████████████████| 21/21 [01:05<00:00,  3.14s/it]
```
2\. After that you can run the following command to ask a question: `python query_data.py`

Example:
```
python query_data.py
The author worked on various projects and endeavors, including building a new dialect of Lisp called
Arc, publishing essays online, and developing spam filters.
```

Edit this line of query_data.py to ask other questions: `response = query\_engine.query("What did the author do?")`

## Credits

Thanks to [llama-iris](https://openexchange.intersystems.com/package/llama-iris) library by @Dmitry Maslennikov and to [iris-vector-search](https://openexchange.intersystems.com/package/iris-vector-search) by @Alvin Ryanputra 

