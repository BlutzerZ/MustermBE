# 
FROM python:3.10
# 
WORKDIR /app/musterm-be

# 
COPY ./requirements.txt /app/musterm-be/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/musterm-be/requirements.txt

# 
COPY . /app/musterm-be

# 
CMD ["fastapi", "run", "main.py", "--port", "8001"]