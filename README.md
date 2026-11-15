# 🛡️ CodeGuard AI – AST-Based Code Clone & Plagiarism Detection System

> **A Compiler Design Academic Project**  
> *Structural Code Similarity, Abstract Syntax Tree Decomposition, Scope-Aware Normalization, and Multi-Metric Tree Analysis*

Please see the comprehensive project documentation in [`codeguard-ai/README.md`](codeguard-ai/README.md).

---

## 🚀 Quick Start (Local Setup)

### 1. Launch the Server
```powershell
py run.py
```
*(Or double click `start.bat` on Windows)*

### 2. Access the Application
Open your browser and navigate to:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### 3. Run Automated Tests
```powershell
py -m unittest discover codeguard-ai/tests
```

### 4. Run CLI Benchmark Test Cases
```powershell
py codeguard-ai/benchmark_cases.py
```

---

## 📂 Project Structure
```
site-overview/
├── run.py                      # Workspace root launcher
├── start.bat                   # Windows batch single-click runner
├── codeguard-ai/
│   ├── app.py                  # Flask web application server
│   ├── requirements.txt        # Dependencies
│   ├── benchmark_cases.py      # Automated benchmark verification script
│   ├── README.md               # Full academic project documentation
│   ├── backend/
│   │   ├── ast_parser.py       # AST parsing & syntax validation
│   │   ├── normalizer.py       # Identifier renaming & AST normalization
│   │   ├── similarity.py       # Multi-metric similarity algorithms
│   │   ├── comparator.py       # Pipeline comparison orchestrator
│   │   └── database.py         # SQLite database management
│   ├── frontend/
│   │   ├── index.html          # Main single-page application
│   │   ├── css/style.css       # Clean light theme stylesheet
│   │   └── js/
│   │       ├── app.js          # Main UI controller & Monaco integration
│   │       └── ast-visualizer.js # D3.js interactive SVG tree visualizer
│   ├── tests/
│   │   ├── test_ast_parser.py  # Parser unit tests
│   │   ├── test_normalizer.py  # Normalizer unit tests
│   │   ├── test_similarity.py  # Similarity & DB tests
│   │   └── test_api.py         # Flask API integration tests
│   └── sample_codes/           # 5 Preloaded benchmark test cases
```
