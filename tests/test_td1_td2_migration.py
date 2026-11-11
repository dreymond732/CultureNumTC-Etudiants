"""Protection des rapports student : pas de publication Git et comparaison Wix au TD2."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_td1_keeps_seven_exercises_without_wix_comparison():
    md = (ROOT / "td1/rapport-td1.md").read_text(encoding="utf-8")
    assert all(f"## Exercice {i}" in md for i in range(1, 8))
    assert "### Mon usage de Wix" not in md
    assert "## Bilan personnel" in md

def test_td2_includes_wix_after_real_server_practice():
    report = (ROOT / "td2/rapport-td2.md").read_text(encoding="utf-8")
    readme = (ROOT / "td2/README.md").read_text(encoding="utf-8")
    assert report.index("## Bilan comparatif — Wix et Codespaces") > report.index("## Exercice 4")
    assert "Dans Codespaces, j'ai effectivement manipulé" in report
    assert "cette comparaison n'est plus demandée au TD1".lower() in readme.lower()

def test_single_readme_warning_prescribes_classroom_submission():
    root = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "NE CLIQUEZ PAS" in root
    assert "Synchroniser" in root and "Publier une branche" in root
    assert "voie de remise" in root
    assert "Codespace supprimé" in root
