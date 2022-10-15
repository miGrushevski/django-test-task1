def get_url_params_for_pagination(request):
    """
    Returns url GET parameters excluding page parameter.
    """
    query = request.GET.copy()

    if 'page' in query:
        query.pop('page')

    params = query.urlencode()
    if params:
        return {'pagination_params': "&" + query.urlencode()}
    return {'pagination_params': ''}
