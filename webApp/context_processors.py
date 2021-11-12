from webApp.models.company_profile import CompanyProfile


def company_profile(request):
    """
      The context processor must return a dictionary.
    """
    return {'company_profile': CompanyProfile.load()}
