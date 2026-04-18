# 🤖 AI Assistant (Gemini Powered)

A simple AI assistant that takes a user’s question and returns a **concise, structured answer** using a Large Language Model (LLM).
This project focuses on clean output formatting using prompt engineering.

---

## 🚀 Features

* 💬 Accepts natural language questions
* ⚡ Uses **Google Gemini API** for generating responses
* 📌 Returns:

  * Exactly **3 bullet points**
  * Short and clear answers
  * Includes **one simple real-life example**
* 🖥️ Built with **Streamlit** for an interactive UI

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API (`google-genai`)
* python-dotenv

---

## 📂 Project Structure

```plaintext
ai-assistant-task/
│
├── app.py                # Main Streamlit app
├── find_names.py         # Script to fetch available model names
├── .env                  # API key (not pushed to GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions (Run Locally)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-assistant-task.git
cd ai-assistant-task
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

👉 Get API key from: https://aistudio.google.com/app/apikey

---

### 5. Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works (Flow Diagram)

```plaintext
        User Input (Question)
                 │
                 ▼
        Streamlit UI (app.py)
                 │
                 ▼
        Prompt Engineering Layer
   (3 bullets + short + example enforced)
                 │
                 ▼
        Gemini API (LLM)
                 │
                 ▼
        Generated Response
                 │
                 ▼
        Display on UI (Streamlit)
```

---

## 🧠 Approach

* Built a simple AI assistant using **Gemini LLM**
* Used **prompt engineering** to strictly control output:

  * 3 bullet points only
  * Each line short (10–12 words max)
  * Last point includes an example
* Streamlit handles user interaction and display
* `.env` ensures API key security

---

## 📌 Example

**Input:**

```
What is overfitting?
```

**Output:**

* Model memorizes training data instead of learning general patterns
* Performs well on training but poorly on unseen data
* Example: student memorizing answers but failing new questions

---

## 📦 Requirements

```txt
streamlit
google-genai
python-dotenv
```

---

## 👨‍💻 Author

**Shivam Mishra**

* Passionate about building AI-powered applications
* Interested in real-world problem solving using technology
* Currently working on projects involving AI, automation, and web apps

---

## 📌 Notes

* `.env` file is ignored via `.gitignore` for security
* `find_names.py` was used to fetch available Gemini models dynamically
* Designed to be **simple, fast, and assignment-ready**

---

## ⭐ Future Improvements

* Chat history support
* Better UI (chat-style interface)
* Multiple response formats (summary, detailed, etc.)

---

## Live Link

https://ai-assistant-task-assignmant-zcqdrjkgh3ehrlzg5q9cz2.streamlit.app/
