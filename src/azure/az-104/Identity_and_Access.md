# Azure Active Directory (Microsoft Entra ID)

## Overview
Microsoft Entra ID (formerly Azure AD) is Microsoft's cloud-based identity and access management service. It helps your employees sign in and access resources in both external and internal resources.

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
    
    E --> E1[Azure AD Join]
    E --> E2[Hybrid Join]
    E --> E3[Registration]
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
        D[Profile]
        E[Authentication]
        F[Licenses]
    end
    
    A --> G[Direct Management]
    B --> H[Directory Sync]
    C --> I[B2B]
```

### 2. Group Management
```mermaid
graph LR
    A[Groups] --> B[Membership]
    A --> C[Types]
    A --> D[Access]
    
    B --> E[Assigned]
    B --> F[Dynamic]
    
    C --> G[Security]
    C --> H[M365]
    
    D --> I[Resources]
    D --> J[Applications]
```

## Authentication

### 1. Authentication Methods
```mermaid
graph TB
    A[Authentication] --> B[Passwords]
    A --> C[MFA]
    A --> D[Passwordless]
    
    B --> E[Policies]
    B --> F[Protection]
    
    C --> G[Methods]
    C --> H[Conditional]
    
    D --> I[FIDO2]
    D --> J[Certificate]
```

### 2. Conditional Access
```mermaid
graph LR
    A[Conditional] --> B[Signals]
    A --> C[Decisions]
    A --> D[Policies]
    
    B --> E[User/Group]
    B --> F[Location]
    B --> G[Device]
    
    C --> H[Allow]
    C --> I[Block]
    C --> J[Challenge]
    
    D --> K[Rules]
    D --> L[Actions]
```

## Application Management

### 1. Enterprise Applications
```mermaid
graph TB
    A[Enterprise Apps] --> B[SSO]
    A --> C[Provisioning]
    A --> D[Permissions]
    
    B --> E[SAML]
    B --> F[OAuth]
    
    C --> G[Users]
    C --> H[Groups]
    
    D --> I[Admin]
    D --> J[User]
```

### 2. App Registration
```mermaid
graph LR
    A[Registration] --> B[Identity]
    A --> C[Authentication]
    A --> D[API]
    
    B --> E[App ID]
    B --> F[Tenant]
    
    C --> G[Platform]
    C --> H[Credentials]
    
    D --> I[Permissions]
    D --> J[Expose]
```

## Device Management

### 1. Device Identity
```mermaid
graph TB
    A[Devices] --> B[Join Types]
    A --> C[Management]
    A --> D[Access]
    
    B --> E[Azure AD]
    B --> F[Hybrid]
    B --> G[Register]
    
    C --> H[MDM]
    C --> I[MAM]
    
    D --> J[Conditional]
    D --> K[MFA]
```

### 2. Device Compliance
```mermaid
graph LR
    A[Compliance] --> B[Policies]
    A --> C[State]
    A --> D[Actions]
    
    B --> E[Requirements]
    B --> F[Rules]
    
    C --> G[Compliant]
    C --> H[Non-compliant]
    
    D --> I[Allow]
    D --> J[Block]
```

## Security Features

### 1. Identity Protection
```mermaid
graph TB
    A[Protection] --> B[Risks]
    A --> C[Policies]
    A --> D[Reports]
    
    B --> E[Users]
    B --> F[Sign-ins]
    
    C --> G[Detection]
    C --> H[Response]
    
    D --> I[Analysis]
    D --> J[Alerts]
```

### 2. Access Reviews
```mermaid
graph LR
    A[Reviews] --> B[Scope]
    A --> C[Reviewers]
    A --> D[Outcomes]
    
    B --> E[Groups]
    B --> F[Apps]
    
    C --> G[Self]
    C --> H[Managers]
    
    D --> I[Approve]
    D --> J[Deny]
```

## Monitoring and Reporting

### 1. Audit Logs
```mermaid
graph TB
    A[Logs] --> B[Activities]
    A --> C[Categories]
    A --> D[Retention]
    
    B --> E[Users]
    B --> F[Apps]
    B --> G[Resources]
    
    C --> H[Authentication]
    C --> I[Management]
    
    D --> J[Storage]
    D --> K[Export]
```

### 2. Sign-in Logs
```mermaid
graph LR
    A[Sign-ins] --> B[Interactive]
    A --> C[Non-interactive]
    A --> D[Service Principal]
    
    B --> E[Success]
    B --> F[Failure]
    
    C --> G[Background]
    C --> H[System]
    
    D --> I[Apps]
    D --> J[APIs]
```

## Best Practices Summary

1. **Identity Security**
   - Enable MFA
   - Use Conditional Access
   - Monitor risky sign-ins
   - Regular access reviews

2. **Application Management**
   - Implement SSO
   - Manage permissions
   - Monitor usage
   - Regular cleanup

3. **Device Management**
   - Enforce compliance
   - Enable device management
   - Monitor device health
   - Regular updates

## Implementation Guidelines

### 1. Identity Strategy
```mermaid
graph TB
    A[Strategy] --> B[Planning]
    A --> C[Implementation]
    A --> D[Management]
    
    B --> E[Requirements]
    B --> F[Architecture]
    
    C --> G[Deployment]
    C --> H[Integration]
    
    D --> I[Operations]
    D --> J[Maintenance]
```

### 2. Security Roadmap
```mermaid
graph LR
    A[Security] --> B[Basics]
    A --> C[Advanced]
    A --> D[Zero Trust]
    
    B --> E[MFA]
    B --> F[SSPR]
    
    C --> G[PIM]
    C --> H[Identity Protection]
    
    D --> I[Conditional Access]
    D --> J[Risk-based]
```

## Further Reading
- [Microsoft Entra ID Documentation](https://learn.microsoft.com/en-us/azure/active-directory/)
- [Identity Security Best Practices](https://learn.microsoft.com/en-us/azure/security/fundamentals/identity-management-best-practices)
- [Zero Trust Implementation Guide](https://learn.microsoft.com/en-us/security/zero-trust/)