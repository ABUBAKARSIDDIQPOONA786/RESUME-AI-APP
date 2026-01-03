from fastapi import FastAPI
from app.routers import resume
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Resume.AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://resume-ai-app.vercel.app",
        "https://resume-ai-app-git-main-poona-abubakar-siddiqs-projects.vercel.app",
        "https://resume-ai-9imxo6bns-poona-abubakar-siddiqs-projects.vercel.app",
        "https://resume-ai-96k0c5rx9-poona-abubakar-siddiqs-projects.vercel.app"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def limit_upload_size(request: Request, call_next):
    if request.method == "POST":
        content_length = request.headers.get("content-length")
        if content_length and int(content_length) > 5_000_000:
            raise HTTPException(
                status_code=413,
                detail="File too large. Max allowed size is 5MB."
            )
    return await call_next(request)

app.include_router(resume.router)
