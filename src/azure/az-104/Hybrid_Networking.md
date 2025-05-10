# Azure Hybrid Networking: VPN Gateway and ExpressRoute

## Overview
Azure Hybrid Networking solutions enable organizations to connect their on-premises networks with Azure through secure and reliable connections using VPN Gateway and ExpressRoute services.

## Core Components

```mermaid
graph TB
    A[Hybrid Networking] --> B[VPN Gateway]
    A --> C[ExpressRoute]
    A --> D[Network Planning]
    
    B --> B1[Site-to-Site]
    B --> B2[Point-to-Site]
    B --> B3[VNet-to-VNet]
    
    C --> C1[Private Peering]
    C --> C2[Microsoft Peering]
    C --> C3[Circuits]
    
    D --> D1[Address Space]
    D --> D2[Routing]
    D --> D3[Security]
```

## VPN Gateway

### 1. VPN Types
```mermaid
graph TB
    subgraph "Gateway Types"
        A[Policy-based]
        B[Route-based]
    end
    
    subgraph "SKUs"
        C[Basic]
        D[VpnGw1-5]
        E[VpnGw1-5AZ]
    end
    
    A --> F[Static Routing]
    B --> G[Dynamic Routing]
    
    D --> H[Performance]
    E --> I[Availability Zones]
```

### 2. Site-to-Site Configuration
```mermaid
sequenceDiagram
    participant OnPrem
    participant VPN
    participant Azure
    
    OnPrem->>VPN: Configure Device
    VPN->>Azure: Establish Tunnel
    Azure->>VPN: Exchange Routes
    VPN->>OnPrem: Enable Traffic
```

### 3. Point-to-Site Setup
```mermaid
graph LR
    A[P2S] --> B[Certificates]
    A --> C[Authentication]
    A --> D[Client]
    
    B --> E[Root]
    B --> F[Client]
    
    C --> G[Azure AD]
    C --> H[RADIUS]
    
    D --> I[VPN Client]
    D --> J[Configuration]
```

## ExpressRoute

### 1. Circuit Configuration
```mermaid
graph TB
    A[ExpressRoute] --> B[Provider]
    A --> C[Peering]
    A --> D[SKU]
    
    B --> E[Connectivity]
    B --> F[Location]
    
    C --> G[Private]
    C --> H[Microsoft]
    
    D --> I[Standard]
    D --> J[Premium]
```

### 2. Routing Configuration
```mermaid
graph LR
    A[Routing] --> B[BGP]
    A --> C[Routes]
    A --> D[Filters]
    
    B --> E[ASN]
    B --> F[Sessions]
    
    C --> G[Advertised]
    C --> H[Learned]
    
    D --> I[Communities]
    D --> J[Prefixes]
```

## High Availability

### 1. VPN Gateway HA
```mermaid
graph TB
    A[HA Options] --> B[Active-Active]
    A --> C[Active-Standby]
    A --> D[Zones]
    
    B --> E[Multiple Tunnels]
    B --> F[Load Balancing]
    
    C --> G[Automatic Failover]
    C --> H[Recovery]
    
    D --> I[Zone-redundant]
    D --> J[Zonal]
```

### 2. ExpressRoute HA
```mermaid
graph LR
    A[HA Design] --> B[Circuits]
    A --> C[Peering]
    A --> D[Locations]
    
    B --> E[Primary]
    B --> F[Secondary]
    
    C --> G[Redundant]
    C --> H[Independent]
    
    D --> I[Different]
    D --> J[Disaster Recovery]
```

## Performance and Monitoring

### 1. Performance Metrics
```mermaid
graph TB
    A[Metrics] --> B[Bandwidth]
    A --> C[Latency]
    A --> D[Availability]
    
    B --> E[Usage]
    B --> F[Capacity]
    
    C --> G[Round Trip]
    C --> H[Jitter]
    
    D --> I[Uptime]
    D --> J[SLA]
```

### 2. Monitoring Tools
```mermaid
graph LR
    A[Monitoring] --> B[Azure Monitor]
    A --> C[Network Watcher]
    A --> D[Diagnostics]
    
    B --> E[Metrics]
    B --> F[Alerts]
    
    C --> G[Connection Monitor]
    C --> H[Packet Capture]
    
    D --> I[Logs]
    D --> J[Troubleshooting]
```

## Security Configuration

### 1. VPN Security
```mermaid
graph TB
    A[Security] --> B[Encryption]
    A --> C[Authentication]
    A --> D[Policies]
    
    B --> E[IPsec]
    B --> F[IKE]
    
    C --> G[Pre-shared Key]
    C --> H[Certificates]
    
    D --> I[Traffic]
    D --> J[Routing]
```

### 2. ExpressRoute Security
```mermaid
graph LR
    A[Security] --> B[Private]
    A --> C[Encryption]
    A --> D[Access]
    
    B --> E[Connection]
    B --> F[Peering]
    
    C --> G[IPsec]
    C --> H[MACSec]
    
    D --> I[RBAC]
    D --> J[NSGs]
```

## Best Practices Summary

1. **Design Considerations**
   - Plan IP addressing
   - Configure redundancy
   - Implement monitoring
   - Security first approach

2. **Implementation Guidelines**
   - Use appropriate SKUs
   - Configure HA
   - Implement encryption
   - Regular testing

3. **Operational Excellence**
   - Monitor performance
   - Regular maintenance
   - Documentation
   - Disaster recovery

## Planning Guidelines

### 1. Network Design
```mermaid
graph TB
    A[Design] --> B[Topology]
    A --> C[Addressing]
    A --> D[Security]
    
    B --> E[Architecture]
    B --> F[Connectivity]
    
    C --> G[Subnetting]
    C --> H[Routing]
    
    D --> I[Encryption]
    D --> J[Policies]
```

### 2. Implementation Process
```mermaid
graph LR
    A[Process] --> B[Plan]
    A --> C[Deploy]
    A --> D[Validate]
    
    B --> E[Requirements]
    C --> F[Configuration]
    D --> G[Testing]
```

## Further Reading
- [VPN Gateway Documentation](https://learn.microsoft.com/en-us/azure/vpn-gateway/)
- [ExpressRoute Documentation](https://learn.microsoft.com/en-us/azure/expressroute/)
- [Hybrid Networking Best Practices](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/)