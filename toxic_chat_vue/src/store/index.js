import { createStore } from 'vuex'
import axios from "axios"


export default createStore({
  state: {
    token: "",
    isAuthenticated: false,
    channels: [],
    currentChannel: {}
  },
  mutations: {
    switchToChannel(state, args) {
      state.currentChannel = args
      console.log(args)
    },
    initialize(state) {
      let auth_token = localStorage.getItem("token")
      if (auth_token) {
        state.token = auth_token
        state.isAuthenticated = true
        axios.defaults.headers.common["Authorization"] = "Token " + state.token
        axios.defaults.headers.common["Content-Type"] = "application/json"
      }
    },
    setToken(state, args) {
      const token = args["token"]
      state.token = token
      localStorage.setItem("token", token)
      state.isAuthenticated = true
      axios.defaults.headers.common["Authorization"] = "Token " + state.token
      axios.defaults.headers.common["Content-Type"] = "application/json"
    },
    removeToken() {
      this.token = ""
      this.isAuthenticated = false
    },
  },
  actions: {
  },
  modules: {
  }
})
