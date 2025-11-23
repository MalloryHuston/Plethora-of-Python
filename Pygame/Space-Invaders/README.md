# 🛸 Space Invaders: A Pygame Remake

A modern recreation of the classic **Space Invaders** arcade game, built using **Python** and **Pygame**. Designed for 750×750 resolution with pixel-art assets and a retro aesthetic powered by the Press Start 2P font.

---

## 🚀 Features (So Far)

- Classic-style **2D arcade shooter**
- Enemy wave system with red, green, and blue alien ships
- Player-controlled laser cannon with health and collision
- Pixel-art assets and background
- Lives and level tracking displayed via retro-styled HUD
- "YOU DIED!!!" screen upon defeat
- Press-to-start main menu screen
- Dynamic font scaling based on screen resolution

---

## 🖥️ Resolution & Fonts

- Default resolution: **750 × 750**
- Fonts:
  - **[Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P)** (retro 8-bit style)
  - **[Pixelify Sans](https://fonts.google.com/specimen/Pixelify+Sans)**
- Fonts scale proportionally to screen width for UI consistency

---

## 🎮 Controls

| Key       | Action         |
|-----------|----------------|
| `A`       | Move Left      |
| `D`       | Move Right     |
| `W`       | Move Up        |
| `S`       | Move Down      |
| `Space`   | Shoot Laser    |
| `Mouse`   | Click to Start |

---

## 🧱 Folder Structure

```bash
Space-Invaders/
│
├── main.py
├── README.md
│
└── assets/
    ├── fonts/
    │   └── list_fonts.py          # Utility script to preview and list all available system fonts
    │   └── PixelifySans.ttf
    │   └── PressStart2P.ttf
    │
    ├── imgs/
    │   └── background-black.png
    │   └── pixel_laser_blue.png
    │   └── pixel_laser_green.png
    │   └── pixel_laser_red.png
    │   └── pixel_laser_yellow.png
    │   └── pixel_ship_blue_small.png
    │   └── pixel_ship_green_small.png
    │   └── pixel_ship_red_small.png
    │   └── pixel_ship_yellow.png
    │
    ├── sounds/
    │   └── explosion.wav
    │   └── game-over.wav
    │   └── game-start.wav
    │   └── laser.wav
    │   └── victory.wav
```

---

## 🔧 Getting Started

### 1. Install Pygame

```bash
pip install pygame
```

### 2. Run the Game

```bash
python main.py
```

---

## 🛠️ In Progress

- 🎵 Sound effects and background music
- 💥 Power-ups and more alien types
- 🧮 Score tracking + high score saving
- ⬆️ Level progression with difficulty scaling
- 📱 Touchscreen or mobile-friendly controls
