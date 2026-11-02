"""Command line interface for model-fallback-router."""
from .router import FallbackRouter

def main():
    def fail_p(p): raise Exception("503 Outage")
    def good_p(p): return f"Processed: {p}"

    router = FallbackRouter([("primary", fail_p), ("backup", good_p)])
    provider, resp = router.execute_with_fallback("Test prompt")
    print(f"Success from provider '{provider}':", resp)

if __name__ == "__main__":
    main()
