from fastapi.testclient import TestClient

from truck_agent.main import app

client = TestClient(app)

def test_single_cargo_should_result_in_deliver_response():
    """
    Use this test to check if the truck_agent is working correctly.
    Currently it tests only one cargo offer, but you can add more and adjust the test.
    Of course, when you change the agent, you should also change this test.
    """
    payload = open("tests/decide.json", "r").read()
    response = client.post(
        "/decide",
        headers={"Content-Type": "application/json"},
        data=payload,
    )
    assert response.status_code == 200
    assert response.json() == {
        "command": "DELIVER",
        "argument": "10",
    }
