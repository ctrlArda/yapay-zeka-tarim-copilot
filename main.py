from typing import List
import pandas as pd
from data_loader import EnvironmentalData, CropData, load_environmental_data, load_crop_data
from prediction_model import CropPredictionModel
from recommendation_engine import RecommendationEngine
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def load_crop_data(filepath: str) -> List[CropData]:
    crops = []
    df = pd.read_csv(filepath)
    for _, row in df.iterrows():
        crops.append(CropData(
            name=row['name'],
            optimal_temp=row['optimal_temp'],
            optimal_humidity=row['optimal_humidity'],
            water_needs=row['water_needs'],
            optimal_ph=row['optimal_ph'],
            pest_resistance=row['pest_resistance']
        ))
    return crops

def load_environmental_data(filepath: str) -> EnvironmentalData:
    df = pd.read_csv(filepath)
    return EnvironmentalData(
        temperature=df['temperature'].mean(),
        humidity=df['humidity'].mean(),
        rainfall=df['rainfall'].mean(),
        soil_ph=df['soil_ph'].mean(),
        soil_moisture=df['soil_moisture'].mean(),
        pest_risk=df['pest_risk'].mean()
    )

def generate_pdf(recommendations, filename="tarim_raporu.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.drawString(100, height - 100, "Tarım Raporu")
    c.drawString(100, height - 120, "Önerilen Ürünler:")

    y = height - 140
    for recommendation in recommendations:
        c.drawString(100, y, f"{recommendation[0]}: {recommendation[1]:.2f}")
        y -= 20

    c.save()

def main():
    # Dosya yollarını tam olarak belirtiyoruz
    crop_data_filepath = 'c:/Users/safa/Desktop/bolt.new/flask-app/data/crops.csv'
    environmental_data_filepath = 'c:/Users/safa/Desktop/bolt.new/flask-app/data/crop_conditions.csv'

    # Verileri yüklüyoruz
    crop_data = load_crop_data(crop_data_filepath)
    environmental_data = load_environmental_data(environmental_data_filepath)

    # Modeli oluşturuyoruz ve en iyi ürünleri tahmin ediyoruz
    model = CropPredictionModel(crop_data)
    recommendations = model.predict_best_crops(environmental_data)

    # Önerileri PDF dosyasına yazdırıyoruz
    generate_pdf(recommendations)

if __name__ == "__main__":
    main()