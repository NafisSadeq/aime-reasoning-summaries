from reasoning_client import ReasoningClient
from tqdm.auto import tqdm
from datasets import load_dataset
import json

rc = ReasoningClient()

# Login using e.g. `huggingface-cli login` to access this dataset
ds1 = load_dataset("opencompass/AIME2025", "AIME2025-I")

ds2 = load_dataset("opencompass/AIME2025", "AIME2025-II")

def save_result(result_list):

    with open("aime.json",'w') as file:
        json.dump(result_list,file,indent=4,ensure_ascii=False)

result_list = []

for problem in tqdm(ds1['test']):
    result = rc.get_reasoning_summary_and_output(
        prompt=problem["question"]
    )
    result["ground_truth"] = problem["answer"]

    result_list.append(result)
    save_result(result_list)

for problem in tqdm(ds2['test']):
    result = rc.get_reasoning_summary_and_output(
        prompt=problem["question"]
    )
    result["ground_truth"] = problem["answer"]

    result_list.append(result)
    save_result(result_list)