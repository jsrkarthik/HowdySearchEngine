import web
from facepy import GraphAPI
from urlparse import parse_qs

url = ('/', 'index')

app_id = "YOUR_APP_ID"
app_secret = "APP_SECRET"
post_login_url = "http://0.0.0.0:8080/"

user_data = web.input(code=None)

if not user_data.code:
    dialog_url = ( "http://www.facebook.com/dialog/oauth?" +
                               "client_id=" + app_id +
                               "&redirect_uri=" + post_login_url +
                               "&scope=publish_stream" )

    print "<script>top.location.href='" + dialog_url + "'</script>"
else:
    graph = GraphAPI()
    response = graph.get(
        path='oauth/access_token',
        client_id=app_id,
        client_secret=app_secret,
        redirect_uri=post_login_url,
        code=code
    )
    data = parse_qs(response)
    graph = GraphAPI(data['access_token'][0])
    #graph.post(path = 'me/feed', message = 'Your message here')
