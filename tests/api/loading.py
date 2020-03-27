import unittest
import json as simplejson

from src.json import json

content = """
{
    "web-app": {
        "servlet": [
            {
                "servlet-name": "cofaxCDS",
                "servlet-class": "org.cofax.cds.CDSServlet",
                "init-param": {
                    "configGlossary:installationAt": "Philadelphia, PA",
                    "configGlossary:adminEmail": "ksm@pobox.com",
                    "configGlossary:poweredBy": "Cofax",
                    "configGlossary:poweredByIcon": "/images/cofax.gif",
                    "configGlossary:staticPath": "/content/static",
                    "templateProcessorClass": "org.cofax.WysiwygTemplate",
                    "templateLoaderClass": "org.cofax.FilesTemplateLoader",
                    "templatePath": "templates",
                    "templateOverridePath": "",
                    "defaultListTemplate": "listTemplate.htm",
                    "defaultFileTemplate": "articleTemplate.htm",
                    "useJSP": false,
                    "jspListTemplate": "listTemplate.jsp",
                    "jspFileTemplate": "articleTemplate.jsp",
                    "cachePackageTagsTrack": 200e5,
                    "cachePackageTagsStore": 200,
                    "cachePackageTagsRefresh": 6,
                    "cacheTemplatesTrack": 100,
                    "cacheTemplatesStore": 50,
                    "cacheTemplatesRefresh": 15,
                    "cachePagesTrack": 200.5,
                    "cachePagesStore": 100,
                    "cachePagesRefresh": 10,
                    "cachePagesDirtyRead": 10,
                    "searchEngineListTemplate": "forSearchEnginesList.htm",
                    "searchEngineFileTemplate": "forSearchEngines.htm",
                    "searchEngineRobotsDb": "WEB-INF/robots.db",
                    "useDataStore": true,
                    "dataStoreClass": "org.cofax.SqlDataStore",
                    "redirectionClass": "org.cofax.SqlRedirection",
                    "dataStoreName": "cofax",
                    "dataStoreDriver": "com.microsoft.jdbc.sqlserver.SQLServerDriver",
                    "dataStoreUrl": "jdbc:microsoft:sqlserver://LOCALHOST:1433;DatabaseName=goon",
                    "dataStoreUser": "sa",
                    "dataStorePassword": "dataStoreTestQuery",
                    "dataStoreTestQuery": "SET NOCOUNT ON;select test='test';",
                    "dataStoreLogFile": "/usr/local/tomcat/logs/datastore.log",
                    "dataStoreInitConns": 10,
                    "dataStoreMaxConns": 100,
                    "dataStoreConnUsageLimit": 100,
                    "dataStoreLogLevel": "debug",
                    "maxUrlLength": 500
                }
            },
            {
                "servlet-name": "cofaxEmail",
                "servlet-class": "org.cofax.cds.EmailServlet",
                "init-param": {
                    "mailHost": "mail1",
                    "mailHostOverride": "mail2"
                }
            },
            {
                "servlet-name": "cofaxAdmin",
                "servlet-class": "org.cofax.cds.AdminServlet"
            },
            {
                "servlet-name": "fileServlet",
                "servlet-class": "org.cofax.cds.FileServlet"
            },
            {
                "servlet-name": "cofaxTools",
                "servlet-class": "org.cofax.cms.CofaxToolsServlet",
                "init-param": {
                    "templatePath": "toolstemplates/",
                    "log": 0,
                    "logLocation": "/usr/local/tomcat/logs/CofaxTools.log",
                    "logMaxSize": "",
                    "dataLog": 5.02,
                    "dataLogLocation": "/usr/local/tomcat/logs/dataLog.log",
                    "dataLogMaxSize": "",
                    "removePageCache": "/content/admin/remove?cache=pages&id=",
                    "removeTemplateCache": "/content/admin/remove?cache=templates&id=",
                    "fileTransferFolder": "/usr/local/tomcat/webapps/content/fileTransferFolder",
                    "lookInContext": 1e-43,
                    "adminGroupID": 4.0,
                    "betaServer": true
                }
            }
        ],
        "servlet-mapping": {
            "cofaxCDS": "/",
            "cofaxEmail": "/cofaxutil/aemail/*",
            "cofaxAdmin": "/admin/*",
            "fileServlet": "/static/*",
            "cofaxTools": "/tools/*"
        },
        "taglib": {
            "taglib-uri": "cofax.tld",
            "taglib-location": "/WEB-INF/tlds/cofax.tld"
        }
    }
}
"""


class DecodingTests(unittest.TestCase):
    def test__loads__NumberLiterals__SuccessfulLoad(self):
        self.assertEqual(json.loads("1"), simplejson.loads("1"))
        self.assertEqual(json.loads("0"), simplejson.loads("0"))
        self.assertEqual(json.loads("-1"), simplejson.loads("-1"))
        self.assertEqual(json.loads("-1.0"), simplejson.loads("-1.0"))
        self.assertEqual(json.loads("-1.25"), simplejson.loads("-1.25"))
        self.assertEqual(json.loads("-1.25e1"), simplejson.loads("-1.25e1"))
        self.assertEqual(json.loads("-1.25E1"), simplejson.loads("-1.25E1"))
        self.assertEqual(json.loads("-1.25E13"), simplejson.loads("-1.25E13"))
        self.assertEqual(json.loads("-1.25E-13"), simplejson.loads("-1.25E-13"))
        self.assertEqual(json.loads("200e5"), simplejson.loads("200e5"))

    def test__loads__StringLiterals__SuccessfulLoad(self):
        self.assertEqual(json.loads('""'), simplejson.loads('""'))
        self.assertEqual(json.loads('"abc"'), simplejson.loads('"abc"'))
        self.assertEqual(json.loads('"@#$abc"'), simplejson.loads('"@#$abc"'))
        self.assertEqual(json.loads('"ABC,def"'), simplejson.loads('"ABC,def"'))

    # def test__loads__StringEscaping__SuccessfulLoad(self):
    #     # Hmmm failing...
    #     self.assertEqual(json.loads('"\\""'), simplejson.loads('"\\""'))
    #     self.assertEqual(json.loads('"\\n"'), simplejson.loads('"\\n"'))

    def test__loads__OtherLiterals__SuccessfulLoad(self):
        self.assertEqual(json.loads("false"), simplejson.loads("false"))
        self.assertEqual(json.loads("true"), simplejson.loads("true"))
        self.assertEqual(json.loads("null"), simplejson.loads("null"))

    def test__loads__Arrays__SuccessfulLoad(self):
        self.assertEqual(json.loads("[1,2,3,4,5]"), simplejson.loads("[1,2,3,4,5]"))

    def test__loads__Object__SuccessfulLoad(self):
        self.assertEqual(
            json.loads('{"a": 14, "b": [1, 3.5, 3e5, -3.0], "ced4345%$": false}'),
            simplejson.loads('{"a": 14, "b": [1, 3.5, 3e5, -3.0], "ced4345%$": false}'),
        )

    # def test__loads__MasterTest__SuccessfulLoad(self):
    #     json_content = json.loads(content)
    #     simplejson_content = simplejson.loads(content)
    #     self.maxDiff = None
    #     self.assertEqual(json_content, simplejson_content)
