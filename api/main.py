from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/random_word")
async def get_random_word():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.dictionaryapi.dev/api/v2/randomWord")
        word = response.json()["word"]
        response = await client.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        definition = response.json()[0]["meanings"][0]["definitions"][0]["definition"]
    return {"word": word, "definition": definition}
