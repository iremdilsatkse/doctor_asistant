"""
Fast API ile Gemini Doktor Asistanı
Her kullanıcı için ayrı bir memory tutalım
"""
import os
from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

app = FastAPI(title = "Doktor Asistanı API")

llm = ChatGoogleGenerativeAI(
    google_api_key=api_key,
    model="gemini-2.5-flash",
    temperature=0.7
)
# Hafıza 
user_memories: Dict[str, ConversationBufferMemory] = {}

# Chat mesajı input
class ChatRequest(BaseModel):
    name : str
    age : int
    message : str

# Chat mesajı output
class ChatResponse(BaseModel):
    response : str

# Endpoint
@app.post("/chat", response_model = ChatResponse)
async def chat_with_doctor(request: ChatRequest):
    try:
        if request.name not in user_memories:
            user_memories[request.name] = ConversationBufferMemory(return_messages = True)

        memory = user_memories[request.name]

        if len(memory.chat_memory.messages) == 0:
            intro = (
                f"sen bir doktor assitanısın. Hasta: {request.name}, {request.age} yaşında. "
                "Sağlık sorunları hakkında konuşmak istiyor."
                "Yaşına uygun, dikkali ve nazik tavsiyeler ver. "
                "Kullancıya ismiyle hitap et. "
            )
            memory.chat_memory.add_user_message(intro)

        conversation = ConversationChain(llm = llm, memory = memory, verbose = False)
        reply = conversation.predict(input = request.message)

        print(f"\n Memory: ")
        for idx, m in enumerate(memory.chat_memory.messages, start = 1):
            print(f"{idx:02d}. {m.type.upper()}: {m.content}")
        print("-------------------------------------")

        return ChatResponse(response=reply)
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))





































