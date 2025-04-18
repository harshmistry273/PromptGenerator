import { useCallback, useEffect, useRef, useState } from 'react';
import '../../public/WebSocketClient.css';

const WebSocketClient = () => {

    const [input, setInput] = useState('');
    const [answers,setAnswers] = useState([]);
    const inputRef = useRef();
    const [ws, setWs] = useState(null);

 

    useEffect(()=>{
        const socket = new WebSocket('ws://localhost:8000/generate-prompt');
        
        socket.onopen = () => {
            console.log('Connected to WebSocket server');
        };

        socket.onmessage = (event) => {
            const response = JSON.parse(event.data);
            setAnswers((prev) => [response.message, ...prev]);
            setInput('');
        };

        socket.onclose = (event) => {
            if (event.wasClean) {
                console.log('Closed cleanly');
            } else {
                console.error('Connection error');
            }
        };

        setWs(socket);

        return () => {
            socket.close();
        };

    },[])

    const focusInput = () => {
        inputRef.current?.focus();
        setTimeout(()=>{
            inputRef.current?.blur();
        },[900])
        handleSendMessage();
    }

    const handleSendMessage = () => {
        if (ws && input) {
            const messageData = { message: input };
            ws.send(JSON.stringify(messageData));
        }
    };

    return (
        <>
            <h1>Prompt Generator</h1>
            <h2>Say Anything</h2>
            <div style={{display:'flex', flexDirection:'row'}}>
                <input type="text" value={input} onChange={(e) => { setInput(e.target.value) }} placeholder='How Can I Help You?'
                    style={{
                        height: '4vh',
                        minHeight: '40px',
                        width: '40vw',
                        borderRadius: '1vh',
                        fontSize: 'clamp(14px, 2vh, 18px)',
                    }}
                    ref={inputRef}
                />
                <button onClick={focusInput}> Say </button>
            </div>
            <div className='main'>

            <div>
                {
                    answers.map((input,index)=>(
                        <div className='output'key={index}>
                            <p>
                        {index+1}&nbsp;&nbsp;&nbsp; 
                            </p>
                        <p>{input}</p>
                        </div>
                    ))
                }
            </div>
            </div>
        </>
    );
};

export default WebSocketClient;
