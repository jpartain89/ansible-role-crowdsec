# NOTE: The primary verifier for all molecule scenarios has been migrated
# from testinfra to the Ansible verifier (verify.yml in each scenario).
# This file is kept for reference and optional local testinfra usage.
#
# To run these tests directly with pytest-testinfra (not via molecule),
# install pytest-testinfra and run:
#   pytest molecule/tests/test_default.py --hosts='docker://instance'


def test_hosts_file_exists(host):
    """Assert that /etc/hosts is present on the managed host."""
    file_obj = host.file('/etc/hosts')
    assert file_obj.exists


def test_hosts_file_is_readable(host):
    """Assert that /etc/hosts is a regular, readable file."""
    file_obj = host.file('/etc/hosts')
    assert file_obj.is_file
    assert oct(file_obj.mode) == oct(0o644)


def test_crowdsec_config_dir_absent_when_agent_disabled(host):
    """Assert that /etc/crowdsec is absent when cs_install_agent=false."""
    config_dir = host.file('/etc/crowdsec')
    assert not config_dir.exists
