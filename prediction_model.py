from typing import List, Tuple, Dict
from data_loader import EnvironmentalData, CropData

class CropPredictionModel:
    def __init__(self, crop_data: List[CropData]):
        self.crop_data = crop_data
        self.weights = {
            'temperature': 0.25,
            'humidity': 0.2,
            'water': 0.2,
            'ph': 0.2,
            'pest': 0.15
        }

    def calculate_crop_score(self, env: EnvironmentalData, crop: CropData) -> Tuple[float, Dict[str, str]]:
        """Calculate compatibility score between environment and crop."""
        temp_score = 1 - abs(env.temperature - crop.optimal_temp) / 50
        humidity_score = 1 - abs(env.humidity - crop.optimal_humidity) / 100
        water_score = 1 - abs(env.rainfall - crop.water_needs) / 1000
        ph_score = 1 - abs(env.soil_ph - crop.optimal_ph) / 14
        pest_score = (crop.pest_resistance / 10) * (1 - env.pest_risk / 10)

        score = (
            self.weights['temperature'] * temp_score +
            self.weights['humidity'] * humidity_score +
            self.weights['water'] * water_score +
            self.weights['ph'] * ph_score +
            self.weights['pest'] * pest_score
        )

        reasons = {
            'Temperature': f"Score: {temp_score:.2f}",
            'Humidity': f"Score: {humidity_score:.2f}",
            'Water Needs': f"Score: {water_score:.2f}",
            'pH': f"Score: {ph_score:.2f}",
            'Pest Resistance': f"Score: {pest_score:.2f}"
        }

        return score, reasons

    def predict_best_crops(self, env: EnvironmentalData, top_n: int = 3) -> List[Tuple[str, float, Dict[str, str]]]:
        """Predict the best crops for given environmental conditions."""
        scores = []
        for crop in self.crop_data:
            score, reasons = self.calculate_crop_score(env, crop)
            scores.append((crop.name, score, reasons))
        
        return sorted(scores, key=lambda x: x[1], reverse=True)[:top_n]