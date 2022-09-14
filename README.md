# Voice_Assistant (Fedora)

Идея взята с канала [Python Hub Studio](https://www.youtube.com/watch?v=MXdsPKZyZ48&t=1750s)
****
## Языковые модели

- [VOSK](https://alphacephei.com/vosk/models) добавить в папку **_voice_models** внтури проекта (по умолчанию загружена **vosk-model-small-ru-0.22**)

****
## Библиотеки
#### Основные
- **pip install vosk** - автономный набор инструментов для распознавания речи
- **pip install sounddevice** - предоставляет привязки для библиотеки PortAudio и несколько удобных функций для воспроизведения и записи массивов NumPy , содержащих аудиосигналы
- **pip install scikit-learn** - модуль для машинного обучения, созданный на основе SciPy
- **pip install silero** - предварительно подготовленные модели преобразования речи в текст, преобразование текста в речь и уточнение текста

#### Вспомогательные (для прокачки скилов)
- **pip install requests**
****
## Проблемы

- **python -m sounddevice** (отобразить существующие аудиоустойства) - вызывает ошибку ***OSError('PortAudio library not found')***
    **-** скорее всего проблема в отсвтутсвтии драйвера, которая решается
    1. **sudo dnf makecache --refresh**
    2. **sudo dnf -y install portaudio**
****