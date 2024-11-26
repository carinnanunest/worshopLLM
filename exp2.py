# Instalando a biblioteca LangChain
# pip install langchain

from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage

# Temperatura é a variabilidade da saída do modelo​
llm = ChatOllama(model="llama3.2", temperature=0.0)

# Define o prompt
chat_template = ChatPromptTemplate.from_template("Traduza para o {lang} o seguinte texto: {text}")

prompt_engineered = chat_template.format(lang="Português", text="Hello, how are you?")

messages = [HumanMessage(content=prompt_engineered)]

response = llm(messages)

print(response.content)
