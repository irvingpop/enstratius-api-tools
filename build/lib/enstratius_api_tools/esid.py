from mixcoatl.admin.billing_code import BillingCode
from mixcoatl.geography.region import Region
from mixcoatl.admin.group import Group
from mixcoatl.admin.user import User
import resource_filter

def get_account_user_id(**kwargs):
    """ Returns account_user_id from arguments

    Keyword arguments:
    :param vm_login_id: user's VM login ID like p100
    :param email: user's E-Mail address
    :returns: account_user_id
    :rtype: int
    """

    if 'vm_login_id' in kwargs:
        users = User.all()
        selected_user = resource_filter.get_user(users, vm_login_id=kwargs['vm_login_id'])
    elif 'email' in kwargs:
        users = User.all()
        selected_user = resource_filter.get_user(users, email=kwargs['email'])

    return selected_user.account_user_id

def get_vm_login_id(**kwargs):
    """ Returns vm_login_id from arguments

    Keyword arguments:
    :param email: user's E-Mail address
    :returns: vm_login_id
    :rtype: str
    """

    if 'email' in kwargs:
        users = User.all()
        selected_user = resource_filter.get_user(users, email=kwargs['email'])

    return selected_user.vm_login_id

def get_budget_id(budget_name):
    """ Returns budget_id from arguments

    Arguments:
    :param budget_name: budget name
    :returns: budget_id
    :rtype: int
    """
    budgets = BillingCode.all(detail='basic')

    for budget in budgets:
        if hasattr(budget, 'name') and budget.name == budget_name:
            selected_budget = budget

    return selected_budget.billing_code_id

def get_group_id(group_name):
    """ Returns a group ID from group name

    Arguments:
    :param group_name: name of the group
    :returns: group_id
    :rtype: int
    """
    groups = Group.all(detail='basic')

    for group in groups:
        if hasattr(group, 'name') and group.name == group_name:
            selected_group = group

    return selected_group.group_id

def get_region_id(region_pid):
    """ Returns a region ID from provider_id such as us-east-1.

    Arguments:
    :param region_pid: provider ID of the region such as us-east-1
    :returns: region_id such as 19343
    :rtype: int
    """
    regions = Region.all(detail='basic')

    for region in regions:
        if hasattr(region, 'provider_id') and region.provider_id == region_pid:
            selected_region = region

    return selected_region.region_id
