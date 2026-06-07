from rag.analyze import analyze_issue

result = analyze_issue(
    "Login fails after password reset",
    """
    After resetting password,
    users cannot login.
    System shows invalid credentials.
    """
)

print(result)