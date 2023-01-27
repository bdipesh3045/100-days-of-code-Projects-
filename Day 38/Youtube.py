from pytube import YouTube,Playlist
class Download():
    def __init__(self,links):
        self.links=links
        self.Links_resolver()
    
    @staticmethod
    def store(link):
        yt = YouTube(link)
        try:
            stream = yt.streams.get_by_itag(251)
        except:
            try:
                stream = yt.streams.get_by_itag(250)
            except:
                try:
                    stream = yt.streams.get_by_itag(249)
                except:
                    try:
                        stream = yt.streams.get_by_itag(140)
                    except:
                        try:
                            stream = yt.streams.get_by_itag(139)
                        except:
                            print("Something went wrong!")
                        
        stream.download()
        print("Song downloaded!")

        
    
    def Links_resolver(self):
        p=Playlist(self.links)
        print(f"There are total {len(p.video_urls[:3])} to download !")
        for link in p.video_urls[:3]:
            Download.store(link)

Download_initializer=Download("https://youtube.com/playlist?list=PL86oRljAXCzfaqZSWfd4UYgLKfOK27HAx")
