# Sahidhullah H

Backend & AI Systems Engineer

Chennai, India (IST) | Open to Remote — Worldwide | Available for US/EU hours overlap | Full-time or Contract
+91 97894 42466 | sahidhullah@gmail.com | linkedin.com/in/sahidh-h | github.com/sahidhh

---

## SUMMARY

Backend engineer (2 yrs) working across Python and .NET, focused on LLM-integrated document pipelines and cost-efficient AI tooling. Built a production PDF extraction and comparison system processing 500+ documents per cycle, and an open-source prompt-routing layer that cut inference spend by ~60%.

---

## EXPERIENCE

**Propel Technologies** — Backend Developer
Chennai, India | Aug 2024 – Present

- Built the document-comparison pipeline for a B2B tax-review platform: a .NET REST API uploads tax-form PDFs to Azure Blob Storage and tracks processing status, then triggers a Python worker that extracts, compares, and stores form differences with an LLM-generated summary of each change — processing 500+ documents per review cycle.
- Developed coordinate-based PDF field extraction in Python with PyMuPDF, driven by a JSON locator schema, cutting new IRS form onboarding from ~3 days of code changes to under a day of configuration.
- Added missing-page detection and page-number identification to the Python worker, and reworked it to read and write directly from PostgreSQL instead of local JSON files, removing a manual Excel export step from every review cycle.
- Migrated the .NET backend from a layered design to CQRS-based Clean Architecture (MediatR, EF Core, Unit of Work), cutting the time to add a new review tool from ~2 weeks to ~4 days.
- Redesigned and normalized the PostgreSQL schema for clients, engagements, and 5 review tools, removing 6 redundant tables and eliminating duplicate client records.
- Optimized EF Core data access with split queries and shared query helpers, removing N+1 patterns and reducing reporting endpoint response times from ~8s to under 2s.

**Mallow Technologies** — Frontend Developer Intern
Coimbatore, India | Jun 2023 – Dec 2023

- Built responsive interfaces for a time-tracking web application using React.js and Redux, with reusable components for shared layout and state.
- Integrated frontend components with backend REST APIs and participated in code reviews.

---

## PROJECTS

**Profile Router** — TypeScript, Node.js, JSON Schema
github.com/sahidhh/profile-router

- Extension for an AI coding agent that classifies every prompt against a keyword-scored profile table and routes it to the appropriate model, reasoning level, toolset, and rule set.
- Classifier uses word-boundary keyword scoring with zero LLM calls, so routing itself costs nothing; ships 7 profiles (lookup, hotfix, investigation, implementation, architecture, review, premium) with a fallback chain per tier.
- Reduced inference spend by roughly 60% by routing retrieval and quick-fix prompts to cheap models while reserving stronger models for architecture and review work.
- Wrote unit, reachability, and regression tests that fail the build when a new keyword makes one profile outrank another on its own trigger prompt.

**Job Aggregation Pipeline** — Python, SQLite, sentence-transformers, Gemini API
github.com/sahidhh/jobhunt

- Aggregates job listings from public ATS board APIs (Greenhouse, Lever, Ashby) and open datasets, normalizing every source into a single job schema with a stable ID for deduplication.
- Ranks listings against a parsed resume using a hybrid score: sentence-transformer embeddings plus explicit skill overlap.
- Caches resume parsing by file hash in SQLite so each document is parsed exactly once, and routes all LLM calls through a provider-agnostic abstraction layer.
- Delivers ranked matches to a Telegram bot on a GitHub Actions schedule, keeping inference cost near zero across 100+ listings processed per day.

**Learning Card Generator** — TypeScript, JSON Schema, jsPDF
github.com/sahidhh/learning-card-generator

- Mobile-first micro-learning web app that renders any topic as a scrollable feed of bite-sized learning cards.
- Defined a typed JSON schema of 10+ card types (concept, analogy, code, quiz, comparison, recap) as the contract between an LLM content generator and the renderer.
- Implemented ZIP export producing a vector-text PDF, JSON, and Markdown, replacing a screenshot-based PDF with selectable, searchable output ~10x smaller in file size.

---

## TECHNICAL SKILLS

**Languages:** Python, C#, TypeScript, JavaScript, SQL

**AI & Data:** LLM API integration (Gemini, OpenAI-compatible), prompt design, token-cost optimization, sentence-transformers embeddings, PyMuPDF, structured JSON extraction

**Backend:** .NET / ASP.NET Core Web API, CQRS, Clean Architecture, MediatR, Entity Framework Core, REST APIs, Node.js

**Databases:** PostgreSQL, SQL Server, SQLite

**Cloud & Tooling:** Azure (Blob Storage, Entra ID), Docker, Git, GitHub Actions, Postman

**Frontend:** Angular, React.js, TypeScript

---

## EDUCATION

**B.Tech, Information Technology** — Karpagam College of Engineering, Coimbatore | 2020 – 2024
