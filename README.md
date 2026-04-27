# Mobile App Regression Test Suite

Cross-platform mobile regression automation built with Python and Appium for Android and iOS emulator targets.

## What is automated
- Login and logout flows
- Core navigation scenarios
- Basic profile update validation
- Common user journey smoke checks across device profiles

## Reliability strategy
- Explicit waits around asynchronous UI states
- Stable locator hierarchy with fallback selectors
- Flaky test diagnostics with retry-safe logging
