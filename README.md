<<<<<<< HEAD
1      Backend Setup (Python + FastAPI)

Navigate to backend folder:

cd email-reply-assistant/backend


Create a virtual environment (optional but recommended):

python -m venv venv


Activate the virtual environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install required dependencies:

pip install fastapi uvicorn transformers torch


Optional (for Gmail integration):

pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib


Run the backend server:

uvicorn main:app --reload --host 0.0.0.0 --port 8000


Backend will be running at: http://localhost:8000

API endpoint: POST /generate_reply

2️   Frontend Setup (React)

Navigate to frontend folder:

cd ../frontend


Install dependencies:

npm install


Run the React app:

npm start


Frontend will open automatically at: http://localhost:3000

React communicates with backend at: http://localhost:8000
=======
# AI-Email-Reply-Assistant
>>>>>>> 167282e6ed0b2d2be6a69ce464c20a62d6bdaea2
