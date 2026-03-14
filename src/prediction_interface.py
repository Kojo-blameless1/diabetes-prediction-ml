# ============================================
# INTERACTIVE DIABETES PREDICTION
# SIMPLIFIED VERSION - NO SCALER REQUIRED
# ============================================

import joblib
import pandas as pd
import os
from pathlib import Path

print("="*70)
print("🩺 DIABETES RISK ASSESSMENT TOOL")
print("="*70)

# ============================================
# LET USER SPECIFY MODEL PATH
# ============================================

print("\n📂 MODEL SELECTION")
print("-" * 40)
print("Enter the path to your trained model file")
print("(Press Enter to use default location)")

# Default path - YOU CAN CHANGE THIS
model_path = Path(r"C:\Users\USER\Desktop\Machine Learning\diabetes-prediction-ml\model\decisionTree.joblib")

user_path = input(f"\nModel path [{model_path}]: ").strip()

# Use user input or default
if user_path:
    model_path = Path(user_path)
else:
    model_path = Path(model_path)

print(f"\n🔍 Looking for model at: {model_path}")

# Load the model
if os.path.exists(model_path):
    try:
        model = joblib.load(model_path)
        print("✅ Model loaded successfully!")
        print(f"   Model type: {type(model).__name__}")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        exit()
else:
    print(f"❌ Error: Could not find model at {model_path}")
    print("\nPlease check:")
    print("1. Is the path correct?")
    print("2. Does the file exist?")
    print("3. Try using the full absolute path")
    exit()

# ============================================
# NO SCALER - Using raw values directly
# ============================================

print("\n⚙️  Prediction engine ready (using raw values - no scaling)")

# Feature names in correct order
FEATURES = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

# ============================================
# USER INPUT FUNCTIONS
# ============================================

def get_user_input():
    """Collect all health information from user"""
    
    print("\n" + "="*60)
    print("📝 PATIENT HEALTH QUESTIONNAIRE")
    print("="*60)
    print("\nEnter your information (press Enter for average values):")
    
    patient = {}
    
    # 1. Pregnancies
    print("\n1️⃣  PREGNANCIES")
    print("   • Number of times pregnant")
    print("   • Enter 0 if male or never pregnant")
    while True:
        try:
            val = input("   Number of pregnancies [0]: ") or "0"
            patient['Pregnancies'] = int(val)
            if patient['Pregnancies'] >= 0:
                break
            print("   ❌ Please enter 0 or a positive number")
        except ValueError:
            print("   ❌ Please enter a valid number")
    
    # 2. Glucose
    print("\n2️⃣  GLUCOSE LEVEL")
    print("   • Plasma glucose concentration (mg/dL)")
    print("   • Normal: 70-99 | Prediabetes: 100-125 | Diabetes: 126+")
    while True:
        try:
            val = input("   Glucose level [120]: ") or "120"
            patient['Glucose'] = float(val)
            if patient['Glucose'] > 0:
                break
            print("   ❌ Glucose must be greater than 0")
        except ValueError:
            print("   ❌ Please enter a valid number")
    
    # 3. Blood Pressure
    print("\n3️⃣  BLOOD PRESSURE")
    print("   • Diastolic blood pressure (mm Hg)")
    print("   • Normal: Below 80")
    while True:
        try:
            val = input("   Blood pressure [70]: ") or "70"
            patient['BloodPressure'] = float(val)
            if patient['BloodPressure'] > 0:
                break
            print("   ❌ Blood pressure must be greater than 0")
        except ValueError:
            print("   ❌ Please enter a valid number")
    
    # 4. Skin Thickness
    print("\n4️⃣  SKIN THICKNESS")
    print("   • Triceps skin fold thickness (mm)")
    print("   • Indicator of body fat")
    while True:
        try:
            val = input("   Skin thickness [20]: ") or "20"
            patient['SkinThickness'] = float(val)
            if patient['SkinThickness'] >= 0:
                break
            print("   ❌ Please enter a valid number")
        except ValueError:
            print("   ❌ Please enter a valid number")
    
    # 5. Insulin
    print("\n5️⃣  INSULIN LEVEL")
    print("   • 2-Hour serum insulin (mu U/ml)")
    print("   • Normal: 16-166")
    while True:
        try:
            val = input("   Insulin level [80]: ") or "80"
            patient['Insulin'] = float(val)
            if patient['Insulin'] >= 0:
                break
            print("   ❌ Please enter a valid number")
        except ValueError:
            print("   ❌ Please enter a valid number")
    
    # 6. BMI
    print("\n6️⃣  BODY MASS INDEX (BMI)")
    print("   • Weight(kg) / height(m)²")
    print("   • Normal: 18.5-24.9 | Overweight: 25-29.9 | Obese: 30+")
    while True:
        try:
            val = input("   BMI [32]: ") or "32"
            patient['BMI'] = float(val)
            if patient['BMI'] > 0:
                break
            print("   ❌ BMI must be greater than 0")
        except ValueError:
            print("   ❌ Please enter a valid number")
    
    # 7. Diabetes Pedigree Function
    print("\n7️⃣  DIABETES PEDIGREE FUNCTION")
    print("   • Genetic risk score based on family history")
    print("   • 0.0-0.5 = Low genetic risk")
    print("   • 0.5-1.0 = Moderate genetic risk")
    print("   • 1.0+ = High genetic risk")
    while True:
        try:
            val = input("   Diabetes pedigree [0.5]: ") or "0.5"
            patient['DiabetesPedigreeFunction'] = float(val)
            if 0 <= patient['DiabetesPedigreeFunction'] <= 3:
                break
            print("   ❌ Please enter a value between 0 and 3")
        except ValueError:
            print("   ❌ Please enter a valid number")
    
    # 8. Age
    print("\n8️⃣  AGE")
    while True:
        try:
            val = input("   Age in years [40]: ") or "40"
            patient['Age'] = int(val)
            if patient['Age'] > 0:
                break
            print("   ❌ Age must be greater than 0")
        except ValueError:
            print("   ❌ Please enter a valid number")
    
    return patient

# ============================================
# PREDICTION FUNCTION (NO SCALING)
# ============================================

def predict_diabetes(patient_data):
    """Make prediction using raw values (no scaling)"""
    
    # Convert to DataFrame with correct feature order
    patient_df = pd.DataFrame([patient_data])[FEATURES]
    
    # Make prediction
    prediction = model.predict(patient_df)[0]
    
    # Get probability if available
    try:
        probabilities = model.predict_proba(patient_df)[0]
        has_proba = True
    except (AttributeError, NotImplementedError):
        probabilities = [0.5, 0.5]
        has_proba = False
    
    return prediction, probabilities, has_proba

# ============================================
# RESULTS DISPLAY
# ============================================

def display_results(patient_data, prediction, probabilities, has_proba):
    """Show prediction results"""
    
    print("\n" + "="*70)
    print("📊 YOUR HEALTH ASSESSMENT RESULTS")
    print("="*70)
    
    # Summary of inputs
    print("\n📋 Your Information Summary:")
    print("-" * 50)
    for key, value in patient_data.items():
        print(f"   {key:25}: {value}")
    
    # Risk assessment
    print("\n" + "="*50)
    print("🔍 RISK ASSESSMENT")
    print("="*50)
    
    if has_proba:
        risk_percentage = probabilities[1] * 100
        
        # Visual gauge
        gauge_bars = int(risk_percentage / 5)
        gauge = "█" * gauge_bars + "░" * (20 - gauge_bars)
        print(f"\n   Risk Level: [{gauge}] {risk_percentage:.1f}%")
        
        # Risk category
        if risk_percentage >= 70:
            print("\n   🟥 HIGH RISK")
            print("   • You show strong indicators of diabetes")
            print("   • Please consult a healthcare provider promptly")
        elif risk_percentage >= 50:
            print("\n   🟧 MODERATE RISK")
            print("   • You have several risk factors for diabetes")
            print("   • Further testing is recommended")
        elif risk_percentage >= 30:
            print("\n   🟨 LOW RISK")
            print("   • Your risk is relatively low")
            print("   • Maintain healthy lifestyle habits")
        else:
            print("\n   🟩 VERY LOW RISK")
            print("   • Your diabetes risk is minimal")
            print("   • Keep up your healthy habits")
        
        print(f"\n   📌 Model Prediction: ", end="")
        if prediction == 1:
            print("DIABETIC")
        else:
            print("NON-DIABETIC")
    
    # Key risk factors
    print("\n" + "="*50)
    print("⚠️  KEY RISK FACTORS TO MONITOR")
    print("="*50)
    
    risk_factors = []
    if patient_data['Glucose'] > 126:
        risk_factors.append(f"• High glucose ({patient_data['Glucose']} mg/dL) - Above diabetic threshold")
    elif patient_data['Glucose'] > 100:
        risk_factors.append(f"• Elevated glucose ({patient_data['Glucose']} mg/dL) - Prediabetic range")
    
    if patient_data['BMI'] > 30:
        risk_factors.append(f"• Obese BMI ({patient_data['BMI']:.1f}) - Major risk factor")
    elif patient_data['BMI'] > 25:
        risk_factors.append(f"• Overweight BMI ({patient_data['BMI']:.1f}) - Moderate risk factor")
    
    if patient_data['Age'] > 45:
        risk_factors.append(f"• Age ({patient_data['Age']} years) - Risk increases with age")
    
    if patient_data['BloodPressure'] > 80:
        risk_factors.append(f"• Elevated blood pressure ({patient_data['BloodPressure']})")
    
    if risk_factors:
        for factor in risk_factors:
            print(factor)
    else:
        print("• No major risk factors detected")
    
    # Recommendations
    print("\n" + "="*50)
    print("💡 RECOMMENDATIONS")
    print("="*50)
    
    if prediction == 1 or (has_proba and probabilities[1] > 0.5):
        print("• Schedule an appointment with your doctor")
        print("• Get a proper fasting blood glucose test")
        print("• Discuss lifestyle modifications")
    else:
        print("• Maintain regular health check-ups")
        print("• Exercise regularly (150 min/week)")
        print("• Eat a balanced diet low in sugar")
        print("• Monitor your weight")
    
    print("\n" + "="*50)
    print("⚠️  IMPORTANT DISCLAIMER")
    print("="*50)
    print("This is a screening tool only, not a medical diagnosis.")
    print("Always consult with a healthcare professional for proper evaluation.")

def display_risk_info():
    """Show educational information about risk factors"""
    print("\n" + "="*60)
    print("📚 UNDERSTANDING YOUR RISK FACTORS")
    print("="*60)
    print("""
GLUCOSE:
   • Normal: <100 mg/dL
   • Prediabetes: 100-125 mg/dL
   • Diabetes: ≥126 mg/dL

BMI:
   • Normal: 18.5-24.9
   • Overweight: 25-29.9
   • Obese: ≥30

BLOOD PRESSURE:
   • Normal: <80 mm Hg
   • Elevated: 80-89 mm Hg
   • High: ≥90 mm Hg

AGE:
   • Risk increases significantly after 45

FAMILY HISTORY:
   • Higher Diabetes Pedigree Function = higher genetic risk
    """)

# ============================================
# MAIN FUNCTION
# ============================================

def main():
    """Main interactive session"""
    
    while True:
        print("\n" + "="*70)
        print("🏥 DIABETES RISK PREDICTION TOOL")
        print("="*70)
        print("\n1. Start new assessment")
        print("2. View risk factor information")
        print("3. Exit")
        
        choice = input("\nSelect option (1-3): ").strip()
        
        if choice == '1':
            # Get user input
            patient = get_user_input()
            
            # Make prediction (no scaling needed)
            prediction, probabilities, has_proba = predict_diabetes(patient)
            
            # Show results
            display_results(patient, prediction, probabilities, has_proba)
            
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            display_risk_info()
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            print("\n👋 Thank you for using the Diabetes Risk Assessment Tool!")
            print("Stay healthy! 🌿")
            break
        else:
            print("❌ Invalid choice. Please enter 1-3.")

# ============================================
# START THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()