# API Design Concepts and Best Practices

## API Design Principles

```mermaid
mindmap
    root((API Design))
        (Design Principles)
            [Consistency]
            [Simplicity]
            [Evolvability]
            [Security]
        (Documentation)
            [OpenAPI/Swagger]
            [Examples]
            [Error Codes]
            [Use Cases]
        (Versioning)
            [URI Versioning]
            [Header Versioning]
            [Content Negotiation]
        (Security)
            [Authentication]
            [Authorization]
            [Rate Limiting]
            [Encryption]
```

## Common API Styles

### 1. REST (Representational State Transfer)

```mermaid
graph TB
    subgraph "REST Architecture"
        C[Client] --> |HTTP| S[Server]
        
        subgraph "Key Principles"
            R[Resource-Based]
            ST[Stateless]
            U[Uniform Interface]
            CA[Cacheable]
        end
        
        subgraph "Methods"
            GET
            POST
            PUT
            DELETE
        end
    end
```

#### Resource Design
- Nouns over verbs
- Hierarchical structure
- Consistent naming
- Clear relationships

#### HTTP Methods
| Method | Purpose | Idempotent | Safe |
|--------|---------|------------|------|
| GET    | Read    | Yes        | Yes  |
| POST   | Create  | No         | No   |
| PUT    | Update  | Yes        | No   |
| DELETE | Remove  | Yes        | No   |

### 2. GraphQL

```mermaid
graph TB
    subgraph "GraphQL Schema"
        Q[Query] --> T[Types]
        M[Mutation] --> T
        T --> R[Resolvers]
        
        subgraph "Features"
            QF[Query Flexibility]
            DD[Defined Schema]
            SR[Strong Types]
        end
    end
```

#### Schema Definition
```graphql
type User {
    id: ID!
    name: String!
    email: String!
    posts: [Post!]!
}

type Post {
    id: ID!
    title: String!
    content: String!
    author: User!
}

type Query {
    user(id: ID!): User
    users(page: Int, limit: Int): [User!]!
}

type Mutation {
    createUser(input: CreateUserInput!): User!
    updateUser(id: ID!, input: UpdateUserInput!): User!
}
```

### 3. gRPC (Google Remote Procedure Call)

```mermaid
graph LR
    subgraph "gRPC Communication"
        C[Client] --> |Protocol Buffers| S[Server]
        
        subgraph "Patterns"
            U[Unary]
            SS[Server Streaming]
            CS[Client Streaming]
            BD[Bidirectional]
        end
    end
```

#### Service Definition (Protocol Buffers)
```protobuf
syntax = "proto3";

service ProductService {
    rpc GetProduct (ProductRequest) returns (Product);
    rpc ListProducts (ProductFilter) returns (stream Product);
    rpc UpdateProduct (Product) returns (Product);
    rpc WatchProduct (ProductRequest) returns (stream ProductUpdate);
}

message Product {
    string id = 1;
    string name = 2;
    double price = 3;
    string category = 4;
}
```

## API Patterns

### 1. Gateway Pattern

```mermaid
graph TB
    subgraph "API Gateway"
        C[Client] --> G[Gateway]
        G --> |Route| S1[Service 1]
        G --> |Transform| S2[Service 2]
        G --> |Aggregate| S3[Service 3]
        
        subgraph "Cross-Cutting"
            AU[Authentication]
            RL[Rate Limiting]
            CA[Caching]
            MO[Monitoring]
        end
    end
```

### 2. Backend for Frontend (BFF)

```mermaid
graph TB
    subgraph "BFF Pattern"
        M[Mobile Client] --> MB[Mobile BFF]
        W[Web Client] --> WB[Web BFF]
        D[Desktop Client] --> DB[Desktop BFF]
        
        MB --> S[Services]
        WB --> S
        DB --> S
    end
```

## Design Guidelines

### 1. Naming Conventions
- Use nouns for resources
- Consistent casing
- Clear and descriptive
- Domain-specific terms

### 2. Error Handling
| Status Code | Category | Usage |
|-------------|----------|--------|
| 2xx | Success | Successful operations |
| 4xx | Client Error | Invalid requests |
| 5xx | Server Error | System failures |

### 3. Pagination
- Cursor-based
- Offset/limit
- Page/size
- Link headers

### 4. Security Checklist
- [ ] Authentication
- [ ] Authorization
- [ ] Input validation
- [ ] Rate limiting
- [ ] SSL/TLS
- [ ] API keys
- [ ] Audit logging

### 5. Performance
- Response caching
- Compression
- Batch operations
- Partial responses
- Efficient queries

## Documentation Best Practices

### 1. API Documentation
- Clear descriptions
- Request/response examples
- Error scenarios
- Authentication details
- Rate limits
- API versioning

### 2. OpenAPI/Swagger
```yaml
openapi: 3.0.0
info:
  title: Sample API
  version: 1.0.0
paths:
  /users:
    get:
      summary: List users
      parameters:
        - name: page
          in: query
          schema:
            type: integer
      responses:
        '200':
          description: List of users
        '401':
          description: Unauthorized
```

Remember: Good API design focuses on consistency, usability, and maintainability. Implementation details should follow these design principles rather than drive them.