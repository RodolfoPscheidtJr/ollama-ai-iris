
from llama_index.core import StorageContext
from llama_iris import IRISVectorStore
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import load_index_from_storage



url = f"iris://teste:teste@localhost:51774/TESTE"

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-m3")
Settings.llm = Ollama(model="llama3.2", request_timeout=360.0)

vector_store = IRISVectorStore.from_params(
    connection_string=url,
    table_name="your_table_name",
    embed_dim = 1024 # HugginFace BAAI/bge-m3 dimensionality
)

#load the storage context saved in load_data.py
storage_context = StorageContext.from_defaults(vector_store=vector_store,persist_dir="storageExample")
index = load_index_from_storage(
    storage_context,
    # we can optionally override the embed_model here
    # it's important to use the same embed_model as the one used to build the index
    # embed_model=Settings.embed_model,
)
query_engine = index.as_query_engine()
    
response = query_engine.query("Faça um resumo da história de Anakin")

import textwrap
print(textwrap.fill(str(response), 100))

