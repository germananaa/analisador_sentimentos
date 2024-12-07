from textblob import TextBlob
from googletrans import Translator

def analisar_sentimento(texto):

    # Traduzir o texto para inglês
    tradutor = Translator()
    traduzido = tradutor.translate(texto, src='pt', dest='en').text

    # Analisa o sentimento usando TextBlob
    analise = TextBlob(traduzido)
    sentimento = analise.sentiment.polarity

    if sentimento > 0:
        return "Positivo"
    elif sentimento < 0:
        return "Negativo"
    else:
        return "Neutro"

# Exemplo de uso
if __name__ == "__main__":
    print("Digite uma frase para análise de sentimento:")
    frase = input("> ")
    resultado = analisar_sentimento(frase)
    print(f"O sentimento detectado foi: {resultado}")
