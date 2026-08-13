"""H1: Positional Retrieval Experiment"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from experiments import H1Runner

def mock_llm(prompt: str, max_tokens: int = 200) -> str:
    if "0.50" in prompt or "0.20" in prompt:
        return "I cannot find the secret code."
    return "The secret code is 7842."

def main():
    print("=" * 60)
    print("H1: Positional Retrieval")
    print("=" * 60)

    filler = " ".join([f"Paragraph {i} contains general information. " * 20 for i in range(50)])
    h1 = H1Runner(model_fn=mock_llm, model_name="demo-model")

    results = h1.run(
        base_context=filler, critical_fact="The secret code is 7842",
        question="What is the secret code?",
        depths=[0.05, 0.10, 0.20, 0.50, 0.80, 0.95],
        budgets=[50, 100, 200], replicates=3
    )

    agg = h1.analyze(results)
    print(f"\nExp R2: {agg.exp_r2:.3f} | Linear R2: {agg.linear_r2:.3f}")
    print(f"Budget monotonic: {agg.budget_monotonic}")
    for d, acc in sorted(agg.depth_accuracy.items()):
        print(f"  depth={d:.2f}: {acc:.1%}")
    for b, acc in sorted(agg.budget_accuracy.items()):
        print(f"  budget={b}: {acc:.1%}")

if __name__ == "__main__":
    main()
