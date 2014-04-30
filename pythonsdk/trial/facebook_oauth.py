from facepy import utils
app_id = 1476062702607954 # must be integer
app_secret = "dcaa2a6dd1a5c18e068d05341b572395" 
oath_access_token = utils.get_application_access_token(app_id, app_secret)
print "token  = ",oath_access_token
