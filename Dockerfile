# 
FROM python:3.10
# 
WORKDIR /app/mustermAPI

# 
COPY ./requirements.txt /app/mustermAPI/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/mustermAPI/requirements.txt

# 
COPY . /app/mustermAPI
#
EXPOSE 8000
# 
CMD ["fastapi", "run", "main.py", "--port", "8001"]