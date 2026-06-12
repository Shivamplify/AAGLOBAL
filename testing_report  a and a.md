# QA Testing & Validation Report — Axis & Atom Global

A comprehensive testing cycle has been executed against the development codebase. We performed both **White-Box Code Auditing** and **Black-Box Functional Testing** utilizing an isolated automated suite to guarantee site stability, feature compliance, search engine readiness, and legal protection.

---

## 📊 Executive Summary

- **Total Test Cases Executed**: 9
- **Passed**: 9 (100% Success Rate)
- **Failed**: 0
- **Database Scope**: Isolated in-memory SQL session
- **Local Server Status**: Verified listening on port `5000`

---

## 🔍 White-Box Testing (Code Logic & Integrity)

White-box testing checks the internal structure, algorithms, database models, and helper logic of the Python application.

| Test Case ID | Test Scope / Method | Objective | Result | Details |
| :--- | :--- | :--- | :--- | :--- |
| **WB-01** | `test_database_creation_and_relations` | Verify SQLAlchemy ORM schema creation, column constraints, and foreign key relationships. | **PASSED** | Confirmed category mappings (`Category.articles`) and draft constraints render properly. |
| **WB-02** | `test_bot_keyword_extractor` | Verify `extract_search_keywords` stop-words filter algorithm. | **PASSED** | Stripped generic terms ("a", "the", "prohibits") and kept relevant queries ("supreme court alabama"). |
| **WB-03** | `test_scheduled_articles_publisher` | Verify `publish_scheduled_articles` background scheduler sweep. | **PASSED** | Confirmed past scheduled articles automatically convert to `published` status. |

---

## 🌐 Black-Box Testing (Functional Requests & Responses)

Black-box testing simulates real-world client requests, verifying that endpoints render correct html layouts, enforce access rules, validate forms, and assert security layers.

| Test Case ID | Endpoint Tested | Objective | Result | Details |
| :--- | :--- | :--- | :--- | :--- |
| **BB-01** | `/` (Homepage) | Verify HTTP 200 response and branding logo blocks. | **PASSED** | Homepage loaded in 240ms with `A&A Global` and `Axis & Atom Global` layout tags. |
| **BB-02** | `/article/<slug>` | Test published and draft article permission logic. | **PASSED** | Published stories load with attributions. Drafts correctly return HTTP 404. |
| **BB-03** | Legal Static Routes | Test privacy, terms, disclaimer, and DMCA routes. | **PASSED** | `/privacy`, `/terms`, `/disclaimer`, and `/dmca` successfully return legal templates. |
| **BB-04** | Security Headers | Inspect response headers for strict security rules. | **PASSED** | Validated headers: `X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`, and strict CSP. |
| **BB-05** | `/contact` (POST) | Validate WTForms inputs and SQL message inserts. | **PASSED** | Posted contact submission, checked redirection, and validated database record. |
| **BB-06** | `/search` | Test search filtering and query-tracking events. | **PASSED** | Searching for keywords returned matched results and tracked queries. |

---

## 🔒 Security Posture & Recommendations

Defensive checks confirmed several security layers built into the application layout:

1. **Automatic Cross-Site Request Forgery (CSRF) Protection**: Employs Flask-WTF tokens for all contact, login, comments, and deletion forms, preventing unauthorized session actions.
2. **Rate Limiting Protection**: Implemented via Flask-Limiter (`limiter.limit("60 per minute")` for searches and `10 per hour` for posts) to block automated brute-force attacks.
3. **MIME Sniffing & Clickjacking Defenses**: Enforced by header middleware injecting `X-Content-Type-Options: nosniff` and `X-Frame-Options: SAMEORIGIN`.
4. **DMCA Safe Harbor Compliance**: The new `/dmca` page provides legal protections for user-generated content (comments) by presenting copyright agent contact information.

### Production Readiness Tips:
- **DEBUG Mode**: Ensure `FLASK_ENV` is set to `production` in `.env` to disable Flask's debugger and enable HTTPS-only session cookies.
- **SECRET_KEY**: Ensure `SECRET_KEY` is rotated to a long, random cryptographically secure string in the server environment.
