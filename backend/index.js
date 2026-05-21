require('dotenv').config();

const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcodeTerminal = require('qrcode-terminal');
const qrcode = require('qrcode');
const axios = require('axios');
const fs = require('fs');
const GROQ_API_KEY = process.env.GROQ_API_KEY;

function getPrompt() {

    const promptData = JSON.parse(
        fs.readFileSync('./prompt.json', 'utf8')
    );

    return promptData.prompt;
}

const client = new Client({
    authStrategy: new LocalAuth()
});

client.on('qr', async (qr) => {

    qrcodeTerminal.generate(qr, {
        small: true
    });

    console.log('📱 Scan the QR code above!');

    await qrcode.toFile(
        './qr.png',
        qr
    );

    console.log('✅ QR saved as qr.png');
});

client.on('ready', () => {
    console.log('✅ Personalized AI WhatsApp Agent is Ready!');
    console.log('✅ Listening for messages from OTHER numbers...');
    console.log('📱 Bot number:', client.info.wid.user);
});

client.on('auth_failure', (msg) => {
    console.log('❌ Auth failed:', msg);
});

client.on('disconnected', (reason) => {
    console.log('❌ Disconnected:', reason);
});

async function tryGroq(userMessage) {

    try {

        console.log('⚡ Trying Groq...');

        const response = await axios.post(
            'https://api.groq.com/openai/v1/chat/completions',
            {
                model: 'llama-3.1-8b-instant',
                messages: [
                    {
                        role: 'system',
                        content: getPrompt()
                    },
                    {
                        role: 'user',
                        content: userMessage
                    }
                ],
                max_tokens: 80,
                temperature: 0.8
            },
            {
                headers: {
                    'Authorization': `Bearer ${GROQ_API_KEY}`,
                    'Content-Type': 'application/json'
                },
                timeout: 10000
            }
        );

        const text =
            response.data.choices?.[0]?.message?.content?.trim();

        if (text) {

            console.log('✅ Groq replied:', text);

            return text;

        }

    } catch (error) {

        console.log(
            '❌ Groq failed:',
            error.response?.data || error.message
        );

        return null;

    }
}

async function tryOllama(userMessage) {

    try {

        console.log('🤖 Trying Ollama...');

        const response = await axios.post(
            'http://localhost:11434/api/chat',
            {
                model: 'llama3.2',
                messages: [
                    {
                        role: 'system',
                        content: getPrompt()
                    },
                    {
                        role: 'user',
                        content: userMessage
                    }
                ],
                stream: false
            },
            {
                timeout: 30000
            }
        );

        const text =
            response.data.message?.content?.trim();

        if (text) {

            console.log('✅ Ollama replied:', text);

            return text;

        }

    } catch (error) {

        console.log(
            '❌ Ollama failed:',
            error.message
        );

        return null;

    }
}

async function getAIReply(userMessage) {

    const groqReply =
        await tryGroq(userMessage);

    if (groqReply)
        return groqReply;

    const ollamaReply =
        await tryOllama(userMessage);

    if (ollamaReply)
        return ollamaReply;

    return "bro oka sec 😅";
}

client.on('message', async (message) => {

    console.log('\n==================================');

    console.log('From:', message.from);

    console.log('Body:', message.body);

    console.log('==================================\n');

    if (message.from === 'status@broadcast')
        return;

    if (!message.body || message.body.trim() === '')
        return;

    console.log(`📩 Processing: ${message.body}`);

    try {

        const reply =
            await getAIReply(message.body);

        await client.sendMessage(
            message.from,
            reply
        );

        console.log(`📤 Sent: ${reply}`);

    } catch (error) {

        console.log(
            '❌ Send failed:',
            error.message
        );

    }

});

client.initialize();