# API Design Concepts and Best Practices

An API (Application Programming Interface) serves as a contract between different software components. This guide covers different API styles, their design principles, and best practices.

## Common API Styles

### 1. REST (Representational State Transfer)

REST is an architectural style that uses HTTP methods to interact with resources.

#### Key Principles
- Stateless
- Resource-based
- Uses standard HTTP methods
- Uniform interface
- Cacheable
- Client-server architecture

#### Example REST API Structure
```mermaid
graph TD
    A[Client] -->|GET /users| B[List Users]
    A -->|POST /users| C[Create User]
    A -->|GET /users/:id| D[Get User]
    A -->|PUT /users/:id| E[Update User]
    A -->|DELETE /users/:id| F[Delete User]
```

#### HTTP Methods and Their Use
```
GET     - Retrieve a resource
POST    - Create a new resource
PUT     - Update/Replace a resource
PATCH   - Partial update of a resource
DELETE  - Remove a resource
```

#### Example REST Endpoints for an E-commerce API
```
GET    /api/v1/products           # List all products
GET    /api/v1/products/:id       # Get a specific product
POST   /api/v1/products           # Create a new product
PUT    /api/v1/products/:id       # Update a product
DELETE /api/v1/products/:id       # Delete a product
GET    /api/v1/products/:id/reviews  # Get reviews for a product
```

#### REST Response Example
```json
{
    "id": "123",
    "name": "Wireless Headphones",
    "price": 99.99,
    "category": "Electronics",
    "_links": {
        "self": "/api/v1/products/123",
        "reviews": "/api/v1/products/123/reviews",
        "related": "/api/v1/products/123/related"
    }
}
```

### 2. GraphQL

GraphQL is a query language for APIs that enables declarative data fetching.

#### Key Features
- Single endpoint
- Client-specified queries
- Strong typing
- Real-time updates with subscriptions
- Hierarchical structure

#### Example GraphQL Schema
```graphql
type Product {
    id: ID!
    name: String!
    price: Float!
    category: Category!
    reviews: [Review!]!
}

type Category {
    id: ID!
    name: String!
    products: [Product!]!
}

type Review {
    id: ID!
    rating: Int!
    comment: String
    user: User!
}

type Query {
    product(id: ID!): Product
    products(category: ID, filter: ProductFilter): [Product!]!
}

type Mutation {
    createProduct(input: ProductInput!): Product!
    updateProduct(id: ID!, input: ProductInput!): Product!
}

type Subscription {
    productUpdated(id: ID!): Product!
}
```

#### GraphQL Operation Flow
```mermaid
sequenceDiagram
    participant C as Client
    participant S as GraphQL Server
    participant DB as Database
    C->>S: Query/Mutation Request
    S->>S: Validate Query
    S->>S: Parse Query
    S->>DB: Resolve Fields
    DB->>S: Return Data
    S->>C: Format Response
```

#### Example GraphQL Query
```graphql
query {
    products(category: "Electronics") {
        id
        name
        price
        reviews {
            rating
            comment
            user {
                name
            }
        }
    }
}
```

### 3. gRPC (Google Remote Procedure Call)

gRPC is a high-performance RPC framework that uses Protocol Buffers.

#### Key Features
- Binary protocol (Protocol Buffers)
- HTTP/2 based
- Streaming support
- Language agnostic
- Code generation
- Bi-directional streaming

#### Service Definition Example (Protocol Buffers)
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

message ProductRequest {
    string id = 1;
}

message ProductFilter {
    string category = 1;
    double min_price = 2;
    double max_price = 3;
}

message ProductUpdate {
    string id = 1;
    UpdateType type = 2;
    Product product = 3;
}

enum UpdateType {
    CREATED = 0;
    UPDATED = 1;
    DELETED = 2;
}
```

#### gRPC Communication Patterns
```mermaid
graph TD
    A[Unary] -->|Request/Response| B[Simple RPC]
    C[Server Streaming] -->|One Request/Multiple Responses| D[Server Stream RPC]
    E[Client Streaming] -->|Multiple Requests/One Response| F[Client Stream RPC]
    G[Bi-directional] -->|Multiple Requests/Responses| H[Bidirectional Stream RPC]
```

## API Design Best Practices

### 1. Versioning
```mermaid
graph LR
    A[API Versions] --> B[URI Path /v1/]
    A --> C[Query Parameter ?version=1]
    A --> D[Custom Header X-API-Version]
    A --> E[Content Negotiation Accept]
```

### 2. Security
- Authentication
- Authorization
- Rate limiting
- Input validation
- HTTPS
- API keys
- OAuth 2.0/OpenID Connect

### 3. Error Handling
```json
{
    "status": 400,
    "code": "INVALID_INPUT",
    "message": "Invalid product data",
    "details": [{
        "field": "price",
        "error": "must be greater than 0"
    }]
}
```

### 4. Documentation
- OpenAPI/Swagger for REST
- GraphQL Schema/Introspection
- Protocol Buffers for gRPC
- Code examples
- Authentication details
- Rate limiting info

### 5. Performance Optimization
```mermaid
graph TD
    A[API Performance] --> B[Caching]
    A --> C[Pagination]
    A --> D[Compression]
    A --> E[Connection Pooling]
    A --> F[Async Operations]
```

## API Design Patterns

### 1. CQRS (Command Query Responsibility Segregation)
```mermaid
graph TD
    A[API Client] --> B[Query API]
    A --> C[Command API]
    B --> D[Read Database]
    C --> E[Write Database]
    E --> F[Sync] --> D
```

### 2. API Gateway Pattern
```mermaid
graph TD
    A[Clients] --> B[API Gateway]
    B --> C[Authentication]
    B --> D[Rate Limiting]
    B --> E[Load Balancing]
    B --> F[Service 1]
    B --> G[Service 2]
    B --> H[Service 3]
```

### 3. Backend for Frontend (BFF)
```mermaid
graph TD
    A[Mobile Client] --> B[Mobile BFF]
    C[Web Client] --> D[Web BFF]
    E[Desktop Client] --> F[Desktop BFF]
    B --> G[Microservices]
    D --> G
    F --> G
```

## Comparison of API Styles

### REST
**Pros:**
- Simple and familiar
- Cacheable
- Scalable
- Wide tool support

**Cons:**
- Over/under-fetching
- Multiple round trips
- Endpoint proliferation

### GraphQL
**Pros:**
- Flexible data fetching
- Strong typing
- Single endpoint
- Real-time support

**Cons:**
- Complex caching
- Learning curve
- Server complexity

### gRPC
**Pros:**
- High performance
- Strong typing
- Code generation
- Bi-directional streaming

**Cons:**
- Limited browser support
- Binary protocol
- More complex setup

## API Design Decision Matrix

| Criteria | REST | GraphQL | gRPC |
|----------|------|---------|------|
| Performance | Good | Good | Excellent |
| Browser Support | Excellent | Excellent | Limited |
| Learning Curve | Low | Medium | High |
| Flexibility | Good | Excellent | Good |
| Tooling | Excellent | Good | Good |
| Real-time Support | Limited | Good | Excellent |
| Mobile Support | Good | Good | Excellent |

## Implementation Examples

### 1. REST API Implementation (Node.js/Express)
```javascript
const express = require('express');
const app = express();

app.get('/api/v1/products', (req, res) => {
    // List products
});

app.get('/api/v1/products/:id', (req, res) => {
    // Get single product
});

app.post('/api/v1/products', (req, res) => {
    // Create product
});
```

### 2. GraphQL Implementation (Node.js/Apollo)
```javascript
const typeDefs = gql`
  type Product {
    id: ID!
    name: String!
    price: Float!
  }
`;

const resolvers = {
  Query: {
    products: () => products,
    product: (_, { id }) => products.find(p => p.id === id)
  }
};
```

### 3. gRPC Implementation (Node.js)
```javascript
const service = {
  getProduct: (call, callback) => {
    const product = products.find(p => p.id === call.request.id);
    callback(null, product);
  }
};
```

## Conclusion

Choosing the right API style depends on your specific requirements:

- Use **REST** for:
  - Simple CRUD operations
  - Caching requirements
  - Wide client support

- Use **GraphQL** for:
  - Flexible data requirements
  - Reducing network requests
  - Real-time features
  - Multiple client types

- Use **gRPC** for:
  - Microservices communication
  - High-performance requirements
  - Streaming data
  - Code generation needs

The key is to understand these patterns deeply and select the appropriate style based on your specific use case, performance requirements, and team expertise.