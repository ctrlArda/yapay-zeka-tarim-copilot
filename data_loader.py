from typing import List
from dataclasses import dataclass
import csv

@dataclass
class EnvironmentalData:
    temperature: float
    humidity: float
    rainfall: float
    soil_ph: float
    soil_moisture: float
    pest_risk: float

@dataclass
class CropData:
    name: str
    optimal_temp: float
    optimal_humidity: float
    water_needs: float
    optimal_ph: float
    pest_resistance: float

def load_environmental_data(filepath: str) -> EnvironmentalData:
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        data = next(reader)
        return EnvironmentalData(
            temperature=float(data['temperature']),
            humidity=float(data['humidity']),
            rainfall=float(data['rainfall']),
            soil_ph=float(data['soil_ph']),
            soil_moisture=float(data['soil_moisture']),
            pest_risk=float(data['pest_risk'])
        )

def load_crop_data(filepath: str) -> List[CropData]:
    crops = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            crops.append(CropData(
                name=row['name'],
                optimal_temp=float(row['optimal_temp']),
                optimal_humidity=float(row['optimal_humidity']),
                water_needs=float(row['water_needs']),
                optimal_ph=float(row['optimal_ph']),
                pest_resistance=float(row['pest_resistance'])
            ))
    return crops