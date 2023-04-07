Install Docker
=========
> This repository is only a mirror. Development and testing is done on a private gitlab server.

This role install and configure docker on **debian-based** distributions.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/hashicorp_vault.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
hashi_vault_install: true # by default, set to true
```
This variable defines if the vault package is to be installed or not before configuring. If you install vault using another task, you can set this to `false`.

```yaml
install_docker_compose: false # by default, set to false
```
This variables defines whether or not to install docker-compose on the host.

```yaml
install_docker_compose_version: latest # by default, set to latest
```
This variable defines the version of docker-compose to install. It support either `latest`, or the version number (`vX.Y.Z`). Officially, only versions `>=v2.0.1` are supported, as the naming for most packages changed at this release.

Dependencies
------------

This role requires both `ednxzu.manage_repositories` and `ednxzu.manage_apt_packages` to install docker.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:
```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.install_docker
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
