@echo off
call .\.venv\Scripts\activate
uvicorn main:app --host 0.0.0.0 --port 8081 --reload
