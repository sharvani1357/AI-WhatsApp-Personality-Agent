# 🤖 AI WhatsApp Personality Agent

A futuristic AI-powered WhatsApp automation system that allows users to create and deploy dynamic AI texting personalities in real time.

This project combines:
- 📱 WhatsApp automation
- 🧠 AI-generated replies
- 🎭 Dynamic personality customization
- ⚡ Groq AI integration
- 🤖 Ollama fallback support
- 🎨 Futuristic Streamlit frontend

---

# 🚀 Features

## ✨ Dynamic AI Personality System

Create fully customizable AI personalities using:
- Personality descriptions
- Tone selection
- Humor control
- Energy level
- Creativity level
- Emoji usage

The AI dynamically changes its texting behavior based on the selected personality.

---

# 📱 WhatsApp Automation

Built using:
- whatsapp-web.js
- Puppeteer
- LocalAuth session management

The bot:
- Automatically listens to incoming messages
- Sends AI-generated replies
- Works like a real WhatsApp chatting assistant

---

# 🧠 AI Reply System

## ⚡ Groq API
Primary AI provider for fast responses.

## 🤖 Ollama
Local fallback AI model if Groq fails.

The system automatically switches between providers.

---

# 💡 Project Idea

Initially, this project started as a simple rule-based reply system using predefined keyword-based responses.

Later, it was upgraded into an AI-powered personalized messaging system where reply behavior dynamically changes according to custom prompts and personalities created by the user.

The main goal of this project was:
- exploring personality-based AI conversations
- understanding prompt engineering
- learning conversational behavior customization
- experimenting with AI agents and automation workflows
- creating more engaging and human-like AI texting experiences

---

# 🎭 Personality Examples

Users can create personalities like:

## 😂 Chaos Meme Friend
Funny Gen Z texting personality with memes, sarcasm, casual slang, and chaotic energy.

## 😎 Smooth Confident Texter
Cool, confident, stylish texting behavior with smooth replies.

## 🌙 Comfort Friend
Emotionally supportive personality with calm and caring conversations.

The AI dynamically changes its texting style according to the selected personality prompt.

---

# ⚠️ Important Limitation

This project does NOT truly know real-world information such as:
- What someone is doing right now
- Live activities
- Real-world awareness
- Actual current events around the user

Instead, it generates human-like conversational replies based on:
- prompts
- personality behavior
- conversation context
- AI-generated conversational flow

So the project focuses more on:
- 🧠 conversational behavior simulation
- 🎭 personality-based texting
- 💬 realistic conversational experiences

rather than factual real-world awareness.

---

# 🏗️ Project Structure

```text
AI-WhatsApp-Personality-Agent/
│
├── backend/
│   ├── index.js
│   ├── prompt.json
│   ├── default_prompt.json
│   ├── package.json
│   ├── package-lock.json
│   ├── .env
│   └── qr.png
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

# ⚙️ Technologies Used

## Backend
- Node.js
- whatsapp-web.js
- Puppeteer
- Axios
- dotenv
- qrcode-terminal
- qrcode

## Frontend
- Python
- Streamlit
- Custom CSS
- Glassmorphism UI

## AI
- Groq API
- Ollama
- Llama Models

---

# 🔥 How It Works

## Step 1
Run the frontend:

```bash
python -m streamlit run app.py
```

---

## Step 2
Frontend automatically starts backend.

---

## Step 3
QR code generates in terminal.

---

## Step 4
Scan QR using WhatsApp.

---

## Step 5
Bot starts replying automatically.

---

# 🧠 Dynamic Prompt System

The frontend updates:

```text
prompt.json
```

The backend dynamically reads the latest prompt before every AI response.

This allows:
- Instant personality updates
- Real-time AI behavior changes
- No backend restart required

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sharvani1357/AI-WhatsApp-Personality-Agent.git
```

---

## 2️⃣ Backend Setup

```bash
cd backend
npm install
```

---

## 3️⃣ Frontend Setup

```bash
cd frontend
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file inside backend folder:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Running The Project

## Run Frontend

```bash
cd frontend
python -m streamlit run app.py
```

The backend starts automatically.

---

# 🗑️ Reset WhatsApp Session

The frontend includes a:

```text
Reset WhatsApp Session
```

button which:
- Clears WhatsApp auth session
- Removes cached login
- Generates a new QR code

Useful when changing phones/accounts.

---

# 🎨 Frontend UI

Features:
- Futuristic glassmorphism design
- Neon gradients
- AI personality customization dashboard
- Smooth modern UI
- Cyberpunk-inspired visuals

---

# 🎥 Demo Video

Watch the full project demo here:

https://www.linkedin.com/posts/sharvani-karnati-90614b318_ai-python-nodejs-activity-7463496116903391232-t4i9?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFB3n1YBCJWNLwSLSWg9wnoAxHECqh50HkA

---

# 🌟 Future Improvements

Although the project works successfully, there are still many areas that can be improved further such as:

- Better memory/context handling
- More advanced conversational intelligence
- Cloud deployment
- Multi-user scalability
- Voice interaction support
- Improved long-term conversational flow
- AI memory systems
- Advanced agent workflows

---

# 🔥 Biggest Challenges Faced

- Managing WhatsApp sessions
- Dynamic prompt updates without restarting backend
- Puppeteer & QR authentication handling
- Integrating AI response systems
- Stable frontend-backend communication

---

# 🛡️ Disclaimer

This project is for educational and personal automation purposes only.

Please follow WhatsApp policies and use responsibly.

---

# 👩‍💻 Author

Developed by Karnati Sharvani.

---

# 🔗 GitHub Repository

https://github.com/sharvani1357/AI-WhatsApp-Personality-Agent

---

# ⭐ Support

If you like this project:
- Star the repository
- Share with others
- Contribute improvements

---

# 🚀 Final Result

An AI-powered WhatsApp personality automation platform capable of dynamically changing conversation styles in real time while providing a modern and futuristic AI customization experience.