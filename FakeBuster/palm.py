import google.generativeai as genai
from . import traductor

genai.configure(api_key='api_key') #Sustituir por tu api key que te ofrece Google Cloud Console y Google AI Studio
model = genai.GenerativeModel('gemini-1.5-flash')


def buscarInformacion(texto):
    textoTraducidoAlIngles = traductor.traducirAIngles(texto)
    
    prompt = textoTraducidoAlIngles

    completion = model.generate_content(prompt)
    
    textoTraducidoAlEspañol = traductor.traducirAEspañol(completion.text)

    return textoTraducidoAlEspañol