from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers import resume

app = FastAPI(title="Resume Intelligence API")

# ✅ CORS (important for mobile & Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://resume-ai-app.vercel.app",
        "http://localhost:3000",
        "https://resume-ai-app.vercel.app",
        "https://resume-ai-app-git-main-poona-abubakar-siddiqs-projects.vercel.app",
        "https://resume-ai-9imxo6bns-poona-abubakar-siddiqs-projects.vercel.app",
        "https://resume-ai-96k0c5rx9-poona-abubakar-siddiqs-projects.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Upload size guard (now safe)
@app.middleware("http")
async def limit_upload_size(request: Request, call_next):
    if request.method == "POST":
        content_length = request.headers.get("content-length")
        if content_length and int(content_length) > 5 * 1024 * 1024:
            return JSONResponse(
                status_code=413,
                content={"error": "File too large (max 5MB)"},
            )
    return await call_next(request)

app.include_router(resume.router)
