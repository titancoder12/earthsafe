from django import template

register = template.Library()

@register.filter
def user_has_status_g(earthquake, user):
    # Check if there are any statuses for this user with the specified status 'green'
    return earthquake.statuses.filter(user=user, status='green').exists()

@register.filter
def user_has_status_y(earthquake, user):
    # Check if there are any statuses for this user with the specified status 'yellow'
    return earthquake.statuses.filter(user=user, status='yellow').exists()

@register.filter
def user_has_status_r(earthquake, user):
    # Check if there are any statuses for this user with the specified status 'red'
    return earthquake.statuses.filter(user=user, status='red').exists()