# 🚀 Python Beginners Project – Tutorial 2

Welcome to **Python Beginners Project**! 🎉  
This tutorial teaches you **reading and writing files** in Python.

---

## 📂 Project Structure

```
python-beginners/
├── .github/
│   └── workflows/
│       └── python-app.yml   # GitHub Actions workflow
├── simple_example.py        # Tutorial 1: Basics
├── file_example.py          # Tutorial 2: Files
└── README.md                # Instructions
```

---

## ▶️ How to Run Locally

1. Make sure you have **Python 3.10+** installed.  
2. Navigate to the project folder in terminal:

```bash
cd path/to/python-beginners
```
3. Run the file example script:

```bash
python file_example.py
```

4. Check the newly created `greetings.txt` in the folder.  
5. Observe the output printed in the terminal.

---

## 📖 What You’ll Learn

- Creating a new text file  
- Writing lines to a file (`w`)  
- Appending lines to a file (`a`)  
- Reading the file content (`r`)  
- Counting lines and basic text manipulation  

---

## 🤖 GitHub Actions CI/CD

The workflow automatically runs `simple_example.py` on every push to main.  
You can extend it to run `file_example.py` as well (already added below).

---

### **GitHub Actions workflow** (`python-app.yml`)  

```yaml
name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    - name: Run simple_example.py
      run: python simple_example.py <<< "World"

    - name: Run file_example.py
      run: python file_example.py
```

Happy learning Python! ❤️
