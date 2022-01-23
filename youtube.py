import requests

"""
Telegram : @zzaaz
Telegram Channel : @rickpro3
Instagram : @_69lw
"""

def download(url,format):
    try:

        response = requests.get(f"https://loader.to/ajax/download.php?format="+ str(format) +"&url="+str(url))

        title = response.json()['title']

        id = response.json()['id']

        while True:
            progress = requests.get(f"https://loader.to/ajax/progress.php?id="+str(id)).json()
            progress_url = progress['download_url']

            if "http" in str(progress_url):
                return {
   "success":"Ok",
   "progress":1000,
   "Title":title,
   "Id": id,
   "Download Url":progress_url,
   "Status":"Finished"
}

            else:
                pass
    except:
        return {
            "success": "False",
            "progress": 0,
            "Title": None,
            "Id": None,
            "Download Url": None,
            "Status": None
        }





