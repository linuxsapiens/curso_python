# pip install 

import os
from langchain_community.llms import Anthropic
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Asegúrate de tener las API keys necesarias en tus variables de entorno
os.environ["OPENAI_API_KEY"] = ""
os.environ["ANTHROPIC_API_KEY"] = ""

# Inicializar los modelos
openai_llm = OpenAI(temperature=0.7)
claude_llm = Anthropic(temperature=0.7)
#llama_llm = LlamaCpp(model_path="ruta/a/tu/modelo/llama.cpp")

# Crear un prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Escribe un párrafo corto sobre el siguiente tema: {topic}",
)

# Función para generar texto con un modelo específico
def generate_text(llm, topic):
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(topic)

# Ejemplo de uso
topic = "El mejor sistema economico del mundo"

print("Generado por OpenAI:")
print(generate_text(openai_llm, topic))

print("\nGenerado por Claude:")
print(generate_text(claude_llm, topic))

#print("\nGenerado por Llama:")
#print(generate_text(llama_llm, topic))
