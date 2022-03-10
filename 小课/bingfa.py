import requests,time
stime=int(time.time())
url='http://10.221.122.90:8081/ocndb/adi2Inject?systemId=ADIPANEL'
xml='''
<?xml version="1.0" encoding="utf-8"?>
<adi:ADI2 xmlns="http://www.cablelabs.com/VODSchema/default" xmlns:adi="http://www.cablelabs.com/VODSchema/adi" xmlns:vod="http://www.cablelabs.com/VODSchema/vod">
    <!-- series-->
    <adi:OpenGroupAsset type="VODRelease" product="adipanel">
        <vod:VODRelease providerID="adipanel" providerType="2" assetID="adipanelseries"+stime+"001" updateNum="" groupAsset="Y" serialNo=""+stime+"001">
            <adi:AssetLifetime startDateTime="2016-08-01" endDateTime="2050-12-31" />
        </vod:VODRelease>
    </adi:OpenGroupAsset>
    <adi:AddMetadataAsset groupProviderID="adipanel" groupAssetID="adipanelseries"+stime+"001" type="Title" product="adipanel">
        <vod:Title providerID="adipanel" assetID="adipanelseries"+stime+"001" updateNum="1">
            <adi:AssetLifetime startDateTime="2016-08-01" endDateTime="2050-12-31" />
            <vod:TitleFull>电视剧"+stime+"001</vod:TitleFull>
			<vod:ImageUrl>ftp://adipanel:adipanel@10.27.247.70/cacheFolder/"+stime+"001.jpg</vod:ImageUrl>
            <vod:ShowType>Series</vod:ShowType>
            <vod:EnglishName>
                <![CDATA[]]>
</vod:EnglishName>
            <vod:SummaryShort>
                <![CDATA[${series.shortSummary}]]>
</vod:SummaryShort>
            <vod:IsAdvertise>0</vod:IsAdvertise>
            <vod:Status>1</vod:Status>
            <vod:Actor type="Actor">
                <vod:LastNameFirst>
                    <![CDATA[]]>
</vod:LastNameFirst>
            </vod:Actor>
            <vod:Actor type="Actress">
                <vod:LastNameFirst>
                    <![CDATA[]]>
</vod:LastNameFirst>
            </vod:Actor>
            <vod:Actor type="CoActor">
                <vod:LastNameFirst>
                    <![CDATA[]]>
</vod:LastNameFirst>
            </vod:Actor>
            <vod:Actor type="CoActress">
                <vod:LastNameFirst>
                    <![CDATA[]]>
</vod:LastNameFirst>
            </vod:Actor>
            <vod:Director>
                <vod:LastNameFirst>
                    <![CDATA[无]]>
</vod:LastNameFirst>
            </vod:Director>
            <vod:Year>
                <![CDATA[2010]]>
</vod:Year>
            <vod:Language>
                <![CDATA[${series.vodDub}]]>
</vod:Language>
            <vod:Items>7</vod:Items>
            <vod:Keyword>
                <![CDATA[${series.keyword}]]>
</vod:Keyword>
            <vod:Priority>1</vod:Priority>
            <vod:Tag>
                <![CDATA[幼儿,少年,搞笑]]>
</vod:Tag>
            <vod:ProgramType>1</vod:ProgramType>
        </vod:Title>
    </adi:AddMetadataAsset>
    <adi:AddMetadataAsset groupProviderID="adipanel" groupAssetID="adipanelseries"+stime+"001" type="CategoryPath" product="adipanel">
        <vod:CategoryPath mso="" providerID="adipanel" assetID="adipanelseries"+stime+"001" updateNum="1">
            <adi:AssetLifetime startDateTime="2016-08-01" endDateTime="2050-12-31" />
            <vod:Classification>
                <![CDATA[少儿]]>
</vod:Classification>
            <vod:Category>
                <![CDATA[动画]]>
</vod:Category>
        </vod:CategoryPath>
    </adi:AddMetadataAsset>
    <adi:AddMetadataAsset groupProviderID="adipanel" groupAssetID="adipanelseries"+stime+"001" type="Copyright" product="adipanel">
        <vod:Copyright providerID="adipanel" assetID="adipanelseries"+stime+"001" updateNum="1">
            <adi:AssetLifetime startDateTime="2016-08-01" endDateTime="2050-12-31" />
        </vod:Copyright>
    </adi:AddMetadataAsset>
    <!-- program-->
    <adi:OpenGroupAsset type="VODRelease" product="adipanel">
        <vod:VODRelease providerID="adipanel" providerType="2" assetID="adipanelseries"+stime+"001_1" updateNum="" groupAsset="Y" serialNo=""+stime+"001">
            <adi:AssetLifetime startDateTime="2016-08-01" endDateTime="2050-12-31" />
        </vod:VODRelease>
    </adi:OpenGroupAsset>
    <adi:AddMetadataAsset groupProviderID="adipanel" groupAssetID="adipanelseries"+stime+"001_1" type="Title" product="adipanel">
        <vod:Title providerID="adipanel" assetID="adipanelseries"+stime+"001_1" updateNum="1">
            <adi:AssetLifetime startDateTime="2016-08-01" endDateTime="2050-12-31" />
            <vod:ShowType>Serie</vod:ShowType>
            <vod:EpisodeID>6</vod:EpisodeID>
            <vod:IsAdvertise>0</vod:IsAdvertise>
            <vod:TitleFull>电视剧"+stime+"001[1]_B</vod:TitleFull>
            <vod:SourceType></vod:SourceType>
            <vod:Status>1</vod:Status>
            <vod:SummaryMedium>八个可爱的小动物组成了海底探险小队。他们居住在神秘基地章鱼堡，随时准备出发去解决海底遇险，排除海底可能发生的危险。</vod:SummaryMedium>
            <vod:SummaryShort></vod:SummaryShort>
        </vod:Title>
    </adi:AddMetadataAsset>
    <adi:AcceptContentAsset type="Video" metadataOnly="N" fileName="J9101408220073.ts" fileSize="663842852" mD5CheckSum="2bf24533c494c6a3387573560fdcdbea">
        <vod:Video providerID="adipanel" assetID="adipanelMOVI"+stime+"001_1" updateNum="1" fileName=""+stime+"001.ts" fileSize="663842852" mD5CheckSum="2bf24533c494c6a3387573560fdcdbea" transferContentURL="ftp://ADIPANEL:ADIPANEL@10.27.247.70/cacheFolder/201907/19/336968/"+stime+"001_1.ts" encodingProfile="" encodingCode="">
            <adi:AssetLifetime startDateTime="2016-08-01" endDateTime="2050-12-31" />
            <vod:HDFlag>0</vod:HDFlag>
            <vod:FrameHeight>1080</vod:FrameHeight>
            <vod:FrameWidth>1920</vod:FrameWidth>
            <vod:Bitrate>7600</vod:Bitrate>
            <vod:FrameRate>25</vod:FrameRate>
            <vod:MimeType>99</vod:MimeType>
            <vod:ServiceType>11</vod:ServiceType>
            <vod:NeedDRM>1</vod:NeedDRM>
            <vod:Usage>1</vod:Usage>
            <vod:IsDRM>1</vod:IsDRM>
            <vod:Duration>1379</vod:Duration>
            <vod:FileType>1</vod:FileType>
        </vod:Video>
    </adi:AcceptContentAsset>
    <adi:AssociateContent type="Video" effectiveDate="" groupProviderID="adipanel" groupAssetID="adipanelseries"+stime+"001_1" providerID="adipanel" assetID="adipanelMOVI"+stime+"001_1" />
    <!-- Associate-->
    <adi:AssociateGroup effectiveDate="" groupProviderID="adipanel" providerID="adipanel" assetID="adipanelseries"+stime+"001_1" sourceGroupAssetID="adipanelseries"+stime+"001_1" targetGroupAssetID="adipanelseries"+stime+"001" />
</adi:ADI2>
'''
r=requests.post(url,data=xml.encode('utf-8'))
print(r.text)
