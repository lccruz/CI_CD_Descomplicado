import os

from src import create_app

app = create_app()

if __name__ == "__main__":
    app = create_app()
    print("Running on port 8080")
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
