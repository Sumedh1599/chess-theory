"""
Basic CHESS Agent Usage Example
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from chess_core import CHESSAgent

def mock_llm(prompt: str, max_tokens: int = 200) -> str:
    responses = [
        "I understand your concern. Let me help.",
        "Based on our policy, here's what I can do.",
        "I apologize for the inconvenience. Here's a solution."
    ]
    idx = hash(prompt) % len(responses)
    return responses[idx]

def mock_generator(prompt: str, params: dict):
    n = params.get("n", 3)
    return [(mock_llm(prompt, 200), -0.3 * i) for i in range(n)]

def main():
    print("=" * 60)
    print("CHESS Three-Seat Agent Demo")
    print("=" * 60)

    agent = CHESSAgent(hindsight_budget=200, foresight_k=3,
                       arbitration_policy="variational", eta=1.0)

    turns = [
        {"context": "Customer: I want a refund for my order #12345.",
         "outcome": "resolved", "summary": "Refund approved, customer satisfied"},
        {"context": "Customer: My order #12346 arrived damaged.",
         "outcome": "resolved", "summary": "Replacement sent, customer satisfied"},
        {"context": "Customer: I want a refund but my order is from 6 months ago.",
         "outcome": "pending", "summary": "Policy conflict: outside refund window"}
    ]

    for i, turn in enumerate(turns):
        print(f"\n--- Turn {i+1} ---")
        print(f"Context: {turn['context']}")

        action, metadata = agent.act(context=turn["context"], generate_fn=mock_generator)

        print(f"Selected: {action}")
        print(f"Weights: {metadata['arbitration']['influence_weights']}")
        print(f"Converged: {metadata['arbitration']['converged']}")
        print(f"Steps: {metadata['arbitration']['steps']}")

        agent.observe_outcome(action=action, outcome=turn["outcome"],
                              context_summary=turn["summary"])

    print("\n" + "=" * 60)
    H_final = agent.hindsight.compress()
    print("Final hindsight:", H_final.summary[:200] + "...")

if __name__ == "__main__":
    main()
