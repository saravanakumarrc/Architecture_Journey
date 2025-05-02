# Database Concepts and Patterns

## Core Database Types

### 1. SQL Databases
- ACID Properties
- Transaction Management
- Referential Integrity
- Schema Enforcement

### 2. NoSQL Databases
- Document Stores
- Key-Value Stores
- Column-Family Stores
- Graph Databases

## Implementation Patterns

### 1. Multi-Model Database Pattern
```typescript
interface DatabaseStrategy<T> {
    create(data: T): Promise<T>;
    read(id: string): Promise<T>;
    update(id: string, data: Partial<T>): Promise<T>;
    delete(id: string): Promise<boolean>;
}

class MongoDbStrategy<T> implements DatabaseStrategy<T> {
    private collection: Collection<T>;
    
    async create(data: T): Promise<T> {
        const result = await this.collection.insertOne(data);
        return { ...data, _id: result.insertedId };
    }
    // ... other implementations
}

class PostgresStrategy<T> implements DatabaseStrategy<T> {
    private table: string;
    
    async create(data: T): Promise<T> {
        const result = await this.pool.query(
            `INSERT INTO ${this.table} ($1) VALUES ($2) RETURNING *`,
            [Object.keys(data), Object.values(data)]
        );
        return result.rows[0];
    }
    // ... other implementations
}
```

### 2. Connection Pool Pattern
```typescript
class DatabasePool {
    private static instance: DatabasePool;
    private pool: Pool;
    
    private constructor() {
        this.pool = new Pool({
            max: 20,
            idleTimeoutMillis: 30000,
            connectionTimeoutMillis: 2000,
        });
    }
    
    public static getInstance(): DatabasePool {
        if (!DatabasePool.instance) {
            DatabasePool.instance = new DatabasePool();
        }
        return DatabasePool.instance;
    }
    
    public async query(sql: string, params?: any[]): Promise<QueryResult> {
        const client = await this.pool.connect();
        try {
            return await client.query(sql, params);
        } finally {
            client.release();
        }
    }
}
```

### 3. Database Sharding Pattern
```typescript
interface ShardingStrategy {
    getShardId(key: string): string;
    getShardConnection(shardId: string): Promise<Connection>;
}

class HashBasedSharding implements ShardingStrategy {
    private shardConnections: Map<string, Connection>;
    private totalShards: number;
    
    getShardId(key: string): string {
        const hash = createHash('md5').update(key).digest('hex');
        const shardNumber = parseInt(hash, 16) % this.totalShards;
        return `shard_${shardNumber}`;
    }
    
    async getShardConnection(shardId: string): Promise<Connection> {
        return this.shardConnections.get(shardId);
    }
}
```

## Design Considerations

### 1. Scaling Strategies
- Vertical Scaling
- Horizontal Scaling
- Read Replicas
- Write Sharding

### 2. Data Consistency Models
```typescript
enum ConsistencyLevel {
    STRONG = 'STRONG',
    EVENTUAL = 'EVENTUAL',
    CAUSAL = 'CAUSAL'
}

interface ConsistencyStrategy {
    read(key: string, level: ConsistencyLevel): Promise<any>;
    write(key: string, value: any, level: ConsistencyLevel): Promise<void>;
}

class DatabaseConsistency implements ConsistencyStrategy {
    async read(key: string, level: ConsistencyLevel): Promise<any> {
        switch (level) {
            case ConsistencyLevel.STRONG:
                return await this.readFromPrimary(key);
            case ConsistencyLevel.EVENTUAL:
                return await this.readFromAnyReplica(key);
            case ConsistencyLevel.CAUSAL:
                return await this.readWithCausalConsistency(key);
        }
    }
}
```

### 3. Caching Strategies
```typescript
interface CacheStrategy {
    get(key: string): Promise<any>;
    set(key: string, value: any, ttl?: number): Promise<void>;
    invalidate(key: string): Promise<void>;
}

class MultiLevelCache implements CacheStrategy {
    private l1Cache: Map<string, any>;
    private l2Cache: Redis;
    
    async get(key: string): Promise<any> {
        // Try L1 Cache
        const l1Result = this.l1Cache.get(key);
        if (l1Result) return l1Result;
        
        // Try L2 Cache
        const l2Result = await this.l2Cache.get(key);
        if (l2Result) {
            this.l1Cache.set(key, l2Result);
            return l2Result;
        }
        
        return null;
    }
}
```

## Best Practices

### 1. Query Optimization
- Use appropriate indexes
- Optimize query patterns
- Monitor query performance
- Use query caching

### 2. Data Security
- Encryption at rest
- Encryption in transit
- Access control
- Audit logging

### 3. Backup and Recovery
- Regular backups
- Point-in-time recovery
- Disaster recovery planning
- Data validation

## Common Anti-patterns to Avoid

1. **N+1 Query Problem**
2. **Database as a Message Queue**
3. **Single Table for All Data**
4. **No Index Strategy**
5. **Storing File Blobs in Database**

## Performance Monitoring

### 1. Key Metrics
- Query response time
- Connection pool utilization
- Cache hit ratio
- Index effectiveness

### 2. Monitoring Implementation
```typescript
class DatabaseMonitor {
    private metrics: Map<string, Metric>;
    
    trackQuery(sql: string, duration: number): void {
        const metric = this.metrics.get(sql) || new QueryMetric();
        metric.recordExecution(duration);
        this.metrics.set(sql, metric);
    }
    
    getSlowQueries(threshold: number): Query[] {
        return Array.from(this.metrics.entries())
            .filter(([_, metric]) => metric.averageDuration > threshold)
            .map(([sql, metric]) => ({
                sql,
                avgDuration: metric.averageDuration,
                executionCount: metric.executionCount
            }));
    }
}
```

## Testing Strategies

### 1. Unit Testing
```typescript
describe('Database Operations', () => {
    it('should handle concurrent writes correctly', async () => {
        const db = new Database();
        const writes = Array(10).fill(0).map(() => 
            db.write('key', Math.random())
        );
        
        await Promise.all(writes);
        const finalValue = await db.read('key');
        expect(finalValue).toBeDefined();
    });
});
```

### 2. Integration Testing
```typescript
describe('Database Integration', () => {
    it('should maintain ACID properties', async () => {
        const transaction = new Transaction();
        
        try {
            await transaction.begin();
            await account1.withdraw(100);
            await account2.deposit(100);
            await transaction.commit();
        } catch (error) {
            await transaction.rollback();
            throw error;
        }
        
        const balance1 = await account1.getBalance();
        const balance2 = await account2.getBalance();
        expect(balance1 + balance2).toBe(initialTotal);
    });
});
```