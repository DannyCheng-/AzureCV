import http.client, urllib.request, urllib.parse, urllib.error, base64, json
from gtts import gTTS


subscription_key = '71520a2e267345ec8398ff6c7fc33cd3'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'westus.api.cognitive.microsoft.com'

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories,Description,Color',
    'language': 'en',
})

# Replace the three dots below with the URL of a JPEG image of a celebrity.
body = "{'url':'http://cdn.blog.rvshare.com/wp-content/uploads/2015/08/rsvlts.com_.jpg?93555e'}"

try:
    # Execute the REST API call and get the response.
    conn = http.client.HTTPSConnection(uri_base)
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print ("Response:")
    #print (json.dumps(parsed, sort_keys=True, indent=2))
    print (json.dumps(parsed["description"]["captions"][0]["text"]))
    conn.close()

except Exception as e:
    print('Error:')
    print(e)


#tts = gTTS(text='Hello', lang='en', slow=True)
