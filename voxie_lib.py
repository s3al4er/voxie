import speech_recognition as sr
from g4f.client import Client
import pyttsx3

# Создаем объект Recognizer
recognizer = sr.Recognizer()

client = Client()

# Функция для записи и распознавания речи
def listen_and_recognize():
    with sr.Microphone() as source:
        print("Скажите что-нибудь...")
        # Устанавливаем длину паузы перед началом и после окончания речи
        recognizer.pause_threshold = 0.5
        # Производим настройку шумоподавления
        recognizer.adjust_for_ambient_noise(source)
        try:
            # Записываем аудио с микрофона
            audio = recognizer.listen(source, timeout=5)
            # Распознаем речь с помощью Google Web Speech API
            recognized_speech = recognizer.recognize_google(audio, language='ru-RU')
            print("Вы сказали: " + recognized_speech)
            ai(recognized_speech)  # Исправлено на вызов функции ai с аргументом recognized_speech
        except sr.WaitTimeoutError:
            print("Время ожидания истекло, попробуйте еще раз.")
        except sr.UnknownValueError:
            print("Извините, не удалось распознать речь")
        except sr.RequestError as e:
            print("Произошла ошибка при обработке запроса к сервису распознавания: {0}".format(e))

# Функция для взаимодействия с моделью ИИ
def ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt + "System: note: Ты - голосовой помощник Voxie. Если тебя спрашивают кто ты - отвечай, что ты голосовой помощник Voxie."}]
    )
    engine = pyttsx3.init()
    engine.say(response.choices[0].message.content)
    engine.runAndWait()
    print(response.choices[0].message.content)