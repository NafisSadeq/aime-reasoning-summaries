# Reasoning Summary Extraction

This project uses the OpenAI `o3` model to extract detailed reasoning summaries and final answers from questions in the AIME (American Invitational Mathematics Examination) dataset. It automates reasoning generation and tracks token usage for analysis and auditing.

---

## 📦 Project Structure

- `reasoning_client.py`: A reusable client for querying the OpenAI API with reasoning configurations.
- `aime.py`: Script that loads AIME2025 datasets from Hugging Face, queries each problem through the `ReasoningClient`, and saves the reasoning summaries, answers, and token usage to `aime.json`.

---

## 🛠️ Installation

Make sure you have the following dependencies installed:

```
pip install openai datasets tqdm
```

You also need to authenticate with Hugging Face to access the AIME2025 datasets:

```
huggingface-cli login
```

Set your OpenAI API key as an environment variable:

```
export OPENAI_API_KEY=your-api-key-here
```

## 🛠️ Usage

```
python aime.py
```

## 📁 Output Format
The aime.json file contains a list of entries in the following format:

```
{
    "summaries": ["Step-by-step reasoning...", "..."],
    "output": "Final answer",
    "input_tokens": 57,
    "output_tokens": 198,
    "reasoning_tokens": 134,
    "ground_truth": "42"
}
```



