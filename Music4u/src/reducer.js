export const initialState = {
  user: null,
  playlists: [],
  playing: false,
  item: null,
  // token:  "BQDHWe6y7KSRdzErZbNlwNtGB5XLxOY3V5SiB4OgjTdc_vEnPxA2bgTJDO_Qky2hSg3XqfZP54xFyKDhlq3byreStrmkr_NIYP-CURFvuGNfDLKV_HM9LPns-YQuzNT3dyoR5kd_OI4P81OG9h9oGPdowgkpeYPX6MQgSPQ1JMHyQhOQ5JpcZsHTeetMfra0fFVt5HTpARS9Sspz",
};

const reducer = (state, action) => {
  console.log("action:", action);
  switch (action.type) {
    case "SET_USER":
      return {
        ...state,
        user: action.user,
      };
    case "SET_TOKEN":
      return {
        ...state,
        token: action.token,
      };
    case "SET_PLAYLISTS":
      return {
        ...state,
        playlists: action.playlists,
      };
    default:
      return state;
  }
};

export default reducer;
