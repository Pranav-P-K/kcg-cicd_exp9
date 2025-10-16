# #!/usr/bin/env python3
# """
# Test runner script for the Flask API.
# Usage: python run_tests.py [options]
# """

# import sys
# import subprocess
# from pathlib import Path


# def run_tests():
#     """Run all tests using pytest."""
#     project_root = Path(__file__).parent
#     test_file = project_root / "test_app.py"

#     # Build pytest command
#     cmd = [
#         sys.executable,
#         "-m",
#         "pytest",
#         str(test_file),
#         "-v",  # verbose output
#         "--tb=short",  # shorter traceback format
#         "--color=yes",  # colored output
#     ]

#     print(f"Running tests from: {test_file}")
#     print(f"Command: {' '.join(cmd)}")
#     print("-" * 50)

#     # Run the tests
#     result = subprocess.run(cmd, cwd=str(project_root))

#     if result.returncode == 0:
#         print("\n✅ All tests passed!")
#     else:
#         print("\n❌ Some tests failed!")
#         sys.exit(result.returncode)


# def run_tests_with_coverage():
#     """Run tests with coverage report."""
#     project_root = Path(__file__).parent
#     test_file = project_root / "test_app.py"

#     # Install pytest-cov if not available
#     try:
#         import pytest_cov
#     except ImportError:
#         print("Installing pytest-cov for coverage reporting...")
#         subprocess.run([sys.executable, "-m", "pip", "install", "pytest-cov"])

#     cmd = [
#         sys.executable,
#         "-m",
#         "pytest",
#         str(test_file),
#         "--cov=app",
#         "--cov-report=term-missing",
#         "--cov-report=html",
#         "-v",
#     ]

#     print(f"Running tests with coverage from: {test_file}")
#     print(f"Command: {' '.join(cmd)}")
#     print("-" * 50)

#     result = subprocess.run(cmd, cwd=str(project_root))

#     if result.returncode == 0:
#         print("\n✅ All tests passed!")
#         print("📊 Coverage report generated in htmlcov/index.html")
#     else:
#         print("\n❌ Some tests failed!")
#         sys.exit(result.returncode)


# if __name__ == "__main__":
#     if len(sys.argv) > 1 and sys.argv[1] == "--coverage":
#         run_tests_with_coverage()
#     else:
#         run_tests()
