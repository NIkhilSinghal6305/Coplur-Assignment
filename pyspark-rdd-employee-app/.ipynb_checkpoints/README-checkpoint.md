## Build Docker Image

```bash
docker build -t spark-app-1 .
```

## Run Docker Container

### Linux / macOS

```bash
docker run -it --rm -p 8080:8080 -v "$(pwd):/workspace" spark-app-1
```

### Windows PowerShell

```powershell
docker run -it --rm -p 8080:8080 -v "${PWD}:/workspace" spark-app-1
```

## Access JupyterLab

Open the URL displayed in the terminal, for example:

```text
http://localhost:8080/lab?token=<generated-token>
```