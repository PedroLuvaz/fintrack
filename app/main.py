from fastapi import FastAPI

from app.routers import users, categories, transactions, summary

app = FastAPI(
    title="FinTrack API",
    description="Personal Finance Tracker",
    version="0.1.0",
)

app.include_router(users.router)
app.include_router(categories.router)
app.include_router(transactions.router)
app.include_router(summary.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}