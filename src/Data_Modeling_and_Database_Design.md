# Data Modeling and Database Design

```mermaid
mindmap
    root((Database
        Design))
        (Relational)
            [Normalization]
            [Indexes]
            [Constraints]
        (NoSQL)
            [Document]
            [Key-Value]
            [Graph]
        (Patterns)
            [Sharding]
            [Replication]
            [Caching]
```

## Data Modeling Concepts

### 1. Conceptual Data Model
The highest-level view of data relationships, focusing on business concepts rather than technical implementation.

Example:
```mermaid
erDiagram
    Customer ||--o{ Order : places
    Order ||--|{ OrderItem : contains
    Product ||--o{ OrderItem : "is part of"
```

### 2. Logical Data Model
Describes data in detail without regard to physical implementation. Includes all entities and relationships.

Example for an E-commerce System:
```mermaid
erDiagram
    Customer {
        int customer_id PK
        string name
        string email
        string address
    }
    Order {
        int order_id PK
        int customer_id FK
        date order_date
        string status
    }
    OrderItem {
        int order_item_id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal price
    }
    Product {
        int product_id PK
        string name
        decimal price
        int stock
    }
    Customer ||--o{ Order : places
    Order ||--|{ OrderItem : contains
    Product ||--o{ OrderItem : "is part of"
```

### 3. Physical Data Model
Represents the actual implementation of the database, including tables, columns, data types, and constraints.

Example SQL Schema:
```sql
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    address TEXT
);

CREATE TABLE Order (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);
```

## Database Design Concepts

### 1. Normalization
Process of organizing data to reduce redundancy and improve data integrity.

#### First Normal Form (1NF)
- Atomic values (indivisible)
- No repeating groups

Before 1NF:
```
Customer(id, name, phone_numbers)
1, John Doe, "555-0123, 555-0124"
```

After 1NF:
```
Customer(id, name)
1, John Doe

CustomerPhone(customer_id, phone_number)
1, 555-0123
1, 555-0124
```

#### Second Normal Form (2NF)
- Must be in 1NF
- No partial dependencies

#### Third Normal Form (3NF)
- Must be in 2NF
- No transitive dependencies

### 2. Denormalization
Strategic decision to allow redundancy for performance benefits.

Example:
```mermaid
erDiagram
    Order {
        int order_id PK
        int customer_id FK
        string customer_name
        string customer_email
        date order_date
    }
```

### 3. Database Relationships

```mermaid
graph TD
    A[One-to-One] --> B[Example: Person - Passport]
    C[One-to-Many] --> D[Example: Customer - Orders]
    E[Many-to-Many] --> F[Example: Students - Courses]
```

#### Implementation Examples:

1. One-to-One:
```sql
CREATE TABLE Person (
    person_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Passport (
    passport_id INT PRIMARY KEY,
    person_id INT UNIQUE,
    passport_number VARCHAR(20),
    FOREIGN KEY (person_id) REFERENCES Person(person_id)
);
```

2. One-to-Many:
```sql
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Order (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);
```

3. Many-to-Many:
```sql
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Course (
    course_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE StudentCourse (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);
```

### 4. Indexing Strategies

#### Types of Indexes:
- Primary Index
- Secondary Index
- Composite Index
- Clustered vs. Non-clustered Index

Example:
```sql
-- Primary Index (automatically created with PRIMARY KEY)
CREATE TABLE Product (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2)
);

-- Secondary Index
CREATE INDEX idx_product_name ON Product(name);

-- Composite Index
CREATE INDEX idx_product_name_price ON Product(name, price);
```

### 5. Partitioning

#### Horizontal Partitioning (Sharding)
```mermaid
graph TD
    A[Orders Table] --> B[Orders 2023]
    A --> C[Orders 2024]
    A --> D[Orders 2025]
```

#### Vertical Partitioning
```mermaid
graph TD
    A[Product Table] --> B[Product Basic Info<br>id, name, price]
    A --> C[Product Details<br>description, specifications]
    A --> D[Product Media<br>images, videos]
```

## Database Patterns

```mermaid
graph TB
    subgraph "Data Storage Patterns"
        direction TB
        
        subgraph "RDBMS Patterns"
            N1[1NF]
            N2[2NF]
            N3[3NF]
            N1 --> N2
            N2 --> N3
        end
        
        subgraph "NoSQL Patterns"
            D[Denormalization]
            E[Embedding]
            R[Referencing]
            D --- E
            E --- R
        end
        
        subgraph "Hybrid Patterns"
            P[Polyglot Persistence]
            C[CQRS]
            ES[Event Sourcing]
        end
    end
```

## Data Access Patterns

```mermaid
sequenceDiagram
    participant A as Application
    participant C as Cache
    participant DB as Database
    participant R as Replica
    
    A->>C: Check Cache
    alt Cache Hit
        C-->>A: Return Data
    else Cache Miss
        C->>DB: Read Data
        DB-->>C: Return Data
        C-->>A: Return Data
    end
    
    DB->>R: Replicate Changes
```

## Implementation Examples

### 1. Repository Pattern

```typescript
interface Repository<T> {
    findById(id: string): Promise<T | null>;
    findAll(criteria: FilterCriteria): Promise<T[]>;
    create(entity: T): Promise<T>;
    update(id: string, entity: Partial<T>): Promise<T>;
    delete(id: string): Promise<void>;
}

class UserRepository implements Repository<User> {
    constructor(
        private db: Database,
        private cache: Cache
    ) {}

    async findById(id: string): Promise<User | null> {
        // Check cache first
        const cached = await this.cache.get(`user:${id}`);
        if (cached) return JSON.parse(cached);

        // Query database
        const user = await this.db.query(
            'SELECT * FROM users WHERE id = ?',
            [id]
        );

        // Cache result
        if (user) {
            await this.cache.set(
                `user:${id}`,
                JSON.stringify(user),
                { ttl: 3600 }
            );
        }

        return user;
    }

    async create(user: User): Promise<User> {
        const result = await this.db.query(
            'INSERT INTO users (name, email) VALUES (?, ?)',
            [user.name, user.email]
        );

        // Invalidate cache
        await this.cache.delete(`user:${result.id}`);

        return { ...user, id: result.id };
    }
}
```

### 2. Query Builder Pattern

```typescript
class QueryBuilder {
    private conditions: string[] = [];
    private params: any[] = [];
    private sorts: string[] = [];
    private limitValue?: number;
    private offsetValue?: number;

    where(field: string, operator: string, value: any): this {
        this.conditions.push(`${field} ${operator} ?`);
        this.params.push(value);
        return this;
    }

    orderBy(field: string, direction: 'ASC' | 'DESC'): this {
        this.sorts.push(`${field} ${direction}`);
        return this;
    }

    limit(value: number): this {
        this.limitValue = value;
        return this;
    }

    offset(value: number): this {
        this.offsetValue = value;
        return this;
    }

    build(): { sql: string; params: any[] } {
        let sql = 'SELECT * FROM users';

        if (this.conditions.length) {
            sql += ` WHERE ${this.conditions.join(' AND ')}`;
        }

        if (this.sorts.length) {
            sql += ` ORDER BY ${this.sorts.join(', ')}`;
        }

        if (this.limitValue !== undefined) {
            sql += ` LIMIT ${this.limitValue}`;
        }

        if (this.offsetValue !== undefined) {
            sql += ` OFFSET ${this.offsetValue}`;
        }

        return { sql, params: this.params };
    }
}
```

### 3. Unit of Work Pattern

```typescript
class UnitOfWork {
    private transactions: Transaction[] = [];

    async begin(): Promise<void> {
        const transaction = await this.db.beginTransaction();
        this.transactions.push(transaction);
    }

    async commit(): Promise<void> {
        const transaction = this.transactions.pop();
        if (!transaction) {
            throw new Error('No active transaction');
        }
        await transaction.commit();
    }

    async rollback(): Promise<void> {
        const transaction = this.transactions.pop();
        if (!transaction) {
            throw new Error('No active transaction');
        }
        await transaction.rollback();
    }

    async execute<T>(work: () => Promise<T>): Promise<T> {
        await this.begin();
        try {
            const result = await work();
            await this.commit();
            return result;
        } catch (error) {
            await this.rollback();
            throw error;
        }
    }
}
```

## Data Model Visualization

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    USER {
        string id
        string name
        string email
        datetime created_at
    }
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER {
        string id
        string user_id
        decimal total
        string status
        datetime created_at
    }
    ORDER_ITEM {
        string id
        string order_id
        string product_id
        integer quantity
        decimal price
    }
    PRODUCT ||--o{ ORDER_ITEM : references
    PRODUCT {
        string id
        string name
        string description
        decimal price
        integer stock
    }
```

## Best Practices

1. **Use Appropriate Data Types**
   - Choose the most appropriate data type for each column
   - Consider storage and performance implications

2. **Implement Constraints**
   - Primary Keys
   - Foreign Keys
   - Unique Constraints
   - Check Constraints
   - Not Null Constraints

3. **Design for Scale**
   - Consider future growth
   - Plan for partitioning
   - Implement proper indexing
   - Use appropriate normalization level

4. **Security Considerations**
   - Implement proper access controls
   - Encrypt sensitive data
   - Use parameterized queries
   - Regular security audits

5. **Performance Optimization**
   - Efficient indexing strategy
   - Query optimization
   - Proper normalization/denormalization balance
   - Regular maintenance and monitoring

## Common Design Patterns

### 1. Event Sourcing
```mermaid
sequenceDiagram
    participant C as Client
    participant ES as Event Store
    participant S as State Store
    C->>ES: Store Event
    ES->>S: Update State
    S->>C: Return Current State
```

### 2. CQRS (Command Query Responsibility Segregation)
```mermaid
graph TD
    A[Client] --> B[Command Model]
    A --> C[Query Model]
    B --> D[Write Database]
    C --> E[Read Database]
    D --> F[Sync]
    F --> E
```

### 3. Multi-tenant Data Architecture
```mermaid
graph TD
    A[Multi-tenant Application] --> B[Separate Databases]
    A --> C[Shared Database, Separate Schemas]
    A --> D[Shared Database, Shared Schema]
```

## Database Types and Use Cases

```mermaid
graph TB
    subgraph "Database Categories"
        direction TB
        
        subgraph "Relational"
            R1[PostgreSQL]
            R2[MySQL]
            R3[SQL Server]
        end
        
        subgraph "Document"
            D1[MongoDB]
            D2[CouchDB]
        end
        
        subgraph "Key-Value"
            K1[Redis]
            K2[DynamoDB]
        end
        
        subgraph "Graph"
            G1[Neo4j]
            G2[ArangoDB]
        end
    end
```

### 1. Relational Databases (RDBMS)
- PostgreSQL
- MySQL
- SQL Server
- Oracle

Best for: Structured data with complex relationships

### 2. Document Databases
- MongoDB
- CouchDB

Best for: Semi-structured data, flexible schema requirements

### 3. Key-Value Stores
- Redis
- DynamoDB

Best for: Caching, session management, real-time data

### 4. Graph Databases
- Neo4j
- ArangoDB

Best for: Highly connected data (social networks, recommendation engines)

### 5. Time Series Databases
- InfluxDB
- TimescaleDB

Best for: Time-series data, monitoring, IoT applications

## Data Relationships

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : "ordered in"
    CUSTOMER {
        string id
        string name
        string email
    }
    ORDER {
        string id
        date created_at
        string status
    }
    PRODUCT {
        string id
        string name
        decimal price
    }
    ORDER_ITEM {
        string order_id
        string product_id
        integer quantity
    }
```

## Conclusion

Effective data modeling and database design are crucial for building scalable, maintainable, and efficient systems. The key is to understand these concepts deeply and know when to apply which approach based on your specific use case and requirements.