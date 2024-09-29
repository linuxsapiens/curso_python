import os
from langchain_community.llms import huggingface_pipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

os.environ["OPENAI_API_KEY"] = ""


# Configurar el modelo de generacion de texto
generation_model = pipeline("text-generation", model="GPT4")
llm = huggingface_pipeline(pipeline=generation_model)

# Configurar el modelo de analisis de sentimientos
sentiment_tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
sentiment_model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
sentiment_pipeline = pipeline("sentiment-analysis", model=sentiment_model, tokenizer=sentiment_tokenizer)

# Crear un prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Escribe una opinión breve sobre: {topic}",
)

# Función para generar texto y analizar sentimiento
def generate_and_analyze(topic):
    # Generar texto
    chain = LLMChain(llm=llm, prompt=prompt)
    generated_text = chain.run(topic)
    
    # Analizar sentimiento
    sentiment = sentiment_pipeline(generated_text)[0]
    
    return generated_text, sentiment

# Ejemplo de uso
topic = "Inteligencia Artificial en la educación"
text, sentiment = generate_and_analyze(topic)

print(f"Texto generado sobre '{topic}':")
print(text)
print(f"\nSentimiento: {sentiment['label']} (Score: {sentiment['score']:.2f})")