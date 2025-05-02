# Cloud Architecture Patterns

## Core Cloud Design Patterns

### 1. Availability Patterns

#### Circuit Breaker Pattern
```typescript
class CircuitBreaker {
    private failureThreshold: number;
    private resetTimeout: number;
    private failures: number = 0;
    private lastFailureTime?: Date;
    private state: 'CLOSED' | 'OPEN' | 'HALF_OPEN' = 'CLOSED';

    constructor(threshold: number, resetTimeoutMs: number) {
        this.failureThreshold = threshold;
        this.resetTimeout = resetTimeoutMs;
    }

    async execute<T>(operation: () => Promise<T>): Promise<T> {
        if (this.isOpen()) {
            throw new Error('Circuit breaker is OPEN');
        }

        try {
            const result = await operation();
            this.reset();
            return result;
        } catch (error) {
            this.recordFailure();
            throw error;
        }
    }

    private isOpen(): boolean {
        if (this.state === 'OPEN') {
            if (this.lastFailureTime && 
                Date.now() - this.lastFailureTime.getTime() > this.resetTimeout) {
                this.state = 'HALF_OPEN';
                return false;
            }
            return true;
        }
        return false;
    }

    private recordFailure(): void {
        this.failures++;
        this.lastFailureTime = new Date();
        if (this.failures >= this.failureThreshold) {
            this.state = 'OPEN';
        }
    }

    private reset(): void {
        this.failures = 0;
        this.state = 'CLOSED';
    }
}
```

#### Health Check Pattern
```typescript
interface HealthCheck {
    check(): Promise<HealthStatus>;
}

class ServiceHealthCheck implements HealthCheck {
    private services: Map<string, () => Promise<boolean>>;

    async check(): Promise<HealthStatus> {
        const results = new Map<string, boolean>();
        
        for (const [service, checkFn] of this.services) {
            try {
                results.set(service, await checkFn());
            } catch {
                results.set(service, false);
            }
        }

        return {
            status: Array.from(results.values()).every(v => v) ? 'healthy' : 'unhealthy',
            timestamp: new Date(),
            checks: results
        };
    }
}
```

### 2. Scalability Patterns

#### Queue-Based Load Leveling
```typescript
class MessageQueue<T> {
    private queue: Array<T> = [];
    private consumers: Set<(item: T) => Promise<void>> = new Set();

    async enqueue(item: T): Promise<void> {
        this.queue.push(item);
        await this.processQueue();
    }

    registerConsumer(consumer: (item: T) => Promise<void>): void {
        this.consumers.add(consumer);
    }

    private async processQueue(): Promise<void> {
        while (this.queue.length > 0) {
            const item = this.queue.shift();
            if (item) {
                const promises = Array.from(this.consumers)
                    .map(consumer => consumer(item));
                await Promise.all(promises);
            }
        }
    }
}
```

#### Auto-Scaling Pattern
```typescript
interface ScalingStrategy {
    evaluate(metrics: SystemMetrics): ScalingDecision;
}

class HorizontalScaling implements ScalingStrategy {
    private readonly maxInstances: number;
    private readonly minInstances: number;
    private readonly targetCpuUtilization: number;

    evaluate(metrics: SystemMetrics): ScalingDecision {
        const avgCpu = metrics.getCpuUtilization();
        
        if (avgCpu > this.targetCpuUtilization && 
            metrics.instanceCount < this.maxInstances) {
            return {
                action: 'SCALE_OUT',
                amount: 1
            };
        }

        if (avgCpu < this.targetCpuUtilization / 2 && 
            metrics.instanceCount > this.minInstances) {
            return {
                action: 'SCALE_IN',
                amount: 1
            };
        }

        return { action: 'NO_ACTION' };
    }
}
```

### 3. Data Management Patterns

#### Cache-Aside Pattern
```typescript
class CacheAside<T> {
    constructor(
        private cache: Cache<T>,
        private dataStore: DataStore<T>
    ) {}

    async get(key: string): Promise<T> {
        // Try cache first
        const cached = await this.cache.get(key);
        if (cached) {
            return cached;
        }

        // Cache miss - get from data store
        const data = await this.dataStore.get(key);
        if (data) {
            await this.cache.set(key, data);
        }
        return data;
    }

    async update(key: string, value: T): Promise<void> {
        await this.dataStore.set(key, value);
        await this.cache.invalidate(key);
    }
}
```

#### CQRS Pattern
```typescript
interface Command {
    execute(): Promise<void>;
}

interface Query<T> {
    execute(): Promise<T>;
}

class CommandBus {
    private handlers: Map<string, (command: any) => Promise<void>> = new Map();

    register<T extends Command>(
        commandType: string, 
        handler: (command: T) => Promise<void>
    ): void {
        this.handlers.set(commandType, handler);
    }

    async dispatch(command: Command): Promise<void> {
        const handler = this.handlers.get(command.constructor.name);
        if (!handler) {
            throw new Error(`No handler for command ${command.constructor.name}`);
        }
        await handler(command);
    }
}
```

## Implementation Considerations

### 1. Security
- Identity and Access Management (IAM)
- Network Security Groups
- Encryption in Transit and at Rest
- Key Management
- Security Monitoring and Logging

### 2. Cost Optimization
- Resource Right-sizing
- Reserved Instances
- Auto-scaling Policies
- Storage Tier Optimization
- Network Traffic Optimization

### 3. Operational Excellence
- Infrastructure as Code
- Automated Deployments
- Monitoring and Alerting
- Incident Response
- Disaster Recovery

## Best Practices

### 1. Infrastructure Design
- Use managed services when possible
- Implement proper tagging strategy
- Define network boundaries
- Plan for multi-region deployment
- Design for failure

### 2. Application Design
- Follow 12-factor app principles
- Implement proper logging
- Use configuration management
- Design for statelessness
- Implement proper error handling

### 3. Monitoring and Maintenance
- Set up comprehensive monitoring
- Implement automated scaling
- Regular security updates
- Backup and recovery testing
- Performance optimization

## Common Anti-patterns to Avoid

1. **Lift and Shift Without Optimization**
2. **Treating Cloud as Data Center**
3. **Ignoring Cloud-Native Features**
4. **Over-provisioning Resources**
5. **Insufficient Monitoring**

## Cloud Provider Patterns

### AWS-Specific Patterns
```typescript
class AwsLambdaHandler {
    async handle(event: any, context: any): Promise<any> {
        try {
            // Implement cold start optimization
            await this.warmup();
            
            // Process event
            const result = await this.processEvent(event);
            
            return {
                statusCode: 200,
                body: JSON.stringify(result)
            };
        } catch (error) {
            return {
                statusCode: 500,
                body: JSON.stringify({ error: error.message })
            };
        }
    }
}
```

### Azure-Specific Patterns
```typescript
class AzureFunctionApp {
    @FunctionName('HttpTrigger')
    async run(
        @HttpTrigger(AuthLevel.Function) req: HttpRequest,
        context: Context
    ): Promise<void> {
        context.log('Processing request');
        
        try {
            const result = await this.processRequest(req);
            context.res = {
                status: 200,
                body: result
            };
        } catch (error) {
            context.res = {
                status: 500,
                body: error.message
            };
        }
    }
}
```

## Testing Cloud Applications

### 1. Unit Testing
```typescript
describe('Cloud Service Tests', () => {
    it('should handle service unavailability', async () => {
        const service = new CloudService();
        const circuitBreaker = new CircuitBreaker(3, 1000);
        
        // Simulate service failure
        mockCloudApi.failNext(3);
        
        await expect(
            circuitBreaker.execute(() => service.call())
        ).rejects.toThrow('Circuit breaker is OPEN');
    });
});
```

### 2. Integration Testing
```typescript
describe('Cloud Integration', () => {
    it('should handle eventual consistency', async () => {
        const dataStore = new CloudDataStore();
        const item = { id: '123', value: 'test' };
        
        await dataStore.write(item);
        
        // Account for eventual consistency
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        const result = await dataStore.read(item.id);
        expect(result).toEqual(item);
    });
});
```