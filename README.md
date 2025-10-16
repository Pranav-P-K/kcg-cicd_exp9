# Minimal Flask API

This is a minimal Flask project with a simple API for learning and testing.

## Endpoints

- GET / -> welcome message
- GET /health -> returns {"status": "ok"}
- POST /echo -> echoes back posted JSON as {"echo": <payload>}
- GET /todos -> list all todos
- POST /todos -> create a new todo (requires JSON with "title" field)
- DELETE /todos/<id> -> delete a todo by ID

## Quick start

1. Create a virtualenv and activate it:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:

    ```bash
    python app.py
    ```

## Testing

The project includes comprehensive tests using pytest.

### Run all tests

```bash
pytest -v
```

### Run tests with coverage

```bash
python run_tests.py --coverage
```

### Run specific test classes

```bash
# Test only basic endpoints
pytest test_app.py::TestBasicEndpoints -v

# Test only todo endpoints
pytest test_app.py::TestTodoEndpoints -v

# Test only echo endpoint
pytest test_app.py::TestEchoEndpoint -v
```

### Test Structure

- `test_app.py` - Main test file with all API tests
- `pytest.ini` - Pytest configuration
- `run_tests.py` - Convenient test runner script

The tests cover:

- ✅ Basic endpoints (index, health)
- ✅ Echo endpoint with various inputs
- ✅ Todo CRUD operations
- ✅ Error handling and edge cases
- ✅ HTTP method validation
- ✅ JSON validation
