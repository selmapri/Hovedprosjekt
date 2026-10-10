import requests
import json


BASE_URL = "https://search.api.fellesdatakatalog.digdir.no/search/datasets"


def search_datasets(query):
    payload = {
        "query": query,
        "pagination": {
            "size": 10,
            "page": 1
        }
    }

    response = requests.post(
        BASE_URL,
        json=payload,
        headers={
            "Content-Type": "application/json"
        },
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def print_datasets(data):
    """
    Skriver ut resultatene fra Data.norge.no.
    """

    hits = data.get("hits", [])

    print(f"\nAntall treff: {len(hits)}\n")

    if not hits:
        print("Ingen datasett funnet.")
        return

    for i, hit in enumerate(hits, start=1):

        print(f"--- Datasett {i}[{hit.get('organization', 'Ukjent')}] ---")

        # Skriv ut hele treffet slik at vi ser strukturen
        """print(json.dumps(hit, indent=2, ensure_ascii=False))"""

        print()
