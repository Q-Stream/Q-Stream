from googletrans import Translator
import os, pickle


def translateLang(language):
    langfile = "lang.bat"
    if os.path.exists(langfile):
        with open(langfile, 'rb') as sf:
            langs = pickle.load(sf)
    else:
        langs = {
            "present": ['Video Settings', 'Select Video Quality', 'OK', 'Close', ' Enter URL', ' Status: Open File',
                        'Select Media File', ' Status : Getting Video Online', 'Status : Fetching Video Details',
                        'Status: Invalid Url', ' Status: Url Box Empty', 'Status: NO Online Video Playing',
                        'Status: Playing '
                , 'Status: Time in Wrong Format Be In (HH:MM:SS)', "Status : ", "Status: Platform Restriced Content"],
            "english": ['Video Settings', 'Select Video Quality', 'OK', 'Close', ' Enter URL', ' Status: Open File',
                        'Select Media File', ' Status : Getting Video Online', 'Status : Fetching Video Details',
                        'Status: Invalid Url', ' Status: Url Box Empty', 'Status: NO Online Video Playing',
                        'Status: Playing '
                , 'Status: Time in Wrong Format Be In (HH:MM:SS)', "Status : ", "Status: Platform Restriced Content"]}

    if language not in langs.keys():
        temp = ['Video Settings', 'Select Video Quality', 'OK', 'Close', ' Enter URL', ' Status: Open File',
                'Select Media File', ' Status : Getting Video Online', 'Status : Fetching Video Details',
                'Status: Invalid Url', ' Status: Url Box Empty', 'Status: NO Online Video Playing', 'Status: Playing '
            , 'Status: Time in Wrong Format Be In (HH:MM:SS)', "Status : ", "Status: Platform Restriced Content"]
        translator = Translator()
        try:
            langs[language] = [translator.translate(i, dest=language).text for i in temp]
            langs['present'] = langs[language]
        except:
            print("[ Invalid Language ]")
    else:
        langs['present'] = langs[language]
    with open(langfile, "wb") as sf:
        pickle.dump(langs, sf)
    return langs

if __name__ == '__main__':
    inputLang = "english".lower()
    languages = [
                "English",
                "Spanish",
                "French",
                "Arabic",
                "Bulgarian",
                "Danish",
                "German",
                "Greek",
                "Persian",
                "Hindi",
                "Italian",
                "Japanese",
                "Korean",
                "Polish",
                "Urdu",
            ]
    for i in languages:
        print(translateLang(i))
