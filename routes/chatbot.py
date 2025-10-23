# backend/routes/chatbot.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/chatbot", tags=["Chatbot"])

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str

@router.post("/ask", response_model=ChatResponse)
async def ask_chatbot(request: ChatRequest):
    """
    Simple chatbot response logic — replace with AI later.
    """
    question = request.question.lower()
    if "fever" in question:
        answer = "If your pet has a fever, keep it hydrated and consult a vet immediately."
    elif "vaccine" in question:
        answer = "Pets should be vaccinated every 6–12 months depending on species and age."
    elif "food" in question:
        answer = "Provide balanced nutrition — avoid chocolate, onions, and spicy food."
    else:
        answer = "I’m your vet assistant! Please ask about symptoms, vaccines, or care tips."

    return ChatResponse(answer=answer)
