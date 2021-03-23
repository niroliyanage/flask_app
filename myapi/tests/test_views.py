from app.views import app

def test_home():
    """
    GIVEN a return text
    WHEN the landing page is hit
    THEN ensure hello world! is returned
    """  
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'hello world'

def test_status():
    """
    GIVEN check for metadata
    WHEN the metadata endpoint is hit
    THEN json payload with metadata is returned
    """      
    response = app.test_client().get('/meta')
    assert response.status_code == 200
    assert b"version" in response.data
    assert b"description" in response.data
    assert b"lastcommitsha" in response.data
