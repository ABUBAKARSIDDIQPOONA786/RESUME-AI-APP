from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers import resume

app = FastAPI(title="Resume AI API")

# ✅ CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://resume-ai-app.vercel.app",
        "http://localhost:5173",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ FILE SIZE LIMIT (5MB)
@app.middleware("http")
async def limit_upload_size(request: Request, call_next):
    content_length = request.headers.get("content-length")
    if content_length and int(content_length) > 5_000_000:
        return JSONResponse(
            status_code=413,
            content={"detail": "File too large. Max 5MB"}
        )
    return await call_next(request)

# ✅ ROUTES
app.include_router(resume.router)

@app.get("/")
def health():
    return {"status": "API running"}

@app.get("/")
def health():
    return {"status": "ok"}

