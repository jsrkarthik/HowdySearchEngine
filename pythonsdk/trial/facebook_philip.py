import web, requests

url = (
'/', 'index'
)

app_id = "147970838631413"
app_secret = "f445e4a4011c68c12d0851ecdb190df1"
post_login_url = "http://0.0.0.0:8080/"

class index:
    def GET(self):
        user_data = web.input(code=None)
        code = user_data.code

        if not code:
            dialog_url = ( "http://www.facebook.com/dialog/oauth?" +
                           "client_id=" + app_id +
                           "&redirect_uri=" + post_login_url +
                           "&scope=publish_stream" )

            return "<script>top.location.href='" + dialog_url + "'</script>"
        else:
            token_url = ( "https://graph.facebook.com/oauth/access_token?" +
                          "client_id=" + app_id +
                          "&redirect_uri=" + post_login_url +
                          "&client_secret=" + app_secret +
                          "&code=" + code )
            response = requests.get(token_url).content

            params = {}
            result = response.split("&", 1)
            for p in result:
                (k,v) = p.split("=")
                params[k] = v

            access_token = params['access_token']

            graph_url = ( "https://graph.facebook.com/me/photos?" +
                          "access_token=" + access_token )

            return ( '<html><body>' + '\n' +
                     '<form enctype="multipart/form-data" action="' +
                     graph_url + ' "method="POST">' + '\n' +
                     'Please choose a photo: ' + '\n' +
                     '<input name="source" type="file"><br/><br/>' + '\n' +
                     'Say something about this photo: ' + '\n' +
                     '<input name="message" type="text" value=""><br/><br/>' + '\n' +
                     '<input type="submit" value="Upload"/><br/>' + '\n' +
                     '</form>' + '\n' +
                     '</body></html>' )

if __name__ == "__main__":
    app = web.application(url, globals())
    app.run()
