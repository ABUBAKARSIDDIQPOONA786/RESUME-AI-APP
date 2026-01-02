from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

try:
    from app.routers import resume
except ImportError:
    from .routers import resume

app = FastAPI(title="AI Resume Intelligence")

@app.get("/")
async def root():
    return {"status": "online", "message": "Resume AI Backend is running. Visit /docs for API testing."}
    
# ---- CORS ----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with Vercel URL after deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- FILE SIZE LIMIT (5MB) ----
@app.middleware("http")
async def limit_upload_size(request: Request, call_next):
    if request.headers.get("content-length"):
        if int(request.headers["content-length"]) > 5_000_000:
            raise HTTPException(
                status_code=413,
                detail="File too large. Max allowed size is 5MB."
            )
    return await call_next(request)

# ---- ROUTES ----
app.include_router(resume.router)
