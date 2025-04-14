# Load environment variables from .env file
Get-Content .env | ForEach-Object {
    if ($_ -match '^([^=]+)=(.*)$') {
        $name = $matches[1]
        $value = $matches[2]
        Set-Item -Path "Env:$name" -Value $value
    }
}

# Login to Docker Registry
Write-Host "Logging in to Docker Registry..."
$env:DOCKER_USERNAME = $env:DOCKER_USERNAME
$env:DOCKER_TOKEN = $env:DOCKER_TOKEN
$env:REGISTRY = $env:REGISTRY

# Login using the credentials
docker login $env:REGISTRY -u $env:DOCKER_USERNAME -p $env:DOCKER_TOKEN

Write-Host "Docker login completed!" 