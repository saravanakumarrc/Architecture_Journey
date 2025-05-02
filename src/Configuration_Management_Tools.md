# Configuration Management Tools

## Ansible

### Architecture
- Agentless
- Push-based
- SSH-based communication
- YAML syntax
- Idempotent operations

### Playbook Example
```yaml
# Example Ansible playbook
---
- name: Configure web servers
  hosts: webservers
  become: true
  vars:
    http_port: 80
    
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        
    - name: Copy nginx config
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: Restart nginx
        
  handlers:
    - name: Restart nginx
      service:
        name: nginx
        state: restarted
```

### Roles Structure
```
roles/
├── webserver/
│   ├── defaults/
│   │   └── main.yml
│   ├── handlers/
│   │   └── main.yml
│   ├── tasks/
│   │   └── main.yml
│   └── templates/
│       └── nginx.conf.j2
```

## Puppet

### Manifest Example
```ruby
# Example Puppet manifest
class profile::web {
  class { 'nginx':
    manage_repo    => true,
    http_configs   => {
      'upstream' => {
        'app' => {
          'members' => [
            'localhost:3000',
            'localhost:3001',
          ],
        },
      },
    },
  }
  
  nginx::resource::server { 'example.com':
    listen_port => 80,
    proxy       => 'http://app',
    ssl        => true,
    ssl_cert   => '/etc/ssl/certs/example.com.crt',
    ssl_key    => '/etc/ssl/private/example.com.key',
  }
}
```

### Key Features
- Model-driven approach
- Pull-based architecture
- Agent-based
- Rich module ecosystem
- Enterprise support

## Chef

### Recipe Example
```ruby
# Example Chef recipe
package 'nginx' do
  action :install
end

template '/etc/nginx/nginx.conf' do
  source 'nginx.conf.erb'
  owner 'root'
  group 'root'
  mode '0644'
  notifies :restart, 'service[nginx]'
end

service 'nginx' do
  action [ :enable, :start ]
  supports status: true, restart: true, reload: true
end
```

### Cookbook Structure
```
cookbook/
├── attributes/
│   └── default.rb
├── recipes/
│   └── default.rb
├── templates/
│   └── nginx.conf.erb
└── metadata.rb
```

## SaltStack

### State Example
```yaml
# Example Salt state file
nginx:
  pkg.installed: []
  
  service.running:
    - enable: True
    - watch:
      - file: /etc/nginx/nginx.conf
      
/etc/nginx/nginx.conf:
  file.managed:
    - source: salt://nginx/nginx.conf
    - user: root
    - group: root
    - mode: 644
    - template: jinja
```

### Key Features
- Event-driven automation
- Remote execution
- Configuration management
- Both push and pull modes
- Strong security model

## Comparison

### Architecture Patterns

| Tool | Architecture | Communication | Scaling | Language |
|------|--------------|---------------|----------|-----------|
| Ansible | Agentless | Push | Control node | YAML |
| Puppet | Agent-based | Pull | Master-Agent | Puppet DSL |
| Chef | Agent-based | Pull | Server-Client | Ruby |
| SaltStack | Agent-based | Both | Master-Minion | YAML |

### Use Case Selection

#### Ansible
- Quick automation needs
- Simple deployment scenarios
- Limited system requirements
- SSH-based management

#### Puppet
- Large infrastructure
- Complex configurations
- Policy enforcement
- Compliance requirements

#### Chef
- Development-focused teams
- Ruby expertise
- Custom resource needs
- Test-driven infrastructure

#### SaltStack
- High-speed execution
- Event-driven needs
- Real-time system management
- Remote command execution

## Best Practices

### 1. Code Organization
```
infrastructure/
├── ansible/
│   ├── inventory/
│   ├── group_vars/
│   ├── host_vars/
│   └── roles/
├── puppet/
│   ├── manifests/
│   ├── modules/
│   └── data/
└── common/
    ├── files/
    └── templates/
```

### 2. Security
- Secret management
- Role-based access
- Encrypted communication
- Compliance automation

### 3. Testing
```yaml
# Example Molecule test for Ansible
---
dependency:
  name: galaxy
driver:
  name: docker
platforms:
  - name: instance
    image: ubuntu:20.04
verifier:
  name: testinfra
```

### 4. Version Control
- Infrastructure as Code
- Change tracking
- Peer review process
- Automated testing

## Common Patterns

### 1. Role-Based Configuration
```yaml
# Example role structure
roles:
  - base_security
  - monitoring
  - application
  - backup
```

### 2. Environment Management
```ruby
# Example Puppet environment
node 'web-prod-01' {
  include role::web_server
  include profile::monitoring
  include profile::security
}
```

### 3. Data Separation
```yaml
# Example group variables
---
app_name: myapp
app_version: 1.2.3
app_port: 8080
app_environment: production
```

## Monitoring and Reporting

### 1. Execution Reports
- Success/failure metrics
- Configuration drift
- Compliance status
- Performance metrics

### 2. Dashboard Integration
```ruby
# Example Puppet reporting to Grafana
notify { 'Sending metrics':
  message => 'Configuration applied successfully',
  loglevel => 'info',
}
```

## References
- Ansible Documentation
- Puppet Documentation
- Chef Documentation
- SaltStack Documentation
- Infrastructure as Code (Kief Morris)