# AI PM Agents Suite — Feedback-to-Strategy Pipeline

**Built by Varun Kulkarni** · Works with Claude Code and GitHub Copilot

Sequential agent orchestration for product management workflows. The pipeline
runs 6 AI agents that transform raw customer feedback into strategic
recommendations and stakeholder communications.

> ⚠️ **All data is 100% synthetic and fictional.** No real customer data, no API
> keys, no secrets. Strict security, governance, and confidentiality alignment.

## Pipeline Agents

| # | Agent | Cognitive Function |
|---|-------|--------------------|
| 1 | Customer Feedback Pipeline | Pattern Recognition & Synthesis |
| 2 | Data Scientist | Statistical Analysis & Correlation |
| 3 | Metrics Narrator | Narrative Intelligence & Forecasting |
| 4 | Chief of Staff | Strategic Reasoning & Decision Framing |
| 5 | PRD Architect | Structured Documentation & Specification |
| 6 | Stakeholder Translator | Audience-Adaptive Communication |

## Installation

```bash
# From the repo root:
cd pipelines/feedback-to-strategy
pip install -e ".[dev]"
```

> **Note:** `pyproject.toml` lives at the repository root, not inside this
> directory. The `cd` above just puts you in the working directory the CLI
> expects.

## Usage

### CLI

```bash
# Run the full pipeline
pipeline run

# List all agents
pipeline agents

# Show agent details
pipeline agent 3

# Show input data summary
pipeline data

# Run with JSON output
pipeline run --output results.json
```

### Programmatic

```python
from pipeline import PipelineOrchestrator

orchestrator = PipelineOrchestrator()
result = orchestrator.run(verbose=True)

# Access individual agent outputs
agent1_output = orchestrator.get_agent_output(1)
```

## Testing

```bash
pytest                       # Run all tests
pytest tests/test_security.py  # Run a specific test file
pytest -v                    # Verbose output
```

## Scripts

```bash
python scripts/run_pipeline.py        # Run with Rich output
python scripts/analyze_data.py        # Analyze synthetic data
python scripts/validate_outputs.py    # Validate all agent outputs
```

## Security

- No real customer data — all 50 feedback tickets are synthetic
- No API keys committed — use environment variables
- PII detection and sanitization utilities included
- All outputs validated against Pydantic schemas
