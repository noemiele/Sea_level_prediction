# This entrypoint file to be used in development. Start by reading README.md
import sea_level_predictor
from unittest import main

# Exécuter la fonction principale (modifie ici si le nom est différent)
sea_level_predictor.predict_sea_level()  

# Exécuter les tests unitaires
if __name__ == "__main__":
    main(module='test_module', exit=False)
