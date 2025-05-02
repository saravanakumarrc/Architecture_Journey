# Kubernetes Components and Architecture

## Control Plane Components

### API Server
- Primary management point
- RESTful API interface
- Authentication and authorization
- Resource validation and persistence

### etcd
- Distributed key-value store
- Cluster state storage
- Consistency and high availability
- Backup and recovery options

### Controller Manager
- Node Controller
- Replication Controller
- Endpoint Controller
- Service Account & Token Controllers

### Scheduler
- Pod placement decisions
- Resource requirements
- Node selection
- Affinity/anti-affinity rules

## Node Components

### kubelet
```yaml
# Example kubelet configuration
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
address: "0.0.0.0"
port: 10250
authentication:
  webhook:
    enabled: true
authorization:
  mode: Webhook
```

### kube-proxy
- Network proxy
- Service abstraction
- Load balancing
- IP tables management

### Container Runtime
- containerd/Docker
- CRI compliance
- Image management
- Container lifecycle

## Core Concepts

### Pods
```yaml
# Example Pod manifest
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```

### Services
```yaml
# Example Service types
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8080
  type: LoadBalancer  # ClusterIP, NodePort, LoadBalancer
```

### Deployments
```yaml
# Example Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
```

## Advanced Concepts

### StatefulSets
```yaml
# Example StatefulSet
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: "nginx"
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi
```

### DaemonSets
```yaml
# Example DaemonSet
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd-elasticsearch
spec:
  selector:
    matchLabels:
      name: fluentd-elasticsearch
  template:
    metadata:
      labels:
        name: fluentd-elasticsearch
    spec:
      containers:
      - name: fluentd-elasticsearch
        image: quay.io/fluentd_elasticsearch/fluentd:v2.5.2
```

## Networking

### CNI (Container Network Interface)
- Network plugin architecture
- Pod networking
- Network policies
- Service networking

### Service Discovery
1. DNS
```yaml
# CoreDNS configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |
    .:53 {
        errors
        health
        kubernetes cluster.local in-addr.arpa ip6.arpa {
           pods insecure
           upstream
           fallthrough in-addr.arpa ip6.arpa
        }
        prometheus :9153
        forward . /etc/resolv.conf
        cache 30
        loop
        reload
        loadbalance
    }
```

2. Service Types
- ClusterIP
- NodePort
- LoadBalancer
- ExternalName

## Storage

### Storage Classes
```yaml
# Example StorageClass
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
reclaimPolicy: Retain
allowVolumeExpansion: true
```

### Persistent Volumes
```yaml
# Example PV and PVC
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0003
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Recycle
  storageClassName: slow
  nfs:
    path: /tmp
    server: 172.17.0.2
```

## Security

### RBAC
```yaml
# Example Role and RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
- kind: User
  name: jane
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

### Network Policies
```yaml
# Example NetworkPolicy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-allow
spec:
  podSelector:
    matchLabels:
      app: api
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
    ports:
    - protocol: TCP
      port: 8080
```

## High Availability

### Control Plane HA
1. Multi-Master Setup
   - Load balancer configuration
   - etcd cluster
   - API server redundancy

2. Node HA
   - Multiple worker nodes
   - Pod anti-affinity
   - Node auto-repair

### Backup and Recovery
```bash
# Example etcd backup
ETCDCTL_API=3 etcdctl snapshot save snapshot.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key
```

## Monitoring

### Metrics Server
```yaml
# Metrics Server deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: metrics-server
  namespace: kube-system
spec:
  selector:
    matchLabels:
      k8s-app: metrics-server
  template:
    metadata:
      labels:
        k8s-app: metrics-server
    spec:
      containers:
      - name: metrics-server
        image: k8s.gcr.io/metrics-server/metrics-server:v0.6.1
```

### Prometheus & Grafana
1. Service Monitor
```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: api-monitor
spec:
  selector:
    matchLabels:
      app: api
  endpoints:
  - port: metrics
```

## Best Practices

### Resource Management
1. Resource Requests/Limits
2. Horizontal Pod Autoscaling
3. Cluster Autoscaling
4. Pod Disruption Budgets

### Security
1. Pod Security Policies
2. Image Scanning
3. Secret Management
4. Network Policies

### Operations
1. Rolling Updates
2. Health Checks
3. Log Management
4. Backup Procedures

## References
- Kubernetes Documentation
- Kubernetes Patterns Book
- Cloud Native Computing Foundation
- Kubernetes the Hard Way