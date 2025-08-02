# AURORA - AI-powered Unified Review and Organization for Resourceful Academics

AURORA is a cutting-edge academic platform built using AI and NLP to revolutionize personalized learning and student productivity. It features resume analysis, note summarization, topic-specific chatbots, gamification modules, and AI-driven recommendations.

## 🚀 Key Features

- ✨ **Personalized Note-Making** – Organize, summarize, and download notes as PDFs.
- 💬 **AI Chatbot Assistants** – Get contextual academic help using Gemini-powered AI.
- 📄 **Resume Analyzer** – Extracts key fields and evaluates GenAI/ML exposure.
- 🧠 **AI Notes & Summarization** – Generates summaries, flashcards, and concept maps.
- 🎮 **Interactive Learning** – Quizzes, gamification, simulations, and case studies.
- 📚 **Career & Skill Development** – AI-guided internship/job matching and micro-certifications.
- 🔗 **External Integrations** – Connect with LMS tools (Moodle, Canvas), Google Drive, and Notion.
- ♿ **Accessibility & Inclusivity** – Multi-language support and voice recognition features.
- 🔬 **AI Research Tools** – Advanced research and resource curation capabilities.

## Project Structure

```
AURORA/
├── main.py                          # Main application entry point
├── requirements.txt                 # Python dependencies
├── README.md                       # Project documentation
├── env_example.txt                 # Environment variables template
├── config/
│   └── settings.py                 # Configuration and settings
├── utils/
│   ├── ai_helpers.py              # AI utility functions
│   └── file_handlers.py           # File processing utilities
├── modules/
│   ├── resume_analyzer.py         # Resume analysis module
│   ├── ai_notes.py                # AI notes and summarization
│   ├── interactive_learning.py    # Interactive learning features
│   ├── community_features.py      # Community and collaboration tools
│   ├── research_tools.py          # AI research capabilities
│   ├── accessibility.py           # Accessibility features
│   ├── external_integrations.py   # LMS and app integrations
│   ├── career_development.py      # Career development tools
│   └── personalization.py         # AI personalization features
├── output/                         # Generated files (PDFs, Excel)
└── temp/                          # Temporary files
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/PreethamNoelP/AURORA.git
   cd AURORA
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Copy `env_example.txt` to `.env` and add your API key:
   ```bash
   cp env_example.txt .env
   # Edit .env file and add your Gemini API key
   ```

4. **Download spaCy model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

### Configuration

1. **API Keys**: Add your Gemini API key to the `.env` file
2. **File Paths**: Update paths in `config/settings.py` if needed
3. **Email Configuration**: Configure email settings in `config/settings.py`

## Running the Application

```bash
streamlit run main.py
```

The application will be available at `http://localhost:8501`

## Usage

### Getting Started
1. Navigate to the application in your browser
2. Use the sidebar to select different features
3. Follow the on-screen instructions for each module

### Key Features

#### Resume Builder
- Upload PDF or DOCX resumes
- Get AI-powered analysis and insights
- Download results as Excel files

#### AI Notes
- Create and organize notes
- Generate AI-powered summaries
- Create flashcards and concept maps
- Download notes as PDF

#### Interactive Learning
- Participate in gamified learning
- Take quizzes and assessments
- Run virtual lab simulations
- Engage with case studies

#### Community Features
- Join discussion forums
- Collaborate on group projects
- Attend live expert Q&A sessions
- Generate email links for communication

## Configuration

### Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key
- `EMAIL_CONFIG`: Email server configuration (optional)

### Customization
- Modify `config/settings.py` to change default settings
- Update course recommendations in the settings file
- Customize quiz questions and learning paths

## Dependencies

### Core Dependencies
- `streamlit`: Web application framework
- `google-generativeai`: Gemini AI integration
- `pandas`: Data manipulation
- `spacy`: Natural language processing
- `textblob`: Sentiment analysis

### File Processing
- `pdfminer.six`: PDF text extraction
- `python-docx`: DOCX file processing
- `openpyxl`: Excel file handling
- `fpdf`: PDF generation

### AI and ML
- `speech_recognition`: Voice recognition
- `deep-translator`: Multi-language translation
- `plotly`: Data visualization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the repository
- Check the documentation in each module
- Review the configuration settings

## Future Enhancements

- [ ] Advanced analytics dashboard
- [ ] Real-time collaboration features
- [ ] Mobile app development
- [ ] Integration with more LMS platforms
- [ ] Advanced AI model support
- [ ] Multi-language interface
- [ ] Offline mode support

## 📊 Performance Notes

- Large file uploads may take time to process
- AI responses depend on API availability
- Voice recognition requires microphone access
- PDF generation works best with smaller documents

## 🔒 Security

- API keys are stored in environment variables
- Temporary files are automatically cleaned up
- User data is processed locally when possible
- Secure file handling for uploaded documents
