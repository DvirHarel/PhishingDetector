import sys
import numpy as np
import pandas as pd
from Model import loadModel
from Features import *

# Add yours absolute path to the files.
whiteListPath = ""
modelPath = ""
dataSetPath = ""

def buildFeatureVector(url):
    # Calling each feature on the url. (must work with internet connection)
    return [ANumOfDots(url),BSubDomainLevel(url),CPathLevel(url),DUrlLength(url),ENumDash(url),FNumDashInHostname(url),GAtSymbol(url),HTildeSymbol(url),
            INumUnderscore(url),JNumPercent(url),KNumQueryComponents(url),LNumAmpersand(url),MNumHash(url),NNumNumericChars(url),ONoHttp(url),
            PPopUpWindow(url),QIpAddress(url),RDomainInSubdomains(url),SDomainInPaths(url),THttpsInHostName(url),UHostnameLength(url),VPathLength(url),
            WQueryLength(url),XDoubleSlashInPath(url),YMissingTitle(url),ZSubmitInfoToEmail(url),AANumOfSensetiveWords(url)]
def predictUrl(url,model):
    df = pd.read_csv(dataSetPath).drop(columns=['PhishingResults'])
    colNames = np.array(df.columns.array)
    # Split our url to feature vector
    vector = np.array(buildFeatureVector(url)).reshape(1,-1)
    # Rearrange our vector with the col names
    vector = pd.DataFrame(columns=colNames, data=vector)
    # Call predict func which return our result
    return model.predict(vector)
def predictPhishing(url,modelPath,white_list):
    if checkWhiteList(url,white_list):
        return 0
    # Load our ML model
    model = loadModel(modelPath)
    prediction = predictUrl(url,model)
    return prediction[0]
def checkWhiteList(url,white_list):
    res = tldextract.extract(url)
    if(res.registered_domain):
        url_parsed = res.registered_domain
        for site in white_list.iterrows():
            if(url_parsed.startswith(site[1]['Root Domain'])):
                return True
    return False
if __name__ == '__main__':
    # Getting the url from the chrome extension
    url = sys.argv[1]
    # list of webpages in the top500
    white_list = pd.read_csv(whiteListPath)
    # Call predictPhishing which return 1 if the page is a phishing else 0
    print(predictPhishing(url,modelPath,white_list))

