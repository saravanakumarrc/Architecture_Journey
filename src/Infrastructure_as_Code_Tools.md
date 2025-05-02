# Infrastructure as Code Tools

## Terraform

### Core Concepts
- Providers
- Resources
- Data Sources
- Variables
- State Management
- Workspaces
- Modules

### Basic Example
```hcl
# Example Terraform configuration
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
  
  tags = {
    environment = "Production"
    department  = "IT"
  }
}

resource "azurerm_storage_account" "example" {
  name                     = "examplestorage"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "GRS"
  
  tags = {
    environment = "Production"
  }
}
```

### Module Structure
```
modules/
├── webapp/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── README.md
└── database/
    ├── main.tf
    ├── variables.tf
    ├── outputs.tf
    └── README.md
```

## AWS CloudFormation

### Template Structure
```yaml
# Example CloudFormation template
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Example Stack'

Parameters:
  EnvironmentName:
    Type: String
    Default: Production

Resources:
  MyS3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub '${AWS::StackName}-bucket'
      VersioningConfiguration:
        Status: Enabled
      
  MyEC2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      InstanceType: t2.micro
      ImageId: ami-0c55b159cbfafe1f0
      Tags:
        - Key: Environment
          Value: !Ref EnvironmentName

Outputs:
  BucketName:
    Value: !Ref MyS3Bucket
    Description: 'S3 Bucket Name'
```

### Features
- Nested Stacks
- Change Sets
- Drift Detection
- Stack Policies
- Resource Dependencies

## Azure Bicep

### Basic Syntax
```bicep
// Example Bicep template
param location string = resourceGroup().location
param environment string = 'prod'

resource storageAccount 'Microsoft.Storage/storageAccounts@2021-09-01' = {
  name: 'mystorageaccount${environment}'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
    supportsHttpsTrafficOnly: true
  }
}

resource appServicePlan 'Microsoft.Web/serverfarms@2021-03-01' = {
  name: 'myappserviceplan'
  location: location
  sku: {
    name: 'S1'
    tier: 'Standard'
  }
}

output storageAccountId string = storageAccount.id
```

### Module System
```
bicep/
├── main.bicep
├── modules/
│   ├── storage.bicep
│   └── webapp.bicep
└── parameters/
    ├── dev.json
    └── prod.json
```

## Comparison

### Feature Matrix

| Feature | Terraform | CloudFormation | Bicep |
|---------|-----------|----------------|--------|
| Multi-Cloud | Yes | AWS Only | Azure Only |
| State Management | External | Managed | Managed |
| Language | HCL | JSON/YAML | DSL |
| Modularity | Modules | Nested Stacks | Modules |
| Dependencies | Explicit | Implicit/Explicit | Explicit |
| Preview | Plan | Change Sets | What-If |

### Use Case Selection

#### Terraform
- Multi-cloud deployments
- Custom provider needs
- Complex dependencies
- State management requirements

#### CloudFormation
- AWS-native deployments
- Compliance requirements
- Managed services integration
- Native AWS tooling

#### Bicep
- Azure-native deployments
- ARM template replacement
- Azure DevOps integration
- Azure-managed state

## Best Practices

### 1. Code Organization
```
project/
├── environments/
│   ├── dev/
│   ├── staging/
│   └── prod/
├── modules/
│   ├── networking/
│   ├── compute/
│   └── storage/
└── scripts/
```

### 2. Security
- Secret management
- Least privilege access
- Resource encryption
- Network security
- Compliance as code

### 3. State Management
```hcl
# Example Terraform backend configuration
terraform {
  backend "azurerm" {
    resource_group_name  = "tfstate"
    storage_account_name = "tfstate"
    container_name      = "tfstate"
    key                 = "prod.terraform.tfstate"
  }
}
```

### 4. Testing
- Unit testing
- Integration testing
- Policy compliance
- Security scanning
- Cost estimation

## Common Patterns

### 1. Resource Tagging
```hcl
# Example Terraform tagging
locals {
  common_tags = {
    Environment = var.environment
    Project     = var.project_name
    Owner       = var.owner
    CostCenter  = var.cost_center
  }
}

resource "azurerm_resource_group" "example" {
  name     = "example-rg"
  location = "eastus"
  tags     = local.common_tags
}
```

### 2. Environment Management
```yaml
# Example CloudFormation environment variables
Parameters:
  Environment:
    Type: String
    AllowedValues:
      - dev
      - staging
      - prod
    Default: dev
```

### 3. Resource Naming
```bicep
// Example Bicep naming convention
param environmentName string
param location string
param workloadName string

var resourcePrefix = '${workloadName}-${environmentName}-${location}'

resource storageAccount 'Microsoft.Storage/storageAccounts@2021-09-01' = {
  name: '${replace(resourcePrefix, '-', '')}sa'
  // ...
}
```

## References
- Terraform Documentation
- AWS CloudFormation User Guide
- Azure Bicep Documentation
- Infrastructure as Code (Kief Morris)