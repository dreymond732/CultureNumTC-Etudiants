"""Tests hors ligne du plugin d'accès Adminer TD6 (PHP réel, Adminer simulé)."""
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "td6" / "demarrer_adminer.sh"

def php(args, *, cwd=None):
    return subprocess.run(
        ["php", *args], cwd=cwd, text=True, capture_output=True,
        check=False, timeout=15
    )

def plugin_source():
    code = SCRIPT.read_text(encoding="utf-8")
    match = re.search(
        r"cat > \"\$WEB/adminer-plugins\.php\" <<'PHP'\n(.*?)\nPHP\n",
        code, re.S
    )
    if match is None:
        raise AssertionError("Le bloc PHP de configuration Adminer est introuvable.")
    return match.group(1) + "\n"

class AdminerLoginTests(unittest.TestCase):
    def test_bash_syntax_and_short_pin(self):
        check = subprocess.run(
            ["bash", "-n", str(SCRIPT)], capture_output=True, text=True,
            check=False, timeout=10
        )
        self.assertEqual(check.returncode, 0, check.stderr)
        content = SCRIPT.read_text(encoding="utf-8")
        self.assertIn('secrets.randbelow(100_000_000):08d', content)
        self.assertIn('ACCES_ADMINER.txt', content)
        self.assertNotIn('login-password-less.php', content)
        self.assertIn('td6/ACCES_ADMINER.txt', (ROOT / ".gitignore").read_text())

    def test_php_plugin_valid_invalid_pin_and_db_autofill(self):
        with TemporaryDirectory() as temp:
            base = Path(temp)
            (base / "www").mkdir()
            plugin = base / "www" / "adminer-plugins.php"
            plugin.write_text(plugin_source(), encoding="utf-8")
            lint = php(["-l", str(plugin)])
            self.assertEqual(lint.returncode, 0, lint.stderr)

            h = php(["-r", 'echo password_hash("12345678", PASSWORD_DEFAULT);'])
            self.assertEqual(h.returncode, 0, h.stderr)
            (base / "pin.hash").write_text(h.stdout)
            (base / "database.path").write_text("/tmp/test-td6.sqlite")

            stub = base / "stub.php"
            stub.write_text(
                """<?php
namespace Adminer {
    const SERVER = "";
    class Plugin {}
}
namespace {
    $plugins = include __DIR__ . "/www/adminer-plugins.php";
    if (count($plugins) !== 1) { exit(1); }
    $p = $plugins[0];
    if ($p->login("", "12345678") !== true) { exit(2); }
    if ($p->login("", "00000000") === true) { exit(3); }
    if ($p->credentials() !== ["", "", ""]) { exit(4); }
    if ($p->database() !== "/tmp/test-td6.sqlite") { exit(5); }
    if (!str_contains($p->loginFormField("driver", "", ""), 'value="sqlite"')) { exit(6); }
    if (!str_contains($p->loginFormField("password", "", ""), 'inputmode="numeric"')) { exit(7); }
    if (!str_contains($p->loginFormField("db", "", ""), '/tmp/test-td6.sqlite')) { exit(8); }
    if (!str_contains($p->loginFormField("db", "", ""), 'auth[db]')) { exit(9); }
    echo "PLUGIN_TD6_OK\\n";
}
""",
                encoding="utf-8"
            )
            result = php([str(stub)])
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
            self.assertIn("PLUGIN_TD6_OK", result.stdout)

if __name__ == "__main__":
    unittest.main()
