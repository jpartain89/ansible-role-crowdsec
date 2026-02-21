def test_hosts_file_exists(host):
    file_obj = host.file('/etc/hosts')
    assert file_obj.exists
