# Company-Voice-Assistant-Agent
<img width="447" height="896" alt="image" src="https://github.com/user-attachments/assets/730cc019-8a1a-4d06-87fc-bb75e394fbff" />

🤖 Enterprise Voice AI Agent
A high-performance, custom-trained Voice AI Agent designed to provide seamless customer interactions by leveraging proprietary company data and live website content.

📖 Overview
This project is an end-to-end solution for companies looking to automate client-facing communication. Unlike generic LLMs, this agent is context-aware, utilizing Retrieval-Augmented Generation (RAG) to pull information directly from your company’s website and internal datasets.

Key Capabilities
Contextual Intelligence: Trained on custom documentation and real-time website scraping.

Voice-First Interface: Optimized for low-latency voice interactions.

Full-Stack Deployment: Includes a Flask backend (app.py) and a responsive web frontend.

Data Processing: Includes specialized scripts for data cleaning and model fine-tuning (test.ipynb).


<img width="776" height="375" alt="image" src="https://github.com/user-attachments/assets/be28dfec-2d61-441c-9674-184949be7709" />


🚀 Getting Started
Prerequisites
Python 3.9 or higher

An API Key (e.g., OpenAI, Anthropic, or ElevenLabs for voice)

Installation
Clone the repository:

Bash
git clone https://github.com/Parvez-kabir/your-repo-name.git
cd your-repo-name
Set up a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory and add your credentials:

Code snippet
AI_API_KEY=your_api_key_here
VOICE_ID=your_elevenlabs_voice_id
Run the Application:

Bash
python app.py
Access the interface at http://127.0.0.1:5000.


🧠 Training & Customization
To update the agent's knowledge base:

Add your custom PDFs or Text files to a data/ folder (not pictured, but recommended).

Update the URL list in the scraping script to include your company website.

Run the test.ipynb notebook to re-index the vector database.

🛠️ Tech Stack
Backend: Flask (Python)

Frontend: HTML5, CSS3, JavaScript

AI Engine: LangChain / OpenAI GPT-4o

Data Processing: Pandas, BeautifulSoup4

Voice Synthesis: ElevenLabs / Google TTS

📝 License
Distributed under the MIT License. See LICENSE for more information.
