from .chatterbox import mtl_tts
import torchaudio as ta
import torch
from safetensors.torch import load_file as load_safetensors


class MedadTTS():
    def __init__(
            self,
            weights_path, 
            device="cuda" if torch.cuda.is_available() else "cpu"
        ):
        
        self.multilingual_model = mtl_tts.ChatterboxMultilingualTTS.from_pretrained(device=device)
        t3_state = load_safetensors(weights_path, device="cuda")
        self.multilingual_model.t3.load_state_dict(t3_state)
        self.multilingual_model.t3.to(device).eval()
        print('model loaded')
        
    def __call__(self, prompt, **options):
        # default options
        settings = {
            "language_id": None,
            "temperature": 0.5,
            "cfg_weight": 0.5,
            "top_p": 0.3,
            "exaggeration": 0.3,
        }
        settings.update(options)
        
        wav = multilingual_model.generate(
            prompt,
            **options)
        
        return wav
