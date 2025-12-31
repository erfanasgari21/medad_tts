# Medad TTS

## Installation and Usage
First install the dependecies:

```cmd
pip install chatterbox-tts --no-deps
pip install -r requirements.txt
```

Instantiate the MedadTTS class and run the pipe to get a wav with 24000 sample rate:

```python
from medad_tts import MedadTTS
pipe = MedadTTS("path/to/t3_fa.safetensors", device="cuda")

prompt="سلام و عرض ادب خدمت هم میهنان گرامی"
wav = pipe(prompt)
```

you can save the wav file:
```
import torchaudio as ta
ta.save("test.wav", wav, 24000)
```

you can also pass more optional settings to the pipe:
```python
wav = pipe(
    prompt,
    # reference audio to get voice id from
    audio_prompt_path="arman.wav",
    # generation options
    temperature=0.5,
    cfg_weight=0.5,
    top_p=0.3,
    exaggeration=0.3
)
```