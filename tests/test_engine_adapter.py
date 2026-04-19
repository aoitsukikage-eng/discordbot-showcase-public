from src.engine_adapter import EngineRequest, MockEngineAdapter


def test_mock_engine_adapter_returns_text():
    adapter = MockEngineAdapter()
    req = EngineRequest(
        model="demo-model",
        system_prompt="system",
        user_prompt="hello",
        timeout_sec=10,
    )
    out = adapter.call_ai(req)
    assert out.provider == "mock"
    assert out.error is None
    assert "mock-response" in out.text
