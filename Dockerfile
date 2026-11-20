FROM python:3.11-slim

WORKDIR /usr/src/app

COPY *.py ./
COPY inventory.json products.csv ./
COPY tests/ ./tests/

CMD ["python", "inventory_manager_oop.py"]