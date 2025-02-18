import unittest
import pandas as pd
from sea_level_predictor import predict_sea_level

class TestSeaLevelPredictor(unittest.TestCase):

    def test_data_loading(self):
        df = pd.read_csv('epa-sea-level.csv')
        # Vérifiez que le DataFrame contient bien les colonnes nécessaires
        self.assertIn('Year', df.columns)
        self.assertIn('CSIRO Adjusted Sea Level', df.columns)

    def test_predict_sea_level(self):
        # Vous pouvez tester la fonction de prédiction si elle ne génère pas d'erreur
        try:
            predict_sea_level()
        except Exception as e:
            self.fail(f"Prediction failed with error: {e}")

if __name__ == '__main__':
    unittest.main()
