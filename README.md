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

# 🎭 Personality Examples

## 😂 Chaotic Meme Friend
Funny internet-style texting personality.

## 😎 Smooth Confident Friend
Cool, confident, stylish replies.

## 🌙 Comfort Friend
Emotionally supportive personality.

## 💀 Dry Humor Friend
Sarcastic and witty texting style.

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-WhatsApp-Personality-Agent.git
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

# 📸 Screenshots

Add screenshots here:

```text
Frontend screenshots
QR generation screenshots
Personality customization screenshots
```

---

# 🌟 Future Improvements

- 🎤 Voice reply support
- 👥 Multi-user support
- 📊 Chat analytics dashboard
- 🧠 Long-term conversation memory
- ☁️ Cloud deployment
- 📱 Mobile app integration
- 🤖 Custom AI avatars
- 🧬 Fine-tuned personality models

---

# 🛡️ Disclaimer

This project is for educational and personal automation purposes only.

Please follow WhatsApp policies and use responsibly.

---

# 👩‍💻 Author

Developed by Karnati Sharvani.

---

# ⭐ Support

If you like this project:
- Star the repository
- Share with others
- Contribute improvements

---

# 🚀 Final Result

An AI-powered WhatsApp personality automation platform capable of dynamically changing conversation styles in real time while providing a modern and futuristic AI customization experience.