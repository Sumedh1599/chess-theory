"""H2: Hindsight Injection Experiment"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from experiments import H2Runner
from chess_core import TurnRecord

def mock_llm(prompt: str, max_tokens: int = 200) -> str:
    if "HINDSIGHT" in prompt:
        if "capital" in prompt.lower(): return "Paris"
        if "2+2" in prompt: return "4"
        return "Correct answer with hindsight."
    else:
        if "capital" in prompt.lower(): return "London"
        if "2+2" in prompt: return "5"
        return "Unsure."

def main():
    print("=" * 60)
    print("H2: Hindsight Injection")
    print("=" * 60)

    h2 = H2Runner(model_fn=mock_llm, model_name="demo-model")

    tasks = [
        {"id": "qa_1", "task_type": "factual_qa",
         "prompt": "What is the capital of France?", "reference": "Paris",
         "history": [TurnRecord(0, "Asked about Germany", "success", "Berlin"),
                     TurnRecord(1, "Asked about Italy", "success", "Rome")]},
        {"id": "math_1", "task_type": "arithmetic",
         "prompt": "What is 2+2?", "reference": "4",
         "history": [TurnRecord(0, "Solved 1+1", "success", "2"),
                     TurnRecord(1, "Solved 3+3", "success", "6")]},
        {"id": "logic_1", "task_type": "logical_reasoning",
         "prompt": "If all cats are mammals and some mammals are pets, are all cats pets?",
         "reference": "No",
         "history": [TurnRecord(0, "Solved syllogism A", "success", "Valid"),
                     TurnRecord(1, "Solved syllogism B", "failure", "Invalid")]}
    ]

    results, agg = h2.run(tasks, replicates=2)
    print(f"\nWith: {agg.with_mean:.2%} | Without: {agg.without_mean:.2%}")
    print(f"Uplift: {agg.uplift:+.2f} | Cohen's d: {agg.cohens_d:.2f} | p: {agg.wilcoxon_p:.4f}")

    ablation = h2.run_ablation(tasks)
    print(f"\nFull: {ablation['full']:.2%} | Last: {ablation['last']:.2%} | Noise: {ablation['noise']:.2%}")

if __name__ == "__main__":
    main()
