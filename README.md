# VentureDecision-AI-powered-startup-investment-decision-support-System-
VentureDecision is an AI-powered startup investment decision-support platform that analyzes Indian startups across financial, operational, growth, market, and competitive factors. It uses Python, Machine Learning (Logistic Regression, Random Forest, XGBoost), FastAPI, React, Vite, Tailwind CSS, Recharts, Axios, and Ollama (Qwen2.5:3B) to generate investment predictions, startup intelligence metrics such as Valuation Growth, Follow-on Funding, Market Leadership, and Competitive Survival, scenario analysis, and AI-powered services including VC Copilot, Natural Language Q&A, Due Diligence, and Investment Memo generation.

Technologies Used
Machine Learning & Data Science
Python
Pandas
NumPy
Scikit-learn
XGBoost
Random Forest
Logistic Regression
Backend
FastAPI
Uvicorn
Pydantic
Python REST APIs
Frontend
React
Vite
Tailwind CSS
Recharts
Axios
React Router
React Icons
Generative AI
Ollama
Qwen2.5:3B
Data
CSV-based training dataset
CSV-based inference dataset
📊 Machine Learning

The system compares multiple classification models:

Logistic Regression
Random Forest
XGBoost

Models are evaluated using:

Accuracy
Precision
Recall
F1 Score
Weighted Precision
Weighted Recall
Weighted F1 Score

Representative evaluation results achieved up to 95% accuracy and 88.9% F1 score for binary classification tasks.

🏗️ System Architecture
Startup Data
     ↓
CSV Training / Inference Data
     ↓
EDA & Data Preprocessing
     ↓
Feature Engineering
     ↓
ML Models
     ↓
Predictions & Probabilities
     ↓
Startup Intelligence Engine
     ↓
FastAPI Backend
     ↓
React Dashboard
     ↓
Ollama / Qwen2.5:3B
     ↓
AI Insights & Reports
📋 Requirements
Software Requirements
Python 3.10+
Node.js 18+
npm
Git
Ollama
Modern web browser
Python Dependencies

Create a Python environment and install:

pip install -r requirements.txt

The backend requires packages such as:

fastapi
uvicorn
pandas
numpy
scikit-learn
xgboost
requests
pydantic
python-dotenv
Frontend Dependencies

Inside the dashboard directory:

npm install

The frontend uses packages including:

react
react-dom
react-router-dom
axios
recharts
react-icons
tailwindcss
vite
🤖 Ollama Setup

Install Ollama and download the required model:

ollama pull qwen2.5:3b

Start Ollama:

ollama serve

The application communicates with Ollama through its local API.

▶️ Running the Backend

From the VentureDecision project directory:

python -m uvicorn api.main:app --reload

The FastAPI backend will run locally.

API documentation can be accessed through the FastAPI Swagger interface.

▶️ Running the Dashboard

Navigate to the dashboard:

cd venturedecision-dashboard

Install dependencies:

npm install

Start the development server:

npm run dev

⚠️ Limitations

VentureDecision is a prototype decision-support system. The current dataset is relatively small and startup information can be difficult to obtain consistently. The predictions should therefore support, rather than replace, professional investment analysis and due diligence.

🔮 Future Improvements
Larger and continuously updated startup datasets
Database integration
Automated data collection through reliable APIs
Model retraining pipelines
Cross-validation and external model validation
Cloud deployment
Advanced investor matching and portfolio analytics
👨‍💻 Project

VentureDecision — AI-Powered Startup Investment Decision Support System

Open the local URL shown by Vite in your browser.

