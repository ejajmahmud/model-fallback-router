"""Resilient multi-provider LLM failover router."""
from typing import List, Callable, Any, Tuple, Dict

class FallbackRouter:
    def __init__(self, providers: List[Tuple[str, Callable[[str], Any]]]):
        self.providers = providers
        self.failure_counts: Dict[str, int] = {p[0]: 0 for p in providers}

    def execute_with_fallback(self, prompt: str) -> Tuple[str, Any]:
        last_err = None
        for name, fn in self.providers:
            try:
                res = fn(prompt)
                return name, res
            except Exception as e:
                self.failure_counts[name] += 1
                last_err = e

        raise RuntimeError(f"All providers exhausted. Last error: {last_err}")
