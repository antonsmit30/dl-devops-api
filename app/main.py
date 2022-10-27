from fastapi import FastAPI, Request

description = """
## Overview
Send a string that will replace the following keywords:\n
```
"Oracle", "Google", "Microsoft", "Amazon", "Deloitte"\n
```
with this character©:\n
```
"Oracle©", "Google©", "Microsoft©", "Amazon©", "Deloitte©"\n
```
## Data
Method Type: **POST**\n
Content-Type: **application/json**\n

## Example:\n
### Request Path:
```
/replace
```

### Request Body:\n
```
{ 
    "data": "Google, Microsoft and Amazon are the top Cloud competitors."
}\n
```
###Response:\n
```
{"data": "Google©, Microsoft© and Amazon© are the top Cloud competitors."
}\n
```
"""

app = FastAPI(
    title="DlApi",
    description=description
)

# code to use
special_char = "©"
words_to_replace = ["Oracle", "Google", "Microsoft", "Amazon", "Deloitte"]

@app.get("/")
def home():
    return {"message": "Success, API connection works©. Perform a GET to /docs to get started."}

@app.post("/replace")
async def replace_string_words(request: Request):
    data = await request.json()
    for i, w in enumerate(words_to_replace):
        if w in data['data']:
            data['data'] = data['data'].replace(w, w + special_char)
    return data
