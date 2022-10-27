## DLApi
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