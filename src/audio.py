import pygame
import os

class AudioManager:
    def __init__(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        
        self.base_path = os.path.join("assets", "sounds")
        
        self.bg_music_path = os.path.join(self.base_path, "bg_music.mp3")

        self.sounds = {
            "hit_paddle": self._load_sound("hit_paddle.mp3"),
            "hit_wall": self._load_sound("hit_wall.mp3"),
            "score": self._load_sound("score.mp3")
        }

    def _load_sound(self, filename):
        path = os.path.join(self.base_path, filename)
        if os.path.exists(path):
            try:
                return pygame.mixer.Sound(path)
            except pygame.error as e:
                print(f"Erro ao carregar o som {filename}: {e}")
        else:
            print(f"Aviso: Arquivo de som não encontrado em {path}")
        return None

    def play(self, sound_name):
        sound = self.sounds.get(sound_name)
        if sound:
            sound.play()

    def start_bg_music(self, volume=0.5):
        if os.path.exists(self.bg_music_path):
            try:
                pygame.mixer.music.load(self.bg_music_path)
                pygame.mixer.music.set_volume(volume)
                pygame.mixer.music.play(-1)
            except pygame.error as e:
                print(f"Erro ao reproduzir música de fundo: {e}")
        else:
            print(f"Aviso: Música de fundo não encontrada em {self.bg_music_path}")
