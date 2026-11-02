"""Unit tests for FallbackRouter."""
import unittest
from model_fallback_router.router import FallbackRouter

class TestFallbackRouter(unittest.TestCase):
    def test_failover(self):
        def p1(p): raise ValueError("429 Too Many Requests")
        def p2(p): return "OK response"
        r = FallbackRouter([("openai", p1), ("gemini", p2)])
        name, resp = r.execute_with_fallback("hello")
        self.assertEqual(name, "gemini")
        self.assertEqual(resp, "OK response")

if __name__ == "__main__":
    unittest.main()
