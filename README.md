#### Machine-Downtime-Prediction

This project aims to predict machine downtime using a Logistic Regression model trained on manufacturing data. The application provides RESTful endpoints to upload data, train the model, and make predictions. It also offers insights into downtime probabilities, enabling businesses to reduce unexpected downtime and optimize production.

### Features 
- Upload Dataset: Upload CSV files containing manufacturing data (Machine_ID, Temperature, Run_Time) for training the model.
- Train Model: Train the Logistic Regression model on uploaded data.
- Predict Downtime: Predict machine downtime using JSON input (Temperature, Run_Time) and return predictions in JSON format.
- Confidence Scores: Each prediction includes a confidence score to assist with decision-making.

### API Endpoints
1.Root Endpoint
- URL: /
- Method: GET
- Description: Welcome message for the API.
  
2.Upload Endpoint
- URL: /upload
- Method: POST
- Description: Upload a CSV file containing manufacturing data.
- Input: CSV file (e.g., Machine_ID, Temperature, Run_Time).

3. Train Endpoint
- URL: /train
- Method: POST
- Description: Train the model on the uploaded dataset.

4. Predict Endpoint
- URL: /predict
- Method: POST
- Description: Predict downtime based on input data.

#### Technologies Used
Programming Language: Python
Libraries: FastAPI (RESTful API), Scikit-learn (Logistic Regression model), Pandas, NumPy (Data processing), Pickle (Model persistence)
Tools: Git, VS Code

#### Installation & Setup
1. Clone the Repository :
   git clone https://github.com/your_username/Machine-Downtime-Prediction.git
   cd Machine-Downtime-Prediction
2. Create a Virtual Environment :
   python -m venv venv
   source venv/bin/activate
3. Install Dependencies : pip install -r requirements.txt
4. Start the FastAPI Application : uvicorn api:app --reload

#### Interactive Testing with Swagger UI
1. Start the server: uvicorn api:app --reload.
2. Visit http://127.0.0.1:8000/docs.
3. Use the /upload endpoint to upload training data:
   - Click "Try it out".
   - Upload a .csv file and hit "Execute".
4. Use the /predict endpoint to test predictions:
   - Click "Try it out".
   - Enter the required input fields (Temperature and Run_Time) in JSON format.
   - Click "Execute" to see the prediction results.

 
