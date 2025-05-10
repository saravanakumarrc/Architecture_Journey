# Microsoft Entra ID (formerly Azure Active Directory)

## Overview
Microsoft Entra ID is Azure's cloud-based identity and access management service. It handles authentication, authorization, and identity management for Azure resources, Microsoft 365, and third-party applications.

## Core Components

```mermaid
graph TB
    A[Entra ID] --> B[Users]
    A --> C[Groups]
    A --> D[Applications]
    A --> E[Devices]
    
    B --> B1[Cloud Users]
    B --> B2[Synced Users]
    B --> B3[Guest Users]
    
    C --> C1[Security Groups]
    C --> C2[Microsoft 365]
    C --> C3[Dynamic Groups]
    
    D --> D1[Enterprise Apps]
    D --> D2[App Registrations]
    D --> D3[Service Principals]
    
    E --> E1[Registered]
    E --> E2[Joined]
    E --> E3[Hybrid Joined]
```

## Identity Management

### 1. User Management
```mermaid
graph TB
    subgraph "User Types"
        A[Cloud Identity]
        B[Synchronized]
        C[Guest]
    end
    
    subgraph "Properties"
        D[Authentication]
        E[Authorization]
        F[Profile]
    end
    
    A --> D
    B --> D
    C --> D
    
    D --> G[Methods]
    E --> H[Roles]
    F --> I[Attributes]
```

### 2. Group Management
```mermaid
graph LR
    A[Groups] --> B[Assigned]
    A --> C[Dynamic]
    A --> D[Microsoft 365]
    
    B --> E[Manual]
    C --> F[Rules]
    D --> G[Team]
```

## Authentication Methods

### 1. Authentication Types
```mermaid
graph TB
    A[Authentication] --> B[Passwords]
    A --> C[MFA]
    A --> D[Passwordless]
    
    B --> B1[Policies]
    B --> B2[Protection]
    
    C --> C1[Methods]
    C --> C2[Enforcement]
    
    D --> D1[FIDO2]
    D --> D2[Biometric]
```

### 2. Conditional Access
```mermaid
graph LR
    A[Conditional Access] --> B[Signals]
    A --> C[Conditions]
    A --> D[Controls]
    
    B --> E[User/Group]
    B --> F[Location]
    B --> G[Device]
    
    C --> H[Risk]
    C --> I[Platform]
    
    D --> J[Allow]
    D --> K[Block]
    D --> L[MFA]
```

## Application Integration

### 1. App Registration
```mermaid
sequenceDiagram
    participant Admin
    participant AppReg
    participant Enterprise
    participant Users
    
    Admin->>AppReg: Register App
    Admin->>AppReg: Configure Auth
    AppReg->>Enterprise: Create Service Principal
    Enterprise->>Users: Grant Access
```

### 2. Enterprise Applications
```mermaid
graph TB
    subgraph "Enterprise Apps"
        A[Gallery Apps]
        B[Custom Apps]
        C[SSO Config]
    end
    
    A --> D[Pre-integrated]
    B --> E[SAML/OIDC]
    C --> F[Methods]
    
    D --> G[Setup]
    E --> H[Development]
    F --> I[Configuration]
```

## Identity Protection

### 1. Risk Detection
```mermaid
graph TB
    A[Protection] --> B[Risk Events]
    A --> C[Policies]
    A --> D[Monitoring]
    
    B --> E[User Risk]
    B --> F[Sign-in Risk]
    
    C --> G[Conditions]
    C --> H[Actions]
    
    D --> I[Alerts]
    D --> J[Reports]
```

### 2. Security Features
```mermaid
graph LR
    A[Security] --> B[MFA]
    A --> C[PIM]
    A --> D[Access Reviews]
    
    B --> E[Methods]
    C --> F[Just-in-Time]
    D --> G[Periodic]
```

## Hybrid Identity

### 1. Synchronization
```mermaid
graph TB
    A[Azure AD Connect] --> B[Sync]
    A --> C[Authentication]
    A --> D[Features]
    
    B --> E[Objects]
    B --> F[Attributes]
    
    C --> G[Password Hash]
    C --> H[Pass-through]
    C --> I[Federation]
    
    D --> J[Write-back]
    D --> K[Filtering]
```

### 2. Federation
```mermaid
graph LR
    A[Federation] --> B[ADFS]
    A --> C[Third-party]
    A --> D[Configuration]
    
    B --> E[Claims]
    C --> F[Integration]
    D --> G[Setup]
```

## Monitoring and Reporting

### 1. Audit Logs
```mermaid
graph TB
    A[Audit] --> B[Sign-ins]
    A --> C[Activity]
    A --> D[Risk Events]
    
    B --> E[User]
    B --> F[App]
    
    C --> G[Admin]
    C --> H[System]
    
    D --> I[Detection]
    D --> J[Resolution]
```

### 2. Security Reports
```mermaid
graph LR
    A[Reports] --> B[Risk]
    A --> C[Usage]
    A --> D[Health]
    
    B --> E[Detections]
    C --> F[Analytics]
    D --> G[Status]
```

## Governance Features

### 1. Access Reviews
```mermaid
graph TB
    A[Reviews] --> B[Scope]
    A --> C[Reviewers]
    A --> D[Frequency]
    
    B --> E[Groups]
    B --> F[Apps]
    B --> G[Roles]
    
    C --> H[Self]
    C --> I[Managers]
    
    D --> J[One-time]
    D --> K[Recurring]
```

### 2. PIM Configuration
```mermaid
graph LR
    A[PIM] --> B[Roles]
    A --> C[Resources]
    A --> D[Settings]
    
    B --> E[Eligibility]
    C --> F[Assignments]
    D --> G[Rules]
```

## Best Practices

### 1. Identity Security
```mermaid
graph TB
    A[Security] --> B[Authentication]
    A --> C[Authorization]
    A --> D[Monitoring]
    
    B --> E[MFA]
    B --> F[Policies]
    
    C --> G[RBAC]
    C --> H[PIM]
    
    D --> I[Alerts]
    D --> J[Reviews]
```

### 2. Configuration Guidelines
```mermaid
graph LR
    A[Guidelines] --> B[Sync]
    A --> C[Apps]
    A --> D[Security]
    
    B --> E[Setup]
    C --> F[Integration]
    D --> G[Controls]
```

## Best Practices Summary

1. **Identity Management**
   - Enable MFA
   - Use Conditional Access
   - Implement PIM
   - Regular access reviews

2. **Application Security**
   - Configure proper permissions
   - Use managed identities
   - Implement SSO
   - Monitor usage

3. **Governance**
   - Document policies
   - Regular reviews
   - Monitor compliance
   - Automate processes

## Further Reading
- [Microsoft Entra Documentation](https://learn.microsoft.com/en-us/entra/)
- [Identity Security Best Practices](https://learn.microsoft.com/en-us/azure/security/fundamentals/identity-management-best-practices)
- [Hybrid Identity Documentation](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/)