import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import App from "./App";


const root = ReactDOM.createRoot(document.getElementById('root'));

const renderApp = (position) => {
    root.render(
        <React.StrictMode>
            <App position={position}/>
        </React.StrictMode>
    );
}

//ask for the user's location
navigator.geolocation.getCurrentPosition((position) => {
    renderApp(position);
}, () => {
    const position = {coords: {latitude: 50.2092, longitude: 15.8328}}
    renderApp(position);
});

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
