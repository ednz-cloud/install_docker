"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    etc_hosts = host.file("/etc/hosts")
    assert etc_hosts.exists
    assert etc_hosts.user == "root"
    assert etc_hosts.group == "root"

def test_docker_service(host):
    """Validate docker service."""
    docker_service = host.service("docker.service")
    assert docker_service.is_enabled
    assert docker_service.is_running
    assert docker_service.systemd_properties["Restart"] == "always"
    assert docker_service.systemd_properties["FragmentPath"] == "/lib/systemd/system/docker.service"

def test_docker_daemon(host):
    """Validate /etc/docker/daemon.json file."""
    docker_daemon_file = host.file("/etc/docker/daemon.json")
    assert docker_daemon_file.exists
    assert docker_daemon_file.user == "root"
    assert docker_daemon_file.group =="root"
    assert docker_daemon_file.mode == 0o644
    assert docker_daemon_file.contains("{}")

def test_docker_interaction(host):
    """Validate interaction with docker."""
    docker_ps = host.check_output("docker ps")
    assert docker_ps == "CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES"

def test_docker_compose(host):
    """Validate docker-compose installation"""
    docker_compose_bin = host.file("/usr/local/bin/docker-compose")
    assert not docker_compose_bin.exists

def test_docker_python_package(host):
    """Validate docker python package installation"""
    pip_packages_list = host.pip.get_packages(pip_path='pip')
    pip_outdated_list = host.pip.get_outdated_packages(pip_path='pip')
    assert 'docker' not in pip_packages_list
    assert 'docker' not in  pip_outdated_list
