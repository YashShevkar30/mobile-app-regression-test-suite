# Test Case Traceability

## User story mapping
- US-101: User signs in with valid credentials -> `tests/test_login_flow.py`
- US-109: User navigates to profile view -> `tests/test_navigation_flow.py`
- US-115: Session persists across app foreground events -> planned
- US-123: User edits profile details -> planned

## Iterative enhancement log
- Added wait-based synchronization helper
- Introduced locator fallback for username input field
- Added profile navigation regression coverage
- Added CI workflow for pull request gating
