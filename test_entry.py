import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def test_entry():
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
        r = subprocess.run(
            [sys.executable, os.path.join(HERE, "main.py")],
            env=env, capture_output=True, text=True, timeout=60,
        )
        assert r.returncode == 0, r.stderr
        with open(os.path.join(tmp, "entry.txt"), encoding="utf-8") as f:
            content = f.read()
    text = content.strip()
    assert text == "ULTRACREPIDARIAN", f"expected exactly one word, got {text!r}"
    assert 1 <= len(text) <= 24, f"length {len(text)} outside 1-24"
    print(f"ok: entry is exactly one word ({len(text)} chars): {text}")


if __name__ == "__main__":
    test_entry()
