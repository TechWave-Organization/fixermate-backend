# Fixermate-Backend


Create Root User:
python manage.py shell < seeds/create_root_user.py
# Container Management Commands

This project provides two bash commands for managing the container:

## Rebuild and Restart the Container

To rebuild and restart the container, run the following command:

```bash
sudo bash run restart
```
This command will stop the current container, rebuild it with the latest configurations from docker-compose.yml, and then start the container again. Your data will be preserved during this process.

## Start the Container
To start the container without rebuilding, run the following command:

```bash
sudo bash run start
```
