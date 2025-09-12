# Simple runner to ensure files execute without import errors.
import subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1] / "src"
FILES = [
    "q01_oop_book_basics.py",
    "q02_oop_encapsulation.py",
    "q03_oop_inheritance.py",
    "q04_oop_polymorphism.py",
    "q05_oop_all_in_one.py",
    "q06_requests_get.py",
    "q07_requests_get_params.py",
    "q08_requests_post.py",
    "q09_requests_put_delete.py",
    "q10_http_status_classifier.py",
    "q11_fetch_with_status_handling.py",
    "q12_cli_http_client.py",
]

for f in FILES:
    print(f"Running {f} ...")
    p = subprocess.run([sys.executable, str(ROOT / f)], capture_output=True, text=True)
    print(p.stdout)
    if p.returncode != 0:
        print(p.stderr)
        raise SystemExit(f"Failed: {f}")
print("Done.")
