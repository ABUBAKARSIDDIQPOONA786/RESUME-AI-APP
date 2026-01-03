from fastapi import FastAPI
from ..routers import resume
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Resume.AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://resume-ai-app.vercel.app",
        "https://resume-ai-app-git-main-poona-abubakar-siddiqs-projects.vercel.app",
        "https://resume-ai-9imxo6bns-poona-abubakar-siddiqs-projects.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router)
