# Container Technologies

## Docker

### Core Components

#### Docker Engine
- Docker daemon (dockerd)
- REST API
- Docker CLI
- containerd integration

#### Docker Objects
```dockerfile
# Example Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

### Image Management
```bash
# Common image commands
docker build -t myapp:1.0 .
docker tag myapp:1.0 registry.example.com/myapp:1.0
docker push registry.example.com/myapp:1.0
docker pull nginx:latest
```

### Container Lifecycle
```bash
# Container lifecycle commands
docker run -d --name webapp myapp:1.0
docker stop webapp
docker start webapp
docker restart webapp
docker rm webapp
```

### Networking
1. Bridge Networks
```bash
docker network create mynetwork
docker run --network mynetwork myapp:1.0
```

2. Host Networking
```bash
docker run --network host myapp:1.0
```

3. Overlay Networks
```bash
docker network create -d overlay myswarm
```

### Storage
1. Volumes
```bash
docker volume create mydata
docker run -v mydata:/data myapp:1.0
```

2. Bind Mounts
```bash
docker run -v $(pwd):/app myapp:1.0
```

### Docker Compose
```yaml
# docker-compose.yml example
version: '3.8'
services:
  webapp:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
    depends_on:
      - db
  db:
    image: postgres:13
    volumes:
      - db-data:/var/lib/postgresql/data
volumes:
  db-data:
```

## containerd

### Architecture
1. Core Components
   - containerd daemon
   - CRI plugin
   - containerd-shim
   - runc

2. Plugin System
   - Snapshotter plugins
   - Content plugins
   - Service plugins

### Container Runtime Interface (CRI)
```go
// Example CRI implementation
type RuntimeService interface {
    RunPodSandbox(config *PodSandboxConfig) (string, error)
    StopPodSandbox(podSandboxID string) error
    RemovePodSandbox(podSandboxID string) error
    // ...other methods
}
```

### Command Line Tool (ctr)
```bash
# Basic containerd commands
ctr images pull docker.io/library/nginx:latest
ctr run docker.io/library/nginx:latest web
ctr tasks ls
ctr containers ls
```

### Namespace Management
```bash
# Namespace operations
ctr ns create myproject
ctr ns ls
ctr -n myproject containers ls
```

### Image Management
```bash
# Image operations
ctr images pull docker.io/library/redis:latest
ctr images tag docker.io/library/redis:latest myredis:v1
ctr images rm docker.io/library/redis:latest
```

## Security Considerations

### Docker Security
1. Image Security
   - Scan for vulnerabilities
   - Use minimal base images
   - Sign images
   - Implement content trust

2. Runtime Security
```json
{
    "default-runtime": "runc",
    "seccomp-profile": "/etc/docker/seccomp.json",
    "no-new-privileges": true,
    "selinux-enabled": true
}
```

### containerd Security
1. Security Features
   - Namespace isolation
   - cgroup constraints
   - Seccomp profiles
   - AppArmor integration

2. Best Practices
   - Regular security updates
   - Minimal runtime privileges
   - Network policy enforcement
   - Image signing verification

## Performance Optimization

### Docker Optimization
1. Image Size
```dockerfile
# Multi-stage build example
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

2. Layer Caching
```dockerfile
# Optimize layer caching
COPY package*.json ./
RUN npm install
COPY . .
```

### containerd Optimization
1. Resource Constraints
```bash
# Set resource limits
ctr run --memory-limit 512m --cpu-quota 50000 image-name container-name
```

2. Snapshot Optimization
- Overlayfs configuration
- Garbage collection tuning
- Snapshot compression

## Monitoring and Logging

### Docker Monitoring
```bash
# Basic monitoring commands
docker stats
docker events
docker logs webapp
```

### containerd Monitoring
1. Metrics
   - Prometheus integration
   - Custom metric collection
   - Performance monitoring

2. Logging
```bash
# Configure containerd logging
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
  runtime_type = "io.containerd.runc.v2"
  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
    SystemdCgroup = true
```

## Best Practices

### Docker Best Practices
1. Image Building
   - Use .dockerignore
   - Minimize layers
   - Multi-stage builds
   - Version pinning

2. Runtime
   - Resource limits
   - Health checks
   - Logging configuration
   - Network isolation

### containerd Best Practices
1. Configuration
   - Proper plugin setup
   - Resource management
   - Security configuration
   - Monitoring integration

2. Operations
   - Regular garbage collection
   - Backup procedures
   - Update strategies
   - High availability setup

## References
- Docker Documentation
- containerd Documentation
- OCI Runtime Specification
- Kubernetes CRI Documentation