import React, { useState, useContext, useEffect } from 'react'
import {
  ACCESS_TOKEN_NAME,
  API_AUTH_ACCOUNT,
  API_BASE_URL,
} from '../constants/urls'

const AuthContext = React.createContext({
  auth: null,
  setAuth: null,
  token: null,
  setToken: null,
  user: null,
  setUser: null,
})

export const useAuth = () => {
  const context = useContext(AuthContext)
  if (!context) throw new Error('Hook vne providera Sanya blin')
  return context
}

export const AuthProvider = ({ children }) => {
  const [auth, setAuth] = useState(
    localStorage.getItem(ACCESS_TOKEN_NAME) ? true : false
  )
  const [token, setToken] = useState(localStorage.getItem(ACCESS_TOKEN_NAME))
  const [user, setUser] = useState(null)

  // if (auth) {
  //   useEffect(() => {
  //     const getUser = async () => {
  //       try {
  //         const resp = await fetch(API_BASE_URL + API_AUTH_ACCOUNT, {
  //           method: 'GET',
  //           headers: {
  //             Authorization: ACCESS_TOKEN_NAME + ' ' + token,
  //           },
  //         })
  //         const json = await resp.json()
  //         console.log
  //         if (resp.ok && json.token) {
  //           setUser(json.account)
  //           setToken(json.token)
  //           console.log(user)
  //         }
  //       } catch (e) {
  //         console.error(e)
  //       }
  //     }
  //     void getUser()
  //   }, [setUser])
  // }
  // console.log(user)

  return (
    <AuthContext.Provider
      value={{ auth, setAuth, token, setToken, user, setUser }}
    >
      {children}
    </AuthContext.Provider>
  )
}
