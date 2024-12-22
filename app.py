from flask import Flask, request, jsonify, render_template
from data_loader import load_crop_data, load_environmental_data
from prediction_model import CropPredictionModel

app = Flask(__name__)

# Load data
crop_data = load_crop_data('c:/Users/safa/Desktop/bolt.new/flask-app/data/crops.csv')
model = CropPredictionModel(crop_data)

@app.route("/")
def index():
    products = [crop.name for crop in crop_data]
    return render_template("index.html", products=products)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    selected_product = data.get("product")
    
    # Simulate environmental data for demonstration
    environmental_data = EnvironmentalData(
        temperature=25.0,
        humidity=60.0,
        rainfall=200.0,
        soil_ph=6.5,
        soil_moisture=30.0,
        pest_risk=2.0
    )
    
    recommendations = model.predict_best_crops(environmental_data)
    
    if selected_product:
        return jsonify({"recommendations": recommendations})
    return jsonify({"error": "Ürün seçimi yapılmadı."}), 400

if __name__ == "__main__":
    app.run(debug=True)