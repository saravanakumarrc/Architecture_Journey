# Resilience Patterns and Implementation

```mermaid
mindmap
    root((Resilience
        Patterns))
        (Circuit Breaker)
            [State Management]
            [Fallback Logic]
            [Reset Strategy]
        (Retry)
            [Backoff Strategy]
            [Max Attempts]
            [Jitter]
        (Bulkhead)
            [Resource Isolation]
            [Thread Pools]
            [Connection Limits]
        (Timeout)
            [Connection Timeout]
            [Request Timeout]
            [Circuit Response]
```

## Fault Tolerance Architecture

```mermaid
graph TB
    subgraph "Resilience Layers"
        direction TB
        
        subgraph "Application Layer"
            CB[Circuit Breaker]
            RT[Retry Logic]
            TO[Timeout Handler]
        end
        
        subgraph "Infrastructure Layer"
            FO[Failover]
            HA[High Availability]
            DR[Disaster Recovery]
        end
        
        subgraph "Monitoring"
            M1[Health Checks]
            M2[Metrics]
            M3[Alerts]
        end
        
        CB --> M1
        RT --> M2
        TO --> M3
    end
```

## Implementation Examples

### 1. Circuit Breaker Pattern

```typescript
interface CircuitBreakerConfig {
    failureThreshold: number;
    resetTimeout: number;
    fallbackFn?: () => Promise<any>;
}

class CircuitBreaker {
    private failures: number = 0;
    private lastFailureTime?: Date;
    private state: 'CLOSED' | 'OPEN' | 'HALF_OPEN' = 'CLOSED';

    constructor(private config: CircuitBreakerConfig) {}

    async execute<T>(fn: () => Promise<T>): Promise<T> {
        if (this.state === 'OPEN') {
            if (this.shouldReset()) {
                this.state = 'HALF_OPEN';
            } else {
                return this.handleOpen();
            }
        }

        try {
            const result = await fn();
            this.handleSuccess();
            return result;
        } catch (error) {
            return this.handleFailure(error);
        }
    }

    private shouldReset(): boolean {
        if (!this.lastFailureTime) return false;
        const now = new Date();
        return (now.getTime() - this.lastFailureTime.getTime()) 
            >= this.config.resetTimeout;
    }

    private handleSuccess(): void {
        this.failures = 0;
        this.state = 'CLOSED';
    }

    private async handleFailure(error: Error): Promise<any> {
        this.failures++;
        this.lastFailureTime = new Date();

        if (this.failures >= this.config.failureThreshold) {
            this.state = 'OPEN';
        }

        if (this.config.fallbackFn) {
            return this.config.fallbackFn();
        }
        throw error;
    }

    private async handleOpen(): Promise<any> {
        if (this.config.fallbackFn) {
            return this.config.fallbackFn();
        }
        throw new Error('Circuit is OPEN');
    }
}
```

### 2. Retry Pattern with Exponential Backoff

```typescript
interface RetryConfig {
    maxAttempts: number;
    baseDelay: number;
    maxDelay: number;
    shouldRetry?: (error: Error) => boolean;
}

class RetryWithBackoff {
    constructor(private config: RetryConfig) {}

    async execute<T>(fn: () => Promise<T>): Promise<T> {
        let lastError: Error;
        
        for (let attempt = 1; attempt <= this.config.maxAttempts; attempt++) {
            try {
                return await fn();
            } catch (error) {
                lastError = error;
                
                if (this.config.shouldRetry && !this.config.shouldRetry(error)) {
                    throw error;
                }

                if (attempt === this.config.maxAttempts) {
                    throw error;
                }

                await this.delay(attempt);
            }
        }
        
        throw lastError;
    }

    private async delay(attempt: number): Promise<void> {
        const delay = Math.min(
            this.config.maxDelay,
            this.config.baseDelay * Math.pow(2, attempt - 1)
        );
        
        // Add jitter to prevent thundering herd
        const jitter = Math.random() * 100;
        await new Promise(resolve => setTimeout(resolve, delay + jitter));
    }
}
```

### 3. Bulkhead Pattern

```typescript
interface BulkheadConfig {
    maxConcurrentCalls: number;
    maxQueueSize: number;
    timeout: number;
}

class Bulkhead {
    private executingCalls: number = 0;
    private queue: Array<{
        resolve: (value: any) => void;
        reject: (error: Error) => void;
        fn: () => Promise<any>;
    }> = [];

    constructor(private config: BulkheadConfig) {}

    async execute<T>(fn: () => Promise<T>): Promise<T> {
        if (this.executingCalls >= this.config.maxConcurrentCalls) {
            return this.enqueue(fn);
        }

        return this.executeWithTimeout(fn);
    }

    private async enqueue<T>(fn: () => Promise<T>): Promise<T> {
        if (this.queue.length >= this.config.maxQueueSize) {
            throw new Error('Bulkhead queue is full');
        }

        return new Promise((resolve, reject) => {
            this.queue.push({ resolve, reject, fn });
        });
    }

    private async executeWithTimeout<T>(fn: () => Promise<T>): Promise<T> {
        this.executingCalls++;

        try {
            const timeoutPromise = new Promise((_, reject) => {
                setTimeout(() => reject(new Error('Operation timed out')), 
                    this.config.timeout);
            });

            const result = await Promise.race([fn(), timeoutPromise]);
            return result as T;
        } finally {
            this.executingCalls--;
            this.processQueue();
        }
    }

    private processQueue(): void {
        if (this.queue.length === 0) return;
        if (this.executingCalls >= this.config.maxConcurrentCalls) return;

        const next = this.queue.shift();
        if (next) {
            this.executeWithTimeout(next.fn)
                .then(next.resolve)
                .catch(next.reject);
        }
    }
}
```

## Resilience Strategy Patterns

```mermaid
flowchart TB
    subgraph "Resilience Strategy"
        direction TB
        
        Request[Client Request] --> CB{Circuit Breaker}
        CB -->|Closed| RT[Retry Pattern]
        CB -->|Open| FB[Fallback]
        
        RT --> BH[Bulkhead]
        BH --> S[Service]
        
        S -->|Success| CB
        S -->|Failure| CB
        
        subgraph "Monitoring & Recovery"
            M[Metrics]
            A[Alerts]
            R[Recovery]
        end
    end
```

## Monitoring and Recovery Flow

```mermaid
sequenceDiagram
    participant C as Client
    participant R as Resilience Layer
    participant S as Service
    participant M as Monitoring
    
    C->>R: Request
    R->>S: Protected Call
    
    alt Success
        S-->>R: Response
        R-->>C: Response
        R->>M: Log Success
    else Failure
        S-->>R: Error
        R->>M: Log Failure
        R->>R: Apply Pattern
        R-->>C: Fallback/Retry
    end
```

## Best Practices

1. **Pattern Combination**
   - Layer resilience patterns appropriately
   - Consider interaction between patterns
   - Monitor pattern effectiveness
   - Adjust thresholds based on metrics

2. **Configuration Guidelines**
   - Set appropriate timeouts
   - Configure reasonable retry limits
   - Implement gradual circuit breaker recovery
   - Use backoff strategies

3. **Monitoring Requirements**
   - Track pattern state changes
   - Monitor failure rates
   - Measure recovery times
   - Alert on pattern activation

4. **Testing Strategies**
   - Chaos engineering
   - Failure injection
   - Load testing
   - Recovery validation

Remember: Resilience patterns should be implemented thoughtfully and monitored continuously. The goal is to maintain system stability while gracefully handling failures.