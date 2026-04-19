import pytest

from src.engine_adapter import EngineRequest, ExternalEngineAdapter, MockEngineAdapter


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


def test_external_adapter_raises_guidance_error(monkeypatch):
    monkeypatch.setenv("ENGINE_MODE", "external")
    adapter = ExternalEngineAdapter(
        engine_path="/tmp/private-engine",
        engine_api_env_file="/tmp/private.env",
    )
    req = EngineRequest(
        model="demo-model",
        system_prompt="system",
        user_prompt="hello",
        timeout_sec=10,
    )
    with pytest.raises(RuntimeError) as exc:
        adapter.call_ai(req)
    assert "requires your own private Engine integration" in str(exc.value)
