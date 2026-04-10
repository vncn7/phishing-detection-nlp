import subprocess
import sys

notebooks = [
    "notebooks/bert_mail_baseline.ipynb",
    "notebooks/bert_sms_baseline.ipynb",
    "notebooks/gpt2_mail_baseline.ipynb",
    "notebooks/gpt2_sms_baseline.ipynb",
    "notebooks/bert_mail_finetuned.ipynb",
    "notebooks/bert_sms_finetuned.ipynb",
    "notebooks/gpt2_mail_finetuned.ipynb",
    "notebooks/gpt2_sms_finetuned.ipynb",
]

for i, nb in enumerate(notebooks, 1):
    print(f"[{i}/{len(notebooks)}] Running {nb}...")
    result = subprocess.run(
        ["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", nb],
    )
    if result.returncode != 0:
        print(f"FAILED: {nb}")
        sys.exit(1)
    print(f"Done: {nb}\n")

print("All notebooks finished.")
