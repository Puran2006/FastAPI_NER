If you want to pull and run the image directly from **Docker Hub**, use the following commands:
# Prerequisites
**Docker**

```cmd
docker pull puran2006/fastapi-app:latest
```

Run the container:
```cmd
docker run -p 8000:8000 puran2006/fastapi-app:latest
```

The API will now be accessible at:
- [http://127.0.0.1:8000](http://127.0.0.1:8000)
- [http://localhost:8000](http://localhost:8000)

Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the API.

---
