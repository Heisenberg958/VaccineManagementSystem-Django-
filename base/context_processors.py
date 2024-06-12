


def site_settings(request):
    return {'userid':request.session.get("userid",0),'username':request.session.get("username","")}