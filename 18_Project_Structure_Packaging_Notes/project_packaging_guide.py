"""
Python Project Structure and Packaging - Comprehensive Guide
===========================================================

Educational guide to Python project organization, virtual environments, packaging, and deployment.
Includes best practices for project structure, dependency management, and distribution.

Author: Python Learning Notes
Date: September 2025
Topic: Project Structure, Packaging, Virtual Environments, Deployment
"""

import os
import sys
import subprocess
from pathlib import Path

# =============================================================================
# PROJECT STRUCTURE GUIDELINES
# =============================================================================

def project_structure_demo():
    """Demonstrate recommended Python project structure"""
    print("\n📁 Python Project Structure:")
    
    structure = """
my_project/
├── README.md                 # Project description and usage
├── requirements.txt          # Dependencies
├── setup.py                 # Package configuration
├── pyproject.toml           # Modern Python packaging
├── .gitignore               # Git ignore patterns
├── .github/                 # GitHub Actions workflows
│   └── workflows/
│       └── ci.yml
├── docs/                    # Documentation
│   ├── index.md
│   └── api.md
├── tests/                   # Test files
│   ├── __init__.py
│   ├── test_main.py
│   └── conftest.py
├── src/                     # Source code (src layout)
│   └── my_project/
│       ├── __init__.py
│       ├── main.py
│       ├── utils.py
│       └── config.py
└── scripts/                 # Utility scripts
    ├── build.py
    └── deploy.py
    """
    
    print(structure)
    
    print("Key Components:")
    components = [
        ("README.md", "Project overview, installation, usage instructions"),
        ("requirements.txt", "List of dependencies with versions"),
        ("setup.py", "Package metadata and configuration"),
        ("src/ layout", "Isolates source code from other files"),
        ("tests/", "Unit tests and test configuration"),
        ("docs/", "Documentation files"),
        (".gitignore", "Files to exclude from version control")
    ]
    
    for component, description in components:
        print(f"  • {component}: {description}")

# =============================================================================
# VIRTUAL ENVIRONMENTS
# =============================================================================

def virtual_environment_demo():
    """Demonstrate virtual environment concepts and commands"""
    print("\n🐍 Virtual Environments:")
    
    print("What are Virtual Environments?")
    print("  Virtual environments create isolated Python installations")
    print("  for different projects, preventing dependency conflicts.")
    
    print("\nCommands (Windows):")
    commands = [
        ("Create venv", "python -m venv myenv"),
        ("Activate", "myenv\\Scripts\\activate"),
        ("Deactivate", "deactivate"),
        ("Install packages", "pip install package_name"),
        ("Freeze dependencies", "pip freeze > requirements.txt"),
        ("Install from requirements", "pip install -r requirements.txt")
    ]
    
    for action, command in commands:
        print(f"  {action:<20}: {command}")
    
    print("\nBest Practices:")
    practices = [
        "Always use virtual environments for projects",
        "Keep requirements.txt updated",
        "Use specific version numbers for dependencies",
        "Include virtual environment in .gitignore",
        "Document Python version requirements"
    ]
    
    for practice in practices:
        print(f"  • {practice}")

# =============================================================================
# DEPENDENCY MANAGEMENT
# =============================================================================

def dependency_management_demo():
    """Demonstrate dependency management practices"""
    print("\n📦 Dependency Management:")
    
    # Create sample requirements.txt content
    requirements_content = """
# Core dependencies
numpy>=1.21.0,<2.0.0
pandas>=1.3.0
matplotlib>=3.4.0

# Development dependencies
pytest>=6.0.0
black>=21.0.0
flake8>=3.9.0

# Optional dependencies
scikit-learn>=1.0.0  # For machine learning features
requests>=2.25.0     # For API integrations
"""
    
    print("Sample requirements.txt:")
    print(requirements_content)
    
    print("Dependency Specifications:")
    specs = [
        ("==1.0.0", "Exact version"),
        (">=1.0.0", "Minimum version"),
        (">=1.0.0,<2.0.0", "Version range"),
        ("~=1.4.2", "Compatible release (>=1.4.2, <1.5.0)"),
        ("package[extra]", "Optional dependencies")
    ]
    
    for spec, description in specs:
        print(f"  {spec:<20}: {description}")

# =============================================================================
# PACKAGING WITH SETUP.PY
# =============================================================================

def packaging_demo():
    """Demonstrate package configuration"""
    print("\n📋 Package Configuration:")
    
    setup_py_content = '''
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="my-project",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-project",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
        ],
        "ml": [
            "scikit-learn>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "my-tool=my_project.main:main",
        ],
    },
)
'''
    
    print("Sample setup.py:")
    print(setup_py_content)

# =============================================================================
# MODERN PACKAGING (PYPROJECT.TOML)
# =============================================================================

def modern_packaging_demo():
    """Demonstrate modern packaging with pyproject.toml"""
    print("\n🚀 Modern Packaging (pyproject.toml):")
    
    pyproject_content = '''
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-project"
version = "0.1.0"
description = "A short description of your project"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"},
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
]
dependencies = [
    "numpy>=1.21.0",
    "pandas>=1.3.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=6.0.0",
    "black>=21.0.0",
    "flake8>=3.9.0",
]
ml = [
    "scikit-learn>=1.0.0",
]

[project.scripts]
my-tool = "my_project.main:main"

[tool.black]
line-length = 88
target-version = ['py38']

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
'''
    
    print("Sample pyproject.toml:")
    print(pyproject_content)

# =============================================================================
# GITIGNORE FOR PYTHON
# =============================================================================

def gitignore_demo():
    """Demonstrate Python .gitignore patterns"""
    print("\n🚫 Python .gitignore:")
    
    gitignore_content = '''
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/
.venv/

# IDE files
.vscode/
.idea/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db

# Testing
.coverage
.pytest_cache/
.tox/

# Documentation
docs/_build/

# Jupyter Notebook
.ipynb_checkpoints

# Environment variables
.env
.env.local
'''
    
    print("Sample .gitignore:")
    print(gitignore_content)

# =============================================================================
# DEPLOYMENT STRATEGIES
# =============================================================================

def deployment_demo():
    """Demonstrate deployment strategies"""
    print("\n🚀 Deployment Strategies:")
    
    strategies = [
        ("PyPI", "pip install my-package", "Public package distribution"),
        ("Git + pip", "pip install git+https://github.com/user/repo.git", "Direct from repository"),
        ("Docker", "docker build -t my-app .", "Containerized deployment"),
        ("GitHub Actions", "Automated CI/CD pipeline", "Continuous deployment"),
        ("Heroku", "git push heroku main", "Platform-as-a-Service"),
        ("AWS Lambda", "Serverless functions", "Event-driven compute")
    ]
    
    print("Deployment Options:")
    for method, command, description in strategies:
        print(f"  {method:<15}: {description}")
        print(f"  {'Command':<15}: {command}")
        print()
    
    print("Deployment Checklist:")
    checklist = [
        "✓ All tests pass",
        "✓ Dependencies are specified",
        "✓ Version number updated",
        "✓ Documentation is current",
        "✓ Security vulnerabilities checked",
        "✓ Environment variables configured",
        "✓ Monitoring and logging set up"
    ]
    
    for item in checklist:
        print(f"  {item}")

# =============================================================================
# CONTINUOUS INTEGRATION EXAMPLE
# =============================================================================

def ci_demo():
    """Demonstrate CI/CD configuration"""
    print("\n🔄 Continuous Integration (GitHub Actions):")
    
    ci_yaml = '''
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, "3.10"]

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .[dev]
    
    - name: Lint with flake8
      run: |
        flake8 src tests
    
    - name: Format with black
      run: |
        black --check src tests
    
    - name: Test with pytest
      run: |
        pytest tests/ --cov=src --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
'''
    
    print("Sample .github/workflows/ci.yml:")
    print(ci_yaml)

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    
    project_structure_demo()
    virtual_environment_demo()
    dependency_management_demo()
    packaging_demo()
    modern_packaging_demo()
    gitignore_demo()
    deployment_demo()
    ci_demo()
    
    print("\n" + "="*70)
    print("📚 Python Project Best Practices Summary:")
    print("="*70)
    
    summary_points = [
        "Use src/ layout for better project organization",
        "Always work in virtual environments",
        "Pin dependency versions in requirements.txt",
        "Include comprehensive README.md",
        "Set up automated testing with CI/CD",
        "Use type hints and docstrings",
        "Follow PEP 8 style guidelines",
        "Keep secrets in environment variables",
        "Version your releases semantically",
        "Document your API and usage examples"
    ]
    
    for i, point in enumerate(summary_points, 1):
        print(f"{i:2d}. {point}")
    
    print("\nProject structure and packaging guide completed!")

if __name__ == "__main__":
    main()