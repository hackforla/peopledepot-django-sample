# Create your tests here.
import pytest
from django.contrib.auth.models import User
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_unauthenticated_user_sees_sign_in_link(client):
    url = reverse("index")
    response = client.get(url)

    assert response.status_code == 200
    assert any(t.name == "index.html" for t in response.templates)
    content = response.content.decode()
    assert "Sign In" in content
    assert "Sign Out" not in content


def test_login_page_renders_google_sso(client):
    url = reverse("account_login")
    response = client.get(url)

    assert response.status_code == 200
    content = response.content.decode()
    assert "Google" in content


def test_authenticated_user_sees_sign_out(client):
    user = User.objects.create_user(username="testuser", email="test@example.com")
    client.force_login(user)

    url = reverse("index")
    response = client.get(url)

    assert response.status_code == 200
    assert any(t.name == "index.html" for t in response.templates)
    content = response.content.decode()
    assert "Welcome, testuser!" in content
    assert "Sign Out" in content
    assert "Sign In" not in content
