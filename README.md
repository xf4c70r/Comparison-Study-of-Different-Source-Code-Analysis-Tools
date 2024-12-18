# Comparison-Study-of-Different-Source-Code-Analysis-Tools

This research project addresses a critical gap in cybersecurity by conducting a comprehensive comparative analysis of security vulnerability detection tools across two prominent Python web frameworks: Django and FastAPI. As web technologies rapidly evolve, understanding the effectiveness of modern and legacy security analysis tools becomes increasingly important for developers and security professionals.

## Research Motivation
The project is driven by several key challenges in the current cybersecurity landscape:

- Inconsistent vulnerability detection capabilities across different security tools
- Limited comparative studies of tool effectiveness
- The need to understand how tool age and framework maturity impact vulnerability identification

##  Research Objectives
The primary goals of this study are to:

- Conduct a comprehensive analysis of security tool performance across Django and FastAPI
- Quantitatively assess vulnerability detection capabilities of modern and legacy security analysis tools
- Compare tool performance against baseline vulnerability databases
- Investigate the relationship between framework maturity and vulnerability detection

## Research Questions

- How do modern security analysis tools (Semgrep, SonarQube) compare to legacy tools (Bandit), using Vulert as a baseline database for identifying vulnerabilities across Django and FastAPI?
- To what extent does the age and maturity of a web framework influence the types and severity of detected vulnerabilities?
- What are the performance differences among security analysis tools in terms of lines of code scanned and time required for comprehensive vulnerability detection?

```
web-framework-security-analysis/
│
├── Bandit/
│   ├── Django/
│   │   ├── django.txt (Raw vulnerability scan results for Django)
│   │   └── django-script.py (Script to parse and categorize Django vulnerabilities)
│   └── FastAPI/
│       ├── fastapi.txt (Raw vulnerability scan results for FastAPI)
│       └── fastapi-script.py (Script to parse and categorize FastAPI vulnerabilities)
│
├── Semgrep/
│   ├── Django/
│   │   └── screenshots (Visual results of Semgrep vulnerability scan for Django)
│   └── FastAPI/
│       └── screenshots (Visual results of Semgrep vulnerability scan for FastAPI)
│
├── SonarQube/
│   ├── Django/
│   │   └── screenshots (Visual results of SonarQube vulnerability scan for Django)
│   └── FastAPI/
│       └── screenshots (Visual results of SonarQube vulnerability scan for FastAPI)
│
└── Vulert/
    ├── Django/
    │   ├── vulert_django_scrape.py (Web scraping script for Django vulnerabilities from Vulert)
    │   └── django_vulnerabilities.csv (Compiled list vulnerabilities after scraping)
    └── FastAPI/
        ├── fastapi_vulert_scrape.py (Web scraping script for FastAPI vulnerabilities from Vulert)
        └── fastapi_vulnerabilities.csv (Compiled list vulnerabilities after scraping)
```
