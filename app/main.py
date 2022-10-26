from fastapi import FastAPI, Request

app = FastAPI()

# code to use
special_char = "©"
words_to_replace = ["Oracle", "Google", "Microsoft", "Amazon", "Deloitte"]

@app.get("/")
def home():
    return {"message": "Success, API connection works. Perform a GET to /docs to get started."}

@app.post("/replace")
async def replace_string_words(request: Request):
    """
Send a string that will replace the following keywords:\n
"Oracle", "Google", "Microsoft", "Amazon", "Deloitte"\n
with:\n
"Oracle©", "Google©", "Microsoft©", "Amazon©", "Deloitte©"\n

Method: POST\n
Content-Type: application/json\n

example:\n
Request:\n
{"data": "Google, Microsoft and Amazon are the top Cloud competitors."}\n

Response:\n
{"data": "Google©, Microsoft© and Amazon© are the top Cloud competitors."}\n

    """
    data = await request.json()
    for i, w in enumerate(words_to_replace):
        if w in data['data']:
            data['data'] = data['data'].replace(w, w + special_char)
    return data
