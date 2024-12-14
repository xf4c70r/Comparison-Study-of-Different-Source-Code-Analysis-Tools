# Comparison-Study-of-Different-Source-Code-Analysis-Tools

This research project addresses a critical gap in cybersecurity by conducting a comprehensive comparative analysis of security vulnerability detection tools across two prominent Python web frameworks: Django and FastAPI. As web technologies rapidly evolve, understanding the effectiveness of modern and legacy security analysis tools becomes increasingly important for developers and security professionals.
Research Motivation
The project is driven by several key challenges in the current cybersecurity landscape:

Inconsistent vulnerability detection capabilities across different security tools
Limited comparative studies of tool effectiveness
The need to understand how tool age and framework maturity impact vulnerability identification

Research Objectives
The primary goals of this study are to:

- Conduct a comprehensive analysis of security tool performance across Django and FastAPI
- Quantitatively assess vulnerability detection capabilities of modern and legacy security analysis tools
- Compare tool performance against baseline vulnerability databases
- Investigate the relationship between framework maturity and vulnerability detection


```
web-framework-security-analysis/
│
├── Bandit/
│   ├── Django/
│   │   ├── django.txt
│   │   └── django-script.py
│   └── FastAPI/
│       ├── vulnerabilities.txt
│       └── fastapi-script.py
│
├── Semgrep/
│   ├── Django/
│   │   └── screenshots
│   └── FastAPI/
│       └── screenshots
│
├── SonarQube/
│   ├── Django/
│   │   └── screenshots
│   └── FastAPI/
│       └── screenshots
│
└── Vulert/
    ├── Django/
    │   ├── vulert_django_scrape.py
    │   └── django_vulnerabilities.csv
    └── FastAPI/
        ├── fastapi_vulert_scrape.py
        └── fastapi_vulnerabilities.csv
```