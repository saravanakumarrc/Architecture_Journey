# Azure Local Network Gateway

Azure Local Network Gateway represents your on-premises network when configuring a Site-to-Site VPN connection or a VNet-to-VNet connection. It defines the address space, public IP address, and BGP settings of your on-premises location for Azure to route traffic appropriately.

## Core Components

```mermaid
graph TB
    A[Local Network Gateway] --> B[Configuration]
    A --> C[Connectivity]
    A --> D[Routing]
    
    B --> B1[Public IP Address]
    B --> B2[Address Space]
    B --> B3[BGP Settings]
    
    C --> C1[Site-to-Site VPN]
    C --> C2[Multi-Site VPN]
    C --> C3[VNet-to-VNet]
    
    D --> D1[Static Routes]
    D --> D2[Dynamic Routes]
    D --> D3[BGP Peering]
```

## Implementation Architecture

### 1. Site-to-Site Configuration
```mermaid
graph TB
    subgraph "Azure"
        A[Virtual Network Gateway]
        B[Local Network Gateway]
        C[Connection Resource]
    end
    
    subgraph "On-premises"
        D[VPN Device]
        E[Local Network]
        F[Branch Offices]
    end
    
    A --- C
    B --- C
    C --- D
    D --- E
    E --- F
```

### 2. Multi-Site Setup
```mermaid
graph LR
    A[Azure VNet] --> B[Virtual Network Gateway]
    B --> C[Connection 1]
    B --> D[Connection 2]
    B --> E[Connection 3]
    
    C --> F[Local Network Gateway 1]
    D --> G[Local Network Gateway 2]
    E --> H[Local Network Gateway 3]
    
    F --> I[Site 1]
    G --> J[Site 2]
    H --> K[Site 3]
```

## BGP Configuration

### 1. BGP Settings
```mermaid
graph TB
    A[BGP Configuration] --> B[ASN]
    A --> C[BGP Peering IP]
    A --> D[Weight]
    
    B --> B1[Private ASN]
    B --> B2[Public ASN]
    
    C --> C1[Peer Address]
    C --> C2[Custom Address]
    
    D --> D1[Route Priority]
    D --> D2[Path Selection]
```

### 2. Route Advertisement
```mermaid
graph LR
    A[Route Exchange] --> B[Local Routes]
    A --> C[Connected Routes]
    A --> D[Static Routes]
    
    B --> E[Address Space]
    C --> F[Branch Routes]
    D --> G[Custom Routes]
```

## High Availability Design

### 1. Redundant Connectivity
```mermaid
graph TB
    A[HA Design] --> B[Active-Active]
    A --> C[Active-Passive]
    A --> D[Multi-Link]
    
    B --> B1[Load Balancing]
    B --> B2[Failover]
    
    C --> C1[Primary Link]
    C --> C2[Backup Link]
    
    D --> D1[ExpressRoute]
    D --> D2[VPN Backup]
```

### 2. Failover Configuration
```mermaid
graph LR
    A[Failover] --> B[Health Probes]
    A --> C[Route Updates]
    A --> D[Connection Switch]
    
    B --> E[Monitor]
    C --> F[Convergence]
    D --> G[Automatic]
```

## Security Features

```mermaid
graph TB
    A[Security] --> B[Connection Security]
    A --> C[Network Security]
    A --> D[Monitoring]
    
    B --> B1[IPsec/IKE]
    B --> B2[Pre-shared Key]
    B --> B3[Certificates]
    
    C --> C1[Firewall]
    C --> C2[NSG]
    C --> C3[Azure Policies]
    
    D --> D1[Logs]
    D --> D2[Metrics]
    D --> D3[Alerts]
```

## Implementation Examples

### 1. Basic Configuration
```yaml
localNetworkGateway:
  name: "onprem-gateway"
  resourceGroup: "network-rg"
  location: "eastus"
  gatewayIpAddress: "203.0.113.1"
  addressPrefixes:
    - "10.1.0.0/16"
    - "172.16.0.0/12"
  bgpSettings:
    asn: 65515
    bgpPeeringAddress: "10.1.0.1"
    peerWeight: 0
```

### 2. Multi-Site Configuration
```yaml
connections:
  - name: "site1-connection"
    type: "IPsec"
    sharedKey: "<key>"
    enableBgp: true
    localNetworkGateway: "site1-gateway"
    
  - name: "site2-connection"
    type: "IPsec"
    sharedKey: "<key>"
    enableBgp: true
    localNetworkGateway: "site2-gateway"
```

## Monitoring and Management

### 1. Connection Monitoring
```mermaid
graph TB
    A[Monitoring] --> B[Connection Status]
    A --> C[Data Transfer]
    A --> D[Tunnel Status]
    
    B --> B1[Connected]
    B --> B2[Disconnected]
    
    C --> C1[Ingress]
    C --> C2[Egress]
    
    D --> D1[Active]
    D --> D2[Standby]
```

### 2. Diagnostic Settings
```mermaid
graph LR
    A[Diagnostics] --> B[Gateway Logs]
    A --> C[Tunnel Logs]
    A --> D[BGP Logs]
    
    B --> E[Events]
    C --> F[Statistics]
    D --> G[Routes]
```

## Best Practices

1. **Design Considerations**
   - Plan address spaces carefully
   - Configure BGP when possible
   - Implement redundancy
   - Monitor connection health

2. **Security Guidelines**
```mermaid
graph TB
    A[Security] --> B[Encryption]
    A --> C[Authentication]
    A --> D[Monitoring]
    
    B --> E[Strong Algorithms]
    C --> F[Keys/Certs]
    D --> G[Alerts]
```

## Troubleshooting Guide

1. **Common Issues**
   - Connection drops
   - BGP peering problems
   - Route propagation delays
   - IPsec misconfigurations

2. **Resolution Steps**
```mermaid
graph TB
    A[Issue] --> B[Check Status]
    A --> C[Verify Config]
    A --> D[Test Connection]
    
    B --> E[Logs]
    C --> F[Settings]
    D --> G[Tools]
```

## Further Reading
- [Local Network Gateway Documentation](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-gateway-settings)
- [BGP with VPN Gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-bgp-overview)
- [VPN Troubleshooting](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-troubleshoot)
- [High Availability Design](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-highlyavailable)