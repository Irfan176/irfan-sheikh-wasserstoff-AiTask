from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from embeddings import update_embeddings_on_new_post
from chain_of_thought import process_query_with_chain_of_thought
from rag_processor import generate_response
import uvicorn

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class QueryRequest(BaseModel):
    query: str
    previous_context: List[str] = []

class EmbeddingUpdate(BaseModel):
    content: str

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Query API"}

@app.get("/health")
async def health_check():
    return {"status": "OK"}

@app.post("/query")
async def query_handler(request: QueryRequest):
    try:
        final_response = process_query_with_chain_of_thought(request.query, request.previous_context)
        return {"response": final_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/update_embeddings")
async def update_embeddings(update: EmbeddingUpdate):
    try:
        update_embeddings_on_new_post({"content": update.content})
        return {"status": "embeddings updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate")
async def generate(request: QueryRequest):
    try:
        response = generate_response(request.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)