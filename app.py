from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from loan_processing_logic import LoanBusinessLogicController
from datetime import datetime

app = Flask(__name__)
CORS(app)

loan_controller = LoanBusinessLogicController()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_loan', methods=['POST'])
def process_loan():
    try:
        data = request.json
        
        # Convert date string to datetime object
        dob = datetime.strptime(data['dob'], '%Y-%m-%d').date()
        
        loan_application = {
            'name': data['name'],
            'gender': data['gender'],
            'dob': dob,
            'monthly_income': data['income'] / 12,  # Convert annual to monthly
            'requested_loan_amount': data['loanAmount'],
            'loan_tenure': 240  # Default 20 years (240 months)
        }
        
        result = loan_controller.process_loan_application(loan_application)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'approval_status': False,
            'message': f'Error processing application: {str(e)}',
            'emi': 0
        }), 400

if __name__ == '__main__':
    app.run(debug=True)