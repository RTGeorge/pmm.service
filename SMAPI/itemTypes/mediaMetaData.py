class MediaMetadata():
    def __init__(self, id):
        self.id = id 
        self.itemType = 'unknown' ### TDO  this is object
        self.displayType = 'unknown'
        self.title = 'uknown'
        self.summary = 'Description'
        self.isFavorite = false
        self.language = 'en'
        self.country = 'US'
        self.genreId = '666'
        self.genre = 'Black Metal'
        self.twitterId = '@FoxDen'
        self.liveNow = false
        self.onDemand = false
        self.mimeType = 'MP4'
        #({trackMetadata: ns0:trackMetadata} | {streamMetadata: ns0:streamMetadata})
        self.dynamic =  {} #ns0:dynamicData, 
        self.behaviors = {} #ns0:behaviorsData
