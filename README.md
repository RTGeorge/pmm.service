# Playback My Meeting (PMM) Service

This is a music service that adheres to the requirements defined by the Sonoos Music API (SMAPI).

# API

The API is defined by http://musicpartners.sonos.com/sites/default/files/Sonos.wsdl.

## This Specific Schema Used by This Build
In the event the API is updated, this is what this version of PMM was built against:

Prefixes:
     ns0: http://www.sonos.com/Services/1.1
     xsd: http://www.w3.org/2001/XMLSchema

Global elements:
     ns0:addToContainer(id: ns0:id, parentId: ns0:id, index: xsd:int, updateId: ns0:id)
     ns0:addToContainerResponse(addToContainerResult: ns0:addToContainerResult)
     ns0:context(timeZone: xsd:string, _value_1: ANY[])
     ns0:createContainer(containerType: xsd:string, title: xsd:string, parentId: ns0:id, seedId: ns0:id)
     ns0:createContainerResponse(createContainerResult: ns0:createContainerResult)
     ns0:createItem(favorite: ns0:id)
     ns0:createItemResponse(createItemResult: ns0:id)
     ns0:credentials(zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}}))
     ns0:customFaultDetail(({SonosError: xsd:int, ExceptionInfo: xsd:string} | {refreshAuthTokenResult: ns0:deviceAuthTokenResult}))
     ns0:deleteContainer(id: ns0:id)
     ns0:deleteContainerResponse(deleteContainerResult: ns0:deleteContainerResult)
     ns0:deleteItem(favorite: ns0:id)
     ns0:deleteItemResponse()
     ns0:getAppLink(householdId: ns0:id, hardware: xsd:string, osVersion: xsd:string, sonosAppName: xsd:string, callbackPath: xsd:string)
     ns0:getAppLinkResponse(getAppLinkResult: ns0:appLinkResult)
     ns0:getContentKey(id: ns0:id, uri: xsd:anyURI, deviceSessionToken: ns0:deviceSessionToken)
     ns0:getContentKeyResponse(contentKey: ns0:contentKey)
     ns0:getDeviceAuthToken(householdId: ns0:id, linkCode: xsd:string, linkDeviceId: xsd:string, callbackPath: xsd:string)
     ns0:getDeviceAuthTokenResponse(getDeviceAuthTokenResult: ns0:deviceAuthTokenResult)
     ns0:getDeviceLinkCode(householdId: ns0:id)
     ns0:getDeviceLinkCodeResponse(getDeviceLinkCodeResult: ns0:deviceLinkCodeResult)
     ns0:getExtendedMetadata(id: ns0:id)
     ns0:getExtendedMetadataResponse(getExtendedMetadataResult: ns0:extendedMetadata)
     ns0:getExtendedMetadataText(id: ns0:id, type: xsd:string)
     ns0:getExtendedMetadataTextResponse(getExtendedMetadataTextResult: xsd:string)
     ns0:getLastUpdate()
     ns0:getLastUpdateResponse(getLastUpdateResult: ns0:lastUpdate)
     ns0:getMediaMetadata(id: ns0:id)
     ns0:getMediaMetadataResponse(getMediaMetadataResult: ns0:mediaMetadata)
     ns0:getMediaURI(id: ns0:id, action: ns0:mediaUriAction, secondsSinceExplicit: xsd:int, deviceSessionToken: ns0:deviceSessionToken)
     ns0:getMediaURIResponse(getMediaURIResult: xsd:anyURI, deviceSessionToken: ns0:deviceSessionToken, deviceSessionKey: ns0:encryptionContext, contentKey: ns0:encryptionContext, httpHeaders: ns0:httpHeaders, uriTimeout: xsd:int, positionInformation: ns0:positionInformation, privateDataFieldName: xsd:string)
     ns0:getMetadata(id: ns0:id, index: xsd:int, count: xsd:int, recursive: xsd:boolean)
     ns0:getMetadataResponse(getMetadataResult: ns0:mediaList)
     ns0:getScrollIndices(id: ns0:id)
     ns0:getScrollIndicesResponse(getScrollIndicesResult: xsd:string)
     ns0:getSessionId(username: ns0:username, password: ns0:password)
     ns0:getSessionIdResponse(getSessionIdResult: ns0:id)
     ns0:getStreamingMetadata(id: ns0:id, startTime: xsd:dateTime, duration: xsd:int)
     ns0:getStreamingMetadataResponse(getStreamingMetadataResult: ns0:segmentMetadataList)
     ns0:getUserInfo()
     ns0:getUserInfoResponse(getUserInfoResult: ns0:userInfo)
     ns0:id(ns0:id)
     ns0:itemType(ns0:itemType)
     ns0:label(ns0:label)
     ns0:login(username: ns0:username, password: ns0:password)
     ns0:loginToken(token: xsd:string, key: xsd:string, householdId: xsd:string)
     ns0:mediaUriAction(ns0:mediaUriAction)
     ns0:nickname(ns0:nickname)
     ns0:password(ns0:password)
     ns0:rateItem(id: ns0:id, rating: xsd:int)
     ns0:rateItemResponse(rateItemResult: ns0:itemRating)
     ns0:refreshAuthTokenResponse(refreshAuthTokenResult: ns0:deviceAuthTokenResult)
     ns0:removeFromContainer(id: ns0:id, indices: xsd:string, updateId: ns0:id)
     ns0:removeFromContainerResponse(removeFromContainerResult: ns0:removeFromContainerResult)
     ns0:renameContainer(id: ns0:id, title: xsd:string)
     ns0:renameContainerResponse(renameContainerResult: ns0:renameContainerResult)
     ns0:reorderContainer(id: ns0:id, from: xsd:string, to: xsd:int, updateId: ns0:id)
     ns0:reorderContainerResponse(reorderContainerResult: ns0:reorderContainerResult)
     ns0:reportAccountAction(type: xsd:string)
     ns0:reportAccountActionResponse()
     ns0:reportPlaySeconds(id: ns0:id, seconds: xsd:int, contextId: xsd:string, privateData: ns0:privateDataType, offsetMillis: xsd:int)
     ns0:reportPlaySecondsResponse(reportPlaySecondsResult: ns0:reportPlaySecondsResult)
     ns0:reportPlayStatus(id: ns0:id, status: xsd:string, contextId: xsd:string, offsetMillis: xsd:int)
     ns0:reportPlayStatusResponse()
     ns0:reportStatus(id: ns0:id, errorCode: xsd:int, message: xsd:string)
     ns0:reportStatusResponse()
     ns0:search(id: ns0:id, term: xsd:string, index: xsd:int, count: xsd:int)
     ns0:searchResponse(searchResult: ns0:mediaList)
     ns0:sessionId(ns0:sessionId)
     ns0:setPlayedSeconds(id: ns0:id, seconds: xsd:int, contextId: xsd:string, privateData: ns0:privateDataType, offsetMillis: xsd:int)
     ns0:setPlayedSecondsResponse()
     ns0:username(ns0:username)
     

Global types:
     
     ns0:AbstractMedia(id: ns0:id, itemType: ns0:itemType, displayType: xsd:string, title: xsd:string, summary: xsd:string, isFavorite: xsd:boolean, language: xsd:string, country: xsd:string, genreId: xsd:string, genre: xsd:string, twitterId: xsd:string, liveNow: xsd:boolean, onDemand: xsd:boolean)
     ns0:addToContainerResult(updateId: ns0:id)
     ns0:albumArtUrl(xsd:anyURI, requiresAuthentication: xsd:boolean)
     ns0:algorithm
     ns0:appLinkInfo(appUrl: ns0:sonosUri, appUrlStringId: xsd:string, deviceLink: ns0:deviceLinkCodeResult, failureStringId: xsd:string, failureUrl: ns0:sonosUri, failureUrlStringId: xsd:string)
     ns0:appLinkResult(({authorizeAccount: ns0:appLinkInfo, createAccount: ns0:appLinkInfo, installAction: ns0:callToActionInfo} | {callToAction: ns0:callToActionInfo}))
     ns0:behaviorsData(supportsQuickSkip: xsd:boolean)
     ns0:callToActionInfo(messageStringId: xsd:string, url: ns0:sonosUri, urlStringId: xsd:string)
     ns0:contentKey(uri: xsd:anyURI, deviceSessionToken: ns0:deviceSessionToken, deviceSessionKey: ns0:encryptionContext, contentKey: ns0:encryptionContext)
     ns0:createContainerResult(id: ns0:id, updateId: ns0:id)
     ns0:deleteContainerResult()
     ns0:deviceAuthTokenResult(authToken: xsd:string, privateKey: xsd:string, userInfo: ns0:userInfo)
     ns0:deviceLinkCodeResult(regUrl: xsd:string, linkCode: xsd:string, showLinkCode: xsd:boolean, linkDeviceId: xsd:string)
     ns0:deviceSessionToken
     ns0:dynamicData(property: ns0:property[])
     ns0:encryptionContext(xsd:string, type: ns0:encryptionType)
     ns0:encryptionType
     ns0:extendedMetadata(({mediaCollection: ns0:mediaCollection} | {mediaMetadata: ns0:mediaMetadata}), relatedBrowse: ns0:relatedBrowse[], relatedText: ns0:relatedText[], relatedPlay: ns0:relatedPlay)
     ns0:httpHeader(header: xsd:string, value: xsd:string)
     ns0:httpHeaders(httpHeader: ns0:httpHeader[])
     ns0:id
     ns0:itemRating(shouldSkip: xsd:boolean, messageStringId: xsd:string)
     ns0:itemType
     ns0:lastUpdate(catalog: xsd:string, favorites: xsd:string, pollInterval: xsd:int, autoRefreshEnabled: xsd:boolean)
     ns0:mediaCollection(id: ns0:id, itemType: ns0:itemType, displayType: xsd:string, title: xsd:string, summary: xsd:string, isFavorite: xsd:boolean, language: xsd:string, country: xsd:string, genreId: xsd:string, genre: xsd:string, twitterId: xsd:string, liveNow: xsd:boolean, onDemand: xsd:boolean, ({artist: xsd:string, artistId: ns0:id} | {authorId: xsd:string, author: xsd:string, narratorId: xsd:string, narrator: xsd:string}), canScroll: xsd:boolean, canPlay: xsd:boolean, canEnumerate: xsd:boolean, canAddToFavorites: xsd:boolean, containsFavorite: xsd:boolean, canCache: xsd:boolean, canSkip: xsd:boolean, albumArtURI: ns0:albumArtUrl, canResume: xsd:boolean, authRequired: xsd:boolean, homogeneous: xsd:boolean, canAddToFavorite: xsd:boolean, readOnly: xsd:boolean, userContent: xsd:boolean, renameable: xsd:boolean)
     ns0:mediaList(index: xsd:int, count: xsd:int, total: xsd:int, positionInformation: ns0:positionInformation, ({mediaCollection: ns0:mediaCollection} | {mediaMetadata: ns0:mediaMetadata})[])
     ns0:mediaMetadata(id: ns0:id, itemType: ns0:itemType, displayType: xsd:string, title: xsd:string, summary: xsd:string, isFavorite: xsd:boolean, language: xsd:string, country: xsd:string, genreId: xsd:string, genre: xsd:string, twitterId: xsd:string, liveNow: xsd:boolean, onDemand: xsd:boolean, mimeType: xsd:string, ({trackMetadata: ns0:trackMetadata} | {streamMetadata: ns0:streamMetadata}), dynamic: ns0:dynamicData, behaviors: ns0:behaviorsData)
     ns0:mediaUriAction
     ns0:positionInformation(id: ns0:id, index: xsd:int, offsetMillis: xsd:int)
     ns0:privateDataType
     ns0:property(name: xsd:string, value: xsd:string)
     ns0:radioTrackList(count: xsd:int, id: xsd:string, name: xsd:string, ({mediaMetadata: ns0:mediaMetadata})[])
     ns0:relatedBrowse(id: ns0:id, type: xsd:string)
     ns0:relatedPlay(id: ns0:id, itemType: ns0:itemType, title: xsd:string, canPlay: xsd:boolean)
     ns0:relatedText(id: ns0:id, type: xsd:string)
     ns0:removeFromContainerResult(updateId: ns0:id)
     ns0:renameContainerResult()
     ns0:reorderContainerResult(updateId: ns0:id)
     ns0:reportPlaySecondsResult(interval: xsd:int)
     ns0:segmentMetadata(id: ns0:id, trackId: ns0:id, track: xsd:string, artistId: ns0:id, artist: xsd:string, composerId: ns0:id, composer: xsd:string, albumId: ns0:id, album: xsd:string, albumArtistId: ns0:id, albumArtist: xsd:string, genreId: ns0:id, genre: xsd:string, showId: ns0:id, show: xsd:string, episodeId: ns0:id, episode: xsd:string, host: xsd:string, topic: xsd:string, rating: xsd:int, albumArtURI: xsd:anyURI, startTime: xsd:dateTime, duration: xsd:int)
     ns0:segmentMetadataList(startTime: xsd:dateTime, duration: xsd:int, segmentMetadata: ns0:segmentMetadata[])
     ns0:sonosUri
     ns0:streamMetadata(currentHost: xsd:string, currentShowId: ns0:id, currentShow: xsd:string, secondsRemaining: xsd:int, secondsToNextShow: xsd:int, bitrate: xsd:int, logo: ns0:albumArtUrl, description: xsd:string, isEphemeral: xsd:boolean, reliability: xsd:anyURI, title: xsd:anyURI, subtitle: xsd:anyURI, nextShowSeconds: xsd:anyURI, hasOutOfBandMetadata: xsd:boolean)
     ns0:trackMetadata(({artistId: ns0:id, artist: xsd:string, composerId: ns0:id, composer: xsd:string, albumArtistId: ns0:id, albumArtist: xsd:string, albumId: ns0:id, album: xsd:string} | {authorId: xsd:string, author: xsd:string, narratorId: xsd:string, narrator: xsd:string, bookId: xsd:string, book: xsd:string}), genreId: ns0:id, genre: xsd:string, duration: xsd:int, rating: xsd:int, albumArtURI: ns0:albumArtUrl, trackNumber: xsd:int, canPlay: xsd:boolean, canSkip: xsd:boolean, canAddToFavorites: xsd:boolean, canResume: xsd:boolean, canSeek: xsd:boolean, hasOutOfBandMetadata: xsd:boolean)
     ns0:userAccountStatus
     ns0:userAccountType
     ns0:userInfo(userIdHashCode: xsd:string, accountType: ns0:userAccountType, accountStatus: ns0:userAccountStatus, nickname: ns0:nickname, profileUrl: ns0:sonosUri, pictureUrl: ns0:sonosUri)
     xsd:ENTITIES
     xsd:ENTITY
     xsd:ID
     xsd:IDREF
     xsd:IDREFS
     xsd:NCName
     xsd:NMTOKEN
     xsd:NMTOKENS
     xsd:NOTATION
     xsd:Name
     xsd:QName
     xsd:anySimpleType
     xsd:anyURI
     xsd:base64Binary
     xsd:boolean
     xsd:byte
     xsd:date
     xsd:dateTime
     xsd:decimal
     xsd:double
     xsd:duration
     xsd:float
     xsd:gDay
     xsd:gMonth
     xsd:gMonthDay
     xsd:gYear
     xsd:gYearMonth
     xsd:hexBinary
     xsd:int
     xsd:integer
     xsd:language
     xsd:long
     xsd:negativeInteger
     xsd:nonNegativeInteger
     xsd:nonPositiveInteger
     xsd:normalizedString
     xsd:positiveInteger
     xsd:short
     xsd:string
     xsd:time
     xsd:token
     xsd:unsignedByte
     xsd:unsignedInt
     xsd:unsignedLong
     xsd:unsignedShort

Bindings:
     Soap11Binding: {http://www.sonos.com/Services/1.1}SonosSoap

Service: Sonos
     Port: SonosSoap (Soap11Binding: {http://www.sonos.com/Services/1.1}SonosSoap)
         Operations:
            addToContainer(id: ns0:id, parentId: ns0:id, index: xsd:int, updateId: ns0:id, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> addToContainerResult: ns0:addToContainerResult
            createContainer(containerType: xsd:string, title: xsd:string, parentId: ns0:id, seedId: ns0:id, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> createContainerResult: ns0:createContainerResult
            createItem(favorite: ns0:id, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> createItemResult: ns0:id
            deleteContainer(id: ns0:id, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> deleteContainerResult: ns0:deleteContainerResult
            deleteItem(favorite: ns0:id, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> 
            getAppLink(householdId: ns0:id, hardware: xsd:string, osVersion: xsd:string, sonosAppName: xsd:string, callbackPath: xsd:string, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> getAppLinkResult: ns0:appLinkResult
            getContentKey(id: ns0:id, uri: xsd:anyURI, deviceSessionToken: ns0:deviceSessionToken, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> contentKey: ns0:contentKey
            getDeviceAuthToken(householdId: ns0:id, linkCode: xsd:string, linkDeviceId: xsd:string, callbackPath: xsd:string, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> getDeviceAuthTokenResult: ns0:deviceAuthTokenResult
            getDeviceLinkCode(householdId: ns0:id, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> getDeviceLinkCodeResult: ns0:deviceLinkCodeResult
            getExtendedMetadata(id: ns0:id, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> getExtendedMetadataResult: ns0:extendedMetadata
            getExtendedMetadataText(id: ns0:id, type: xsd:string, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> getExtendedMetadataTextResult: xsd:string
            getLastUpdate(_soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> getLastUpdateResult: ns0:lastUpdate
            getMediaMetadata(id: ns0:id, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> getMediaMetadataResult: ns0:mediaMetadata
            getMediaURI(id: ns0:id, action: ns0:mediaUriAction, secondsSinceExplicit: xsd:int, deviceSessionToken: ns0:deviceSessionToken, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> getMediaURIResult: xsd:anyURI, deviceSessionToken: ns0:deviceSessionToken, deviceSessionKey: ns0:encryptionContext, contentKey: ns0:encryptionContext, httpHeaders: ns0:httpHeaders, uriTimeout: xsd:int, positionInformation: ns0:positionInformation, privateDataFieldName: xsd:string
            getMetadata(id: ns0:id, index: xsd:int, count: xsd:int, recursive: xsd:boolean, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> getMetadataResult: ns0:mediaList
            getScrollIndices(id: ns0:id, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> getScrollIndicesResult: xsd:string
            getSessionId(username: ns0:username, password: ns0:password, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> getSessionIdResult: ns0:id
            getStreamingMetadata(id: ns0:id, startTime: xsd:dateTime, duration: xsd:int, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> getStreamingMetadataResult: ns0:segmentMetadataList
            getUserInfo(_soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> getUserInfoResult: ns0:userInfo
            rateItem(id: ns0:id, rating: xsd:int, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> rateItemResult: ns0:itemRating
            removeFromContainer(id: ns0:id, indices: xsd:string, updateId: ns0:id, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> removeFromContainerResult: ns0:removeFromContainerResult
            renameContainer(id: ns0:id, title: xsd:string, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> renameContainerResult: ns0:renameContainerResult
            reorderContainer(id: ns0:id, from: xsd:string, to: xsd:int, updateId: ns0:id, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> reorderContainerResult: ns0:reorderContainerResult
            reportAccountAction(type: xsd:string, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> 
            reportPlaySeconds(id: ns0:id, seconds: xsd:int, contextId: xsd:string, privateData: ns0:privateDataType, offsetMillis: xsd:int, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> reportPlaySecondsResult: ns0:reportPlaySecondsResult
            reportPlayStatus(id: ns0:id, status: xsd:string, contextId: xsd:string, offsetMillis: xsd:int, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> 
            reportStatus(id: ns0:id, errorCode: xsd:int, message: xsd:string, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> 
            search(id: ns0:id, term: xsd:string, index: xsd:int, count: xsd:int, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> searchResult: ns0:mediaList
            setPlayedSeconds(id: ns0:id, seconds: xsd:int, contextId: xsd:string, privateData: ns0:privateDataType, offsetMillis: xsd:int, _soapheaders={credentials: {zonePlayerId: ns0:id, deviceId: ns0:id, deviceProvider: xsd:string, deviceCert: xsd:string, ({sessionId: ns0:sessionId} | {login: {username: ns0:username, password: ns0:password}} | {loginToken: {token: xsd:string, key: xsd:string, householdId: xsd:string}})}, context: {timeZone: xsd:string, _value_1: ANY[]}}) -> 

