FROM python:3.11-slim

WORKDIR /usr/src/app

COPY *.py ./
COPY inventory.json ./

CMD ["python", "inventory_manager_oop.py"]