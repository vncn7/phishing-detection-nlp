# Phishing Detection with NLP

Comparison of DistilBERT and GPT-2 for phishing detection in emails and SMS messages. Each model is evaluated with and without fine-tuning to demonstrate the impact of task-specific training.

## Results

| Model | Task | Accuracy | F1 | Precision | Recall |
|---|---|---|---|---|---|
| DistilBERT (fine-tuned) | Email | 99.49% | 99.51% | 99.34% | 99.69% |
| DistilBERT (fine-tuned) | SMS | 99.16% | 97.98% | 98.37% | 97.58% |
| GPT-2 (fine-tuned) | Email | 99.53% | 99.55% | 99.58% | 99.51% |
| GPT-2 (fine-tuned) | SMS | 99.41% | 98.35% | 99.52% | 97.21% |
| DistilBERT (baseline) | Email | 48.21% | 62.87% | 50.18% | 84.18% |
| DistilBERT (baseline) | SMS | 71.97% | 27.33% | 27.63% | 27.04% |
| GPT-2 (baseline) | Email | 47.90% | 0.00% | 0.00% | 0.00% |
| GPT-2 (baseline) | SMS | 80.50% | 0.00% | 0.00% | 0.00% |

Training was done on an NVIDIA GeForce RTX 4080.

## Notebooks

| Notebook | Description |
|---|---|
| `bert_mail_finetuned.ipynb` | DistilBERT fine-tuned on email dataset |
| `bert_sms_finetuned.ipynb` | DistilBERT fine-tuned on SMS dataset |
| `gpt2_mail_finetuned.ipynb` | GPT-2 fine-tuned on email dataset |
| `gpt2_sms_finetuned.ipynb` | GPT-2 fine-tuned on SMS dataset |
| `bert_mail_baseline.ipynb` | DistilBERT without fine-tuning (baseline, email) |
| `bert_sms_baseline.ipynb` | DistilBERT without fine-tuning (baseline, SMS) |
| `gpt2_mail_baseline.ipynb` | GPT-2 without fine-tuning (baseline, email) |
| `gpt2_sms_baseline.ipynb` | GPT-2 without fine-tuning (baseline, SMS) |

## Datasets

- [Kaggle E-Mail Phishing Dataset (2024)](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset): ~82,500 messages (42,891 phishing, 39,595 legitimate) → save as `datasets/mail_phishing.csv`
- [Mendeley SMS Phishing Dataset (2022)](https://data.mendeley.com/datasets/f45bkkt8pr/1): 5,971 messages (ham, spam, smishing) → save as `datasets/smishing.csv`

## Requirements

- Docker
- NVIDIA GPU with Docker GPU support
- VS Code with [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension

## Setup

1. Open the project in VS Code
2. Run `Dev Containers: Rebuild and Reopen in Container` (`Ctrl+Shift+P`)
3. Place datasets in `datasets/`
4. Open a notebook in `notebooks/` and run it, or run all notebooks sequentially with:
   ```
   python run_all.py
   ```
