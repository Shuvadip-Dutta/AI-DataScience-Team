# AI Data Science Team

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-black)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A LangGraph-powered multi-agent AI system that automates exploratory data analysis (EDA), data cleaning, feature engineering, visualization, and report generation for tabular datasets.

---

## Overview

This project uses a coordinated team of specialized agents to analyze a dataset end-to-end. A CEO-style router decides which agent should run next based on the current workflow state.

### Core capabilities
- Automated dataset cleaning
- Feature engineering with categorical encoding
- Dataset evaluation and summary reporting
- Automated visualization generation
- Final Markdown report creation
- Modular multi-agent architecture
- LangGraph-based workflow orchestration

---

## Architecture

The system is organized as a state-driven workflow:

```text
User Request
    ↓
Planner
    ↓
CEO Router
    ↓
┌──────────────┬──────────────────────┬───────────────┬──────────────┬──────────────────┐
│   Cleaner    │ Feature Engineer     │  Evaluator    │ Visualization│ Report Generator │
└──────────────┴──────────────────────┴───────────────┴──────────────┴──────────────────┘
    ↓                    ↓                    ↓                ↓                 ↓
Shared State Updates → CEO Router decides next step → Final report/output
```

### Workflow details
- **Planner** creates a task list for the execution pipeline
- **CEO** inspects the task list and routes execution to the next agent
- **Cleaner** removes duplicates and fills missing values
- **Feature Engineer** encodes categorical features and removes unnecessary columns
- **Evaluator** summarizes the processed dataset
- **Visualization** generates charts and saves them to disk
- **Report Generator** compiles all outputs into a final Markdown report

---

## Project Structure

```text
AI-DataScience-Team/
├── agents/
│   ├── ceo.py
│   ├── planner.py
│   ├── cleaner.py
│   ├── feature_engineer.py
│   ├── evaluator.py
│   ├── visualization.py
│   └── report_generator.py
├── graph/
│   └── workflow.py
├── state/
│   ├── ceo.py
│   ├── cleaning_report.py
│   ├── evaluation_report.py
│   ├── feature_engineering_report.py
│   ├── planner.py
│   ├── report_generator_report.py
│   ├── state.py
│   ├── todo.py
│   └── visualization_report.py
├── outputs/
│   └── EDA_Report.md
├── datasets/
│   └── titanic.csv
├── main.py
└── requirements.txt
```

---

## Requirements

Install the dependencies listed in `requirements.txt`:

```txt
langgraph
langchain
langsmith
ipykernel
python-dotenv
langchain-groq
pandas
scikit-learn
matplotlib
seaborn
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Shuvadip-Dutta/AI-DataScience-Team.git
cd AI-DataScience-Team
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

- **Windows**
  ```bash
  .venv\\Scripts\\activate
  ```

- **macOS/Linux**
  ```bash
  source .venv/bin/activate
  ```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Setup

This project may require API credentials for the LLM provider. Create a `.env` file in the project root and add your keys there.

### Example `.env`
```env
GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langchain_api_key_here
LANGCHAIN_PROJECT=AI-DataScience-Team
```

### Load environment variables
The project uses `python-dotenv`, so you can load variables from `.env` in your Python code before initializing models.

Example:

```python
from dotenv import load_dotenv

load_dotenv()
```

### Important
- Do **not** commit your `.env` file to GitHub
- `.env` is already ignored in `.gitignore`

---

## Usage

Run the main script:

```bash
python main.py
```

The workflow will:

1. Load the dataset
2. Plan the execution steps
3. Clean the data
4. Engineer features
5. Evaluate the processed dataset
6. Generate visualizations
7. Create a final report in `outputs/EDA_Report.md`

---

## Outputs

After running the pipeline, the following artifacts are produced:

- Cleaned and engineered dataframe in memory
- Cleaning report
- Feature engineering report
- Evaluation report
- Visualization charts saved in the `outputs/` directory
- Final Markdown report at:
  - `outputs/EDA_Report.md`

Generated charts may include:

- `histograms.png`
- `correlation_heatmap.png`
- `target_distribution.png`
- `feature_relationships.png`

---

## Example Workflow

The default `main.py` uses the Titanic dataset:

```python
initial_state = {
    "user_request": "Please analyze the Titanic dataset and provide insights.",
    "dataset_path": "datasets/titanic.csv",
    "messages": [],
}
```

You can change `user_request` and `dataset_path` to run the workflow on another tabular dataset.

---

## Notes

- The `Feature Engineer` currently encodes categorical columns using `LabelEncoder`.
- The visualization step assumes certain Titanic-style columns such as:
  - `Survived`
  - `Age`
  - `Fare`
- If your dataset does not contain these columns, you may need to adjust the plotting logic in `agents/visualization.py`.

---

## Generated Report

The final report is written to:

```text
outputs/EDA_Report.md
```

It contains:

- Cleaning summary
- Feature engineering summary
- Evaluation summary
- Visualization summary
- Final conclusion

---

## Author

Shuvadip Dutta
