# Sahidhullah H

Backend Developer — .NET

Chennai, India (IST) | Open to Remote — Worldwide | Available for US/EU hours overlap | Full-time or Contract
sahidhullah@gmail.com | linkedin.com/in/sahidh-h | github.com/sahidhh

---

## SUMMARY

Backend developer (2 yrs) building B2B platforms with .NET, CQRS/Clean Architecture, Entity Framework Core, PostgreSQL, and Azure. Migrated a production tax-review platform to Clean Architecture and cut reporting endpoint response times from ~8s to under 2s.

---

## EXPERIENCE

**Propel Technologies** — L2 Software Engineer (promoted from Backend Developer, 2025)
Chennai, India | Aug 2024 – Present

*B2B tax-review platform (.NET, PostgreSQL, Angular, Azure)*

- Migrated the backend from a layered design to CQRS-based Clean Architecture using MediatR, EF Core, and the Unit of Work pattern, cutting the time to add a new review tool from ~2 weeks to ~4 days.
- Redesigned and normalized the PostgreSQL schema modelling clients, engagements, and 5 review tools, removing 6 redundant tables and eliminating duplicate client records.
- Built 8+ backend modules covering Azure Entra ID authentication, IRS-form version comparison, year-over-year comparison, summary and admin audit reporting, Excel export, activity tracking, and bookmarks.
- Optimized EF Core data access using split queries and shared query helpers, removing N+1 patterns and reducing reporting endpoint response times from ~8s to under 2s.
- Built the form-comparison pipeline: a .NET REST API uploads PDFs to Azure Blob Storage and tracks processing status, then triggers a Python worker that extracts and compares forms and persists the differences to PostgreSQL — processing 500+ documents per review cycle.
- Developed the Angular interface for the comparison tools, including a side-by-side view that colour-codes changes, comparison side panels, a dashboard stats banner, and 10+ shared components (collapsible lists, dropdowns, modal overlays).

*Commercial healthcare ecosystem (React Native/Expo, React + Vite/TS, .NET, PostgreSQL, Python)*

- Worked across an end-to-end healthcare platform: patient app for Android and iOS, web portals for healthcare data admins, receptionists and doctors, and a pharmacy back office — one .NET backend and one PostgreSQL schema behind all of them.
- Built doctor scheduling with a custom calendar and role-based access control separating admin, receptionist and doctor views; in-app e-commerce and lab-test booking.
- Pharmacy portal: stock management, order processing, payments, prescription review, bill generation and delivery-partner setup; Python services for document processing and generation.
- Designed 20+ REST APIs, reducing response times by ~80% through query optimization and caching.

**Mallow Technologies** — Frontend Developer Intern
Coimbatore, India | Jun 2023 – Dec 2023

- Built responsive interfaces for a time-tracking web application using React.js and Redux, with reusable components for shared layout and state.
- Integrated frontend components with backend REST APIs, aligned on contracts with designers and backend developers, and participated in code reviews.

---

## PROJECTS

**Job Discovery Pipeline** — TypeScript, Next.js 15, Supabase (Postgres), GitHub Actions
github.com/sahidhh/job-scraper

- Scrapes six job boards twice daily on GitHub Actions, normalizing every source into one schema with a stable ID for deduplication.
- Two-stage scoring (keyword gate, then LLM only above threshold) persisted per (job, role); one Telegram digest per run with at-most-once delivery via a notifications log.
**Profile Router** — TypeScript, Node.js, JSON Schema
github.com/sahidhh/profile-router

- Routing layer for an AI coding agent that classifies each prompt and selects the appropriate model and toolset, with zero LLM calls in the classifier itself.
- Reduced inference spend by roughly 60% by routing simple prompts to cheaper models; covered by unit and regression tests.

---

## TECHNICAL SKILLS

**Languages:** C#, Python, TypeScript, JavaScript, SQL

**Backend:** .NET, .NET Core, ASP.NET Core Web API, CQRS, Clean Architecture, MediatR, Entity Framework Core, REST APIs, Node.js

**Databases:** PostgreSQL, SQL Server, SQLite

**Cloud & DevOps:** Microsoft Azure (Blob Storage, Entra ID), Docker, Git, GitHub Actions, Postman

**Frontend:** Angular, React.js, Redux, HTML5, CSS3

**Other:** PyMuPDF, LLM API integration

---

## EDUCATION

**B.Tech, Information Technology** — Karpagam College of Engineering, Coimbatore | 2020 – 2024
