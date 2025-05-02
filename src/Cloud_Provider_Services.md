# Cloud Provider Services (AWS, Azure, GCP)

## Compute Services

### Virtual Machines
| Feature | Azure | AWS | GCP |
|---------|-------|-----|-----|
| Base Service | Virtual Machines | EC2 | Compute Engine |
| Auto-scaling | VM Scale Sets | Auto Scaling Groups | Instance Groups |
| Spot Instances | Spot VMs | Spot Instances | Preemptible VMs |
| Containerized | ACI | ECS/EKS | GKE |

### Serverless
| Feature | Azure | AWS | GCP |
|---------|-------|-----|-----|
| Functions | Azure Functions | Lambda | Cloud Functions |
| Container Apps | Container Apps | Fargate | Cloud Run |
| Logic Apps | Logic Apps | Step Functions | Workflows |

## Storage Services

### Object Storage
| Feature | Azure | AWS | GCP |
|---------|-------|-----|-----|
| Base Service | Blob Storage | S3 | Cloud Storage |
| Archive | Cool/Archive Tiers | Glacier | Archive/Coldline |
| CDN | Azure CDN | CloudFront | Cloud CDN |

### File Storage
| Feature | Azure | AWS | GCP |
|---------|-------|-----|-----|
| Network FS | Azure Files | EFS | Filestore |
| Block Storage | Managed Disks | EBS | Persistent Disk |

## Database Services

### Relational
| Feature | Azure | AWS | GCP |
|---------|-------|-----|-----|
| Managed SQL | Azure SQL | RDS | Cloud SQL |
| Serverless | SQL Serverless | Aurora Serverless | - |
| Enterprise | SQL Managed Instance | RDS Enterprise | Cloud Spanner |

### NoSQL
| Feature | Azure | AWS | GCP |
|---------|-------|-----|-----|
| Document | Cosmos DB | DynamoDB | Firestore |
| Wide Column | Cosmos DB | DynamoDB | Bigtable |
| Cache | Azure Cache for Redis | ElastiCache | Memorystore |

## Networking Services

### Basic Networking
| Feature | Azure | AWS | GCP |
|---------|-------|-----|-----|
| Virtual Network | VNet | VPC | VPC |
| Load Balancer | Azure LB | ELB/ALB/NLB | Cloud Load Balancing |
| DNS | Azure DNS | Route 53 | Cloud DNS |

### Advanced Networking
| Feature | Azure | AWS | GCP |
|---------|-------|-----|-----|
| CDN | Azure CDN | CloudFront | Cloud CDN |
| WAF | App Gateway WAF | AWS WAF | Cloud Armor |
| VPN | VPN Gateway | VPN Gateway | Cloud VPN |

## Integration Services

### Messaging
| Feature | Azure | AWS | GCP |
|---------|-------|-----|-----|
| Queue | Service Bus | SQS | Cloud Pub/Sub |
| Event Bus | Event Grid | EventBridge | Cloud Pub/Sub |
| Streaming | Event Hubs | Kinesis | Cloud Pub/Sub |

## Security Services

### Identity
| Feature | Azure | AWS | GCP |
|---------|-------|-----|-----|
| IAM | Azure AD | IAM | Cloud IAM |
| SSO | Azure AD | IAM Identity Center | Cloud Identity |
| Key Management | Key Vault | KMS | Cloud KMS |

## Cost Comparison Example

### Virtual Machines (General Purpose, Pay-as-you-go)
```
Example configuration: 4 vCPU, 16GB RAM, Linux VM
Prices as of 2025 (approximate)

Azure (D4s v3):
- US East: $0.192/hour
- With 3-year reserved: $0.114/hour

AWS (t3.xlarge):
- US East: $0.1664/hour
- With 3-year reserved: $0.101/hour

GCP (n2-standard-4):
- US East: $0.189/hour
- With 3-year committed use: $0.113/hour
```

## Best Practices

### Multi-Cloud Strategy
1. Service Selection
   - Evaluate vendor lock-in risks
   - Consider service maturity
   - Compare pricing models
   - Assess feature parity

2. Architecture Design
   - Use cloud-agnostic designs where possible
   - Implement abstraction layers
   - Consider hybrid scenarios
   - Plan for disaster recovery

3. Operations
   - Standardize monitoring
   - Unified security policies
   - Consistent compliance controls
   - Centralized logging

## Service Selection Guidelines

### When to Choose Azure
- Microsoft-centric organizations
- .NET/Windows workloads
- Enterprise integration needs
- Hybrid cloud requirements

### When to Choose AWS
- Maximum service variety
- Global reach requirements
- DevOps-focused teams
- Cost-optimization priority

### When to Choose GCP
- Data analytics focus
- Kubernetes-native workloads
- ML/AI requirements
- Open-source emphasis

## Migration Considerations

### To Azure
```powershell
# Example Azure CLI migration assessment
az migrate project create `
    --resource-group myResourceGroup `
    --name myMigrationProject `
    --location eastus
```

### To AWS
```bash
# Example AWS migration assessment
aws migrationhub-strategy get-assessment
```

### To GCP
```bash
# Example GCP migration assessment
gcloud migrate assessment analyze-vms
```

## References
- Azure Pricing Calculator
- AWS Pricing Calculator
- GCP Pricing Calculator
- Cloud Service Comparison Tools