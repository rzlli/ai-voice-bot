import os
import speech_recognition as sr
import cohere
from gtts import gTTS

# تهيئة عميل كوهير بالإصدار الثاني الحديث
co = cohere.ClientV2(api_key="cohere_eWdg7YdehIavl80CAeePpQ1f8b3tQwCLM0z5ajXN0Remxz")

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("...تفضل بالتحدث الآن، أستمع إليك")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    
    try:
        print("...جاري تحويل الصوت إلى نص")
        text = r.recognize_google(audio, language="ar-SA")
        print(f"النص المحول: {text}")
        return text
    except Exception as e:
        print(f"عذراً، لم أتمكن من فهم الصوت أو حدث خطأ: {e}")
        return None

def generate_ai_response(prompt_text):
    print("جاري توليد الرد باستخدام نموذج Cohere...")
    response = co.chat(
        model="command-a-03-2025",
        messages=[
            {
                "role": "user",
                "content": prompt_text,
            }
        ],
    )
    answer = response.message.content[0].text
    print(f"رد المساعد: {answer}")
    return answer

def text_to_speech(text_response):
    print("...جاري تحويل الرد إلى ملف صوتي")
    tts = gTTS(text=text_response, lang='ar', slow=False)
    output_file = "response.mp3"
    tts.save(output_file)
    print(f"تم حفظ الملف الصوتي باسم {output_file}")
    
    try:
        os.system(f"start {output_file}")
    except:
        pass

if __name__ == "__main__":
    user_text = speech_to_text()
    if user_text:
        ai_reply = generate_ai_response(user_text)
        text_to_speech(ai_reply)