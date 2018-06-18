import pyaudio
import wave
import audioop
from collections import deque
import time
import math


def listen():
    print("Listening for loud sounds...")
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44000 # битрейт звука, который мы хотим слушать
    THRESHOLD = 2000  # порог интенсивности звука, если интенсивность ниже, значит звук по нашим меркам слишком тихий
    SILENCE_LIMIT = 1  # длительность тишины, если мы не слышим ничего это время, то начинаем слушать заново

    # открываем стрим
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, input=True, frames_per_buffer=CHUNK)
    cur_data = ''
    rel = RATE / CHUNK
    print(type(SILENCE_LIMIT))
    print(type(rel))
    slid_win = deque(maxlen=int(SILENCE_LIMIT * rel))

    # начинаем слушать и по истечении 5 секунд, отменяем слушалку
    success = False
    listening_start_time = time.time()
    while True:
        # try:
        #     cur_data = stream.read(CHUNK)
        #     slid_win.append(math.sqrt(abs(audioop.avg(cur_data, 4))))
        #     if (sum([x > THRESHOLD for x in slid_win]) > 0):
        #         print("I heart something!")
        #         success = True
        #         break
        #     if time.time() - listening_start_time > 5:
        #         print("I don\'t hear anything during 20 seconds!")
        #         break
        # except IOError:
        #     print("IOError")
        #     break



        cur_data = stream.read(CHUNK)
        slid_win.append(math.sqrt(abs(audioop.avg(cur_data, 4))))
        if (sum([x > THRESHOLD for x in slid_win]) > 0):
            print("I heart something!")
            success = True
            break
        if time.time() - listening_start_time > 10000:
            print("I don\'t hear anything during 10000 seconds!")
            break


    # обязательно закрываем стрим
    stream.close()
    p.terminate()
    return success
