import React, { useState, useEffect } from 'react';
import { Widget, addResponseMessage, toggleWidget } from 'react-chat-widget';
import 'react-chat-widget/lib/styles.css';


var headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
};

var dataString = 'grant_type=client_credentials&client_id=amzn1.application-oa2-client.5fd93d0246974f7ab35acf7f3570cc37&client_secret=e2cacfecc71b0781269fc9f62fb5f23b3e86b945361ab06a92721d996036a6fd&scope=alexa:skill_messaging';

var options = {
    url: 'https://api.amazon.com/auth/o2/token',
    method: 'POST',
    headers: headers,
    body: dataString
};

function callback(error, response, body) {
    if (!error && response.statusCode == 200) {
        console.log(body);
    }
}



function App() {
  const [widgetOpen, setWidgetOpen] = useState(false);
  
  useEffect(() => {
	toggleWidget();
	
	fetch('http://localhost:5000/fast-synonym', {
		mode: 'cors',
		url: 'http://localhost:5000',
		method: 'POST',
		headers: headers,
		body: dataString
	})


	//ResponseMessage(r.response.outputSpeech.ssml)
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
