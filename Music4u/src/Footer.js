import React from 'react'
import './Footer.css'
import PlayCircleOutlineIcon from "@mui/icons-material/PlayCircleOutline";
import SkipPreviousIcon from "@mui/icons-material/SkipPrevious";
import SkipNextIcon from "@mui/icons-material/SkipNext";
import ShuffleIcon from "@mui/icons-material/Shuffle";
import RepeatIcon from "@mui/icons-material/Repeat";
import {Grid, Slider} from "@mui/material"

import VolumeDownIcon from "@mui/icons-material/VolumeDown";
import PauseCircleOutlineIcon from "@mui/icons-material/PauseCircleOutline";
import PlaylistPlayIcon from "@mui/icons-material/PlaylistPlay";

function Footer() {
  return (
    <div className='footer'>
      <div className='footer_left'>
        <img className="footer_albumLogo" src={require('./Music4u.png')}alt='' />
        
        <div className='footer_songInfo'>
          <h4>Yeah!</h4>
          <p>Usher</p>
        </div>
      </div>
      <div className='footer_center'>
        <ShuffleIcon className="footer_green" />
        <SkipPreviousIcon className="footer_icon" />
        <PlayCircleOutlineIcon fontSize="large" className="footer_icon" />
        <SkipNextIcon className="footer_icon"/>
        <RepeatIcon className="footer_green" />
        
      </div>
      <div className='footer_right'>
      <Grid container spacing={2}>
          <Grid item>
            <PlaylistPlayIcon />
          </Grid>
          <Grid item>
            <VolumeDownIcon />
          </Grid>
          <Grid item xs>
            <Slider/>
          </Grid>
        </Grid>
        
      </div>
    </div>
  )
}

export default Footer;