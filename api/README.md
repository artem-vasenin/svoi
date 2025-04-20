# API

## Project to docker
```
docker build -t fastapi:1.0.0 .
docker run -p 8000:8000 fastapi:1.0.0
```

### Compiles and hot-reloads for development
```
uvicorn main:app
```
