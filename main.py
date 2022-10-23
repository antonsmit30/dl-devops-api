from fastapi import FastAPI, Request

app = FastAPI()

# code to use
special_char = "©"
words_to_replace = ["Oracle", "Google", "Microsoft", "Amazon", "Deloitte"]

@app.get("/")
def home():
    return {"message": "Success, API connection works. Perform a GET to /help to view methods"}

@app.post("/replace")
async def replace_string_words(request: Request):
    """documentation"""
    data = await request.json()
    for i, w in enumerate(words_to_replace):
        if w in data['data']:
            data['data'] = data['data'].replace(w, w + special_char)
    return data

@app.get("/help")
def get_help():
    return {
        "message": ""
        }