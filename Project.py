import os
import pygame
import tkinter as tk
from tkinter import filedialog
pygame.init()
pygame.mixer.init()
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("500x200")

        self.music_file = None
        self.playing = False

        # Create GUI elements
        self.label = tk.Label(root, text="Music Player", font=("Helvetica", 20))
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Music", command=self.browse_file)
        self.select_button.pack(pady=5)

        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

    def browse_file(self):
        self.music_file = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])

    def play_music(self):
        if self.music_file:
            if not self.playing:
                pygame.mixer.music.load(self.music_file)
                pygame.mixer.music.play()
                self.playing = True

    def stop_music(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
