from fastapi import FastAPI

app = FastAPI(
    title="AI Research Analyst",
    description="AI-powered academic research analysis platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "AI Research Analyst API",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "ai-research-analyst",
    }