FROM python:3.10.7-alpine AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .


FROM base AS app
RUN pip install gunicorn
CMD ["gunicorn", "todo_list.wsgi:application"]


FROM base AS tests
CMD ["python", "manage.py", "test"]
