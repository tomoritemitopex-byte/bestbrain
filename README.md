
# BestBrain 2.0.0 (Hybrid Edition)

Lightweight edition that runs on:
- Termux (Android)
- Chromebook Linux
- JustRunMy.app
- GitHub sync

## Run locally:
uvicorn app.server:app --host 0.0.0.0 --port 8000

## Deploy to Justrunmy.app:
Zip or tar.gz the folder
Use start command:
uvicorn app.server:app --host 0.0.0.0 --port 8080
