import unittest
import sea_level_predictor
import matplotlib.pyplot as plt

class TestSeaLevelPredictor(unittest.TestCase):
    def setUp(self):
        """Setup: Jalankan fungsi sebelum pengujian."""
        self.ax = sea_level_predictor.draw_plot()

    def test_labels(self):
        """Test apakah label sumbu dan judul sudah benar."""
        self.assertEqual(self.ax.get_xlabel(), "Year")
        self.assertEqual(self.ax.get_ylabel(), "Sea Level (inches)")
        self.assertEqual(self.ax.get_title(), "Rise in Sea Level")

    def test_lines(self):
        """Test apakah ada dua garis regresi yang dibuat."""
        lines = self.ax.get_lines()
        self.assertEqual(len(lines), 2)  # Harus ada dua garis regresi

if __name__ == "__main__":
    unittest.main()
