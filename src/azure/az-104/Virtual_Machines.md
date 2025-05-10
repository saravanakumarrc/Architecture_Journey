# Azure Virtual Machines

## Overview
Azure Virtual Machines (VMs) provide on-demand, scalable computing resources. They support Windows, Linux, and custom images, allowing you to run virtually any workload in the cloud.

## Core Components

```mermaid
graph TB
    A[Azure VM] --> B[Compute]
    A --> C[Storage]
    A --> D[Networking]
    A --> E[Security]
    
    B --> B1[Size/SKU]
    B --> B2[OS Type]
    B --> B3[Extensions]
    
    C --> C1[OS Disk]
    C --> C2[Data Disks]
    C --> C3[Disk Types]
    
    D --> D1[vNIC]
    D --> D2[NSG]
    D --> D3[Public IP]
    
    E --> E1[Identity]
    E --> E2[Encryption]
    E --> E3[Updates]
```

## VM Types and Sizes

```mermaid
graph TB
    subgraph "VM Series"
        A[General Purpose] --> A1[B-Series]
        A --> A2[D-Series]
        
        B[Compute Optimized] --> B1[F-Series]
        
        C[Memory Optimized] --> C1[E-Series]
        C --> C2[M-Series]
        
        D[Storage Optimized] --> D1[L-Series]
        
        E[GPU] --> E1[N-Series]
    end
```

## Deployment Patterns

### 1. High Availability Setup
```mermaid
graph TB
    subgraph "Availability Set"
        A[VM 1] --> C[Fault Domain 1]
        B[VM 2] --> D[Fault Domain 2]
        
        C --> E[Update Domain 1]
        D --> F[Update Domain 2]
    end
    
    subgraph "Load Balancer"
        G[Frontend IP]
        H[Backend Pool]
        I[Health Probes]
    end
```

### 2. Scale Set Architecture
```mermaid
graph TB
    A[VM Scale Set] --> B[Auto-scale]
    A --> C[Load Balancer]
    A --> D[Image Definition]
    
    B --> E[Scale Out]
    B --> F[Scale In]
    
    C --> G[Traffic Distribution]
    
    D --> H[Custom Image]
    D --> I[Marketplace Image]
```

## Storage Configuration

### 1. Disk Types
```mermaid
graph LR
    A[Azure Disks] --> B[Ultra Disk]
    A --> C[Premium SSD]
    A --> D[Standard SSD]
    A --> E[Standard HDD]
    
    B --> F[IOPS Intensive]
    C --> G[Production]
    D --> H[Dev/Test]
    E --> I[Backup/Archive]
```

### 2. Storage Performance
```mermaid
graph TB
    A[Performance Tiers] --> B[Disk Size]
    A --> C[IOPS]
    A --> D[Throughput]
    
    B --> E[P1-P50]
    C --> F[Limits]
    D --> G[MBps]
```

## Networking Features

```mermaid
graph TB
    A[VM Networking] --> B[vNIC]
    A --> C[NSG]
    A --> D[Load Balancer]
    A --> E[Public IP]
    
    B --> B1[IP Config]
    B --> B2[DNS]
    
    C --> C1[Inbound Rules]
    C --> C2[Outbound Rules]
    
    D --> D1[Rules]
    D --> D2[Health Probes]
    
    E --> E1[Static]
    E --> E2[Dynamic]
```

## Security Implementation

### 1. Identity and Access
```mermaid
graph TB
    A[Security] --> B[Managed Identity]
    A --> C[RBAC]
    A --> D[Just-in-time]
    
    B --> B1[System Assigned]
    B --> B2[User Assigned]
    
    C --> C1[Roles]
    C --> C2[Policies]
    
    D --> D1[Access Control]
    D --> D2[Time Windows]
```

### 2. Encryption and Updates
```mermaid
graph LR
    A[Data Protection] --> B[Disk Encryption]
    A --> C[Key Vault]
    A --> D[Update Management]
    
    B --> E[OS Disk]
    B --> F[Data Disks]
    
    C --> G[Key Storage]
    
    D --> H[Patches]
    D --> I[Updates]
```

## Monitoring and Management

```mermaid
graph TB
    A[Monitoring] --> B[Azure Monitor]
    A --> C[Log Analytics]
    A --> D[Metrics]
    
    B --> B1[Insights]
    B --> B2[Alerts]
    
    C --> C1[Queries]
    C --> C2[Workspaces]
    
    D --> D1[Performance]
    D --> D2[Health]
```

## Cost Optimization

### 1. Reserved Instances
```mermaid
graph LR
    A[Cost Management] --> B[Reserved VM]
    A --> C[Hybrid Benefit]
    A --> D[Auto-shutdown]
    
    B --> E[1 Year]
    B --> F[3 Years]
    
    C --> G[License Savings]
    
    D --> H[Dev/Test]
```

### 2. Scaling Strategies
```mermaid
graph TB
    A[Scaling Options] --> B[Vertical]
    A --> C[Horizontal]
    
    B --> D[Size Up]
    B --> E[Size Down]
    
    C --> F[Scale Out]
    C --> G[Scale In]
```

## Best Practices

1. **Resource Organization**
   - Use resource groups logically
   - Implement proper tagging
   - Follow naming conventions
   - Document configurations

2. **Performance Optimization**
   ```mermaid
   graph TB
       A[Optimization] --> B[Size Selection]
       A --> C[Storage Config]
       A --> D[Network Config]
       
       B --> E[Right-sizing]
       C --> F[Premium Storage]
       D --> G[Accelerated Networking]
   ```

3. **Disaster Recovery**
   - Implement backup strategy
   - Use availability sets/zones
   - Configure site recovery
   - Test recovery plans

## Troubleshooting Guide

### 1. Common Issues
```mermaid
graph TB
    A[Issues] --> B[Connection]
    A --> C[Performance]
    A --> D[Boot]
    
    B --> B1[RDP/SSH]
    B --> B2[Network]
    
    C --> C1[CPU]
    C --> C2[Memory]
    
    D --> D1[OS]
    D --> D2[Disk]
```

### 2. Diagnostic Tools
- Boot diagnostics
- Performance diagnostics
- Network Watcher
- Serial console

## Image Management

```mermaid
graph TB
    A[Image Management] --> B[Custom Images]
    A --> C[Shared Images]
    A --> D[Image Versions]
    
    B --> E[Capture]
    B --> F[Generalize]
    
    C --> G[Gallery]
    C --> H[Distribution]
    
    D --> I[Updates]
    D --> J[Rollback]
```

## Maintenance and Updates

1. **Planned Maintenance**
   - OS updates
   - Platform updates
   - Hardware updates
   - Network changes

2. **Update Management**
   ```mermaid
   graph LR
       A[Update Management] --> B[Assessment]
       B --> C[Scheduling]
       C --> D[Deployment]
       D --> E[Reporting]
   ```

## Integration with Azure Services

```mermaid
graph TB
    A[Azure VM] --> B[Key Vault]
    A --> C[Monitor]
    A --> D[Backup]
    A --> E[Site Recovery]
    A --> F[Log Analytics]
    A --> G[Security Center]
    
    B --> H[Secrets]
    C --> I[Insights]
    D --> J[Protection]
    E --> K[DR]
    F --> L[Analysis]
    G --> M[Security]
```

## Further Reading
- [Azure VM Documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/)
- [VM Best Practices](https://learn.microsoft.com/en-us/azure/virtual-machines/best-practices)
- [VM Performance Guidelines](https://learn.microsoft.com/en-us/azure/virtual-machines/premium-storage-performance)