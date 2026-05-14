import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app")))

from app import app, notes


def test_home_page():
    tester = app.test_client()
    response = tester.get("/")

    assert response.status_code == 200


def test_add_note():
    tester = app.test_client()

    response = tester.post("/add", data={"note": "Test Note"}, follow_redirects=True)

    assert response.status_code == 200
    assert "Test Note" in notes
