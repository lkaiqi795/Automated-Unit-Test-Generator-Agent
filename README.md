Automated Unit Test Generator Agent

Overview

Automated Unit Test Generator Agent is an AI-powered software testing assistant that automatically generates pytest unit tests from Python source code.

The system combines static code analysis using Python AST, Large Language Models (LLMs), and automated test execution to create an intelligent Observe → Reason → Act → Retry workflow.

---

Problem Statement

Writing unit tests is one of the most important practices in software development, but many students and beginner developers skip testing because it is time-consuming and requires experience.

As a result, software often contains undetected bugs and lacks sufficient test coverage.

---

Proposed Solution

The Automated Unit Test Generator Agent:

1. Parses Python source files using AST.
2. Extracts function signatures and metadata.
3. Uses Generative AI to create pytest test cases.
4. Executes generated tests automatically.
5. Analyses test failures.
6. Iteratively repairs generated tests until success.

---

System Architecture

Python Source File

↓

AST Parser

↓

Metadata Extraction

↓

LLM Test Generation

↓

Generated Tests

↓

Pytest Runner

↓

Pass?

├── Yes → Output Tests

└── No → Failure Analysis → Repair Prompt → LLM

---

Operating System Concepts Applied

* Process Management
* Inter-Process Communication (IPC)
* File System Operations
* Resource Management
* Timeout Handling
* Subprocess Execution

---

Technology Stack

* Python 3.11+
* OpenAI API
* pytest
* AST
* subprocess
* tempfile

---

Real-World Impact

This project helps software developers and students automatically create test cases, reducing manual testing effort and improving software quality.

---

Future Improvements

* Multi-language support
* CI/CD integration
* Web interface
* Agent memory
* Database-backed learning system

---

Author

LIKAIQI (24013579)

Operating Systems Course Project
