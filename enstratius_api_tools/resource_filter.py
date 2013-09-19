def get_servers(servers, **kwargs):
    """ Returns a list of servers

    Arguments:
    :param servers: a list of servers that needs to be filtered.

    Keyword arguments:
    :param account_user_id: owning user's account user ID.
    :param vm_login_id: owning user's VM login ID.
    :param email: owning user's email address.
    :param group_id: owning group's group ID.
    :param budget_id: budget ID.
    :returns: a list of filtered servers.
    :rtype: list
    """
    filtered_servers = servers

    if kwargs.has_key('account_user_id') and kwargs['account_user_id'] is not None:
        filtered_servers = [server for server in servers if hasattr(server, 'owning_user') and
                            server.owning_user.has_key('account_user_id') and
                            server.owning_user['account_user_id'] == kwargs['account_user_id']]
    if kwargs.has_key('vm_login_id') and kwargs['vm_login_id'] is not None:
        if filtered_servers is not None: servers = filtered_servers
        filtered_servers = [server for server in servers if hasattr(server, 'owning_user') and
                            server.owning_user.has_key('vm_login_id') and
                            server.owning_user['vm_login_id'] == kwargs['vm_login_id']]
    if kwargs.has_key('email') and kwargs['email'] is not None:
        if filtered_servers is not None: servers = filtered_servers
        filtered_servers = [server for server in servers if hasattr(server, 'owning_user') and
                            server.owning_user.has_key('email') and
                            server.owning_user['email'] == kwargs['email']]
    if kwargs.has_key('group_id') and kwargs['group_id'] is not None:
        if filtered_servers is not None: servers = filtered_servers
        filtered_servers = [server for server in servers if hasattr(server, 'owning_groups')
                            for group in server.owning_groups if group['group_id'] == int(kwargs['group_id'])]
    if kwargs.has_key('budget_id') and kwargs['budget_id'] is not None:
        if filtered_servers is not None: servers = filtered_servers
        filtered_servers = [server for server in servers if hasattr(server, 'budget') and
                            server.budget == int(kwargs['budget_id'])]

    return filtered_servers

def get_snapshots(snapshots, **kwargs):
    """ Returns a list of snapshots

    Arguments:
    :param snapshots: a list of snapshots that needs to be filtered.

    Keyword arguments:
    :param group_id: owning group's group ID.
    :param budget_id: budget ID.
    :returns: a list of filtered snapshots.
    :rtype: list
    """
    filtered_snapshots = snapshots

    if kwargs.has_key('group_id') and kwargs['group_id'] is not None:
        filtered_snapshots = [snapshot for snapshot in snapshots if hasattr(snapshot, 'owning_groups')
                              for g in snapshot.owning_groups if g['group_id'] == int(kwargs['group_id'])]
    if kwargs.has_key('budget_id') and kwargs['budget_id'] is not None:
        if filtered_snapshots is not None: snapshots = filtered_snapshots
        filtered_snapshots = [snapshot for snapshot in snapshots if hasattr(snapshot, 'budget') and
                              snapshot.budget == int(kwargs['budget_id'])]

    return filtered_snapshots

def get_volumes(volumes, **kwargs):
    """ Returns a list of volumes

    Arguments:
    :param volumes: a list of volumes that needs to be filtered.

    Keyword arguments:
    :param vm_login_id: owning user's VM login ID.
    :param email: owning user's email address.
    :param group_id: owning group's group ID.
    :param budget_id: budget ID.
    :param size: minimum size of the volume.
    :returns: a list of filtered volumes.
    :rtype: list
    """
    filtered_volumes = volumes

    if kwargs.has_key('vm_login_id') and kwargs['vm_login_id'] is not None:
        filtered_volumes = [volume for volume in volumes if hasattr(volume, 'owning_user') and
                            volume.owning_user.has_key('vm_login_id') and
                            volume.owning_user['vm_login_id'] == kwargs['vm_login_id']]
    if kwargs.has_key('email') and kwargs['email'] is not None:
        if filtered_volumes is not None: volumes = filtered_volumes
        filtered_volumes = [volume for volume in volumes if hasattr(volume, 'owning_user') and
                            volume.owning_user.has_key('email') and
                            volume.owning_user['email'] == kwargs['email']]
    if kwargs.has_key('group_id') and kwargs['group_id'] is not None:
        if filtered_volumes is not None: volumes = filtered_volumes
        filtered_volumes = [volume for volume in volumes if hasattr(volume, 'owning_groups')
                            for group in volume.owning_groups if group['group_id'] == int(kwargs['group_id'])]
    if kwargs.has_key('budget_id') and kwargs['budget_id'] is not None:
        if filtered_volumes is not None: volumes = filtered_volumes
        filtered_volumes = [volume for volume in volumes if hasattr(volume, 'budget') and
                            volume.budget == int(kwargs['budget_id'])]
    if kwargs.has_key('size') and kwargs['size'] is not None:
        if filtered_volumes is not None: volumes = filtered_volumes
        filtered_volumes = [volume for volume in volumes if volume.size_in_gb >= int(kwargs['size'])]

    return filtered_volumes

def get_user(users, **kwargs):
    """ Returns a user that matches with arguments.

    Arguments:
    :param users: a list of users that needs to be filtered.

    Keyword arguments:
    :param vm_login_id: owning user's VM login ID.
    :param email: owning user's email address.
    :returns: a list of filtered users.
    :rtype: list
    """
    selected_user = users

    if kwargs.has_key('vm_login_id') and kwargs['vm_login_id'] is not None:
        for user in users:
            if hasattr(user, 'vm_login_id') and user.vm_login_id == kwargs['vm_login_id']:
                selected_user = user
    elif kwargs.has_key('email') and kwargs['email'] is not None:
        for user in users:
            if hasattr(user, 'email') and user.email == kwargs['email']:
                selected_user = user

    return selected_user
