from dockerspawner import DockerSpawner
from oauthenticator.generic import GenericOAuthenticator
import os

c.JupyterHub.spawner_class = DockerSpawner
c.DockerSpawner.debug = True

c.DockerSpawner.image = 'jupyter/base-notebook:latest'
c.DockerSpawner.remove = False
c.DockerSpawner.name_template = 'jupyterhub-{username}'
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': '/home/jovyan/work' }

# Authenticator: Keycloak OIDC
c.JupyterHub.authenticator_class = GenericOAuthenticator
c.GenericOAuthenticator.client_id = os.environ['KEYCLOAK_CLIENT_ID']
c.GenericOAuthenticator.client_secret = os.environ['KEYCLOAK_CLIENT_SECRET']
c.GenericOAuthenticator.oauth_callback_url = os.environ['KEYCLOAK_REDIRECT_URI']

KEYCLOAK_BASE = os.environ['KEYCLOAK_BASE_URL']
REALM = os.environ['KEYCLOAK_REALM']

c.GenericOAuthenticator.authorize_url = f"{KEYCLOAK_BASE}realms/{REALM}/protocol/openid-connect/auth"
c.GenericOAuthenticator.token_url = f"{KEYCLOAK_BASE}realms/{REALM}/protocol/openid-connect/token"
c.GenericOAuthenticator.userdata_url = f"{KEYCLOAK_BASE}realms/{REALM}/protocol/openid-connect/userinfo"
c.GenericOAuthenticator.userdata_method = 'GET'
c.GenericOAuthenticator.username_key = 'preferred_username'

# Admins
c.Authenticator.admin_users = {'truongtpa'}

# JupyterLab giao diện
c.Spawner.default_url = '/lab'

# Network JupyterLab
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = "jupyterhub_net"
c.JupyterHub.hub_ip = '0.0.0.0'
