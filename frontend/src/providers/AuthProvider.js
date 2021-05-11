import React, { useState, useContext } from 'react'

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
    window.isAuthificated === 'False' ? false : true
  )

  const [token, setToken] = useState(null)

  const [user, setUser] = useState(null)

  return (
    <AuthContext.Provider
      value={{ auth, setAuth, token, setToken, user, setUser }}
    >
      {children}
    </AuthContext.Provider>
  )
}
