# Sahidhullah H

L2 Software Engineer | Python, .NET | Document pipelines and AI tooling

Chennai, Tamil Nadu, India | +91 9789442466 | sahidhullah@gmail.com
sahidhh.github.io/portfolio | linkedin.com/in/sahidh-h | github.com/sahidhh

---

## SUMMARY

Backend-leaning engineer with 2+ years on .NET 8, C#, PostgreSQL and Azure, plus Python for document processing, load testing and LLM work, and agent tooling on my own time. Available to join within 15 days.

---

## TECHNICAL SKILLS

**Languages:** Python, C#, TypeScript, JavaScript, SQL, Java, Kotlin
**AI and agents:** prompt engineering, LLM integration, agentic development, agent harness design
**Backend:** .NET 8, ASP.NET Core, Entity Framework Core, MediatR, CQRS, Clean Architecture, REST APIs, microservices, FastAPI, Node.js
**Databases:** PostgreSQL, SQL Server, MongoDB, SQLite
**Cloud and tools:** Azure (Blob Storage, Entra ID), AWS, Docker, Jenkins, Git, GitHub Actions, unit, integration and load testing

---

## EXPERIENCE

**Propel Technology Group Inc**, Chennai | Aug 2024 to Sep 2026

L2 Software Engineer (Aug 2026 to Sep 2026), promoted from Back End Developer (Aug 2024 to Aug 2026). Worked on a B2B tax-review platform and a healthcare and e-commerce platform.

- Built the backend of a PDF form-comparison pipeline. A .NET API stores files in Azure Blob and tracks status, and a Python worker extracts text, compares versions and writes an LLM summary of the changes. It handles 500+ documents per cycle.
- Wrote Python load tests that I ran against staging and UAT servers for several projects, plus unit and integration tests on a microservice-based tax platform.
- Moved a production backend from a layered design to CQRS and Clean Architecture (MediatR, EF Core, Unit of Work). Adding a new review tool dropped from about 2 weeks to 4 days.
- Cut reporting endpoints from about 8 seconds to under 2 with split queries and shared query helpers, and removed N+1 queries on the read side.

**Frontend Developer Intern**, Mallow Technologies, Coimbatore | Jun 2023 to Dec 2023

- Built responsive React and Redux screens for a time-tracking app and connected them to REST APIs.

---

## PROJECTS

**Job Discovery Pipeline** | Next.js, TypeScript, Supabase, GitHub Actions

- Scrapes six job boards twice a day, scores postings in two stages (keywords first, LLM only for those that pass) and sends one Telegram digest. A notifications log gives at-most-once delivery. Live at job-scraper-liart.vercel.app.

**pi-lean and pi-fleet** | TypeScript, Node, systemd, micro-VM sandbox

- Sandboxed coding-agent runner: agent tools execute in a micro-VM on a throwaway copy of the project, and I review one exported patch. Prompt and tool tuning cut input tokens 40 to 70 percent, and a 6-task eval passes 12 of 12 runs.

---

## EDUCATION

**B.Tech, Information Technology**, Karpagam College of Engineering, Coimbatore | 2020 to 2024
