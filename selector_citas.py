import json
import random
import os

# Ruta al archivo de citas (en el repo de tareas personales)
QUOTES_PATH = "/home/alexeiiw/Personal/moltbot-global-tasks/quotes.json"

def seleccionar_cita():
    if not os.path.exists(QUOTES_PATH):
        print(f"Error: No se encontró el archivo en {QUOTES_PATH}")
        return

    with open(QUOTES_PATH, 'r', encoding='utf-8') as f:
        quotes = json.load(f)

    # Filtrar citas no enviadas
    available_quotes = [q for q in quotes if not q.get('sent', False)]
    
    if not available_quotes:
        print("No hay más citas pendientes por enviar.")
        return

    # Seleccionar una al azar
    selected = random.choice(available_quotes)
    
    print("-" * 30)
    print(f"CITADO POR: {selected['author']} ({selected['source']})")
    print(f"ORIGINAL: \"{selected['text']}\"")
    
    # En un entorno real sin internet, la traducción sería manual o con librería local.
    # Aquí simulamos la lógica solicitada para que el usuario pueda validarla.
    # Para fines académicos, se recomienda usar una API o librería como deep-translator.
    print(f"TRADUCCIÓN: (Lógica de traducción pendiente de API/Librería)")
    print("-" * 30)

    # Marcar como enviada
    for q in quotes:
        if q['text'] == selected['text']:
            q['sent'] = True
            break

    # Guardar cambios
    with open(QUOTES_PATH, 'w', encoding='utf-8') as f:
        json.dump(quotes, f, indent=2, ensure_ascii=False)
    
    print("Cita marcada como 'sent: true' en quotes.json")

if __name__ == "__main__":
    seleccionar_cita()
