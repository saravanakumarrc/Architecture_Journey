# Monitoring and Observability Platforms

## Core Concepts

### 1. Three Pillars of Observability
- Metrics
- Traces
- Logs

### 2. Monitoring Fundamentals
- Data collection
- Aggregation
- Visualization
- Alerting
- Correlation

## Popular Platforms

### 1. Prometheus & Grafana Stack

#### Prometheus
```yaml
# Example prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'spring-actuator'
    metrics_path: '/actuator/prometheus'
    static_configs:
      - targets: ['localhost:8080']

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['localhost:9100']
```

#### Grafana Dashboard
```json
{
  "dashboard": {
    "panels": [
      {
        "title": "CPU Usage",
        "type": "graph",
        "datasource": "Prometheus",
        "targets": [
          {
            "expr": "rate(process_cpu_seconds_total[5m])",
            "legendFormat": "{{instance}}"
          }
        ]
      }
    ]
  }
}
```

### 2. ELK Stack (Elasticsearch, Logstash, Kibana)

#### Logstash Pipeline
```ruby
# Example Logstash config
input {
  beats {
    port => 5044
  }
}

filter {
  grok {
    match => { "message" => "%{COMBINEDAPACHELOG}" }
  }
  date {
    match => [ "timestamp", "dd/MMM/yyyy:HH:mm:ss Z" ]
  }
}

output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "web-logs-%{+YYYY.MM.dd}"
  }
}
```

### 3. Azure Monitor

#### Application Insights
```javascript
// Example instrumentation
const appInsights = require('applicationinsights');
appInsights
  .setup('YOUR_INSTRUMENTATION_KEY')
  .setAutoDependencyCorrelation(true)
  .setAutoCollectRequests(true)
  .setAutoCollectPerformance(true)
  .setAutoCollectExceptions(true)
  .setAutoCollectDependencies(true)
  .setAutoCollectConsole(true)
  .setUseDiskRetryCaching(true)
  .start();
```

### 4. Datadog

#### Agent Configuration
```yaml
# Example datadog.yaml
api_key: YOUR_API_KEY
site: datadoghq.com
logs_enabled: true

apm_config:
  enabled: true
  
process_config:
  enabled: true
```

## Implementation Patterns

### 1. Metrics Collection
```python
# Example using Prometheus client
from prometheus_client import Counter, Histogram
import time

REQUEST_COUNT = Counter(
    'request_count_total',
    'Total number of requests',
    ['method', 'endpoint']
)

REQUEST_LATENCY = Histogram(
    'request_latency_seconds',
    'Request latency in seconds',
    ['method', 'endpoint']
)

def handle_request(method, endpoint):
    REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
    
    start = time.time()
    # ... handle request ...
    duration = time.time() - start
    
    REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(duration)
```

### 2. Distributed Tracing
```python
# Example using OpenTelemetry
from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode

tracer = trace.get_tracer(__name__)

@tracer.start_as_current_span("process_order")
def process_order(order_id):
    with tracer.start_span("validate_order") as span:
        # ... validation logic ...
        span.set_attribute("order.id", order_id)
        span.set_status(Status(StatusCode.OK))
    
    with tracer.start_span("payment_processing") as span:
        # ... payment logic ...
        span.set_attribute("payment.amount", amount)
```

### 3. Log Aggregation
```python
# Example using structured logging
import structlog

logger = structlog.get_logger()

def process_transaction(transaction_id, amount):
    logger.info(
        "processing_transaction",
        transaction_id=transaction_id,
        amount=amount,
        status="started"
    )
    try:
        # Process transaction
        logger.info(
            "transaction_completed",
            transaction_id=transaction_id,
            status="success"
        )
    except Exception as e:
        logger.error(
            "transaction_failed",
            transaction_id=transaction_id,
            error=str(e)
        )
```

## Best Practices

### 1. Metric Design
- Use clear naming conventions
- Define appropriate labels/tags
- Choose proper metric types
- Consider cardinality

### 2. Alert Design
```yaml
# Example Prometheus alert rule
groups:
- name: example
  rules:
  - alert: HighErrorRate
    expr: rate(http_requests_total{status=~"5.."}[5m]) > 1
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: High error rate detected
      description: "Error rate is {{ $value }} per second"
```

### 3. Dashboard Design
- Group related metrics
- Use consistent time ranges
- Include context
- Design for different audiences

## Advanced Patterns

### 1. SLO Monitoring
```yaml
# Example SLO configuration
slo_rules:
  - name: "API Availability"
    target: 99.9
    window: 30d
    metric:
      name: "http_request_duration_seconds"
      success_criteria:
        - status_code < 500
        - latency < 1s
```

### 2. Anomaly Detection
```python
# Example using statistical analysis
def detect_anomalies(metric_values, threshold=3):
    mean = np.mean(metric_values)
    std = np.std(metric_values)
    z_scores = [(x - mean) / std for x in metric_values]
    return [abs(z) > threshold for z in z_scores]
```

### 3. Correlation Analysis
```python
# Example trace correlation
def correlate_events(trace_id):
    logs = query_logs(trace_id=trace_id)
    metrics = query_metrics(trace_id=trace_id)
    traces = query_traces(trace_id=trace_id)
    
    return {
        'logs': logs,
        'metrics': metrics,
        'traces': traces
    }
```

## Integration Examples

### 1. Kubernetes Monitoring
```yaml
# Example Prometheus ServiceMonitor
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: app-monitor
spec:
  selector:
    matchLabels:
      app: myapp
  endpoints:
  - port: metrics
```

### 2. Cloud Integration
```typescript
// Example Azure Monitor integration
import * as monitoring from '@azure/monitor-query';

async function queryMetrics(resourceId: string) {
    const client = new monitoring.MetricsQueryClient(credential);
    const result = await client.queryResource(
        resourceId,
        ['Percentage CPU'],
        {
            timespan: {startTime, endTime},
            interval: monitoring.duration('PT1M')
        }
    );
}
```

## References
- Prometheus Documentation
- Grafana Documentation
- Azure Monitor Documentation
- OpenTelemetry Documentation
- Site Reliability Engineering (Google)