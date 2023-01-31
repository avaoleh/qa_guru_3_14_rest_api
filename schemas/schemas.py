from voluptuous import PREVENT_EXTRA, Schema

create_user = Schema(
    {
        'name': str,
        'job': str,
        'id': str,
        'createdAt': str
    },
    extra=PREVENT_EXTRA,
    required=True
)

update_user = Schema(
    {
        'name': str,
        'job': str,
        'updatedAt': str
    },
    extra=PREVENT_EXTRA,
    required=True
)

register_user = Schema(
    {
        'id': int,
        'token': str,
    },
    extra=PREVENT_EXTRA,
    required=True
)


login_user = Schema(
    {
        'token': str,
    },
    extra=PREVENT_EXTRA,
    required=True
)
