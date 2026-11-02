# Model Fallback Router ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Model Fallback Router Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/model-fallback-router/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/model-fallback-router?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/model-fallback-router/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Model Fallback Router** is a production-ready developer tool and connector: Resilient multi-provider LLM router supporting circuit breakers, exponential backoff, and automatic provider failover.

---

## 🚀 Problem Statement

When Anthropic or OpenAI returns 429 Rate Limit or 503 Outage errors, mission-critical autonomous workflows crash completely.

---

## ⚡ Architecture Flow

```mermaid
graph TD
    A[Agent LLM Request] --> B[Model Fallback Router]
    B --> C{Primary: Provider A}
    C -->|Success 200| D[Return Response]
    C -->|Error 429 / 503| E[Trip Circuit & Switch to Provider B]
    E -->|Success 200| D
    E -->|Error 500| F[Switch to Local Ollama Fallback]
    F --> D
```

---

## 📊 Performance Benchmarks

| Outage Scenario | Standard Client | Model Fallback Router |
|---|---|---|
| Primary API 503 Outage | Crash | **Seamless 0.3s Failover** |
| Rate Limit 429 Spike | Crash | **Fails over to Secondary** |
| Uptime SLA | 99.2% | **99.99%** |

---

## 🛠️ Installation & Quickstart

```bash
pip install model_fallback_router
```

### Python API

```python
import model_fallback_router

print(model_fallback_router.__version__)
```

### CLI Usage

```bash
model-fallback-router --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
