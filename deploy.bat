@echo off

echo "DOCKER COMPOSE DOWN"
docker compose down --remove-orphans

echo "DOCKER COMPOSE UP"
docker compose up --build -d

echo "DOCKER PS"
docker ps

echo "SHOWING PROMPT GENERATOR LOGS"
for /f "tokens=*" %%i in ('docker ps --format "{{.Names}}" ^| findstr /i "prompt_generator"') do (
    echo "Found prompt generator container: %%i"
    docker logs -f %%i
    exit /b
)

echo "Prompt generator container not found. Available containers are:"
docker ps --format "{{.Names}}"