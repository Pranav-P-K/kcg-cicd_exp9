# import pytest
# import json
# from app import create_app


# @pytest.fixture
# def app():
#     """Create and configure a new app instance for each test."""
#     app = create_app()
#     app.config["TESTING"] = True
#     return app


# @pytest.fixture
# def client(app):
#     """A test client for the app."""
#     return app.test_client()


# class TestBasicEndpoints:
#     """Test basic API endpoints."""

#     def test_index(self, client):
#         """Test the index endpoint."""
#         response = client.get("/")
#         assert response.status_code == 200
#         data = json.loads(response.data)
#         assert data["message"] == "Welcome to the Flask API"

#     def test_health(self, client):
#         """Test the health check endpoint."""
#         response = client.get("/health")
#         assert response.status_code == 200
#         data = json.loads(response.data)
#         assert data["status"] == "ok"


# class TestEchoEndpoint:
#     """Test the echo endpoint."""

#     def test_echo_valid_json(self, client):
#         """Test echo endpoint with valid JSON."""
#         test_data = {"message": "Hello, World!", "number": 42}
#         response = client.post(
#             "/echo", data=json.dumps(test_data), content_type="application/json"
#         )
#         assert response.status_code == 200
#         data = json.loads(response.data)
#         assert data["echo"] == test_data

#     def test_echo_empty_json(self, client):
#         """Test echo endpoint with empty JSON."""
#         response = client.post(
#             "/echo", data=json.dumps({}), content_type="application/json"
#         )
#         assert response.status_code == 200
#         data = json.loads(response.data)
#         assert data["echo"] == {}

#     def test_echo_invalid_json(self, client):
#         """Test echo endpoint with invalid JSON."""
#         response = client.post(
#             "/echo", data="invalid json", content_type="application/json"
#         )
#         assert response.status_code == 400
#         # Flask returns HTML error page for malformed JSON, not our JSON error
#         assert b"Bad Request" in response.data

#     def test_echo_no_content_type(self, client):
#         """Test echo endpoint without JSON content type."""
#         response = client.post("/echo", data="some data")
#         assert response.status_code == 400
#         data = json.loads(response.data)
#         assert data["error"] == "Invalid JSON"


# class TestTodoEndpoints:
#     """Test todo-related endpoints."""

#     def test_list_todos_empty(self, client):
#         """Test listing todos when none exist."""
#         response = client.get("/todos")
#         assert response.status_code == 200
#         data = json.loads(response.data)
#         assert data == []

#     def test_create_todo_valid(self, client):
#         """Test creating a valid todo."""
#         todo_data = {"title": "Test Todo"}
#         response = client.post(
#             "/todos", data=json.dumps(todo_data), content_type="application/json"
#         )
#         assert response.status_code == 201
#         data = json.loads(response.data)
#         assert data["id"] == 1
#         assert data["title"] == "Test Todo"

#     def test_create_todo_missing_title(self, client):
#         """Test creating a todo without title."""
#         todo_data = {}
#         response = client.post(
#             "/todos", data=json.dumps(todo_data), content_type="application/json"
#         )
#         assert response.status_code == 400
#         data = json.loads(response.data)
#         assert data["error"] == "`title` is required"

#     def test_create_todo_empty_title(self, client):
#         """Test creating a todo with empty title."""
#         todo_data = {"title": ""}
#         response = client.post(
#             "/todos", data=json.dumps(todo_data), content_type="application/json"
#         )
#         assert response.status_code == 400
#         data = json.loads(response.data)
#         assert data["error"] == "`title` is required"

#     def test_create_todo_invalid_title_type(self, client):
#         """Test creating a todo with non-string title."""
#         todo_data = {"title": 123}
#         response = client.post(
#             "/todos", data=json.dumps(todo_data), content_type="application/json"
#         )
#         assert response.status_code == 400
#         data = json.loads(response.data)
#         assert data["error"] == "`title` is required"

#     def test_create_todo_invalid_json(self, client):
#         """Test creating a todo with invalid JSON."""
#         response = client.post(
#             "/todos", data="invalid json", content_type="application/json"
#         )
#         assert response.status_code == 400
#         # Flask returns HTML error page for malformed JSON, not our JSON error
#         assert b"Bad Request" in response.data

#     def test_list_todos_after_creation(self, client):
#         """Test listing todos after creating some."""
#         # Create first todo
#         todo1_data = {"title": "First Todo"}
#         client.post(
#             "/todos", data=json.dumps(todo1_data), content_type="application/json"
#         )

#         # Create second todo
#         todo2_data = {"title": "Second Todo"}
#         client.post(
#             "/todos", data=json.dumps(todo2_data), content_type="application/json"
#         )

#         # List todos
#         response = client.get("/todos")
#         assert response.status_code == 200
#         data = json.loads(response.data)
#         assert len(data) == 2
#         assert data[0]["title"] == "First Todo"
#         assert data[1]["title"] == "Second Todo"

#     def test_delete_todo_exists(self, client):
#         """Test deleting an existing todo."""
#         # Create a todo first
#         todo_data = {"title": "Todo to Delete"}
#         create_response = client.post(
#             "/todos", data=json.dumps(todo_data), content_type="application/json"
#         )
#         todo = json.loads(create_response.data)
#         todo_id = todo["id"]

#         # Delete the todo
#         response = client.delete(f"/todos/{todo_id}")
#         assert response.status_code == 204
#         assert response.data == b""

#         # Verify it's deleted by listing todos
#         list_response = client.get("/todos")
#         data = json.loads(list_response.data)
#         assert len(data) == 0

#     def test_delete_todo_not_exists(self, client):
#         """Test deleting a non-existent todo."""
#         response = client.delete("/todos/999")
#         assert response.status_code == 404
#         data = json.loads(response.data)
#         assert data["error"] == "Todo not found"

#     def test_todo_workflow(self, client):
#         """Test a complete todo workflow: create, list, delete."""
#         # Initially empty
#         response = client.get("/todos")
#         assert len(json.loads(response.data)) == 0

#         # Create todos
#         for i in range(3):
#             todo_data = {"title": f"Todo {i+1}"}
#             response = client.post(
#                 "/todos", data=json.dumps(todo_data), content_type="application/json"
#             )
#             assert response.status_code == 201

#         # List todos
#         response = client.get("/todos")
#         todos = json.loads(response.data)
#         assert len(todos) == 3

#         # Delete middle todo
#         response = client.delete("/todos/2")
#         assert response.status_code == 204

#         # Verify deletion
#         response = client.get("/todos")
#         todos = json.loads(response.data)
#         assert len(todos) == 2
#         todo_ids = [todo["id"] for todo in todos]
#         assert 2 not in todo_ids
#         assert 1 in todo_ids
#         assert 3 in todo_ids


# class TestErrorHandling:
#     """Test error handling and edge cases."""

#     def test_invalid_endpoints(self, client):
#         """Test accessing non-existent endpoints."""
#         response = client.get("/nonexistent")
#         assert response.status_code == 404

#         response = client.post("/nonexistent")
#         assert response.status_code == 404

#     def test_invalid_http_methods(self, client):
#         """Test using invalid HTTP methods on existing endpoints."""
#         # POST on health endpoint (should only accept GET)
#         response = client.post("/health")
#         assert response.status_code == 405

#         # PUT on todos endpoint (not implemented)
#         response = client.put("/todos")
#         assert response.status_code == 405

#         # GET on echo endpoint (should only accept POST)
#         response = client.get("/echo")
#         assert response.status_code == 405
