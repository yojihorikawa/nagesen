import tweepy
import requests
import json

#override tweepy.StreamListener to add logic to on_status
class TwStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        super(TwStreamListener, self).__init__()
        #initializes the counter
        self.counter = 0

        self.__api = api;

        #tmp address.
        self.__addrMap = {
            "0xf69fc8a0aa6b2d0f3bafa7d40ee501a788b0d65e": "ed19d0e3fc1e8d3bb92389bf993943949c6c96f17f4bf506bb0b5c5194ee780b",
            "0x2dfce98b4ec6a9e8b719c96b8b21cb75bf0c82d7": "bd46a7e1cfef10af7ca7a3b58ff17986ac4fe6783daab1c6464dbd964a408509",
            "0x1dd15d2efd2023f38045a1459ced52b1db2648cd": "4bb7d1c7d4aa82cb5a94a869137d62909621e8761e9a4bbb00883ae55ac6a783",
            "0xf82cffd7888a1815b577a09690fab35a8d3b2b95": "7886ec0190b3fff15de61befd3b6fa4d766edf2404f35f6602a7c22222affad1",
            "0xff141f4b6fb7397c6b0e40ae81aaf5f31fbe5c14": "f0b80e42febf415270ea93765bae9876b321bb108fe368ffa3fbd070b2680188",
            "0x97b8f5b3386bb07b71ca8f6dd0892a6d8623193a": "5eb57762749cd338d4dcd3d8b901461a64952a1d3e57bc1f25adbee64208eb43",
            "0xdf42d72b7259c27df4ed7a9a128257120754ef08": "66a1aaed20391f41a59d58c334983ad3ff6f61c264d5daddf478d2fd4b7c2343",
            "0x62d6034ecd1385ba1f83f6b28a7441e489fd708a": "773424659a0e2ae4b1877338e09b78db2bb6e5434c01dbf290b139fe94f12b5d",
            "0x218aa736b827f804afec647ac025a6cf80e014c3": "3c85cc299dc4318780a0d260157beffd82152e322b58b8b483d06ee272600e7a",
            "0x9e26730bf972d6ae8840b8f6003a61f57e25ff92": "001eec6f80d346f468d032964b34995c9c38c6cabc875fe7dd2a5baa8056a880",
        }

    def on_status(self, status):
        print(status.text)
        commandlist = status.text.split(' ')

        #@heppokopu transfer fromAddr toAddr amount
        if 'transfer' in commandlist[1].lower():
            print "transfer"

            fromAddr = commandlist[2].lower()
            pKey = self.__addrMap[fromAddr]
            toAddr = commandlist[3].lower()
            amount = commandlist[4]

            print("from:" + fromAddr + " pk:" + pKey + " to:" + toAddr + " amount:" + amount)

            if not fromAddr in self.__addrMap.keys():
                raise Exception("from not defined")
                return False
            if not toAddr in self.__addrMap.keys():
                raise Exception("to not defined")
                return False
            if amount <= 0:
                raise Exception("amount is invalid")
                return False

            #url="http://127.0.0.1:3001/sendValue?f=" + fromAddr + "&p=" + pKey + "&t=" + toAddr + "&a=" + amount
            # response = requests.get(url)
            url="http://127.0.0.1:3001/sendValue"
            param={
                "f": fromAddr,
                "p": pKey,
                "t": toAddr,
                "a": amount
            }
            response = requests.post(url, json=param)
            print response.json()
            if response.status_code != 200:
                raise Exception("TX failed!")
                return False

            print status.id
            if not status.id:
                raise Exception("Tweet ID not defined!")
                return False

            self.__api.update_status('TX succeeded!', status.id)

        return True


    def on_warning(self, notice):
        print('WARNING:' + str(notice.message))
        return

    def on_exception(self, exception):
        print('EXCEPTION:' + str(exception))
        return

    def on_error(self, status_code):
        print('ERROR: ' + str(status_code))
        return True

    def on_connect(self):
        print('CONNECTED')
        return

    def on_disconnect(self, notice):
        print('DISCONNECTED:' + str(notice.code))
        return
