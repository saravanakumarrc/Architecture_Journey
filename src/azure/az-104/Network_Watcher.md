# Azure Network Watcher

Azure Network Watcher provides network monitoring and diagnostics tools to observe, diagnose, and gain insights into your network performance and health in Azure. It offers a comprehensive suite of tools for deep network visibility and troubleshooting capabilities.

## Core Features

```mermaid
graph TB
    A[Network Watcher] --> B[Network Diagnostic Tools]
    A --> C[Monitoring Tools]
    A --> D[Network Security]
    A --> E[Connectivity Tests]
    
    B --> B1[Packet Capture]
    B --> B2[Connection Monitor]
    B --> B3[VPN Diagnostics]
    
    C --> C1[NSG Flow Logs]
    C --> C2[Traffic Analytics]
    C --> C3[Network Performance]
    
    D --> D1[Security Group View]
    D --> D2[Next Hop]
    D --> D3[IP Flow Verify]
    
    E --> E1[Connection Troubleshoot]
    E --> E2[Reachability Check]
    E --> E3[Network Path Analysis]
```

## Diagnostic Tools in Detail

### 1. Connection Monitor
```mermaid
graph TB
    A[Connection Monitor] --> B[Tests]
    A --> C[Metrics]
    A --> D[Alerts]
    
    B --> B1[TCP Test]
    B --> B2[HTTP Test]
    B --> B3[ICMP Test]
    
    C --> C1[Latency]
    C --> C2[Packet Loss]
    C --> C3[Jitter]
    
    D --> D1[Thresholds]
    D --> D2[Notifications]
    D --> D3[Integration]
```

### 2. Packet Capture
```mermaid
graph LR
    A[Packet Capture] --> B[Filters]
    A --> C[Storage]
    A --> D[Analysis]
    
    B --> E[Protocol]
    B --> F[Port]
    B --> G[IP Address]
    
    C --> H[Local]
    C --> I[Blob Storage]
    
    D --> J[Wireshark]
    D --> K[Network Tools]
```

## Network Security Analysis

### 1. NSG Flow Logs
```mermaid
graph TB
    A[Flow Logs] --> B[Collection]
    A --> C[Storage]
    A --> D[Analytics]
    
    B --> B1[Version 2]
    B --> B2[4-tuple logging]
    
    C --> C1[Blob Storage]
    C --> C2[Log Analytics]
    
    D --> D1[Traffic Analytics]
    D --> D2[Security Analysis]
```

### 2. Security Group View
```mermaid
graph LR
    A[Security View] --> B[Rules]
    A --> C[Effective Rules]
    A --> D[Applied NSGs]
    
    B --> E[Inbound]
    B --> F[Outbound]
    
    C --> G[Combined Effect]
    C --> H[Rule Priority]
    
    D --> I[NIC Level]
    D --> J[Subnet Level]
```

## Performance Monitoring

### 1. Network Performance Monitor
```mermaid
graph TB
    A[Performance Monitor] --> B[ExpressRoute]
    A --> C[Service Connectivity]
    A --> D[Performance Monitor]
    
    B --> B1[Circuit Health]
    B --> B2[Peering Status]
    
    C --> C1[Service Health]
    C --> C2[Endpoint Status]
    
    D --> D1[Network Metrics]
    D --> D2[Baseline Analysis]
```

### 2. Traffic Analytics
```mermaid
graph LR
    A[Traffic Analytics] --> B[Flow Patterns]
    A --> C[Security Analysis]
    A --> D[Application Traffic]
    
    B --> E[Volume]
    B --> F[Geography]
    
    C --> G[Threats]
    C --> H[Anomalies]
    
    D --> I[Apps]
    D --> J[Ports]
```

## Troubleshooting Features

### 1. Network Troubleshooting
```mermaid
graph TB
    A[Troubleshooting] --> B[IP Flow Verify]
    A --> C[Next Hop]
    A --> D[VPN Troubleshoot]
    
    B --> B1[Rule Check]
    B --> B2[Traffic Allow/Deny]
    
    C --> C1[Routing]
    C --> C2[Path Analysis]
    
    D --> D1[Gateway Issues]
    D --> D2[Connection Problems]
```

### 2. Connectivity Check
```mermaid
graph LR
    A[Connectivity] --> B[Source]
    A --> C[Destination]
    A --> D[Protocol]
    
    B --> E[VM/Resource]
    C --> F[Endpoint]
    D --> G[TCP/HTTP]
```

## Integration with Azure Services

### 1. Monitoring Integration
```mermaid
graph TB
    A[Integration] --> B[Log Analytics]
    A --> C[Azure Monitor]
    A --> D[Azure Security]
    
    B --> B1[Queries]
    B --> B2[Dashboards]
    
    C --> C1[Metrics]
    C --> C2[Alerts]
    
    D --> D1[Security Center]
    D --> D2[Sentinel]
```

### 2. Storage and Analysis
```mermaid
graph LR
    A[Data Storage] --> B[Blob Storage]
    A --> C[Analytics]
    A --> D[Retention]
    
    B --> E[Raw Data]
    C --> F[Insights]
    D --> G[Policies]
```

## Best Practices

1. **Implementation Strategy**
   - Enable NSG flow logs in all regions
   - Configure appropriate retention periods
   - Set up regular connectivity monitoring
   - Implement automated alerts

2. **Resource Monitoring**
```mermaid
graph TB
    A[Monitoring] --> B[Coverage]
    A --> C[Frequency]
    A --> D[Retention]
    
    B --> E[Resources]
    C --> F[Intervals]
    D --> G[Duration]
```

3. **Cost Optimization**
   - Use targeted packet capture
   - Configure appropriate log retention
   - Optimize storage usage
   - Monitor data transfer costs

## Troubleshooting Guide

1. **Common Scenarios**
   - Connectivity issues
   - Performance problems
   - Security rule verification
   - VPN connection issues

2. **Resolution Steps**
```mermaid
graph TB
    A[Issue] --> B[Identify]
    A --> C[Diagnose]
    A --> D[Resolve]
    
    B --> E[Tools]
    C --> F[Analysis]
    D --> G[Action]
```

## Further Reading
- [Network Watcher Documentation](https://learn.microsoft.com/en-us/azure/network-watcher/)
- [NSG Flow Logs Guide](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-nsg-flow-logging-overview)
- [Connection Monitor](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview)
- [Traffic Analytics](https://learn.microsoft.com/en-us/azure/network-watcher/traffic-analytics)