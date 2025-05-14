# Jupyterhub

JupyterHub là một hệ thống mã nguồn mở giúp nhiều người dùng có thể truy cập và sử dụng các môi trường Jupyter Notebook hoặc JupyterLab riêng biệt thông qua trình duyệt web.

```
git clone https://github.com/beta21s/jupyterhub-keycloak
docker-compose down -v --remove-orphans
docker network create jupyterhub_net
docker-compose up --build
```

![](images/images-1.png)

Giao diện sau khi đăng nhập SSO thành công

![](images/images-2.png)
