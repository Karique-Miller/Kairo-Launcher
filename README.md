# Kairo Launcher

Kairo Launcher is a custom desktop application written in **Python** that lets users manage and launch all their installed games from a single GUI.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Motivation & Learning Goals](#motivation--goals)  
- [Technical Details](#technical-details)  
- [Installation](#installation)   
- [Future Improvements](#future-improvements)  


---

## Overview

Kairo Launcher is designed to provide a clean, scrollable graphical user interface for launching games on Windows. Users can add games, remove them, sort and search through their library, and launch any game directly from the app. Game data is saved in a JSON file, allowing persistence between sessions.

---

## Features

- **Add / Remove Games** – Browse for `.exe`, `.lnk`, or shortcut files to add games to the launcher.
  <img width="302" height="332" alt="Kairo_Launcher_Add_Remove_Buttons" src="https://github.com/user-attachments/assets/7259c37e-ad97-49c5-ba77-acb4c43d5068" />
- **Persistent Storage** – Game paths and metadata are stored in `games.json`.
  <img width="618" height="365" alt="Kairo_Launcher_Persistant Storage" src="https://github.com/user-attachments/assets/3711457b-e314-43a3-b719-9644dafbf453" />
 
- **Scrollable UI** – A scrollable canvas in the GUI to support a dynamic list of games.
- 
  <img width="302" height="332" alt="Kairo_Launcher_Scrollabe_UI" src="https://github.com/user-attachments/assets/d884cdb2-f1af-4e94-b8f9-8df243fcb0d2" />
 
- **Search** – Search bar filters games by name.
  
   <img width="302" height="332" alt="Kairo_Launcher_Search" src="https://github.com/user-attachments/assets/9182fb1c-4e2a-4bb2-ad7f-0d67a6b09c54" />

- **Context Menu** – Hovering over a game reveals an options button, allowing you to delete entries and add/change the image of the buttons.

  <img width="302" height="332" alt="Kairo_Launcher_Context_menu" src="https://github.com/user-attachments/assets/9e77ccff-f2c2-4e93-b2d5-329260310393" />

- **Launch Games** – Double-click or click a button to launch a gamel.

  <img width="302" height="332" alt="Kairo_Launcher_Launch_games" src="https://github.com/user-attachments/assets/a48c43a7-b184-4379-a14f-1cc598896d95" />

- **Sort Options** - Sort game list based on prefrence.

  <img width="302" height="332" alt="Kairo_Launcher_Sort" src="https://github.com/user-attachments/assets/5bc4cd0f-8339-4095-999b-1261b34cf088" />

- **Themes** - Change the UI by selecting from a pre-made theme.

  <img width="302" height="332" alt="Kairo_Launcher_themes" src="https://github.com/user-attachments/assets/54f45a47-fa3a-435e-9ecb-6c033992887d" />

- **Reset Library** – Ability to completely reset the launcher back to default.

<img width="302" height="332" alt="Kairo_Launcher_Reset_libary" src="https://github.com/user-attachments/assets/61d51c87-88ff-474c-b133-fe80c8b4ad69" />


---

## Motivation & Goals

I built Kairo Launcher because I hate swaping between diffrent game launchers or scrolling endlessly on Steam to find a game.

1. Real desktop GUI development (using Tkinter).  
2. Persistent data handling using JSON.  
3. Event-driven programming and UI interactivity.  
4. Process management (launching external applications).  
5. Clean, modular code architecture and state management.

This project was particularly helpful in preparing for more advanced software engineering projects and tasks.
---

## Technical Details

- **Language:** Python 3  
- **GUI Framework:** Tkinter  
- **Data Storage:** JSON (`games.json`)  
- **Process Launching:** `subprocess` module  
- **Platform Support:** Windows (uses `os.startfile`, sets AppUserModelID)  
- **UI Layout:** Scrollable canvas with dynamic Frame and Button widgets  
- **Event Handling:** Mouse hover, click, and context menu  

---

## Installation

1. Download the .zip file.
2. Extract it to your desiered location.
3. Open the Kairo Launcher folder.
4. Launch the .exe file.

---

## Future Improvements


- Improved image adding system
- More Sorting options
- Improved searching
- Cross-Platform support
- More image file types supported
