from django.core.exceptions import ObjectDoesNotExist


def has_profile(self):
    try:
        self.profile
    except ObjectDoesNotExist:
        return False
    else:
        return True