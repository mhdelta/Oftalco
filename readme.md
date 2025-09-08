# 👁️ OFTALCO

![Language](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Logic Engine](https://img.shields.io/badge/Logic-pyDatalog-orange)
![GUI](https://img.shields.io/badge/GUI-tkinter-lightgreen)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

**Oftalco** is a small expert system built in Python that uses **pyDatalog** as the main logic engine.  
It provides a graphical interface with **tkinter** to help determine possible eye-related diseases based on a set of symptoms.

---

## ✨ Features

- ✅ Knowledge-based reasoning with **pyDatalog**  
- ✅ GUI built with **tkinter** (buttons, frames, labels, entries)  
- ✅ Diagnosis suggestion based on user symptoms  
- ✅ Knowledge stored in a **facts** file  
- ✅ Minimal ruleset (single assertion with `yes` predicate)  
- ⚠️ Current version available **only in Spanish**

---

## 📦 Prerequisites

Make sure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)  
- [tkinter](https://wiki.python.org/moin/TkInter) (often included with Python)  
- [pyDatalog](https://sites.google.com/site/pydatalog/installation)  

---

## 🚀 Usage

Clone the repository and run the main file:

```bash
git clone https://github.com/your-username/oftalco.git
cd oftalco
python3 main.py
````

Follow the on-screen instructions and button prompts. The program is designed to be simple and intuitive.

---

## 📂 Project Structure

```
oftalco/
├── main.py       # Entry point
├── facts.py      # Knowledge database
├── gui.py        # GUI components (frames, buttons, labels, etc.)
└── README.md     # Project documentation
```

---

## 📚 How It Works

* The **facts** file defines the knowledge base of symptoms and diseases.
* The system applies logic using the `yes` predicate, which is capable of storing all necessary information.
* The GUI gathers user input (symptoms) and displays possible diagnoses.

---
## 👤👤👤 Authors

* **Juliana Pineda** 
* **Cristian Andres Arce**
* **Miguel Angel Henao** - *Main repo* - [OFTALCO](https://github.com/mhdelta/Oftalco)


