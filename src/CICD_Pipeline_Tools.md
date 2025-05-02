# CI/CD Pipeline Tools

## GitHub Actions

### Basic Workflow
```yaml
# Example GitHub Actions workflow
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
    - name: Install dependencies
      run: npm ci
    - name: Run tests
      run: npm test
    - name: Build
      run: npm run build
```

### Advanced Features
- Matrix builds
- Environment secrets
- Artifact management
- Self-hosted runners
- Composite actions

## Jenkins

### Pipeline as Code
```groovy
// Example Jenkinsfile
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'mvn -B -DskipTests clean package'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh './deploy.sh'
            }
        }
    }
}
```

### Key Features
- Extensive plugin ecosystem
- Master-agent architecture
- Shared libraries
- Pipeline templates
- Build artifacts management

## Azure DevOps

### Azure Pipelines
```yaml
# Example Azure Pipeline
trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

variables:
  buildConfiguration: 'Release'

steps:
- task: DotNetCoreCLI@2
  inputs:
    command: 'restore'
    projects: '**/*.csproj'

- task: DotNetCoreCLI@2
  inputs:
    command: 'build'
    projects: '**/*.csproj'
    arguments: '--configuration $(buildConfiguration)'

- task: DotNetCoreCLI@2
  inputs:
    command: 'test'
    projects: '**/*Tests/*.csproj'
    arguments: '--configuration $(buildConfiguration)'
```

### Features
- Build and release pipelines
- Work item tracking
- Code repositories
- Test management
- Package management

## GitLab CI/CD

### Pipeline Configuration
```yaml
# Example .gitlab-ci.yml
image: node:18

stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - npm install
    - npm run build
  artifacts:
    paths:
      - dist/

test:
  stage: test
  script:
    - npm run test
  coverage: /All files[^|]*\|[^|]*\s+([\d\.]+)/

deploy:
  stage: deploy
  script:
    - ./deploy.sh
  only:
    - main
```

### Key Features
- Auto DevOps
- Container registry
- Environment management
- Review apps
- Security scanning

## CircleCI

### Configuration Example
```yaml
# Example .circleci/config.yml
version: 2.1

orbs:
  node: circleci/node@4.7

jobs:
  build-and-test:
    docker:
      - image: cimg/node:18.0
    steps:
      - checkout
      - node/install-packages
      - run:
          name: Run tests
          command: npm test
      - store_test_results:
          path: test-results

workflows:
  version: 2
  build-test-deploy:
    jobs:
      - build-and-test
```

### Features
- Orbs (reusable packages)
- Docker layer caching
- SSH debugging
- Resource classes
- Workflow orchestration

## ArgoCD (GitOps)

### Application Definition
```yaml
# Example Application manifest
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/app.git
    targetRevision: HEAD
    path: k8s
  destination:
    server: https://kubernetes.default.svc
    namespace: myapp
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

### Features
- GitOps workflow
- Kubernetes-native
- Multi-cluster support
- Rollback capabilities
- Application health monitoring

## Tool Comparison

### Build Capabilities
| Feature | GitHub Actions | Jenkins | Azure DevOps | GitLab CI | CircleCI |
|---------|---------------|----------|--------------|-----------|-----------|
| Matrix Builds | ✓ | ✓ | ✓ | ✓ | ✓ |
| Container Support | ✓ | ✓ | ✓ | ✓ | ✓ |
| Custom Runners | ✓ | ✓ | ✓ | ✓ | ✓ |
| Caching | ✓ | Plugin | ✓ | ✓ | ✓ |
| Artifacts | ✓ | ✓ | ✓ | ✓ | ✓ |

### Integration Features
| Feature | GitHub Actions | Jenkins | Azure DevOps | GitLab CI | CircleCI |
|---------|---------------|----------|--------------|-----------|-----------|
| Code Review | ✓ | Plugin | ✓ | ✓ | ✓ |
| Security Scanning | ✓ | Plugin | ✓ | ✓ | ✓ |
| Release Management | Limited | Plugin | ✓ | ✓ | Limited |
| Environment Management | ✓ | Plugin | ✓ | ✓ | ✓ |

## Best Practices

### Pipeline Design
1. Keep it Simple
   - Modular stages
   - Clear dependencies
   - Fail fast principle
   - Consistent naming

2. Security
   - Secret management
   - Least privilege access
   - Image scanning
   - Compliance checks

3. Performance
   - Parallel execution
   - Caching strategies
   - Resource optimization
   - Timeout policies

### Infrastructure Considerations
1. Runners/Agents
   - Scaling strategy
   - Resource allocation
   - Network access
   - Security policies

2. Storage
   - Artifact retention
   - Cache management
   - Log storage
   - Backup strategy

## Common Patterns

### Trunk-Based Development
```yaml
# Example branch protection rules
branches:
  main:
    protection:
      required_pull_request_reviews:
        required_approving_review_count: 2
      required_status_checks:
        strict: true
        contexts: ["ci/build", "ci/test"]
```

### Feature Branch Development
```yaml
# Example feature branch workflow
on:
  push:
    branches:
      - 'feature/**'
      - 'bugfix/**'
  pull_request:
    branches: [ main ]
```

### Environment Promotion
```yaml
# Example promotion workflow
environments:
  development:
    deployment:
      auto: true
  staging:
    deployment:
      requires: ['QA']
  production:
    deployment:
      requires: ['approval']
```

## References
- GitHub Actions Documentation
- Jenkins Handbook
- Azure DevOps Documentation
- GitLab CI/CD Documentation
- CircleCI Documentation
- ArgoCD User Guide