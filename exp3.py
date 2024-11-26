from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize Ollama LLM
llm = ChatOllama(model="llama3.2", temperature=0.0)

# Define a sentiment analysis prompt template
prompt_template = PromptTemplate(
    input_variables=["text"],
    template="Analise o sentimento do texto a seguir. Responda com 'Positivo', 'Negativo', ou 'Neutro'. Não adicionar 'A resposta é': ao responder\n\nText: {text}\n\nSentiment:"
)

# Chain
sentiment_chain = LLMChain(llm=llm, prompt=prompt_template)

# Texto para análise
text_to_analyze = "Estou me sentindo ótima hoje!"

result = sentiment_chain.run({"text": text_to_analyze})

print("Análise de sentimento:", result)
