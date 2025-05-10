# Azure Load Balancer and Application Gateway

## Overview
Azure provides two main load balancing services: Azure Load Balancer for network layer (Layer 4) load balancing and Application Gateway for application layer (Layer 7) load balancing and web application firewall capabilities.

## Azure Load Balancer

### Core Components

```mermaid
graph TB
    A[Load Balancer] --> B[Frontend IP]
    A --> C[Backend Pools]
    A --> D[Health Probes]
    A --> E[Load Balancing Rules]
    
    B --> B1[Public IP]
    B --> B2[Private IP]
    
    C --> C1[VMs]
    C --> C2[VMSS]
    C --> C3[NICs]
    
    D --> D1[Protocol]
    D --> D2[Port]
    D --> D3[Interval]
    
    E --> E1[Frontend Port]
    E --> E2[Backend Port]
    E --> E3[Distribution]
```

### Types and SKUs

```mermaid
graph TB
    subgraph "Load Balancer Types"
        A[Public] --> A1[Internet-facing]
        B[Internal] --> B1[Private Network]
    end
    
    subgraph "SKUs"
        C[Basic]
        D[Standard]
    end
    
    C --> E[Limited Features]
    D --> F[Enhanced Features]
    D --> G[SLA]
    D --> H[Zone Redundant]
```

## Application Gateway

### Architecture Components

```mermaid
graph TB
    A[Application Gateway] --> B[Listeners]
    A --> C[Rules]
    A --> D[Backend Pools]
    A --> E[Health Probes]
    A --> F[WAF]
    
    B --> B1[Multi-site]
    B --> B2[Port]
    B --> B3[Protocol]
    
    C --> C1[Basic]
    C --> C2[Path-based]
    
    D --> D1[VMs]
    D --> D2[VMSS]
    D --> D3[IP/FQDN]
    
    E --> E1[Custom]
    E --> E2[Default]
    
    F --> F1[OWASP]
    F --> F2[Custom Rules]
```

### Routing Capabilities

```mermaid
graph LR
    A[Request Routing] --> B[URL Path-Based]
    A --> C[Multi-site]
    A --> D[Header-Based]
    
    B --> E[Different Backends]
    C --> F[Multiple Domains]
    D --> G[Custom Logic]
```

## Implementation Examples

### 1. Basic Load Balancer Setup
```mermaid
graph TB
    subgraph "Load Balancer Configuration"
        A[Public IP]
        B[Frontend IP Config]
        C[Backend Pool]
        D[Health Probe]
        E[LB Rule]
    end
    
    A --> B
    B --> E
    C --> E
    D --> E
```

### 2. Application Gateway with WAF
```mermaid
graph TB
    subgraph "App Gateway Components"
        A[Public IP]
        B[Listener]
        C[WAF Policy]
        D[Backend Pool]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E[Web Servers]
```

## Security Implementation

### 1. Network Security
```mermaid
graph TB
    A[Security] --> B[NSGs]
    A --> C[WAF]
    A --> D[SSL/TLS]
    
    B --> E[Rules]
    B --> F[Service Tags]
    
    C --> G[OWASP Rules]
    C --> H[Custom Rules]
    
    D --> I[Certificates]
    D --> J[End-to-end SSL]
```

### 2. Access Control
```mermaid
graph LR
    A[Access Control] --> B[RBAC]
    A --> C[Service Endpoints]
    A --> D[Private Link]
    
    B --> E[Roles]
    C --> F[VNet Integration]
    D --> G[Private Access]
```

## Monitoring and Diagnostics

### 1. Load Balancer Monitoring
```mermaid
graph TB
    A[Monitoring] --> B[Metrics]
    A --> C[Logs]
    A --> D[Alerts]
    
    B --> E[Health Status]
    B --> F[Throughput]
    
    C --> G[Connection Logs]
    C --> H[Health Probe Logs]
    
    D --> I[Performance]
    D --> J[Availability]
```

### 2. Application Gateway Insights
```mermaid
graph LR
    A[App Gateway Insights] --> B[Performance]
    A --> C[Access Logs]
    A --> D[WAF Logs]
    
    B --> E[Response Times]
    C --> F[Client Access]
    D --> G[Security Events]
```

## Best Practices

### 1. High Availability
```mermaid
graph TB
    A[HA Design] --> B[Zone Redundancy]
    A --> C[Backend Redundancy]
    A --> D[Health Monitoring]
    
    B --> E[Multiple Zones]
    C --> F[Multiple Instances]
    D --> G[Probe Configuration]
```

### 2. Performance Optimization
```mermaid
graph LR
    A[Optimization] --> B[Session Affinity]
    A --> C[SSL Offloading]
    A --> D[Caching]
    
    B --> E[Cookie Based]
    C --> F[SSL Termination]
    D --> G[Static Content]
```

## Cost Management

### 1. Load Balancer Costs
```mermaid
graph TB
    A[Cost Factors] --> B[SKU Type]
    A --> C[Rule Count]
    A --> D[Data Processing]
    
    B --> E[Basic/Standard]
    C --> F[Configuration]
    D --> G[Bandwidth]
```

### 2. Application Gateway Costs
```mermaid
graph LR
    A[App Gateway Costs] --> B[Instance Count]
    A --> C[WAF]
    A --> D[Data Processing]
    
    B --> E[Fixed Cost]
    C --> F[Additional Cost]
    D --> G[Variable Cost]
```

## Troubleshooting Guide

### 1. Common Issues
```mermaid
graph TB
    A[Issues] --> B[Connectivity]
    A --> C[Performance]
    A --> D[Configuration]
    
    B --> E[Health Probes]
    B --> F[Backend Health]
    
    C --> G[Latency]
    C --> H[Throughput]
    
    D --> I[Rules]
    D --> J[Certificates]
```

### 2. Diagnostic Tools
```mermaid
graph LR
    A[Diagnostics] --> B[Metrics]
    A --> C[Logs]
    A --> D[Network Watcher]
    
    B --> E[Dashboard]
    C --> F[Analytics]
    D --> G[Connection Monitor]
```

## Integration Features

```mermaid
graph TB
    A[Integrations] --> B[Azure Monitor]
    A --> C[Azure DNS]
    A --> D[Key Vault]
    
    B --> E[Insights]
    B --> F[Alerts]
    
    C --> G[DNS Integration]
    
    D --> H[Certificates]
```

## Best Practices Summary

1. **Load Balancer**
   - Use Standard SKU for production
   - Configure proper health probes
   - Implement zone redundancy
   - Monitor backend health

2. **Application Gateway**
   - Enable WAF for web applications
   - Configure SSL properly
   - Implement proper routing rules
   - Monitor performance metrics

3. **Security**
   - Implement proper NSG rules
   - Use WAF policies
   - Regular security monitoring
   - Certificate management

## Further Reading
- [Azure Load Balancer Documentation](https://learn.microsoft.com/en-us/azure/load-balancer/)
- [Application Gateway Documentation](https://learn.microsoft.com/en-us/azure/application-gateway/)
- [Load Balancing Best Practices](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview)