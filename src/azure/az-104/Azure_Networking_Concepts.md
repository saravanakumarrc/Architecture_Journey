# Azure Networking Concepts

This document covers key Azure networking concepts including CIDR notation, GatewaySubnet requirements, Network Watcher capabilities, and Local Network Gateway configuration.

## CIDR (Classless Inter-Domain Routing)

```mermaid
graph TB
    A[CIDR Notation] --> B[Network Prefix]
    A --> C[Subnet Mask]
    A --> D[Available IPs]
    
    B --> B1[IP Range]
    B --> B2[Network ID]
    
    C --> C1[/8 to /32]
    C --> C2[Subnet Size]
    
    D --> D1[Host Addresses]
    D --> D2[Reserved IPs]
```

### Common CIDR Blocks in Azure
| CIDR Block | Subnet Mask | Available IPs | Common Use |
|------------|-------------|---------------|------------|
| /16 | 255.255.0.0 | 65,534 | VNet Address Space |
| /24 | 255.255.255.0 | 254 | Standard Subnet |
| /26 | 255.255.255.192 | 62 | AKS Subnet |
| /27 | 255.255.255.224 | 30 | GatewaySubnet |
| /28 | 255.255.255.240 | 14 | Small Subnet |
| /29 | 255.255.255.248 | 6 | Minimal Subnet |

## GatewaySubnet

### 1. Configuration Requirements
```mermaid
graph TB
    A[GatewaySubnet] --> B[Naming]
    A --> C[Size]
    A --> D[Restrictions]
    
    B --> B1["Must be 'GatewaySubnet'"]
    B --> B2[Case Sensitive]
    
    C --> C1[Minimum /27]
    C --> C2[Recommended /26]
    
    D --> D1[No NSG]
    D --> D2[No Route Table]
    D --> D3[No Delegation]
```

### 2. Implementation
```mermaid
graph LR
    A[VNet] --> B[GatewaySubnet]
    B --> C[VPN Gateway]
    B --> D[ExpressRoute]
    
    C --> E[Site-to-Site]
    C --> F[Point-to-Site]
    
    D --> G[Private Connection]
```

## Network Watcher

### 1. Diagnostic Features
```mermaid
graph TB
    A[Network Watcher] --> B[Connection Monitor]
    A --> C[Packet Capture]
    A --> D[NSG Flow Logs]
    A --> E[IP Flow Verify]
    
    B --> B1[Latency]
    B --> B2[Reachability]
    
    C --> C1[Traffic Analysis]
    C --> C2[Troubleshooting]
    
    D --> D1[Traffic Patterns]
    D --> D2[Security Analysis]
    
    E --> E1[Rule Evaluation]
    E --> E2[Connectivity Check]
```

### 2. Monitoring Capabilities
```mermaid
graph LR
    A[Monitoring] --> B[Topology]
    A --> C[Diagnostics]
    A --> D[Metrics]
    
    B --> E[Network Map]
    C --> F[VPN Analysis]
    D --> G[Performance]
```

## Local Network Gateway

### 1. Core Components
```mermaid
graph TB
    A[Local Network Gateway] --> B[Public IP]
    A --> C[Address Space]
    A --> D[BGP Settings]
    
    B --> B1[On-premises VPN]
    B --> B2[Remote Gateway]
    
    C --> C1[Remote Networks]
    C --> C2[Routing]
    
    D --> D1[ASN]
    D --> D2[Peering]
```

### 2. Configuration Example
```yaml
localNetworkGateway:
  name: "on-prem-gateway"
  publicIPAddress: "203.0.113.1"
  addressPrefixes:
    - "10.0.0.0/16"
    - "192.168.1.0/24"
  bgpSettings:
    asn: "65515"
    bgpPeeringAddress: "10.0.0.254"
```

## Integration Patterns

### 1. Hybrid Connectivity
```mermaid
graph TB
    subgraph "Azure"
        A[VNet]
        B[GatewaySubnet]
        C[VPN Gateway]
    end
    
    subgraph "On-premises"
        D[Local Network]
        E[VPN Device]
        F[Internal Network]
    end
    
    A --> B
    B --> C
    C --- E
    E --> D
    D --> F
```

### 2. Network Monitoring
```mermaid
graph LR
    A[Network Watcher] --> B[VNet]
    A --> C[Connections]
    A --> D[Security]
    
    B --> E[Topology]
    C --> F[Health]
    D --> G[Compliance]
```

## Best Practices

1. **CIDR Planning**
   - Reserve larger ranges for future growth
   - Use consistent sizing across environments
   - Document IP allocation
   - Consider service requirements

2. **Gateway Configuration**
```mermaid
graph TB
    A[Best Practices] --> B[Sizing]
    A --> C[Redundancy]
    A --> D[Monitoring]
    
    B --> E[Address Space]
    C --> F[Active-Active]
    D --> G[Health Checks]
```

3. **Network Watcher Usage**
   - Enable NSG flow logs
   - Configure connection monitoring
   - Use packet capture for troubleshooting
   - Implement regular diagnostics

## Security Considerations

```mermaid
graph TB
    A[Security] --> B[Encryption]
    A --> C[Access Control]
    A --> D[Monitoring]
    
    B --> B1[IPsec/IKE]
    B --> B2[BGP MD5]
    
    C --> C1[RBAC]
    C --> C2[NSG Rules]
    
    D --> D1[Flow Logs]
    D --> D2[Alerts]
```

## Troubleshooting Guide

1. **Common Issues**
   - Gateway connection problems
   - BGP route propagation
   - Subnet sizing constraints
   - NSG rule conflicts

2. **Resolution Steps**
```mermaid
graph TB
    A[Issue] --> B[Network Watcher]
    A --> C[Gateway Diagnostics]
    A --> D[Log Analysis]
    
    B --> E[Connection Monitor]
    C --> F[VPN Troubleshoot]
    D --> G[Flow Logs]
```

## Further Reading
- [CIDR and Subnetting Guide](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-cidr)
- [GatewaySubnet Configuration](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-gateway-settings)
- [Network Watcher Overview](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-overview)
- [Local Network Gateway Guide](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-howto-site-to-site-resource-manager-portal)