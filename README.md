# To-Dos Application
A FastAPI application to learn how to use FastAPI with SQLAlchemy and PostGreSQL.

# Sample Setup 
- Create a virtual environment using `virtualenv` module in python.
```bash
# Generate virtual environment
python3 -m venv "venv"

# Activate virtual environment
venv/Scripts/activate

# Install depdendency packages
pip install -r requirements.txt
```
- Configure `.env` file by creating a copy from `.env.sample`
- Setup a postgres docker container
```bash
docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=<your-preferred-one> -d postgres:14
```
- At `app` directory, run `alembic` migration command. Please make sure your postgres DB is ready and accessible.
```bash
# Migrate to latest revison
alembic upgrade head
```
- At `app` directory, run `uvicorn` web server from `app` directory (`reload` mode is for development purposes)
```bash
uvicorn main:app --reload
```