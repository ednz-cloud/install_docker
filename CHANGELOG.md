## v0.2.0 (2025-06-15)

### Feat

- document variables for docsible
- **main**: allow docker daemon reload in specific cases
- **configure**: install completion for bash shell
- realod docker service on deamon config changes

## v0.1.1 (2025-01-25)

### Fix

- wrong variable names would make docker not restart on upgrades

## v0.1.0 (2024-12-29)

### Feat

- add item_changed_in_list plugin
- install docker without using debian repositories
- **core**: change namespace
- **tests**: remove /etc/hosts testing, fix #1
- remove become from playbook
- normalize tests, verify playbooks are the same for each backend
- add become true to start docker service
- add become: true to not rely on ansible.cfg, add vagrant tests for later
- only reload dokcer service if install_docker_start_service is enabled
