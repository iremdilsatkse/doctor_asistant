"""
Kullanıcının sağlıkla ilgili soruların yanıtlayan bir GPT asistanı
    - Kullanıcının yaşını ve adını dikkate alır.
    - Mesaj geçmişlerini hatırlar.
    - Langchain ve google teknolojileri kullanır.
    - İlk olarak terminalde çalışan bir versiyon. 
    - Sonra FastAPI tabanlı web servisinde çalışan versiyon.
    - Client tarafını yazıp test edilecek.
"""
"""
- Veri seti kullanılmadı. Hazır GPT modelini kullanarak prompt ayarlaması yapıldı.
- Gemini 2-5 Flash modeli kullanıldı
- API üzerinden iletişim kurarak gerçek zamanlı sağlık önerisi alır.

"""
import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

### Ortam Değişkinleri
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

### LLM + Memory
# Dil Modeli
llm = ChatGoogleGenerativeAI(
    google_api_key=api_key,
    model="gemini-2.5-flash",
    temperature=0.7
)
# Hafıza 
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

### Kullanıcı Bilgileri
name = input("Adınız: ")
age = input("Yaşınız: ")

intro = (
    f"Sen bir doktor asistanısın. Hasta {name}, {age} yaşında. "
    "Sağlık sorunları hakkında konuşmak istiyor. "
    "Yaşına uygun dikkatli ve nazik tavsiyeler ver; ismiyle hitap et. "
)

memory.chat_memory.add_user_message(intro)
print("Merhaba, ben bir doktor asistanıyım. Size nasıl yardımcı olabilirim ?")


### Chatbot Döngüsü 
while True:

    # Soru
    user_msg = input(f"{name}:")
    if user_msg.lower() == "quit": 
        print("Sana yardımcı olabildiysem ne mutlu bana, görüşmek üzere.")
        break

    # Cevap
    reply = conversation.predict(input = user_msg)
    print(f"Doktor Asistanı: {reply}")

    # Memory
    print("\nHafıza: ")
    for idx, m in enumerate(memory.chat_memory.messages, start = 1):
        print(f"{idx:02d}. {m.type.upper()}: {m.content}")
    print("-------------------------------------")



























