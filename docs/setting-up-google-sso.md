## Setting up Google Single Sign-On (SSO)

1. Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a new project (or select an existing one):

    - **Project name:** *Can be left as default*
    - **Organization:** No organization

1. Go to **APIs & Services** > **OAuth consent screen** and configure your project:

    - **App name:** any name
    - **User support email:** your email
    - **Audience:** External (Internal requires a Google Workspace organization)
    - **Contact Information:** your email

1. Create **OAuth Client** (*keep note of Client ID and Secret!*):

    - **Application Type:** Web Application
    - **Name:** can be left as default
    - **Authorized redirect URIs:**
        - `http://127.0.0.1:8000/accounts/google/login/callback/`
        - `http://localhost:8000/accounts/google/login/callback/`

    ***Save `Client ID` and `Client Secret`!***

1. Create your local `.env` file from the template:

    ```bash
    cp .env.example .env
    ```

    Add your credentials in `.env`:

    ```env
    GOOGLE_CLIENT_ID=<Your_Client_ID>
    GOOGLE_CLIENT_SECRET=<Your_Client_Secret>
    ```

### Test Google SSO on the server

1. Restart the server if already running.
1. Go to `http://127.0.0.1:8000/` (or `http://localhost:8000/`) and sign in directly with **Google**.
1. Verify the following messages appear at the top of the screen upon:
    - **Sign In:** `Successfully signed in as <username>`
    - **Sign Out:** `You have signed out`

### Resources & Documentation

- [django-allauth: Google Provider](https://docs.allauth.org/en/dev/socialaccount/providers/google.html): Official documentation for configuring Google OAuth in `django-allauth`.
- [Google Identity: Using OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/oauth2/web-server): Official guide detailing server-side authorization code exchange and client setup.
- [Google Identity: Authentication URI Parameters](https://developers.google.com/identity/openid-connect/openid-connect#authenticationuriparameters): Reference for query parameters (`prompt`, `access_type`, etc.) passed to Google's authorization endpoint.
