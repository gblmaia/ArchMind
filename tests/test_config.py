from config import settings

def test_settings_loaded():
    """Testa se as configurações estão sendo carregadas corretamente."""
    assert settings.LLM_MODEL is not None
    assert settings.CHUNK_SIZE > 0
    assert settings.APP_TITLE == "ArchMind API"