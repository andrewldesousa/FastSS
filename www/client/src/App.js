import React, { useState, useEffect } from 'react';
import { Widget, addResponseMessage, toggleWidget } from 'react-chat-widget';
import 'react-chat-widget/lib/styles.css';


const launchRequest = {
	"version": "1.0",
	"session": {
		"new": true,
		"sessionId": "amzn1.echo-api.session.2ba793f4-c6c3-4ca3-82c1-fcda037d06cb",
		"application": {
			"applicationId": "amzn1.ask.skill.ad00c1c4-3c2e-4fd4-8268-d23da34526f5"
		},
		"user": {
			"userId": "amzn1.ask.account.AHTKR7M4GAOLXFWTKA5GWTRS6O4MXO4CVARJWBGQPTZZ3H7K7BASVMLWWKXZLH7ICMLRY4BUYEOJRJFQ4AUQE3AXUCH7TB5NRQJZZZ2MQ6WD6MDCSRVUGJ77WPWX5KRX2WFX24FBOWMGWKJSJYWLX5OAK5BOTBIWNHDORKQVDNOMU5OCYO6NOEQ2D3GXWSNLGXF6UVUNKNSHIGI"
		}
	},
	"context": {
		"Viewports": [
			{
				"type": "APL",
				"id": "main",
				"shape": "RECTANGLE",
				"dpi": 160,
				"presentationType": "STANDARD",
				"canRotate": false,
				"configuration": {
					"current": {
						"video": {
							"codecs": [
								"H_264_42",
								"H_264_41"
							]
						},
						"size": {
							"type": "DISCRETE",
							"pixelWidth": 1024,
							"pixelHeight": 600
						}
					}
				}
			}
		],
		"Viewport": {
			"experiences": [
				{
					"arcMinuteWidth": 246,
					"arcMinuteHeight": 144,
					"canRotate": false,
					"canResize": false
				}
			],
			"shape": "RECTANGLE",
			"pixelWidth": 1024,
			"pixelHeight": 600,
			"dpi": 160,
			"currentPixelWidth": 1024,
			"currentPixelHeight": 600,
			"touch": [
				"SINGLE"
			],
			"video": {
				"codecs": [
					"H_264_42",
					"H_264_41"
				]
			}
		},
		"Extensions": {
			"available": {
				"aplext:backstack:10": {}
			}
		},
		"System": {
			"application": {
				"applicationId": "amzn1.ask.skill.ad00c1c4-3c2e-4fd4-8268-d23da34526f5"
			},
			"user": {
				"userId": "amzn1.ask.account.AHTKR7M4GAOLXFWTKA5GWTRS6O4MXO4CVARJWBGQPTZZ3H7K7BASVMLWWKXZLH7ICMLRY4BUYEOJRJFQ4AUQE3AXUCH7TB5NRQJZZZ2MQ6WD6MDCSRVUGJ77WPWX5KRX2WFX24FBOWMGWKJSJYWLX5OAK5BOTBIWNHDORKQVDNOMU5OCYO6NOEQ2D3GXWSNLGXF6UVUNKNSHIGI"
			},
			"device": {
				"deviceId": "amzn1.ask.device.AE65TJE5CW2UZG7OVSBGYRIFTQLW76MDYCJ66372BRTVNQSN65LG3D6K4EPNZPOOQWCVER6UNQ3N3DX2MIOQX3OSXO5YASHVU2HFLXXATF6NH7GQPVMJTWXJJFZHBPBW5SZKHMP7SY3KXZYE22SBRBR2IC7OHLSL5TTLDKID6B4Y7TTYYZG7O",
				"supportedInterfaces": {}
			},
			"apiEndpoint": "https://api.amazonalexa.com",
			"apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLmFkMDBjMWM0LTNjMmUtNGZkNC04MjY4LWQyM2RhMzQ1MjZmNSIsImV4cCI6MTYwODMzMjYwNCwiaWF0IjoxNjA4MzMyMzA0LCJuYmYiOjE2MDgzMzIzMDQsInByaXZhdGVDbGFpbXMiOnsiY29udGV4dCI6IkFBQUFBQUFBQUFCN1JiSk0rTW1nRXJoRjgxVHUrM05yS2dFQUFBQUFBQUJiZzdnUUQvNktQM1FZQ2Rxd0RjenZuNzQxekVzVDltU3d1bXFIZVFWdTlzNndPYjMwS3hFMEF3NVFUTEF0UUkzY3JjaFVtZkgrZFFTZmwrckxBRWRzaUNNRmszUERvTzNFSGRFVEk3OHlWc084WGJDUll2cDNRejF0ajBnSUR1VjZzK3Q2ZGRmRm5nd1FRc1BEVVFwSUtyS3lNQk9ZeEcrVGphSW04T0xianJwUXVTUU1XMlMyLzlpYWthcTlVZ2tjVEVOY0RPNDdrSTUzY0pscVJFbDBsd2plaVVWQkpvQmFOU1JybkNjckYrMGRRNFpUQmErNGRybnVaMXVwWmxvUGpHRTVUWWJ3SmczeG45dDl0V0NFdElNNTk0ZHF1QzY4Y1RnMjFrbWVZRkFyZGVUbkFhSUJxTXpNWFAvalg0YTVrWUk1emkrL1JhdzVMZEpGUjJpZUN4amVQS3ZUWTJVM1ZBQnZoS2lQRHVxYkJINVBMVm4rUzZ5TzZxTnhOU2xzakw4dWtmK3N1RTJTIiwiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUU2NVRKRTVDVzJVWkc3T1ZTQkdZUklGVFFMVzc2TURZQ0o2NjM3MkJSVFZOUVNONjVMRzNENks0RVBOWlBPT1FXQ1ZFUjZVTlEzTjNEWDJNSU9RWDNPU1hPNVlBU0hWVTJIRkxYWEFURjZOSDdHUVBWTUpUV1hKSkZaSEJQQlc1U1pLSE1QN1NZM0tYWllFMjJTQlJCUjJJQzdPSExTTDVUVExES0lENkI0WTdUVFlZWkc3TyIsInVzZXJJZCI6ImFtem4xLmFzay5hY2NvdW50LkFIVEtSN000R0FPTFhGV1RLQTVHV1RSUzZPNE1YTzRDVkFSSldCR1FQVFpaM0g3SzdCQVNWTUxXV0tYWkxIN0lDTUxSWTRCVVlFT0pSSkZRNEFVUUUzQVhVQ0g3VEI1TlJRSlpaWjJNUTZXRDZNRENTUlZVR0o3N1dQV1g1S1JYMldGWDI0RkJPV01HV0tKU0pZV0xYNU9BSzVCT1RCSVdOSERPUktRVkROT01VNU9DWU82Tk9FUTJEM0dYV1NOTEdYRjZVVlVOS05TSElHSSJ9fQ.Tgc2icUela8dePkSCS3OjsCzravqNuE0wArg5i4avuNGTVxEEDRwfVhj7FE18BI202GP8f7gvnbqTyr_xbwjAUZ3uasrWQF2SCrVTC4MLStHARlKqwVbsxzJD2EBlBJVh_edHEnD6bvFu0H-ngo7KjLtmpgOmPPHLpW4noOzD_YeoyBsKkK3phOZRNGkcC59JZcGMYHsk49-iervzSnfOMKzgN1K4sb7TdUm_VNCjY6_SG6ejzbQq9FTf3r6bU_EJL-h9qNwBtEml1nAWna7Cgz14KS3k9HbTN1y_TlfFBMr73UpiUc19d4Kv9tYfAfCSkT54c3l0lleprdSdtP-5g"
		}
	},
	"request": {
		"type": "LaunchRequest",
		"requestId": "amzn1.echo-api.request.2e78f749-1034-41f9-a9cf-00377dd96ad2",
		"timestamp": "2020-12-18T22:58:24Z",
		"locale": "en-US",
		"shouldLinkResultBeReturned": false
	}
};


function App() {
  const [widgetOpen, setWidgetOpen] = useState(false);
 
  
  useEffect(() => {
    toggleWidget();
    console.log(fetch('http://localhost:5000/'))
    addResponseMessage('Welcome to this awesome chat! You can utilize Fast Synonym. Which one would you like to open?');
  }, []);

  const handleNewUserMessage = (newMessage) => {
    console.log(`New message from user -> ${newMessage}`);
    addResponseMessage('New message incomig!');
  }


  return (
    <div className="App">
      <Widget
        handleNewUserMessage={handleNewUserMessage}
        fullScreenMode={true}
        showCloseButton={false}
        title={'Alexa App'}
        subtitle={'I have a few skills to share with you.'}
      />
    </div>
  ); 
}

export default App;
