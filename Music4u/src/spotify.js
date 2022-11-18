// https://developer.spotify.com/documentation/web-playback-sdk/quick-start/#

export const authEndpoint = "https://accounts.spotify.com/authorize";

const redirectUri = "http://localhost:3000/";

const clientId = "92a72afbf06341d4a8c0345bceff589a";

const scopes = [
  
  // Read access to user's current playing content
    "user-read-currently-playing",

    //read access to user's recently played tracks
  "user-read-recently-played",

  //Read user's currently playing content and Spotify Connect devices informa
  "user-read-playback-state",

  //Read access to a user's top artists and tracks.
  "user-top-read",

  //Control playback on user's Spotify clients and Spotify Connect devices
  "user-modify-playback-state",
];

export const getTokenFromUrl = () => {
    return window.location.hash
    .substring(1)
    .split('&')
    .reduce((prevVal, currVal) => {
        let parts = currVal.split('=')
        prevVal[parts[0]] = parts[1]

        return prevVal;
    }, {})
}

export const loginUrl = `${authEndpoint}?client_id=${clientId}&redirect_uri=${redirectUri}&scope=${scopes.join("%20")}&response_type=token&show_dialog=true`;
