import requests
import json

API_KEY = "5c21aae0af9c462f25498a550933308f"

url = "https://api.the-odds-api.com/v4/sports/soccer_italy_serie_a/odds/"

params = {
    "apiKey": API_KEY,
    "regions": "eu",
    "markets": "h2h"
}

response = requests.get(url, params=params)
data = response.json()

matches = []

for match in data:
    home = match["home_team"]
    away = match["away_team"]

    best_odds = {"1": None, "X": None, "2": None}

    for bookmaker in match["bookmakers"]:
        for outcome in bookmaker["markets"][0]["outcomes"]:
            name = outcome["name"]
            price = outcome["price"]

            if name == home:
                key = "1"
            elif name == away:
                key = "2"
            else:
                key = "X"

            if best_odds[key] is None or price > best_odds[key]:
                best_odds[key] = price

    matches.append({
        "home": home,
        "away": away,
        "odds": best_odds
    })

# salva JSON
with open("odds.json", "w") as f:
    json.dump(matches, f, indent=2)

print("✅ File odds.json aggiornato")