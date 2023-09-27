# langchain-demos

Framework concepts:
* Models: to use such as: chatgpt, llama, etc (text generation, chat, embeddings, etc)
* Prompts: text (prompt template, chat prompt template, prompt value, example selector, output parser) to send and get prediction
* Indexes: data sources
    * Document Loader
    * Models
    * Text Splitter
    * Vector Stores
    * Retriever
* Memory: to keep the context and avoid stateless
* Chains: like pipelines, example: get arduino ideas & development
* Agents: to use internet and data updated, example: what is the latest release of a game which main character is Link? (two iteractions: get zelda, get releases)



Requisitos
```
pip install -r requirements.txt
```

Ejecutar:
```
python 1-hello.py
```
