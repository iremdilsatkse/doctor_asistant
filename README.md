# Doktor Asistanı

Bu proje, Google Gemini LLM ve LangChain teknolojilerini kullanarak sağlıkla ilgili soruları yanıtlayan bir doktor asistanı sohbet uygulamasıdır. Hem terminal üzerinden hem de FastAPI tabanlı bir web servisi olarak kullanılabilir.

## Özellikler

- Kullanıcı adı ve yaşına göre kişiselleştirilmiş yanıtlar
- Sohbet geçmişini hafızada tutma
- Google Gemini 2.5 Flash modeli ile gerçek zamanlı öneriler
- Terminal ve API istemcisi desteği

## Kurulum

1. Depoyu klonlayın ve dizine girin.
2. İlk olarak yeni bir env oluşturun.
   ```sh
    python -m venv venv
    ```
3. Oluşturduğunuz env aktif ettikten sonra gerekli Python paketlerini yükleyin:
    ```sh
    pip install fastapi uvicorn langchain google-generativeai python-dotenv langchain_community
    ```
4. `.env` dosyasına Google API anahtarınızı ekleyin:
    ```
    GOOGLE_API_KEY=your_api_key_here
    ```

## Kullanım

### 1. FastAPI Sunucusunu Başlatma

Aşağıdaki komut ile API sunucusunu başlatın:

```sh
uvicorn doctor_assistant_api:app --reload
```

### 2. Terminal Üzerinden Sohbet

```sh
python doctor_assistant_terminal.py
```

### 3. API ile Sohbet (Test İstemcisi)

Önce API sunucusunu başlatın, ardından:

```sh
python client_test.py
```

## Dosya Açıklamaları

- [`doctor_assistant_api.py`](doctor_assistant_api.py): FastAPI tabanlı sohbet API'si
- [`doctor_assistant_terminal.py`](doctor_assistant_terminal.py): Terminal tabanlı sohbet uygulaması
- [`client_test.py`](client_test.py): API'yi test etmek için terminal istemcisi
- [`.env`](.env): Google API anahtarı

## Notlar

- Sohbet geçmişi her kullanıcı için ayrı tutulur.
- Model tıbbi teşhis koymaz, sadece öneri ve bilgilendirme amaçlıdır.

---

**Uyarı:** Bu uygulama gerçek bir doktorun yerini tutmaz. Sağlık sorunlarınız için mutlaka bir uzmana danışınız.
