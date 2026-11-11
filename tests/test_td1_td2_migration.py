"""Protection des rapports TD1/TD2 et de la consigne de non-publication Git."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class TestProgressionTD1TD2(unittest.TestCase):
    def test_td1_seven_exercises_without_wix(self):
        md = (ROOT / "td1/rapport-td1.md").read_text(encoding="utf-8")
        for i in range(1, 8):
            self.assertIn(f"## Exercice {i}", md)
        self.assertNotIn("### Mon usage de Wix", md)
        self.assertIn("## Bilan personnel", md)

    def test_wix_at_end_of_td2_after_server_practice(self):
        report = (ROOT / "td2/rapport-td2.md").read_text(encoding="utf-8")
        readme = (ROOT / "td2/README.md").read_text(encoding="utf-8")
        self.assertGreater(report.index("## Bilan comparatif — Wix et Codespaces"),
                           report.index("## Exercice 4"))
        self.assertIn("Dans Codespaces, j'ai effectivement manipulé", report)
        self.assertIn("cette comparaison n'est plus demandée au td1", readme.lower())

    def test_readme_warns_against_git_publication(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("NE CLIQUEZ PAS", readme)
        self.assertIn("Synchroniser", readme)
        self.assertIn("Publier une branche", readme)
        self.assertIn("voie de remise", readme)
        self.assertIn("Codespace supprimé", readme)

if __name__ == "__main__":
    unittest.main()
