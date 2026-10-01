# ✨ AI Creative Studio

AI Creative Studio is a modern Streamlit web application that helps users turn simple ideas into creative, ready-to-edit content.

## Features

- ✍️ AI Writer
- 💡 Idea Generator
- 🏷️ Brand Creator
- 📱 Social Media Content
- 🎬 Video Prompt Creator
- 🎨 Design Prompt Creator
- 📚 Study Creator
- 💼 Business Creator
- 🎨 Modern responsive Streamlit interface
- ⬇️ Download generated results as TXT

## Technology

- Python
- Streamlit
- OpenAI API
- GitHub

## Project Files

```text
AI-Creative-Studio/
│
├── app.py
├── requirements.txt
└── README.md
```

## Run Locally

1. Clone or download the repository.

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Create a Streamlit secrets file:

```text
.streamlit/secrets.toml
```

Add:

```toml
OPENAI_API_KEY = "your-api-key-here"
```

Never commit this file or your API key to GitHub.

4. Start the application:

```bash
streamlit run app.py
```

The app will open in your browser.

## Deploy on Streamlit Community Cloud

1. Push `app.py`, `requirements.txt`, and `README.md` to GitHub.
2. Create a new app on Streamlit Community Cloud.
3. Select your GitHub repository and `app.py`.
4. Add the following secret in the app's Secrets settings:

```toml
OPENAI_API_KEY = "your-api-key-here"
```

5. Deploy the app.

## Security

API keys must not be placed directly in Python code or committed to GitHub. Use Streamlit Secrets for local and cloud deployment.

## Future Improvements

Possible future versions can add:

- User accounts
- Creation history
- Favorite creations
- Multiple AI models
- Image generation
- Export to PDF
- Social-media templates
- Brand-kit generation
- Theme customization
- Database storage

## License

This project can be used as a student project and extended for personal or educational purposes.
