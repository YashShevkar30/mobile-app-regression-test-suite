# Mobile App Regression Test Suite

Cross-platform mobile regression automation built with Python and Appium for Android and iOS emulator targets.

## What is automated
- Login and logout flows
- Core navigation scenarios
- Basic profile update validation
- Common user journey smoke checks across device profiles

## Maintenance approach
- Track iterative suite enhancements in Git history (40+ expected over time)
- Keep traceability documents aligned to user stories and release scope
- Publish standardized regression summaries for QA and product stakeholders

## Reliability strategy
- Explicit waits around asynchronous UI states
- Stable locator hierarchy with fallback selectors
- Flaky test diagnostics with retry-safe logging
- Suite stability target above 95% by reducing timing and locator-related failures
