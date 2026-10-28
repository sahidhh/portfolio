# Sahidhullah H

L2 Software Engineer | .NET, C#, ASP.NET Core, PostgreSQL, Azure

Chennai, Tamil Nadu, India | +91 9789442466 | sahidhullah@gmail.com
sahidhh.github.io/portfolio | linkedin.com/in/sahidh-h | github.com/sahidhh

---

## SUMMARY

Backend-leaning engineer with 2+ years on .NET 8, C#, ASP.NET Core, PostgreSQL and Azure, working on CQRS and Clean Architecture backends for B2B and healthcare platforms. Available to join within 15 days.

---

## TECHNICAL SKILLS

**Backend:** .NET 8, ASP.NET Core, Entity Framework Core, MediatR, CQRS, Clean Architecture, REST APIs, microservices
**Languages:** C#, SQL, Python, TypeScript, JavaScript, Java, Kotlin
**Databases:** PostgreSQL, SQL Server, MongoDB, SQLite
**Cloud and tools:** Azure (Blob Storage, Entra ID), AWS, Docker, Jenkins, Git, GitHub Actions, unit, integration and load testing
**Frontend:** Angular, React, Redux, HTML, CSS

---

## EXPERIENCE

**Propel Technology Group Inc**, Chennai | Aug 2024 to Sep 2026

L2 Software Engineer (Aug 2026 to Sep 2026), promoted from Back End Developer (Aug 2024 to Aug 2026). Worked on a B2B tax-review platform and a healthcare and e-commerce platform.

- Moved a production backend from a layered design to CQRS and Clean Architecture (MediatR, EF Core, Unit of Work). Adding a new review tool dropped from about 2 weeks to 4 days.
- Redesigned the PostgreSQL schema for clients, engagements and five review tools, removing 6 redundant tables and duplicate client records.
- Cut reporting endpoints from about 8 seconds to under 2 with split queries and shared query helpers, and removed N+1 queries on the read side.
- Owned 8+ backend modules, including Entra ID authentication, IRS form version comparison, audit reporting and Excel export.
- Built the backend of a PDF form-comparison pipeline. A .NET API stores files in Azure Blob and tracks status, and a Python worker extracts text, compares versions and writes an LLM summary of the changes. It handles 500+ documents per cycle.
- On the healthcare platform, designed 20+ REST APIs (orders, appointments, lab tests, payments, prescriptions) serving a mobile app, three web portals and a pharmacy back office. Query tuning and caching cut response times by about 80%.
- Spent several months on a microservice-based tax platform. Wrote unit and integration tests, and Python load tests run against staging and UAT servers. Deployed builds by hand and with simple Docker scripts, using Jenkins, AWS and Azure.

**Frontend Developer Intern**, Mallow Technologies, Coimbatore | Jun 2023 to Dec 2023

- Built responsive React and Redux screens for a time-tracking app and connected them to REST APIs.

---

## PROJECTS

**Job Discovery Pipeline** | Next.js, TypeScript, Supabase, GitHub Actions

- Scrapes six job boards twice a day, scores postings in two stages (keywords first, LLM only for those that pass) and sends one Telegram digest. A notifications log gives at-most-once delivery.

---

## EDUCATION

**B.Tech, Information Technology**, Karpagam College of Engineering, Coimbatore | 2020 to 2024
