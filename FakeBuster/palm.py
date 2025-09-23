import google.generativeai as genai
from . import traductor

genai.configure(api_key='AIzaSyBw6ZSqOh-mlKJ-Hw_i5xnoV0zU-w-8pow') #Sustituir por la verdader api key que te ofrece Google developer
model = genai.GenerativeModel('gemini-1.5-flash')


def buscarInformacion(texto):
    textoTraducidoAlIngles = traductor.traducirAIngles(texto)
    
    prompt = textoTraducidoAlIngles

    completion = model.generate_content(prompt)
    
    textoTraducidoAlEspañol = traductor.traducirAEspañol(completion.text)

    return textoTraducidoAlEspañol