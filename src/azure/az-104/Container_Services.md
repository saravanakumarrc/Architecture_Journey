# Azure Container Services (ACI and AKS)

## Overview
Azure provides two main container services: Azure Container Instances (ACI) for simple container workloads and Azure Kubernetes Service (AKS) for orchestrating complex container applications.

## Azure Container Instances (ACI)

### Core Components

```mermaid
graph TB
    A[Container Instance] --> B[Container Group]
    A --> C[Resources]
    A --> D[Networking]
    A --> E[Storage]
    
    B --> B1[Multiple Containers]
    B --> B2[Shared Lifecycle]
    B --> B3[Shared Resources]
    
    C --> C1[CPU]
    C --> C2[Memory]
    C --> C3[GPU]
    
    D --> D1[Public IP]
    D --> D2[Virtual Network]
    
    E --> E1[File Share]
    E --> E2[Git Repo]
```

### Container Groups
```mermaid
graph TB
    subgraph "Container Group"
        A[Main Container]
        B[Sidecar]
        C[Init Container]
    end
    
    A --> D[Shared Network]
    B --> D
    C --> D
    
    D --> E[Storage]
    D --> F[DNS]
```

## Azure Kubernetes Service (AKS)

### Architecture Components

```mermaid
graph TB
    subgraph "Control Plane"
        A[API Server]
        B[etcd]
        C[Scheduler]
        D[Controller Manager]
    end
    
    subgraph "Node Pools"
        E[System Node Pool]
        F[User Node Pool]
    end
    
    subgraph "Workload Components"
        G[Pods]
        H[Services]
        I[Deployments]
    end
    
    A --> E
    A --> F
    E --> G
    F --> G
    G --> H
```

### Networking Models

```mermaid
graph TB
    A[AKS Networking] --> B[Kubenet]
    A --> C[Azure CNI]
    
    B --> B1[Basic Networking]
    B --> B2[Limited Features]
    
    C --> C1[Advanced Networking]
    C --> C2[Network Policy]
    C --> C3[Virtual Network]
```

## Implementation Examples

### 1. Basic Container Instance
```mermaid
graph LR
    A[Container Image] --> B[ACI]
    B --> C[Public IP]
    B --> D[Port Mapping]
    B --> E[Environment]
```

### 2. AKS Deployment
```mermaid
graph TB
    subgraph "Deployment Process"
        A[Container Registry]
        B[AKS Cluster]
        C[Node Pools]
        D[Pods]
    end
    
    A --> B
    B --> C
    C --> D
```

## Security Implementation

### 1. Container Security
```mermaid
graph TB
    A[Security] --> B[Image Scanning]
    A --> C[RBAC]
    A --> D[Network Policy]
    
    B --> E[Vulnerabilities]
    B --> F[Compliance]
    
    C --> G[Access Control]
    C --> H[Permissions]
    
    D --> I[Isolation]
    D --> J[Rules]
```

### 2. Identity and Access
```mermaid
graph LR
    A[Identity] --> B[Managed Identity]
    A --> C[Service Principal]
    A --> D[Pod Identity]
    
    B --> E[Key Vault]
    C --> F[Resources]
    D --> G[Azure Services]
```

## Monitoring and Diagnostics

### 1. AKS Monitoring
```mermaid
graph TB
    A[Monitoring] --> B[Container Insights]
    A --> C[Log Analytics]
    A --> D[Metrics]
    
    B --> E[Node Health]
    B --> F[Pod Performance]
    
    C --> G[Diagnostics]
    C --> H[Queries]
    
    D --> I[Resource Usage]
    D --> J[Alerts]
```

### 2. Diagnostic Tools
```mermaid
graph LR
    A[Diagnostics] --> B[kubectl]
    A --> C[Azure CLI]
    A --> D[Portal]
    
    B --> E[Logs]
    B --> F[Exec]
    
    C --> G[Diagnostics]
    C --> H[Troubleshoot]
    
    D --> I[Insights]
    D --> J[Metrics]
```

## Best Practices

### 1. Resource Management
```mermaid
graph TB
    A[Resource Management] --> B[Sizing]
    A --> C[Scaling]
    A --> D[Quota]
    
    B --> E[Right-sizing]
    B --> F[Reserved Capacity]
    
    C --> G[Auto-scale]
    C --> H[Manual Scale]
    
    D --> I[Limits]
    D --> J[Requests]
```

### 2. High Availability
```mermaid
graph LR
    A[HA Design] --> B[Multiple Zones]
    A --> C[Node Pools]
    A --> D[Pod Disruption]
    
    B --> E[Zone Redundancy]
    C --> F[Node Types]
    D --> G[Budget]
```

## Cost Optimization

### 1. AKS Cost Management
```mermaid
graph TB
    A[Cost Management] --> B[Node Pools]
    A --> C[Spot Instances]
    A --> D[Auto-scaling]
    
    B --> E[Right-sizing]
    B --> F[Scale Down]
    
    C --> G[Cost Savings]
    C --> H[Interruption]
    
    D --> I[KEDA]
    D --> J[HPA]
```

### 2. Resource Optimization
```mermaid
graph LR
    A[Optimization] --> B[Resource Quotas]
    A --> C[Limit Ranges]
    A --> D[Budget]
    
    B --> E[Namespace]
    C --> F[Container]
    D --> G[Alerts]
```

## Integration Features

```mermaid
graph TB
    A[Integrations] --> B[Azure Services]
    A --> C[DevOps]
    A --> D[Monitoring]
    
    B --> E[Key Vault]
    B --> F[Storage]
    B --> G[Load Balancer]
    
    C --> H[CI/CD]
    C --> I[Registry]
    
    D --> J[Log Analytics]
    D --> K[Application Insights]
```

## Troubleshooting Guide

1. **Common Issues**
   - Pod scheduling failures
   - Network connectivity
   - Image pull errors
   - Resource constraints

2. **Diagnostic Process**
   ```mermaid
   graph TB
       A[Troubleshooting] --> B[Node Health]
       A --> C[Pod State]
       A --> D[Networking]
       
       B --> E[Resources]
       B --> F[System]
       
       C --> G[Events]
       C --> H[Logs]
       
       D --> I[DNS]
       D --> J[Connectivity]
   ```

## Best Practices Summary

1. **Container Design**
   - Use minimal base images
   - Implement health probes
   - Handle graceful shutdowns
   - Version your images

2. **AKS Management**
   - Regular cluster updates
   - Monitor resource usage
   - Implement auto-scaling
   - Use pod disruption budgets

3. **Security**
   - Enable network policies
   - Use pod security policies
   - Implement RBAC
   - Regular security scans

## Further Reading
- [Azure Container Instances Documentation](https://learn.microsoft.com/en-us/azure/container-instances/)
- [AKS Documentation](https://learn.microsoft.com/en-us/azure/aks/)
- [Container Best Practices](https://learn.microsoft.com/en-us/azure/container-apps/best-practices)