# Flask Crop Recommendation System

This project is a web application built using Flask that provides crop recommendations based on user-selected products and environmental conditions. The application allows users to select a crop from a predefined list and receive tailored recommendations regarding optimal farming practices.

## Project Structure

```
flask-app
├── static
│   └── style.css            # CSS styles for the web application
├── templates
│   └── index.html           # Main HTML template for user interaction
├── data
│   ├── crops.csv            # Data about different crops
│   └── crop_conditions.csv   # Environmental conditions for crops
├── app.py                   # Main Flask application
├── main.py                  # Core logic for crop predictions and recommendations
├── data_loader.py           # Handles loading and preprocessing of data
├── prediction_model.py       # Core prediction model for crop recommendations
├── recommendation_engine.py   # Generates detailed recommendations based on predictions
└── requirements.txt         # Lists project dependencies
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd flask-app
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the Flask application by running:
   ```
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Usage

- Navigate to the home page of the application.
- Select a crop from the dropdown menu.
- Click on "Öneri Al" to receive recommendations based on the selected crop.

## Files Overview

- **static/style.css**: Contains styles for the web application.
- **templates/index.html**: The main HTML template for user interaction.
- **data/crops.csv**: Contains crop data including optimal conditions.
- **data/crop_conditions.csv**: Contains environmental conditions for analysis.
- **app.py**: Sets up the Flask server and handles requests.
- **main.py**: Contains logic for predicting the best crops.
- **data_loader.py**: Loads and preprocesses data from CSV files.
- **prediction_model.py**: Core model for calculating crop scores.
- **recommendation_engine.py**: Generates detailed recommendations.
- **requirements.txt**: Lists the dependencies required for the project.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.