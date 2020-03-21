## Server for service on practice

### Base work with project 

You need use operating system `Linux` and have `poetry` with `pyenv`.
Write next commands for begin work:
```
peynv install 3.6.6
pyenv local 3.6.6
pip install poetry 
poetry install
```

## Rules for JSON

```
"event" -- event can be save/upload/delete/check 
"to_delete" -- id user which need delete
"to_upload" -- rows which need upload
if you choice any one event, then value in other events must be "None"
```