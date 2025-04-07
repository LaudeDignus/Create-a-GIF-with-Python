# 🌀 Create a GIF with Pyhton

A simple and educational Python project that generates an animated GIF from a series of images, while showcasing best practices in image processing, file handling, and user interaction.

---
<p align="center">
  <img src="gif_generate/test_2025-04-06.gif" width="300"/><br>
  <strong>Naruto GIF Generator</strong><br>
  <em>Créez un GIF animé à partir d'images avec Python</em>
</p>

---

## 🎯 Learning objectives
This project has enabled me to learn to :

- Manipulating **image files** with the library `imageio`
- Using **regular expressions** to clean up file names
- Manage **file paths** in a portable way with `pathlib`
- Dynamically create a **GIF file** from local images
- Apply **good Python development practices**:
  - Error handling(`try/except`)
  - Automatic directory creation
  - Secure user input
  - Code readability and structure

---

## ⚙️ Technologies used

| Technologie | Usage |
|-------------|-------|
| `Python 3.13` | Main language |
| `imageio.v3` | Reading/writing images and creating GIFs |
| `pathlib` | Modern file path management |
| `re` | Cleaning up filenames with regular expressions |
| `datetime` | Inserting the date in the name of the generated file |

---

## 💻 Features

- 🔄 Generates an **animated GIF** from images in a folder `images/`
- 🧼 Automatically cleans up GIF file names to avoid forbidden characters
- 📁 Automatically creates the `gif_generate/` si inexistant
- 📅 Adds today's date to the file name to prevent overwriting
- 🔐 Handles errors caused by missing or illegible files
- 🧠 Code that is structured, commented, readable and easy to modify

---

## 🗂️ Structure du projet

```
naruto-gif-generator/
│
├── images/                 # Contient les images source
│   ├── naruto1.jpg
│   └── ...
│
├── gif_generate/           # Contiendra le GIF généré
│   └── naruto_<date>.gif
│
├── create_gif.py          # Script principal
└── README.md               # Description du projet (vous êtes ici)
```

---

## ▶️Use

1. Place your images in the `images/`
2. Run the script :

```bash
python3 gif_creator.py
```

3. Give your GIF a name when requested
4. The file will be generated in `gif_generate/`

---

## 🧪 Example of output

```
Give me the name you want for your gif : naruto_final
✅ GIF generated successfully at: gif_generate/naruto_final_2025-04-06.gif
```

---

## 📦Installation

1. Clone this repository :

```bash
git clone https://github.com/ton-nom-utilisateur/naruto-gif-generator.git
cd naruto-gif-generator
```

2. Installe les dépendances :

```bash
pip install imageio
```

---

## ✨ Ce que vous pouvez apprendre grâce à ce projet

| Compétence | Apprise |
|------------|---------|
| Utilisation de bibliothèques tierces (imageio) | ✅ |
| Nettoyage sécurisé d'entrée utilisateur (regex) | ✅ |
| Création de fichiers et gestion des chemins (`pathlib`) | ✅ |
| Scripts robustes avec gestion d’erreurs | ✅ |
| Structuration de projet Python | ✅ |
| Intégration continue possible | ✅ |

---

## 🔄 Possibilités d’amélioration

- Interface graphique (Tkinter / PyQt)
- Si vous avez des idees n'hesitez pas

---

## 🙌 Remerciements

- A Codedex.io
