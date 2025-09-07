import subprocess

def test_python_in_docker():
    result = subprocess.run(
        ["python", "-c", "print('Hello from Docker!')"],
        capture_output=True, text=True
    )
    assert "Hello from Docker!" in result.stdout