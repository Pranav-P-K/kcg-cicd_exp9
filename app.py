from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello from Flask + Vercel + GitHub Actions!")

@app.route('/about')
def about():
    return jsonify(info="This API was deployed automatically using CI/CD.")

if __name__ == '__main__':
    app.run()

# from flask import Flask, jsonify, request


# def create_app():
#     app = Flask(__name__)

#     # Simple in-memory storage for todos. Stored on app.config so tests
#     # that create new app instances get a fresh store.
#     app.config.setdefault("TODOS", {})
#     app.config.setdefault("NEXT_ID", 1)

#     @app.route("/", methods=["GET"])
#     def index():
#         return jsonify({"message": "Welcome to the Flask API"}), 200

#     @app.route("/health", methods=["GET"])
#     def health():
#         return jsonify({"status": "ok"}), 200

#     @app.route("/echo", methods=["POST"])
#     def echo():
#         if not request.is_json:
#             return jsonify({"error": "Invalid JSON"}), 400
#         data = request.get_json()
#         return jsonify({"echo": data}), 200

#     # Minimal todo endpoints (in-memory)
#     @app.route("/todos", methods=["GET"])
#     def list_todos():
#         todos = list(app.config["TODOS"].values())
#         return jsonify(todos), 200

#     @app.route("/todos", methods=["POST"])
#     def create_todo():
#         if not request.is_json:
#             return jsonify({"error": "Invalid JSON"}), 400
#         data = request.get_json()
#         title = data.get("title")
#         if not title or not isinstance(title, str):
#             return jsonify({"error": "`title` is required"}), 400

#         todo_id = app.config["NEXT_ID"]
#         todo = {"id": todo_id, "title": title}
#         app.config["TODOS"][todo_id] = todo
#         app.config["NEXT_ID"] = todo_id + 1
#         return jsonify(todo), 201

#     @app.route("/todos/<int:todo_id>", methods=["DELETE"])
#     def delete_todo(todo_id: int):
#         todo = app.config["TODOS"].pop(todo_id, None)
#         if not todo:
#             return jsonify({"error": "Todo not found"}), 404
#         return "", 204

#     return app


# if __name__ == "__main__":
#     create_app().run(host="0.0.0.0", port=5000)
