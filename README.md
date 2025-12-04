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
- **Persistent Storage** – Game paths and metadata are stored in `games.json`.  
- **Scrollable UI** – A scrollable canvas in the GUI to support a dynamic list of games.  
- **Search & Sort** – Search bar filters games by name, and buttons are automatically sorted alphabetically.  
- **Context Menu** – Hovering over a game reveals an options button, allowing you to delete entries and add/change the image of the buttons.  
- **Launch Games** – Double-click or click a button to launch a gamel. 
- **Reset Library** – Ability to completely reset the launcher back to default.  

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


- Add settings panel (theme, sort order).
- Implement auto-update: check for self-updates or game path validity.
- Enhance metadata: store playtime, launch history, etc.
- Support for other OS (e.g., macOS, Linux) with cross-platform API.
- Add the ability to rename added button if there is no image.
