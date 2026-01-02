from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.routers import resume
import time

# Initialize FastAPI App for 2026 Standards
app = FastAPI(
    title="Resume AI Intelligence API",
    description="Agentic AI-powered ATS scoring and role mapping engine.",
    version="1.0.0"
)

# ---- 1. CORS Configuration (The Security Bridge) ----
# Replace ["*"] with your specific Vercel/Netlify URL in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- 2. Global Middleware (Performance Tracking) ----
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# ---- 3. File Size Limit (Safety Layer) ----
# Prevents server crashes from massive file uploads
@app.middleware("http")
async def limit_upload_size(request: Request, call_next):
    if request.method == "POST" and request.url.path == "/resume/upload":
        if "content-length" in request.headers:
            if int(request.headers["content-length"]) > 5_242_880:  # 5MB
                raise HTTPException(status_code=413, detail="File too large. Max 5MB.")
    return await call_next(request)

# ---- 4. Route Registration ----
app.include_router(resume.router)

# ---- 5. Health Check & Root ----
@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "Resume AI Backend is running in 2026 production mode.",
        "documentation": "/docs"
    }

# ---- 6. Global Error Handler ----
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return {
        "error": "Internal Server Error",
        "detail": str(exc),
        "timestamp": time.time()
    }
