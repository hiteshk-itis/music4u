import React from 'react';
import './Login.css';
import {loginUrl} from './spotify';

function Login() {
  return (
    <div className='login'>
        
        <img src={require("./Music4u.png")} alt='' />

        {/* Login with spotify buttonj */}
        <a href={loginUrl}>LOGIN WITH Spotify</a>
    </div>
  )
}

export default Login;