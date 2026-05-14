# Flask Notes App with Jenkins CI/CD

Simple Flask Notes Application integrated with Jenkins Pipeline.

---

# Features

- Add notes
- Delete notes
- Flask backend
- Pytest unit testing
- Jenkins CI/CD Pipeline

---

# Technologies

- Python
- Flask
- Pytest
- Jenkins
- GitHub

---

# Pipeline Stages

1. Checkout
2. Build
3. Test
4. Deploy

---

# Run Locally

## Create Virtual Environment

```bash
python3 -m venv venv
```

## Activate Environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

## Install Requirements

```bash
pip install -r app/requirements.txt
```

## Run App

```bash
python app/app.py
```

---

# Run Tests

```bash
pytest tests/
```

---

# Jenkins Setup

1. Install Jenkins
2. Create Pipeline Job
3. Connect GitHub Repository
4. Add Jenkinsfile
5. Build Pipeline

---

# App URL

```text
http://localhost:5000
```